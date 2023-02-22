import numpy as np
import car

if __name__ == '__main__':

    # Create a 2D world of 0's
    height = 4
    width = 6
    world = np.zeros((height, width))

    # Define the initial car state
    initial_position = [0, 0] # [y, x] (top-left corner)
    velocity = [0, 1] # [vy, vx] (moving to the right)
    initial_state = [initial_position, velocity]

    # Create a car object with these initial params
    carla = car.Car(initial_position, velocity, world)

    print('Carla\'s initial state is: ' + str(carla.state))

    # carla.turn_left()
    # carla.turn_left()
    # # carla.display_world()
    # carla.turn_left()
    # carla.move()
    # # for i in range(4):
    # #     carla.turn_left()
    # #     for j in range(3):
    # #         carla.move()
    # #
    # carla.display_world()

    # Using the move() and turn_left() functions, make carla traverse a 4x4 square path.

    carla.turn_left()
    carla.move()
    carla.turn_left()
    carla.move()
    carla.turn_left()
    carla.move()
    carla.turn_left()
    carla.move()

    # Display the world
    carla.display_world()