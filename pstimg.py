import os
from flask import Flask, flash, request, redirect, url_for, render_template,jsonify
import requests
import base64
import io
from PIL import Image



class PostedImage:
    def __init__(self,name):
        self.name = name
        self.payload = request.form.to_dict(flat=False)
        self.im_b64 = self.payload[self.name][0]
        self.im_binary = base64.b64decode(self.im_b64) # characters into bytes
        

    def bufimg(self):
        self.buf = io.BytesIO(self.im_binary)
        self.img = Image.open(self.buf)
    
    def save(self, filename):
        self.filename=filename
        self.img.save(self.filename)