import numpy as np
import os
import pandas as pd
import sys
import StringIO
from PIL import Image


def get_image_and_bbox(filename):
    data = pd.read_table(filename,
                         delim_whitespace=True, header=None, skiprows=[0, 1]).values
    img_name = data[:, 0]
    bboxes = data[:, 1:]

    image_box_map = dict(zip(img_name, bboxes))
    return image_box_map


def crop_image_by_bbox(image_path, bbox):
    img = Image.open(image_path)
    img.show()
    cropped_image = img.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
    return cropped_image


from itertools import islice
img_box_map = get_image_and_bbox(sys.argv[1])

n_items = list(islice(img_box_map.items(), 5))

for image_path, bbox in n_items:
    image_path = os.path.join(sys.argv[2], image_path)
    image = crop_image_by_bbox(image_path, bbox)

    image.show()