import requests
from PIL import Image
import numpy as np


def test_numpy():
    print('Создание массивов')
    m1 = np.array([1, 2, 3])
    m2 = np.array([4, 5, 6])
    print(m1)
    print(m2)
    print('Объединение массивов')
    m2d = np.vstack([m1, m2])
    print(m2d)
    print(m2d.shape, m2d.ndim, m2d.size)

    print('Математические операции')
    print(m2d + 100)
    print(m2d / 2)

    print('Преобразования')
    print(m2d.flatten())
    print(m2d.transpose())

    print('Вычисление суммы элементов вдоль оси 0 (суммируем столбцы)')
    print(m2d.sum(axis=0))


def test_requests():
    JSON_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
    r = requests.get(JSON_URL)
    print(r.status_code, r.headers['content-type'])
    print(r.json())

    JPG_URL = 'https://www.chevyavalanchefanclub.com/cafcna/index.php?media/the_beast-jpg.2958/full'
    r = requests.get(JPG_URL)
    print(r.status_code, r.headers['content-type'])

    with open('car.jpg', 'bw') as im_car:
        im_car.write(r.content)

    print(dir(r))

def test_pillow():
    im = Image.open('car.jpg')
    print(im.format, im.size, im.mode)
    w, h = im.size
    im.thumbnail((w//2, h//2))
    im.rotate(30).save('car_thumbnail.png')
    im.rotate(30).show()
    im.close()


test_numpy()
test_requests()
test_pillow()