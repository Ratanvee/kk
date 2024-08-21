from flask import Flask, render_template, jsonify, redirect, request

# import fitz

# from read import read_txt


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/abc')
def link():
  return render_template('second.html')

@app.route('/')
def link1():
  return render_template('index.html')

@app.route('/submit')
def link12():
  if request.method == "GET":
    information = request.form
  return render_template('submit.html', data=information)

if __name__ == "__main__":
    app.run(port=5000, debug = True)