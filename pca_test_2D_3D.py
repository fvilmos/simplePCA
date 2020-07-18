import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from simplePCA import simplePCA
import timeit

if __name__ == '__main__':

    # generate 3D dataset
    xyz = np.random.random((500, 3)) * 10.0
    xyz[:350, 2:] = xyz[:350, :1]

    start = timeit.default_timer()
    m, eigva, eigve = simplePCA(xyz)
    print("pca execution time, 3D dataset:", timeit.default_timer() - start)

    # scale the eienvector and reduce with half
    eigve = eigve * eigva * 0.5

    fig = plt.figure(figsize=(4,4))
    ax = mplot3d.Axes3D(fig)
    ax.scatter3D(xyz.T[0], xyz.T[1], xyz.T[2], c='r')
    plt.quiver(m[0], m[1], m[2], eigve[0, :], eigve[1, :], eigve[2:], zorder=3)
    ax.view_init(azim=30)
    plt.show()


    #generate 2D dataset, 50% noise
    xy = np.random.randn(500, 2)
    xy[0:300:1,0] = xy[0:300:1,1]

    start = timeit.default_timer()
    m, eigva, eigve = simplePCA(xy)
    print("pca execution time, 2D dataset:", timeit.default_timer() - start)

    # scale the eienvector and reduce with half
    eigve = eigve * eigva

    plt.quiver(m[0],m[1],eigve[0,:],eigve[1,:], zorder=3, scale=5.0)
    plt.plot(xy[:,0],xy[:,1], 'rp',m[0], m[1],'bx', zorder=1)

    plt.show()
