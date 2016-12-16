from bge import logic as GL
from bge import render

height = render.getWindowHeight()
width = render.getWindowWidth()

scene = GL.getCurrentScene()

overheadCam = scene.objects["OverheadCam"]
camera = scene.objects["Camera"]

camera.setViewport(0, 0, width, height)
overheadCam.setViewport(0, int(height*0.7), int(width*0.3), height)

overheadCam.setOnTop()

overheadCam.useViewport = True
camera.useViewport = True