# flask-aws-crud
``
This is a simple python-flask repository, using bootstrap and awesomefonts to reach a beautiful and easily handler view, 
and using the python boto3 aws sdk to consume the S3 aws services.
`` 
## Getting Started
* Virtual enviroment:

``
in a desired location, run: 
python -m venv .venv
To create a virtual enviroment using python virtualenv
and acess this:
source .venv/bin/activate
``
* Clone the repository:

``
git clone https://github.com/victor-s-santos/flask-aws-crud.git
``

* Install the dependencies:

``
pip install -r requirements.txt
``
* Environment variables: create a .env file in the root directory containing:

``
  source .venv/bin/activate
  export FLASK_APP=app.py
  export FLASK_DEBUG=1
  export S3_BUCKET=your_bucket
  export S3_KEY=<your_key>
  export S3_SECRET=<your_s3_secret>
``

* Run the tests:

``python tests.py
``

* Run server:

``
flask run
``

* Work to be done:

``
Expand this tests for the other page(file route);
Test the s3 functionality.
``

Thanks for coming!
