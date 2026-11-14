import numpy as np
def fade_canvas(canvas,alpha=0.9):
    faded=(
        canvas.pixels.astype(np.float32)*alpha
    )
    canvas.pixels[:]=np.clip(faded,0,255).astype(np.uint8)
    