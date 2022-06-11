# Spike

Spike is a GUI library for the pygame library.
<br>
This should be used to handle the frames, buttons, text inputs and menus in a pygame game.

## Colors

Manually typing tuples with rgb values looks pretty ugly.
<br>
That's why Spike has a file just to deal with colors.
<br>
We've already declared the colors black, white, red, green, blue, cyan, pink, yellow, orange, purple, grey and brown.
<br>

```python
import spike
# Some code
surface.fill(spike.RED)
# Some more code
```

<br>
More examples: examples/colors.py and examples/random_colors.py

## Button

Pygame doesn't have any way to create buttons.
<br>
I used to create classes to deal with this, and now I added that to spike.
<br>
First create the button object
<br>

```python
import pygame
import spike
button = spike.Button(pygame.Rect(20, 20, 200, 100), spike.GREEN, text='My button')
```

<br>
Then, in your main loop, tell the button when the mouse button is down.
<br>

```python
if event.type == pygame.MOUSEBUTTONDOWN:
	if button.in_button(pygame.mouse.get_pos()):
		# What you want to do when the button is pressed
```

<br>
And finally, render the button
<br>

```python
button.render(surface)
pygame.display.update()
```

<br>
More examples: examples/button.py

## Images

To be honest its pretty easy to deal with images in pygame, but I still chose to make this module in an attempt to make it even easier.
<br>
First create the image object
<br>

```python
import pygame
import spike
image = spike.Image(pygame.Rect(10, 10, 100, 100), pygame.image.load('player.png')
```

<br>
And then render the image
<br>

```python
image.render(surface)
pygame.display.update()
```

<br>
More examples: examples/images.py

## Text

Text is a little harder to deal in pygame than images, but again I chose to make this trying to make it easier.
<br>
First create the text object
<br>

```python
import pygame
import spike

text = spike.Text('Hello world', 10, 10, font_type='ubuntumono', text_size=50, color=spike.RED)
```

<br>
And then render the text
<br>

```python
text.render(surface)
pygame.display.update()
```

<br>
More examples: examples/text.py

## Text input

Text inputs would be repetitive to make in pygame so I would really rather use spike for this.
<br>
First create a text input object
<br>

```python
import pygame
import sys

text_input = spike.TextInput(pygame.Rect(10, 10, 300, 50), placeholder='Whats your name', border=5) 
```

<br>
Then tell the text input when the mouse is down
<br>

```python
if event.type == pygame.MOUSEBUTTONDOWN:
	if text_input.in_input(pygame.mouse.get_pos()):
		text_input.selected = True
	else:
		text_input.selected = False
```

<br>
Next tell the text input when the player presses a key on the keyboard
<br>

```python
if event.type == pygame.KEYDOWN:
	text_input.received_input(event)
elif event.type == pygame.KEYUP:
	text_input.ended_input(event)
```

<br>
And finally render the text input
<br>

```python
text_input.render(surface, fps)
```


More examples at examples/text_input.py

## Checkboxes

Checkboxes would also be pretty hard to make manually in pygame
<br>
First make the checkbox object
<br>

```python
import pygame
import spike

checkbox = spike.CheckBox(pygame.Rect(10, 10, 20, 20), text='Save changes', border_color=spike.BLUE)
```

<br>
Then see if the checkbox has been pressed
<br>

```python
if event.type == pygame.MOUSEBUTTONDOWN:
	checkbox.marked = checkbox.in_checkbox(pygame.mouse.get_pos())
```

<br>
And finally render the checkbox
<br>

```python
checkbox.render(surface)
```

More examples at examples/checkbox.py

## Select

This is kind of like html select input
<br>
First make the select object
<br>

```python
select = spike.Select(pygame.Rect(20, 20, 170, 50), 'Football club', text_size=35)
```

<br>
And then add all the options you want to the select input
<br>

```python
select.add_option('Barcelona')
select.add_option('Real Madrid')
select.add_option('Liverpool')
select.add_option('PSG')
```

<br>
Next see when the player presses the mouse and check if he clicked the select input or any of its options
<br>

```python
if event.type == pygame.MOUSEBUTTONDOWN:
	mouse_pos = pygame.mouse.get_pos()

	select.in_option(mouse_pos)

	if select.in_select(mouse_pos):
		select.selected = not select.selected
	else:
		select.selected = False
```

<br>
And finally render the select input
<br>

```python
select.render(surface)
```
More examples at examples/select.py

## Drag and drop

Drag and drop was actually way easier than I thought to implement in pygame
<br>
First create the drag and drop object
<br>

```python
drag_and_drop = spike.DragAndDrop(pygame.Rect(10, 10, 100, 100), spike.RED)
```

<br>
Then tell the drag and drop object when the mouse is down
<br>

```python
if event.type == pygame.MOUSEBUTTONDOWN:
	drag_and_drop.mouse_down(pygame.mouse.get_pos())
```

<br>
Also tell the drag and drop object when the mouse is up
<br>

```python
if event.type == pygame.MOUSEBUTTONUP:
	drag_and_drop.mouse_up()
```

<br>
Next tell the drag and drop object when the mouse moved
<br>

```python
drag_and_drop.mouse_moved(pos)
```

<br>
And finally, render the drag and drop object
<br>

```python
drag_and_drop.render(surface)
```

## Frames

First create the frame object
<br>

```python
import pygame
import spike

frame= spike.Frame(pygame.Rect(50, 50, 500, 100), spike.RED, border=5, border_color=spike.YELLOW)
```

<br>
Add all the entities you need to the frame
<br>

```python
text = spike.Text('Some text', 70, 70, color=spike.RED)
frame.add_entity(text)
```

<br>
And finally render the frame
<br>

```python
frame.render(surface, fps)
```

More examples at examples/frames.py and examples/frames_complex.py





