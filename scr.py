import ffmpy

ff = ffmpy.FFmpeg(inputs={'input.mp4':None },outputs={'frames/frame%d.png': '-r 1 -f image2'})

ff.run()