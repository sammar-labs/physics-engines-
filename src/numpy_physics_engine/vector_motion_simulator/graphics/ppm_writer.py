import numpy as np

def save_ppm(image, filename):
    height, width, channel = image.shape
    if channel != 3:
        raise ValueError("RGB IMAGE required")
    
    # Ensure image data is 8-bit unsigned integers (0-255)
    image = np.asarray(image, dtype=np.uint8)
    
    with open(filename, "wb") as file:
        # Uppercase P6, space between width and height, and 255 max value
        header = f"P6\n{width} {height}\n255\n"
        file.write(header.encode("ascii"))
        file.write(image.tobytes())

if __name__ == "__main__":
    # Create a 200x200 RGB NumPy array filled with red (255, 0, 0)
    sample_image = np.zeros((2000, 200, 3), dtype=np.uint8)
    sample_image[:, :] = [255, 0, 0]
    
    save_ppm(sample_image, "image.ppm")
