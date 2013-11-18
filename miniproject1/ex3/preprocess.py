import numpy as np
from PIL import Image
import random

def normalize(data):

    data = (data - data.mean()) / data.std()
    return data
    

def process_file(filename):

    img = Image.open(filename)
    imgData = np.array(img, float)

    normalized = normalize(imgData)

    normalizedFilename = filename.replace('.bmp', '_normalized.data')
    normOut = open(normalizedFilename, 'w')
    normOut.write(normalized.tostring())
    normOut.close()

    patchesFilename = filename.replace('.bmp', '_patches.data')
    patchesOutfile = open(patchesFilename, 'w')
    
    chosen = set([])

    for i in xrange(5000):
        # choose next 16x16 patch
        while True:
            row = random.randint(0, len(imgData) - 16 - 1)
            col = random.randint(0, len(imgData[0]) - 16 - 1)
            if (row,col) not in chosen:
                chosen.add((row,col))
                break

        patchesOutfile.write('%d %d\n' % (row, col))

    patchesOutfile.close()

def preprocess():
    files = []
    for i in xrange(1, 11):
        name = 'images/im' + str(i) + '.bmp'
        files.append(name)

    for filename in files:
        print 'Processing file %s' % filename
        process_file(filename)


if __name__ == "__main__":
    preprocess()
