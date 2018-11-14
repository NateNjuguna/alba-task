# Import all necesarry libraries
import base64, hmac, json, os

from database import Database
from flask import Flask, render_template, request, send_from_directory

# Get a database and configure which table to work with
db = Database('alba_one')

#configure flask to be the main module
application = Flask(__name__)

# Configure jinja2 template cache
application.config['TEMPLATES_AUTO_RELOAD'] = True

# Define my app's routes and write my control functions

@application.route('/', methods = ['GET', 'POST'])
def index():
  entries = []
  errors = []
  if request.method == 'GET':
    entries.extend(db.get_all())
  else:
    try:
      entry = request.form
      db.add(entry)
      entries.extend(db.get_all())
    except Exception as e:
      errors.append(str(e))
  return render_template('index.html', entries = entries, errors = errors, keyword = '')

@application.route('/assets/css/<static_file>', methods = ['GET'])
def css(static_file):
	#Return specified css file
	return send_from_directory('assets', filename='css/' + str(static_file))
		
@application.route('/assets/fonts/<static_file>', methods = ['GET'])
def fonts(static_file):
	return send_from_directory('assets', filename='fonts/' + str(static_file))
		
@application.route('/assets/img/<static_file>', methods = ['GET'])
def img(static_file):
	return send_from_directory('assets', filename='img/' + str(static_file))
		
@application.route('/assets/js/<static_file>', methods = ['GET'])
def js(static_file):
	return send_from_directory('assets', filename='js/' + str(static_file))
		
@application.route('/favicon.ico', methods = ['GET'])
def favicon():
	#Return favicon for default url
	return send_from_directory('assets', 'img/favicon.ico')
		
@application.route('/robots.txt', methods = ['GET'])
def robots():
	#Return robots for default url
	return send_from_directory('config', 'robots.txt')

@application.route('/search', methods = ['GET'])
def search():
  entries = []
  errors = []
  keyword = request.args.get('query')
  try:
    entries.extend(db.search(keyword))
  except Exception as e:
    errors.append(str(e))
  return render_template('index.html', entries = entries, errors = errors, keyword = keyword)

if __name__ == '__main__':
	host = '0.0.0.0'
	port = int(os.environ.get('PORT', 5000))
	application.run(host=host, port=port);