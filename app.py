from flask import Flask, redirect, render_template, request, url_for, flash, session
import array
import xml.etree.ElementTree as ET
import uuid
from random import randint
import re
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        flash("Нажата кнопка")
        subprocess.run(["gpio -1 mode 5 out"], shell=True)
        subprocess.run(["gpio -1 write 5 1"], shell=True)
        return render_template("/index.html")

if __name__ == '__main__':
    app.run(debug=False, port = 8003, host='0.0.0.0')
