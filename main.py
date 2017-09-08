from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def noNinja():
    return render_template('index.html')

@app.route('/ninjas')

def showNinjas():
    return render_template('ninjas.html')

@app.route('/ninjas/<color>')

def showOneNinja(color):
    if color == 'blue':
        y = "../static/leonardo.jpg"
    elif color == 'orange':
        y = "../static/michelangelo.jpg"
    elif color == 'red':
        y = "../static/raphael.jpg"
    elif color == 'purple':
        y = "../static/donatello.jpg"
    else:
        y = "../static/notapril.jpg"
    return render_template('ninja.html', turtle = y)

app.run(debug=True)