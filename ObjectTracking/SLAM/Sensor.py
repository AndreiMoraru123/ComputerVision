import numpy as np


def mu_from_positions(initial_pos, move1, move2, Z0, Z1, Z2):
    ## TODO: construct constraint matrices
    ## and add each position/motion constraint to them

    # initialize constraint matrices with 0's
    # Now these are 4x4 because of 3 poses and a landmark
    omega = np.zeros((4, 4))
    xi = np.zeros((4, 1))

    # add initial pose constraint
    omega[0][0] = 1
    xi[0] = initial_pos

    # account for the first motion, dx = move1
    omega += [[1., -1., 0., 0.],
              [-1., 1., 0., 0.],
              [0., 0., 0., 0.],
              [0., 0., 0., 0.]]
    xi += [[-move1],
           [move1],
           [0.],
           [0.]]

    # account for the second motion
    omega += [[0., 0., 0., 0.],
              [0., 1., -1., 0.],
              [0., -1., 1., 0.],
              [0., 0., 0., 0.]]
    xi += [[0.],
           [-move2],
           [move2],
           [0.]]

    ## TODO: Include three new sensor measurements for the landmark, L
    # incorporate first sense
    omega += [[1., 0., 0., -1.],
              [0., 0., 0., 0.],
              [0., 0., 0., 0.],
              [-1., 0., 0., 1.]]
    xi += [[-Z0],
           [0.0],
           [0.0],
           [Z0]]

    # incorporate second sense
    omega += [[0., 0., 0., 0.],
              [0., 1., 0., -1.],
              [0., 0., 0., 0.],
              [0., -1., 0., 1.]]
    xi += [[0.],
           [-Z1],
           [0.],
           [Z1]]

    # incorporate third sense
    omega += [[0., 0., 0., 0.],
              [0., 0., 0., 0.],
              [0., 0., 1., -1.],
              [0., 0., -1., 1.]]
    xi += [[0.],
           [0.],
           [-Z2],
           [Z2]]

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
    mu = mu_from_positions(-3, 5, 3, 10, 5, 1)
    print('Mu: \n', mu)