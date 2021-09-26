from __future__ import print_function
from unittest.mock import patch, MagicMock
import os
from io import StringIO
cmd_queue = []
from flask import Flask, session, request, after_this_request, jsonify, make_response, url_for, redirect
from queue import Queue
from flask import render_template
from uuid import uuid4
from logical_expressions_quiz import m, main as run_quiz
import logging
import threading
import time
from json import dumps as dump_json
from time import sleep
from sys import stdout
import signal

app = Flask(__name__)
app.secret_key = "eirgjtaepogijeapgoijeagpoiejagpoiejagpoieajgpoerijg"

from helpers import Mocker

@app.route("/get_cli", methods=['GET', 'POST'])
def get_cli():
    print("Fetching")
    sleep(0.5)
    data = m.get_new_lines()
    res = make_response(dump_json({"message":data}), 200)
    print("fetched", data)

    return res

@app.route("/post_cli", methods=["POST"])
def post_cli():
    data = request.get_json()
    print("received the data", data)
    m.add_line(data)
    m.q.put(data)
    return get_cli()



@app.route('/play')
def play():
    return render_template("base.html")

def start_quiz_thread():
    run_quiz()

@app.route("/")
def hello():


    return redirect(url_for('play'))



if __name__ == "__main__":
    with open("output.txt", "w") as f:
        pass



    kwargs = {'host': '127.0.0.1', 'port': 5000, 'threaded': True, 'use_reloader': False, 'debug': False}

    flask_thread = threading.Thread(target=app.run, daemon=True, kwargs=kwargs).start()



    x = threading.Thread(target=run_quiz, daemon=True)
    x.start()

    x.join()

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
