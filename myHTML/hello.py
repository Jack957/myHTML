#!/usr/bin/python

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	try:
		num1_string = request.args.get('num1')
		num2_string = request.args.get('num2')
		number1 = (float(num1_string) if '.' in num1_string else
			int(num1_string))
		number2 = (float(num2_string) if '.' in num2_string else
			int(num2_string))
		result = number1 * number2
		return render_template('hello.html',
			num1 = number1, num2 = number2, result = result)
	except:
		return render_template('hello.html')
		
	if __name__ == '__main__':
		app.debug = True
		app.run(host = '0.0.0.0')