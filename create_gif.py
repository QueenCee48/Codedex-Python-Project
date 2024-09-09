import imageio.v3 as iio

filenames = [
    'gifpic1.png',
    'gifpic2.png',
    'gifpic3.png',
    'gifpic4.png',
    'gifpic5.png',
    'gifpic6.png',
    'gifpic7.png',
    'gifpic8.png'
]

images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('helloworld.gif', images, duration = 500, loop = 0)
