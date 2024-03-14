from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)


# s3 = boto3.client("stylishs3")

# limit picture files
upload_folder = '/main_img'
allow_pic_format = {"pdf", "png", "jpg", "jpeg", "gif"}
app.config['UPLOAD_FOLDER'] = upload_folder


@app.route("/admin/product.html")
def index():
    return render_template('test.html')

@app.route('/admin/test.html', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        main_image = request.files['main_image']  
        print("---------")
        print("success")
        
    return render_template('create_product.html')


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5050)
