from .utils import smart_read_image_v1, image_to_base64, HttpsCall
import numpy as np

def draw_bounding_boxes(image, box_dict_list):
    from PIL import ImageDraw
    draw = ImageDraw.Draw(image)
    width, height = image.size
    for box_dict in box_dict_list:
        x_min = box_dict['x_min'] * width
        y_min = box_dict['y_min'] * height
        x_max = box_dict['x_max'] * width
        y_max = box_dict['y_max'] * height
        score = box_dict['score']
        font_size = int(24 + np.log(width))
        draw.rectangle((x_min, y_min, x_max, y_max), outline='red', width=5)
        draw.text((x_min, y_min), f"{score:.2f}", fill='green', font_size=font_size, stroke_width=2, stroke_fill='black')
    
    return image

class EazyaiLogoV4:
    url = f"https://api.dfpipe.com/detect-logo"

    def __init__(self):
        pass

    def detect_image(self, image):
        # image: see utils.smart_read_image_v1
        image = smart_read_image_v1(image)

        body = {
            "action": "detect_logo",
            "images": [
                {'item_id': '1', 'content_base64': image_to_base64(image)}
            ],
        }
        body = HttpsCall.call_with_json_body(self.url,body)
        return body