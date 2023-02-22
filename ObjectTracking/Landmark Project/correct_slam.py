import numpy as np
from helpers import display_world
from helpers import make_data
import robot_class
import sys


def initialize_constraints(N, num_landmarks, world_size):
    ''' This function takes in a number of time steps N, number of landmarks, and a world_size,
        and returns initialized constraint matrices, omega and xi.'''

    ## Recommended: Define and store the size (rows/cols) of the constraint matrix in a variable

    ## TODO: Define the constraint matrix, Omega, with two initial "strength" values
    ## for the initial x, y location of our robot
    omega = np.zeros((2 * (N + num_landmarks), 2 * (N + num_landmarks)))
    omega[0][0] = 1
    omega[1][1] = 1

    ## TODO: Define the constraint *vector*, xi
    ## you can assume that the robot starts out in the middle of the world with 100% confidence
    xi = np.zeros((2 * (N + num_landmarks), 1))
    xi[0][0] = world_size / 2
    xi[1][0] = world_size / 2

    return omega, xi

## TODO: Complete the code to implement SLAM

## slam takes in 6 arguments and returns mu,
## mu is the entire path traversed by a robot (all x,y poses) *and* all landmarks locations
def slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise):
    ## TODO: Use your initilization to create constraint matrices, omega and xi
    omega, xi = initialize_constraints(N, num_landmarks, world_size)

    ## TODO: Iterate through each time step in the data
    ## get all the motion and measurement data as you iterate

    ## TODO: update the constraint matrix/vector to account for all *measurements*
    ## this should be a series of additions that take into account the measurement noise

    ## TODO: update the constraint matrix/vector to account for all *motion* and motion noise

    for t in range(len(data)):
        measurements = data[t][0]
        motion = data[t][1]
        t *= 2

        # Measurement update for each landmark detected
        for measurement in measurements:
            # print(np.shape(measurement))
            lm_i = 2 * (measurement[0] + N)

            # Measurement update for both x and y. Adding idx allows to loop and do X and Y without repeating code.
            for idx in range(2):
                # diagonals

                omega[t + idx][t + idx] += 1. / measurement_noise
                omega[lm_i + idx][lm_i + idx] += 1. / measurement_noise

                # non-diagonals
                omega[t + idx][lm_i + idx] += -1. / measurement_noise
                omega[lm_i + idx][t + idx] += -1. / measurement_noise

                # Update Xi.
                xi[t + idx] += -measurement[idx + 1] / measurement_noise
                xi[lm_i + idx] += measurement[idx + 1] / measurement_noise

        # Motion update for both x and y. Adding idx allows to loop and do X and Y without repeating code.
        for idx in range(2):
            # diagonals
            print([t + idx],[t + idx])
            print([t + idx + 2],[t + idx + 2])
            omega[t + idx][t + idx] += 1. / motion_noise
            omega[t + idx + 2][t + idx + 2] += 1. / motion_noise

            # non-diagonals
            omega[t + idx][t + idx + 2] += -1. / motion_noise
            omega[t + idx + 2][t + idx] += -1. / motion_noise

            # Update Xi.
            xi[t + idx] += -motion[idx] / motion_noise
            xi[t + idx + 2] += motion[idx] / motion_noise

    original_stdout = sys.stdout
    with open('correct_results.txt', 'w') as f:
        sys.stdout = f
        print(omega, file=f)
        print('', file=f)
        print(xi, file=f)
        sys.stdout = original_stdout

    ## TODO: After iterating through all the data
    ## Compute the best estimate of poses and landmark positions
    ## using the formula, omega_inverse * Xi
    mu = np.linalg.inv(np.matrix(omega)) * xi

    return mu  # return `mu`

if __name__ == '__main__':
    # your implementation of slam should work with the following inputs
    # feel free to change these input values and see how it responds!

    # world parameters
    num_landmarks = 5  # number of landmarks
    N = 20  # time steps
    world_size = 100.0  # size of world (square)

    # robot parameters
    measurement_range = 50.0  # range at which we can sense landmarks
    motion_noise = 2.0  # noise in robot motion
    measurement_noise = 2.0  # noise in the measurements
    distance = 20.0  # distance by which robot (intends to) move each iteratation

    # make_data instantiates a robot, AND generates random landmarks for a given world size and number of landmarks
    data = make_data(N, num_landmarks, world_size, measurement_range, motion_noise, measurement_noise, distance)

    mu = slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise)
