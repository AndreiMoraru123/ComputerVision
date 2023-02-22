import numpy as np
from math import sin, cos, pi
from matplotlib import pyplot as plt


# TODO - Complete the methods in the vehicle class. If the
#        requirements of any method are unclear, look at
#        the testing code in testing.py (you'll need to
#        click on the "Jupyter" logo in the top left and
#        then open testing.py)
#
#        If you really get stuck, take a look at the
#        solution code in the next segment.

class Vehicle:
    def __init__(self):
        self.x = 0.0  # meters
        self.y = 0.0
        self.heading = 0.0  # radians
        self.history = []

    def drive_forward(self, displacement):
        """
        Updates x and y coordinates of vehicle based on
        heading and appends previous (x,y) position to
        history.
        """
        self.x = self.x + displacement * cos(self.heading)
        self.y = self.y + displacement * sin(self.heading)
        self.history.append((self.x, self.y))

    def set_heading(self, heading_in_degrees):
        """
        Sets the current heading (in radians) to a new value
        based on heading_in_degrees. Vehicle heading is always
        between 0 and 2 * pi.
        """

        self.heading = heading_in_degrees * pi / 180

    def turn(self, angle_in_degrees):
        """
        Changes the vehicle's heading by angle_in_degrees. Vehicle
        heading is always between 0 and 2 * pi.
        """
        self.heading = self.heading + angle_in_degrees * pi / 180

    def show_trajectory(self):
        """
        Creates a scatter plot of vehicle's trajectory.
        """
        x = [i[0] for i in self.history]
        y = [i[1] for i in self.history]
        plt.scatter(x, y)

        plt.show()


# timestamp, dispacement, yaw_rate, acceleration
data_list = [(0.0, 0, 0.0, 0.0),
             (0.25, 0.0, 0.0, 19.600000000000001),
             (0.5, 1.2250000000000001, 0.0, 19.600000000000001),
             (0.75, 3.6750000000000003, 0.0, 19.600000000000001),
             (1.0, 7.3500000000000005, 0.0, 19.600000000000001),
             (1.25, 12.25, 0.0, 0.0),
             (1.5, 17.149999999999999, -2.8290163190291664, 0.0),
             (1.75, 22.049999999999997, -2.8290163190291664, 0.0),
             (2.0, 26.949999999999996, -2.8290163190291664, 0.0),
             (2.25, 31.849999999999994, -2.8290163190291664, 0.0),
             (2.5, 36.749999999999993, -2.8290163190291664, 0.0),
             (2.75, 41.649999999999991, -2.8290163190291664, 0.0),
             (3.0, 46.54999999999999, -2.8290163190291664, 0.0),
             (3.25, 51.449999999999989, -2.8290163190291664, 0.0),
             (3.5, 56.349999999999987, -2.8290163190291664, 0.0)]


# def get_speeds(data_list):
#     dt = 0.25
#     speed = []
#     last_disp = 0
#     for i in range(len(data_list)):
#         if i == 0:
#             speed.append(0)
#
#         else:
#             speed.append((data_list[i][1] - last_disp) / dt)
#             last_disp = data_list[i][1]
#     return speed
#
#
# def integral(f, t1, t2, dt=0.1):
#     # area begins at 0.0
#     area = 0.0
#
#     # t starts at the lower bound of integration
#     t = t1
#
#     # integration continues until we reach upper bound
#     while t < t2:
#         # calculate the TINY bit of area associated with
#         # this particular rectangle and add to total
#         dA = f(t) * dt
#         area += dA
#         t += dt
#     return area
#
#
# import math
#
#
# def get_headings(data_list):
#     headings = []
#     radhead = 0
#     last_time = 0
#     dt = 0.25
#     for i in range(len(data_list)):
#         if i == 0:
#             headings.append(0)
#         else:
#             d_radhead = integral(lambda t: data_list[i][2], last_time, data_list[i][0])
#             last_time = dt - data_list[i][0]
#             # d_radhead = data_list[i][2] * dt
#             radhead += d_radhead
#             radhead %= (2 * math.pi)
#             headings.append(radhead)
#     return headings

import math


def get_speeds(data_list):
    last_time = 0.0
    last_disp = 0.0
    speeds = [0.0]
    for entry in data_list[1:]:
        # unpack the entry
        ts, disp, yaw, acc = entry

        # calculate avg speed for this time interval
        dx = disp - last_disp
        dt = ts - last_time
        if dt < 0.0001:
            print("error! dt is too small")
            speeds.append(0.0)
            continue
        v = dx / dt

        # add to history of speeds
        speeds.append(v)

        # update last_time and last_disp to new vals
        last_time = ts
        last_disp = disp

    return speeds


def get_headings(data_list):
    last_time = 0.0
    theta = 0.0
    thetas = [0.0]
    for entry in data_list[1:]:
        ts, disp, yaw, acc = entry
        dt = ts - last_time
        d_theta = dt * yaw
        theta += d_theta
        theta %= (2 * math.pi)
        thetas.append(theta)
        last_time = ts
    return thetas


def get_x_y(data_list):

    speeds = get_speeds(data_list)
    headings = get_headings(data_list)
    x = [0.0]
    y = [0.0]
    for i in range(1, len(data_list)):
        dx = speeds[i] * cos(headings[i])
        dy = speeds[i] * sin(headings[i])
        x.append(x[i - 1] + dx)
        y.append(y[i - 1] + dy)
    return x, y


def show_x_y(data_list):
    x, y = get_x_y(data_list)
    plt.scatter(x, y)
    plt.plot(x,y)
    plt.show()


if __name__ == "__main__":
    velocities = get_speeds(data_list)
    print(velocities)
    print(len(velocities))
    print(len(data_list))
    headings = get_headings(data_list)
    print(headings)
