# Get Started with Minecraft Pi Edition & Python

Use the arrow keys to go forward and back in the presentation.

---
## First Steps
1. Open up IDLE 3.
   * Click on "Menu" (top right) -> "Programming" -> "IDLE 3"
1. Open "1_Get_Started.py"
1. Open up Minecraft
   * Click on "Menu" (top right) -> "Games" -> "Minecraft"
   * Click "Start Game" -> "Create World"
---
## Move about a bit

* Once in Minecraft make sure you know how to get about
* A S W D
* Space bar to jump / fly
* Mouse to look, build blocks and destroy
* ESC to get your mouse back and get out of the Minecraft 

---

## Run your first code

1. Move the windows around so you can see this guide, IDLE and Minecraft
1. Click back into IDLE
1. Press F5 to run the code 
1. Quickly click back into Minecraft to see what happens.

---
# The Code

``` Python
from mcpi import minecraft
from mcpi import block

# Store the connection to Minecraft in a variable called mc
mc = minecraft.Minecraft.create()

# Store the position player is standing in a variable called pos 
pos = mc.player.getTilePos() 

# Store a string which contains the x,y,z of your position
message = "You are at x="+str(pos.x)+", y="+str(pos.y)+", z="+str(pos.z)

# Print the message in the python screen
print(message)

# Send the message to the Minecraft chat
mc.postToChat(message)

# A quicker way to print the position
message2 = "You are at "+str(pos)
```

---

# Make some stuff
Below your current code type

```python
mc.setBlock(pos, block.DIAMOND_BLOCK)

above = pos
above.y = above.y + 4
mc.setBlock(above, block.TNT.id, 1)
```
You can get a list of the blocks by typing "block." and then press CTRL + SPACE

---
# I'm walking on sunshine
```python
while True:
  pos = mc.player.getTilePos() 
  mc.setBlock(pos, block.GOLD_BLOCK)
```
---
# Rainbow Road

```python
while True:
  pos = mc.player.getTilePos() 
  num = (pox.x+pos.y+pos.z) % 16
  mc.setBlock(pos, block.WOOL.id, num)
```




