from flask import Flask
from random import randint
from flask import render_template
import os

PATTERN_FOLDER = "static"
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = "Annotator"
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    random_number = randint(0,len(quotes)-1)
    quote = quotes[random_number]
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    posts = []
    return render_template('index.html', **locals())


@app.route("/annotation")
def annotation():
    pattern_images = []
    for pattern in os.listdir(PATTERN_FOLDER):
        pattern_images.append(pattern)

    return render_template('annotation.html', **locals())

if __name__ == "__main__":
    app.run()