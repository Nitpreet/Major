#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:39:15 2020

@author: nitpreet
"""
from flask import request, redirect,Flask,render_template
import os
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "."

@app.route("/upload-image/", methods=["GET", "POST"])
def upload_image():

    if request.method == "GET":

        if request.files:

            image = request.files["image"]

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            print("Image saved")

            return redirect(request.url)

    return render_template("image_upload.html")
if __name__ == '__main__':
    app.run(debug=True)