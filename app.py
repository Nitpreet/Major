from flask import request, redirect,Flask,render_template
import os
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "."

@app.route("/", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            print("Image saved")

            return redirect(request.url)

    return render_template("image_upload.html")
if __name__ == '__main__':
    app.run(debug=True)
