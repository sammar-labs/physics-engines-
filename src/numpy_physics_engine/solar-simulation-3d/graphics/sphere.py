import math
import numpy as np


def genrate_sphere(radius=1.0, segments=24, rings=16):
  vertices = []
  for i in range(rings + 1):
    phi = math.pi * i / rings
    for j in range(segments + 1):
      theta = 2 * math.pi * j / segments
      x = radius * math.sin(phi) * math.cos(theta)
      y = radius * math.cos(phi)
      z = radius * math.sin(phi) * math.sin(theta)
      vertices.append([x, y, z])

  # Return ko loops ke bahar hona chahiye taake saare vertices return hon
  return np.array(vertices, dtype=np.float32)


# Test print (agar module run kiya jaye)
if __name__ == "__main__":
  print(genrate_sphere())