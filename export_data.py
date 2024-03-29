import json
import os

import click
from PIL import Image
from PIL.ExifTags import TAGS

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

@click.command()
@click.argument("folder_path")
@click.argument("json_filepath")
@click.option('--wh', is_flag=True, help="only export width and height")
def export_exif_data(folder_path, json_filepath, wh):
    export_data = {}
    for f in os.listdir(folder_path):
        try:
            full_path = os.path.join(folder_path, f)
            image_name = os.path.splitext(f)[0]
            pil_image = Image.open(full_path)
            width, height = pil_image.size
            export_data[image_name] = {"width": width, "height": height}
            exif_data = pil_image._getexif()
            if exif_data and not wh:
                for (k, v) in exif_data.items():
                    export_data[image_name][f"{TAGS.get(k)}"] = f"{v}"
        except Exception as e:
            logger.warning(f"Problem with {f}: {e}")

    with open(json_filepath, "w") as w_handle:
        json.dump(export_data, w_handle, indent=4, sort_keys=True)
    print(f"Exported data to {json_filepath}. Have an awesome day!")

if __name__ == '__main__':
    export_exif_data()
