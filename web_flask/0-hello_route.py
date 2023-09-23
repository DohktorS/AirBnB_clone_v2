#!/usr/bin/python3
"""This module uses Flask and starts a web application"""


from flask import Flask
app = Flask(_name_)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello world for flask"""
    return "Hello HBNB!"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port="5000")
