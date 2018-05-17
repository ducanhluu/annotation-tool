from flask import Flask, send_file
from random import randint
from flask import render_template
import os
from io import BytesIO
from image_container import ImageContainer
import base64

PATTERN_FOLDER = "static"
IMG_DIR = "/home/luud/dataset/deep_fashion"
SOURCE_FILE = "/home/luud/dataset/deep_fashion/Anno/list_bbox.txt"
DEST_FILE = ""

app = Flask(__name__)

img_container = ImageContainer(SOURCE_FILE, DEST_FILE, IMG_DIR)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    b64 = base64.b64encode(img_io.read())
    return b64


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
    image_to_annotate = img_container.get_image()
    encoded_string = serve_pil_image(image_to_annotate)
    pattern_images = []
    for pattern in os.listdir(PATTERN_FOLDER):
        pattern_images.append(pattern)

    return render_template('annotation.html', pattern_images=pattern_images, encoded_string=encoded_string)

if __name__ == "__main__":
    app.run()