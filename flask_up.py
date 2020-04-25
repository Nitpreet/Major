"""
Created on Fri Apr 24 21:39:15 2020

@author: kuljeet
"""
from flask import request, redirect,Flask,jsonify
import os
import cv2
from flask import Flask, jsonify, request
from dir import*
from lib import* #library file
# from line_removal import*  #morphological operation file
from tessarct import*  #tessaract processing file

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "image/"
@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" in request.files:
        dir()  #to make directory
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        line()  #calling line_removal file
        return jsonify("Image uploaded succesfully",tess())   #tessarct.py file
    else:
        return jsonify("OOPS!! image not uploaded")

app.run(debug=True)
        