import numpy as np


def projectile_velocity(speed, angle_degrees):
  angle = np.radians(angle_degrees)
  ux = speed * np.cos(angle)
  uy = speed * np.sin(angle)
  return np.array([ux, uy])


def projectile_position(start, speed, angle_degrees, time, gravity=9.8):
  start = np.array(start, dtype=float)
  angle = np.radians(angle_degrees)
  x = start[0] + speed * np.cos(angle) * time
  y = start[1] + speed * np.sin(angle) * time - 0.5 * gravity * time**2
  return np.array([x, y])


def maximum_height(speed, angle_degrees, gravity=9.8):
  angle = np.radians(angle_degrees)
  return (speed**2 * np.sin(angle) ** 2) / (2 * gravity)


def projectile_range(speed, angle_degrees, gravity=9.8):
  angle = np.radians(angle_degrees)
  return (speed**2 * np.sin(2 * angle)) / gravity


def flight_time(speed, angle_degrees, gravity=9.8):
  angle = np.radians(angle_degrees)
  return (2 * speed * np.sin(angle)) / gravity


if __name__ == "__main__":
  # Position at t=100s starting at, speed=100 m/s, angle=100 deg
  print("Position:", projectile_position([100, 200], 100, 100, 100))

  # Initial velocity components for scalar speed=100 m/s, angle=100 deg
  print("Initial Velocity:", projectile_velocity(100, 100))
