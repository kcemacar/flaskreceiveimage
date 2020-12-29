import os
from flask import Flask, flash, request, redirect, url_for, render_template,jsonify
import requests
import base64
import io
from PIL import Image
from pstimg import *
from visioner import *
from random import random


app = Flask(__name__)
counter = 1

@app.route("/", methods = ["POST", "GET"])
def home():
    global counter
    print(request.method)
    if request.method == "POST":
        img_name = "img"+str(counter)
        pimg = PostedImage("image")
        pimg.bufimg()
        pimg.save("static/preprocessed/"+img_name+".jpg")
        
        vsnr = Visioner("static/preprocessed/"+img_name+".jpg")
    
        vsnr.saveImage(vsnr.findred(),"static/processed/"+img_name+".jpg")
        counter+=1
        return render_template("login.html")

    else:
        return render_template("login.html")



    

if __name__ == "__main__":
    app.run(host ="0.0.0.0")

