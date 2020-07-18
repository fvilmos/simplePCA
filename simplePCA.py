import numpy as np
def simplePCA(arr):
    '''

    :param arr: input array of shape shape[N,M]
    :return:
        mean - center of the multidimensional data,
        eigenvalues - scale,
        eigenvectors - direction
    '''

    # calculate mean
    m = np.mean(arr, axis=0)

    # center data
    arrm = arr-m

    # calculate the covariance, decompose eigenvectors and eigenvalues
    # M * vect = eigenval * vect
    # cov = M*M.T
    Cov = np.cov(arrm.T)
    eigval, eigvect = np.linalg.eig(Cov.T)

    # return mean, eigenvalues, eigenvectors
    return m, eigval, eigvect
