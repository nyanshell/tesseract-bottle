import io

import pytesseract
from PIL import Image
from bottle import Bottle, request, run

app = Bottle()


@app.post("/ocr")
def ocr():
    img_data = request.body.read()
    img = Image.open(io.BytesIO(img_data))
    try:
        return pytesseract.image_to_string(img)
    except:
        return ''


if __name__ == "__main__":
    run(app=app, host='0.0.0.0', port=8088, debug=True)
