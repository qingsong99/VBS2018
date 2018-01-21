import numpy as np
import pickle
import json
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='Query.json')
parser.add_argument('--output', type=str, default='result.txt')
parser.add_argument('--number', type=int, default=1000)
args = parser.parse_args()

GRID = 7

duration = time.time()
ivtIndex = np.load('Database/database.npy')
duration = time.time() - duration
print 'Loading database takes', duration, 'second'

class2id  = pickle.load(open('Database/class2id.pickle', 'rb'))
shot2id  = pickle.load(open('Database/shot2id.pickle', 'rb'))
nameShot = {}
for i in shot2id.items():
    nameShot[i[1]] = i[0]

const = np.array([10, 5, 5], dtype=np.uint16)


def cell(x, y):
    if (x < 0 or x >= GRID or y < 0 or y >= GRID):
        return -1
    return  x * GRID + y

def search(objects, ivtIndex):
    #Objects: [size, name, position(x, y)]
    N = ivtIndex.shape[0]
    score = np.zeros(shape=(N), dtype=np.uint16)
    idx = 0
    M = len(objects)
    while (idx < N):
        obj = 0
        while (obj < M):
            classID = class2id[objects[obj][0]]
            pos = objects[obj][1]
            obj = obj + 1
            vx = 0
            while (vx <= 0):
                vy = 0
                while (vy <= 0):
                    k = cell(pos[0] + vx, pos[1] + vy)
                    if (k != -1):
                        score[idx] = score[idx] +  const[vx * vx + vy * vy] * ivtIndex[idx][classID][k]
                    vy = vy + 1
                vx = vx + 1
        idx = idx + 1

    rank = np.argsort(score)
    rank = rank[::-1]
    return rank, score


def process():
    data = json.load(open(args.input))
    objects = []
    for obj in data:
        name = str(obj[0])
        pos = (int(obj[1]), int(obj[2]))
        objects.append([name, pos])

    duration = time.time()
    rank, scores = search(objects, ivtIndex)
    duration = time.time() - duration
    print 'Time Search', duration, 'second'

    output = file(args.output, 'w')
    for i in xrange(args.number):
        shot = 'TRECVID2016_%s.%s..txt\n' % (nameShot[rank[i]][4:9], nameShot[rank[i]])
        #print shot, scores[rank[i]]
        output.write(shot)
    output.close()

    done = file('flag.txt', 'w')
    done.write('Done')
    done.close()
    print 'Finish'

