from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth

import os
path = '/home/pi/Pictures/blink/'
i = 0
while os.path.exists(path + "snap_%s.jpg" % i):
    i += 1
output = path + "snap_%i.jpg" % i


blink = Blink()
# Can set no_prompt when initializing auth handler
auth = Auth({"username": "peter@amytislabs.com", "password": "5QLVFn9F$QZrjDyU"}, no_prompt=True)
blink.auth = auth
blink.start()

for name, camera in blink.cameras.items():
    # print(name)                   # Name of the camera
    # print(camera.attributes)      # Print available attributes of camera
    # blink.refresh(force=True)    # force a cache update USE WITH CAUTION
    # camera.image_from_cache.raw  # bytes-like image object (jpg)
    # camera.video_from_cache.raw  # bytes-like video object (mp4)

    camera.snap_picture()       # Take a new picture with the camera
    blink.refresh()             # Get new information from server
    camera.image_to_file(output)
    # camera.video_to_file('/local/path/for/video.mp4')