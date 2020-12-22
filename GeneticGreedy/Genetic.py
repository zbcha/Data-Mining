import numpy as np

def point_gen(num):
    idx = np.random.choice(200, size=5, replace=0)
    out = np.column_stack((np.unravel_index(idx,(10,20))))
    return(out)


for i in range(10):
    test_size=10
    print(point_gen(test_size))
