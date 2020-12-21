import os
from flask import Flask, flash, request, redirect, url_for, render_template,jsonify
import requests
import base64
import io
from PIL import Image

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    print(request.method)
    if request.method == "POST":
        payload = request.form.to_dict(flat=False)
        im_b64 = payload['image'][0]  
        im_binary = base64.b64decode(im_b64) # characters into bytes
        buf = io.BytesIO(im_binary)
        img = Image.open(buf)
        img.save("geeks.jpg")

        return render_template("login.html")

    else:
        return render_template("login.html")


@app.route("/")
def test(any):
    return f"hello"


if __name__ == "__main__":
    app.run(host ="0.0.0.0")