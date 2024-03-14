from flask import Flask, request, render_template
from flask import redirect, url_for
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import os

#load_dotenv()

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
path_to_upload_main_image = "upload_main_image/"

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/admin/index.html")
def manager():
    return render_template("index.html")

@app.route("/upload", methods=['POST', 'GET'])
def upload():

    if request.method == 'POST':
        
        # Get the main image
        main_image = request.files['main_image']
        print(main_image)
        #other_images = request.files.getlist('other_images')

        # Process the main image
        if main_image.filename == '':
            return 'No main image'
        
        if main_image and allowed_file(main_image.filename):
            main_image_filename = secure_filename(main_image.filename)
            main_image.save(os.path.join(path_to_upload_main_image, main_image_filename))

        # Process other images
        if other_images and allowed_file(other_images.filename):
            for other_image in other_images:
                other_image.save(os.path.join(path_to_upload_other_image, other_image))
                DB.insert_image(last_id, other_image)
    
    return redirect(url_for("manager"))

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)