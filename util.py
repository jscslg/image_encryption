import numpy as np

def convertKey(key):
    key=float(key)
    while int(key)>0:
        key/=10
    return key

def generate_random_indices(rows, cols,key):
    r = 3.94  # growth rate value for chaotic behaviour
    xN = key  # seed 
    seqMap = []

    for i in range(rows):
        list = []
        for j in range(cols):
            xN = r * xN * (1 - xN)
            list.append(xN)
        seqMap.append(np.argsort(list))

    return seqMap

def confusion(image,key):
    confused_img = np.array(image)
    (rows, cols) = image.shape
    x = generate_random_indices(rows, cols, convertKey(key))
    for r in range(rows):
        for c in range(cols):
            confused_img[r, c], confused_img[r, x[r][c]] = confused_img[r, x[r][c]], confused_img[r, c]
    return confused_img

def generate_random_seq(rows, cols,key):
    r = 3.94  # growth rate for chaotic behaviour
    xN = key  # seed
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

def diffusion(image,key):
    diffused_img = np.array(image)
    (rows, cols) = image.shape
    x = generate_random_seq(rows, cols,convertKey(key))
    for r in range(rows):
        for c in range(cols):
            diffused_img[r, c] = diffused_img[r, c] ^ x[r][c]
    return diffused_img

def decrypt_diffusion(image,key):
    # reverse diffusion
    (rows, cols) = image.shape
    x = generate_random_seq(rows, cols,convertKey(key))
    for r in range(rows):
        for c in range(cols):
            image[r, c] = image[r, c] ^ x[r][c]
    return image

def decrypt_confusion(image,key):
    # reverse confusion
    (rows, cols) = image.shape
    x = generate_random_indices(rows, cols,convertKey(key))
    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            image[r, c], image[r, x[r][c]] = image[r, x[r][c]], image[r, c]
    return image

def decrypt(image,key):
    decrypted_image = np.array(image)
    decrypted_image = decrypt_diffusion(decrypted_image,key)
    decrypted_image = decrypt_confusion(decrypted_image,key)
    return decrypted_image