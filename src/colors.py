import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 150, 0)
PURPLE = (100, 0, 100)
GREY = (100, 100, 100)
BROWN = (100, 50, 0)

def random_color():
	color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	return color

def is_color(color):
	if len(color) != 3: return False
	if not (0 < color[0] < 256): return False
	if not (0 < color[1] < 256): return False
	if not (0 < color[2] < 256): return False
	return True	


