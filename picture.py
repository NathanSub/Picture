"""
picture.py
Author: Nathan Subrahmanian
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
window = Color(0xdee5ef, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(300, 200, thinline, blue)
chimney = RectangleAsset(50, 70, thinline, red)
door = RectangleAsset(40, 60, thinline, black)
window1 = CircleAsset(40, thinline, window)
window2 = CircleAsset(40, thinline, window)
# Now display a rectangle
Sprite(rectangle, (300,180))
Sprite(chimney, (350,110))
Sprite(door, (450, 320))
Sprite(window1, (480, 200))
Sprite(window2, (340, 200))

myapp = App()
myapp.run()

# add your code here /\  /\  /\


myapp = App()
myapp.run()
