import os
from flask import Flask,render_template,url_for

app = Flask(__name__)
Doctor_Name = "Karnam Dheeraj"
@app.route("/")
def index():
    return render_template("index.html",Doctor_Name = Doctor_Name)

@app.route("/services")
def services():
    return render_template("services.html",Doctor_Name = Doctor_Name)

@app.route("/about")
def about():
    return render_template("about.html",Doctor_Name = Doctor_Name)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)