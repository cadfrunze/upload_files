from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
# import datetime


app = Flask(__name__)
folder: str = 'uploads' #datetime.datetime.now().strftime(r"%Y-%m-%d_%H-%M-%S")
os.makedirs(folder, exist_ok=True)
app.config['UPLOAD_FOLDER'] = folder
#EXTENNSII: set = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route('/', methods=['GET', 'POST'])
def upload():
    mesaj: str = ''
    if request.method == 'POST':
        f = request.files.getlist("fisier")
        # if f and f.filename.rsplit('.', 1)[-1].lower() in EXTENNSII:
        #     nume = secure_filename(f.filename)
        #     f.save(os.path.join(app.config['UPLOAD_FOLDER'], nume))
        #     mesaj = 'Incarcat'
        # else: mesaj = 'Nepermis'
        for file in f:
            if not file:
                continue
            nume = secure_filename(file.filename)
            if not nume:
                continue
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], nume))
        mesaj = 'Incarcat'
    return render_template("upload.html", mesaj=mesaj)

if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=False) # localhost
    app.run(host="127.0.0.1", debug=False, port=5000) # tailscale
