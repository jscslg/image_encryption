import numpy as np

def generate_random_indices(rows, cols):
    r = 3.94  # growth rate value for chaotic behaviour
    xN = KEY  # seed 
    seqMap = []

    for i in range(rows):
        list = []
        for j in range(cols):
            xN = r * xN * (1 - xN)
            list.append(xN)
        seqMap.append(np.argsort(list))

    return seqMap

def confusion(image):
    confused_img = np.array(image)
    (rows, cols) = image.shape
    x = generate_random_indices(rows, cols)
    for r in range(rows):
        for c in range(cols):
            confused_img[r, c], confused_img[r, x[r][c]] = confused_img[r, x[r][c]], confused_img[r, c]
    return confused_img

def generate_random_seq(rows, cols):
    r = 3.94  # growth rate for chaotic behaviour
    xN = KEY  # seed
    max = 1e6
    seqMap = []

    for i in range(rows):
        list = []
        for j in range(cols):
            #bitlist = []
            #for k in range(8):
            xN = r * xN * (1 - xN)
            #bitlist.append(0 if xN < 0.5 else 1)
            list.append(int((xN*max) % 256))
        seqMap.append(list)
    return seqMap

def diffusion(image):
    diffused_img = np.array(image)
    (rows, cols) = image.shape
    x = generate_random_seq(rows, cols)
    for r in range(rows):
        for c in range(cols):
            diffused_img[r, c] = diffused_img[r, c] ^ x[r][c]
    return diffused_img