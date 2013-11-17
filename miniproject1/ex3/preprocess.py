import numpy as np
from PIL import Image
import random

# this file will contain all the 16x16 input patches for the simulation
# each row will be a string form of numpy array
# rows for xon and xoff will be alternating
outname = 'images/patches_info.data'

def normalize(data):

    data = (data - data.mean()) / data.std()
    return data
    

def process_file(filename, patchesOutfile):

    img = Image.open(filename)
    imgData = np.array(img, float)

    normalized = normalize(imgData)

    normalizedFilename = filename.replace('.bmp', '_normalized.data')
    normOut = open(normalizedFilename, 'w')
    normOut.write(normalized.tostring())
    normOut.close()
    
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

        #patch = normalized[row:row+16, col:col+16]
        #xon = np.maximum(patch, 0.0)
        #xoff = -np.minimum(patch, 0.0)

def preprocess():
    files = []
    for i in xrange(1, 11):
        name = 'images/im' + str(i) + '.bmp'
        files.append(name)

    allPatches = open(outname, 'w')

    for filename in files:
        print 'Processing file %s' % filename
        process_file(filename, allPatches)

    allPatches.close()


if __name__ == "__main__":
    preprocess()
