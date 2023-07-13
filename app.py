from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from main import *

#app = Flask(__name__, template_folder='../frontend/templates', static_folder= "../frontend/static")
app = Flask(__name__, template_folder='frontend/templates/', static_folder= os.getcwd()) 


app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

smt = image_browser(12800, False) 

@app.route("/")
def index():
    return render_template('index.html') 


@app.route("/KNNSearch/<file>/<k>", methods=['GET'])
def KNNSearch(file, k):
    k = int(k)
    res, tiempo = smt.KNN_SEARCH(file, k)
    #res, tiempo = smt.KNN_SEARCH_RTREE(file, k)
    #res, tiempo = smt.KDTREE(file, k)

    print(res)
    print(tiempo)
    return render_template('result.html', data = res, tiempo = tiempo, original = file)


@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['archivo']
  k = request.form['K datos']
  print(k)
  filename = secure_filename(f.filename)
  f.save(os.path.join(app.instance_path, 'uploads', secure_filename(f.filename)))
  # Si se quiere eliminar el archivo usar remove(UPLOADS_PATH + filename)

  return redirect(url_for('KNNSearch', file = filename, k = k))


if __name__ == '__main__':
    #smt = some_class(14500, True) # true or false is a flag that indicates if it is needed to process al 14000 images
    app.run(debug=True, use_reloader = False)
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='../frontend/static/images/logo_utec.png'))
    