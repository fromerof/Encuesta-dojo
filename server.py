from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "top secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    print(request.form)
    session['username'] = request.form['name']
    session["ubicacion"] = request.form['ubicacion']
    session["lenguaje"] = request.form['lenguaje']
    session["comment"] = request.form['comentario']
    return redirect('/result')

@app.route('/result')
def result():
    print(request.form)
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)