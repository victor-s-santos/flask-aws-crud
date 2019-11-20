import os
import mimetypes
import arrow

def datetimeformat(date_str):
	"""Filtro para melhorar a exibição de informações do tipo data"""
	dt = arrow.get(date_str)
	return dt.humanize()

def file_type(key):
	"""Filtro"""
	file_info = os.path.splitext(key)
	file_extension = file_info[1]
	try:
		return mimetypes.types_map[file_extension]
	except KeyError():
		return "Tipo de arquivo desconhecido."