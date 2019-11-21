from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_bootstrap import Bootstrap
import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET
from filters import datetimeformat, file_type
from pprint import pprint

s3_resource = boto3.resource(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)
app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secret'
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type

def get_bucket():
    s3_resource = _get_s3_resource()
    return s3_resource.Bucket(S3_BUCKET)

def get_buckets_list():
    client = boto3.client('s3')
    buckets = client.list_buckets()
    return client.list_buckets().get('Buckets')

@app.route('/')
def index():
	buckets = get_buckets_list()
	return render_template('index.html', buckets=buckets)


@app.route('/files')
def files():
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(S3_BUCKET)
	sunmaries = my_bucket.objects.all()

	return render_template('files.html', my_bucket=my_bucket, files=sunmaries)

@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']
	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(S3_BUCKET)
	my_bucket.Object(file.filename).put(Body=file)
	flash('Upload realizado com sucesso.')

	return redirect(url_for('files'))
	#return "Upload realizado com sucesso.""
	
@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(key).delete()

    flash('Arquivo deletado com sucesso!')
    return redirect(url_for('files'))

@app.route('/download', methods=['POST'])
def download():
	key = request.form['key']

	s3_resource = boto3.resource('s3')
	my_bucket = s3_resource.Bucket(S3_BUCKET)
	file_obj = my_bucket.Object(key).get()

	return Response(
		file_obj['Body'].read(),
		mimetype='text/plain',
		headers={"Content-Disposition": "attachment;filename={}".format(key)}
		)


if __name__ == '__main__':
	app.run()