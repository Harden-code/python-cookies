import sys
import easyocr
from PIL import Image


def find_max_height(text):
    ret = -1
    val = -1
    for idx, info in enumerate(text):
        position, *_ = info
        top, bottom, *_ = position
        height = bottom[0]-top[0]
        if val < height:
            ret = idx
            val = height
    return ret, val


def apply_mosaic(image, area, block_size):
    x1, y1, x2, y2 = area

    # 对给定区域进行马赛克处理
    for y in range(y1, y2, block_size):
        for x in range(x1, x2, block_size):
            box = (x, y, min(x2, x + block_size), min(y2, y + block_size))
            color = image.crop(box).getcolors()[0][1]
            image.paste(color, box)


def masaic(path):
    reader = easyocr.Reader(lang_list=['ch_sim'])
    text = reader.readtext(path)
    idx, _ = find_max_height(text)
    temp = Image.open(path)
    for index, data in enumerate(text):
        position, *info = data
        if index == idx:
            continue
        box = [e.astype('int') for e in (*position[0], *position[2])]
        try:
            apply_mosaic(temp, box, 10)
        except Exception as e:
            e.with_traceback()
            print(e, index, info[0])

    temp.save('temp.png')


args = sys.argv
if len(args) > 3 or len(args) < 2:
    raise RuntimeError('agrs 异常')
command, path = args
masaic(path)
