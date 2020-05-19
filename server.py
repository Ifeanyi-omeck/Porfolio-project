from flask import Flask, render_template, request, url_for, redirect
import csv


app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template('indexx.html') 

@app.route('/<path:variable_name>')
def my_works(variable_name):
    return render_template(variable_name)

def write_to_file(data):
	with open('database.txt',  newline='', mode = 'a') as database:
		email = data ["email"]
		subject = data ["subject"]
		message = data ["message"]
		new_file =database.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
	with open('database.csv',  newline='', mode = 'a') as database2:
		email = data ["email"]
		subject = data ["subject"]
		message = data ["message"]
		file2 = csv.writer(database2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		file2.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong'
