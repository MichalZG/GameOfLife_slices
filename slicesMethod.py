import numpy as np
import time

x = 10

w = np.array([[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0],
              [0, 0 ,1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]], dtype=float)

w = np.random.random_integers(0, 1, (x + 1, x + 1))
print w[1:-1, 1:-1]

w[0, ] = w[-1, ] = w[:, 0] = w[:, -1] = 0

while True:

    n_w = np.zeros(w.shape)

    n_w[1:-1, 1:-1] += w[:-2, :-2] + w[:-2, 1:-1] + w[:-2, 2:] + \
                       w[1:-1, :-2]               + w[1:-1, 2:] + \
                       w[2:, :-2]  + w[2:, 1:-1]  + w[2:, 2:]

    mask_live = w == 1
    mask_2 = n_w == 2

    n_w = np.where(n_w > 3, 0, n_w)
    n_w = np.where(n_w < 2, 0, n_w)
    n_w = np.where((mask_live * mask_2) == True, 1, n_w)
    n_w = np.where(n_w == 2, 0, n_w)
    n_w = np.where(n_w == 3, 1, n_w)

    time.sleep(1)
    print('')
    print(n_w[1:-1, 1:-1])
    w = n_w
