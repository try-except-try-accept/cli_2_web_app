from unittest.mock import patch
import os
cmd_queue = []
from flask import Flask, session, request, after_this_request, jsonify, make_response, url_for, redirect
from flask_session import Session
from flask import render_template
from uuid import uuid4
from quiz import main as run_quiz
import logging
import threading
import time
from json import dumps as dump_json

app = Flask(__name__)
app.secret_key = "eirgjtaepogijeapgoijeagpoiejagpoiejagpoieajgpoerijg"

@app.route("/get_cli", methods=['GET'])
def get_cli():
    print("Fetching")
    with open("output.txt", "r") as f:
        data = f.read()
    res = make_response(dump_json({"message":data}), 200)

    return res

@app.route("/post_cli", methods=["POST"])
def post_cli():
    data = request.get_json()
    print(data)
    session['input'].append(data)

def print_wrapper(s):
    with open("output.txt", "a") as f:
        f.write(s+"\n")
    #session['output'].append(s)

def input_wrapper(s):
    print(s)
    print("awaiting input!!!")
    return session['input'].pop(0)


@app.route('/play')
def play():
    return render_template("base.html")

@app.route("/")
def hello():


    session['output'] = []
    session['input'] = []
    with patch('sys.stdout.write', print_wrapper) as one:
        with patch('builtins.input', input_wrapper) as two:
            x = threading.Thread(target=run_quiz).start()


    return redirect(url_for('play'))


if __name__ == "__main__":
    app.run()


# def next_line():
#     next_action = cmd_queue.pop(0)
#
#     if
#
#
#
# def print_wrapper(text):
#     cmd_queue.append(text)
#
#
# def input_wrapper(prompt):
#     print_wrapper(prompt)
#
#
#
#
# def convert(filename):
#
#     with patch('builtins.print', print_wrapper) as one:
#         with patch('builtins.input', input_wrapper) as two:
#
#
#
#
