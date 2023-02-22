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

    covariance = np.eye(2) * 99

    return omega, xi, covariance


def update_constraints(data, i, omega, xi, measurement_noise, covariance, R):
    global new_covariance
    measurements = data[0]
    # motions = data[1]

    for k in range(len(measurements)):
        # print(i)
        landmark_id = measurements[k][0] + N
        measurement = measurements[k]

        ## TODO: update the constraint matrix/vector to account for all *measurements*
        ## this should be a series of additions that take into account the measurement noise
        omega[2 * i][2 * i] += 1. / measurement_noise
        omega[2 * i + 1][2 * i + 1] += 1. / measurement_noise
        omega[2 * landmark_id][2 * landmark_id] += 1. / measurement_noise
        omega[2 * landmark_id + 1][2 * landmark_id + 1] += 1. / measurement_noise

        omega[2 * i][2 * landmark_id] += -1. / measurement_noise
        omega[2 * i + 1][2 * landmark_id + 1] += -1. / measurement_noise
        omega[2 * landmark_id][2 * i] += -1. / measurement_noise
        omega[2 * landmark_id + 1][2 * i + 1] += -1. / measurement_noise

        xi[2 * i] += -measurement[1] / measurement_noise
        xi[2 * i + 1] += -measurement[2] / measurement_noise
        xi[2 * landmark_id] += measurement[1] / measurement_noise
        xi[2 * landmark_id + 1] += measurement[2] / measurement_noise

        S = covariance + R
        K = covariance/S

        new_covariance = covariance - K * covariance


    return omega, xi, new_covariance

## TODO: update the constraint matrix/vector to account for all *motion* and motion noise
def predict_constraints(data,i, omega, xi, motion_noise, covariance, Q):
    motions = data[1]

    omega[2 * i][2 * i] += 1. / motion_noise
    omega[2 * i + 1][2 * i + 1] += 1. / motion_noise
    omega[2 * i + 2][2 * i + 2] += 1. / motion_noise
    omega[2 * i + 3][2 * i + 3] += 1. / motion_noise

    omega[2 * i][2 * i + 2] += -1. / motion_noise
    omega[2 * i + 1][2 * i + 3] += -1. / motion_noise
    omega[2 * i + 2][2 * i] += -1. / motion_noise
    omega[2 * i + 3][2 * i + 1] += -1. / motion_noise

    xi[2 * i] += -motions[0] / motion_noise
    xi[2 * i + 1] += -motions[1] / motion_noise
    xi[2 * i + 2] += motions[0] / motion_noise
    xi[2 * i + 3] += motions[1] / motion_noise

    covariance = covariance + Q

    return omega, xi, covariance

## TODO: Complete the code to implement SLAM

## slam takes in 6 arguments and returns mu,
## mu is the entire path traversed by a robot (all x,y poses) *and* all landmarks locations
def slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise, R, Q):
    ## TODO: Use your initilization to create constraint matrices, omega and xi

    omega, xi, cov = initialize_constraints(N, num_landmarks, world_size)

    # print(np.shape(omega))

    ## TODO: Iterate through each time step in the data
    ## get all the motion and measurement data as you iterate

    for i in range(len(data)):
        # print(_)
        omega, xi, cov = update_constraints(data[i], i, omega, xi, measurement_noise, cov, R)
        omega, xi, cov = predict_constraints(data[i], i, omega, xi, motion_noise, cov, Q)
        print(cov)

    ## TODO: After iterating through all the data
    ## Compute the best estimate of poses and landmark positions
    ## using the formula, omega_inverse * Xi

    mu = np.linalg.solve(omega, xi)

    return mu  # return `mu`


if __name__ == '__main__':
    # your implementation of slam should work with the following inputs
    # feel free to change these input values and see how it responds!

    Q = np.eye(2) * 0.05
    R = 5

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

    mu = slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise, R, Q)

