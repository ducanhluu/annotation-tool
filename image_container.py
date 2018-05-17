from PIL import Image
import pandas as pd
import os

def _get_image_and_bbox(filename):
    data = pd.read_table(filename,
                         delim_whitespace=True, header=None, skiprows=[0, 1]).values
    img_name = data[:, 0]
    bboxes = data[:, 1:]

    image_box_map = dict(zip(img_name, bboxes))
    return image_box_map


def _crop_image_by_bbox(image_path, bbox):
    img = Image.open(image_path)
    cropped_image = img.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
    return cropped_image


class ImageContainer:
    def __init__(self, source_file, dest_file, img_dir):
        self._image_box_map = _get_image_and_bbox(source_file)
        self._dest_file = dest_file
        self._img_dir = img_dir

    def _get_next_image(self):
        return self._image_box_map.popitem()


    def get_image(self):
        image_path, box = self._get_next_image()
        image_path = os.path.join(self._img_dir, image_path)
        return _crop_image_by_bbox(image_path, box)