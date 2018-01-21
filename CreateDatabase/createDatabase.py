import pickle
import numpy as np
import os.path

NUM_SHOT = 335944
GRID = 5

def get(pos, W, H):
    x = pos[0]
    y = pos[1]
    kx = 0
    ky = 0
    dW = W * 1.0 / GRID
    dH = H * 1.0 / GRID
    for k in xrange(GRID):
        if (k * dW <= x):
            kx = k
        if (k * dH <= y):
            ky = k
    return (kx, ky)

def getGrid(x, y, w, h, W, H):
    A = (x - w / 2, y - h / 2)
    B = (x + w / 2, y + h / 2)
    cellA = get(A, W, H)
    cellB = get(B, W, H)
    list = []
    for i in xrange(cellA[0], cellA[1] + 1):
        for j in xrange(cellB[0], cellB[1] + 1):
            list.append(j * GRID + i)
    return list

def createShot2id(fileName):
    shot2id = {}
    file = open(fileName, 'r')
    ITER = 0
    for line in file:
        [shot, first, last] = line[:-1].split('#')
        shot2id[shot] = ITER
        ITER = ITER + 1

    pickle.dump(shot2id, open('../Server/Database/shot2id.pickle', 'wb'))
    return shot2id

def createClass2id(fileName):
    class2id = {}
    file = open(fileName, 'r')
    ITER = 0
    for line in file:
        str = line[:-1]
        class2id[str] = ITER
        ITER = ITER + 1
    pickle.dump(class2id, open('../Server/Database/class2id.pickle', 'wb'))
    return class2id

def process(video, indexing, shot2id, class2id, fileShot):
    file = open(fileShot, 'r')
    segment = []
    for line in file:
        [sid, first, last] = line[:-1].split('#')
        segment.append((shot2id[sid], int(first), int(last)))

    data = video['content']
    (H, W) = video['info'][:2]
    for frame in data:
        frameid = frame['frame']
        attributes = frame['attributes']
        idx = -1
        for seg in segment:
            if (seg[1] <= frameid and frameid <= seg[2]):
                idx = seg[0]
                break
        if (idx == -1):
            continue

        for attrib in attributes:
            classID = class2id[attrib[0]]
            prob = attrib[1]
            position = getGrid(attrib[2][0], attrib[2][1], attrib[2][2], attrib[2][3], W, H)
            for pos in position:
                indexing[idx][classID][pos] = int(prob * 10)

if __name__ == '__main__':
    fileData  = 'data/%d.pickle'
    fileShot = 'shot/%d.txt'
    indexing = np.zeros((NUM_SHOT, 80, GRID * GRID), dtype=np.uint16)
    shot2id = createShot2id('shot.txt')
    class2id = createClass2id('coco.names')
    for i in xrange(35345, 39937 + 1):
        if (os.path.isfile(fileData % i)):
            video = pickle.load(open(fileData % i, 'rb'))
        else:
            print 'Cannot open file', fileData % i
            continue

        process(video, indexing, shot2id, class2id, fileShot % i)
        print 'Finish file %d / 39937' % i

    np.save('database', indexing)







