import subprocess
from pathlib import Path
def create_video(frames_directory,output_file,fps=30):
    frames_directory=Path(frames_directory)
    output_file=Path(output_file)
    output_file.parent.mkdir(parents=True,exist_ok=True)
    command=["ffmpeg","-y","-framerate",str(fps),"-i",str(frames_directory/"frame_%03d.ppm"),"-c:v","libx264","-pix_fmt","yuv420p",str(output_file)
             ]
    subprocess.run(command,check=True)
    