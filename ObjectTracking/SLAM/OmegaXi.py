import numpy as np


def mu_from_positions(initial_pos, move1, move2):
    ## TODO: construct constraint matrices
    ## and add each position/motion constraint to them

    # initialize constraint matrices with 0's
    omega = np.zeros((3, 3))
    xi = np.zeros((3, 1))

    # add initial pose constraint
    omega[0][0] = 1
    xi[0] = initial_pos

    # account for the first motion, dx = move1
    omega += [[1., -1., 0.],
              [-1., 1., 0.],
              [0., 0., 0.]]
    xi += [[-move1],
           [move1],
           [0.0]]

    # account for the second motion
    omega += [[0., 0., 0.],
              [0., 1., -1.],
              [0., -1., 1.]]
    xi += [[0.],
           [-move2],
           [move2]]

    # display final omega and xi
    print('Omega: \n', omega)
    print('\n')
    print('Xi: \n', xi)
    print('\n')

    ## TODO: calculate mu as the inverse of omega * xi
    ## recommended that you use: np.linalg.inv(np.matrix(omega)) to calculate the inverse
    omega_inv = np.linalg.inv(np.matrix(omega))
    mu = omega_inv * xi
    return mu


if __name__ == '__main__':
    # call function and print out `mu`
    mu = mu_from_positions(-3, 5, 3)
    print('Mu: \n', mu)
