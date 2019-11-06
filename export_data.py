import click
import os
from exif import Image as ExifImage
from PIL import Image
from PIL.ExifTags import TAGS
import json
import sys

@click.command()
@click.argument("folder_path")
@click.argument("json_filepath")
def export_exif_data(folder_path, json_filepath):
    export_data = {}
    for f in os.listdir(folder_path):
        full_path = os.path.join(folder_path, f)
        pil_image = Image.open(full_path)
        width, height = pil_image.size
        export_data[full_path] = {"width": width, "height": height}
        exif_data = pil_image._getexif()
        if exif_data:
            for (k, v) in exif_data.items():
                export_data[full_path][f"{TAGS.get(k)}"] = f"{v}"
        print(export_data)
        with open(json_filepath, "w") as w_handle:
            json.dump(export_data, w_handle, indent=4, sort_keys=True)
        # with open(full_path, "rb") as image_handle:
        #     exif_image = ExifImage(image_handle)
        # print(f"{full_path} {width} {height} {getattr(exif_image, gps_latitude)}")

if __name__ == '__main__':
    export_exif_data()
