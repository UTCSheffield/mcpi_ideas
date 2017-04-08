# Buildings


Use the arrow keys to go forward and back in the presentation.

---
## First Steps

1. Open up the "mcpi_ideas" folder and "2_Buildings"
1. Double click on "Your Building.py" and Python will open.

# Code Explained


```python
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

print(pos)

mc.player.setPos(0,50,0)
mc.setBlocks(0,-1,0,6,6,6,block.STONE_BRICK)
mc.setBlocks(1,0,1,5,5,5,block.AIR)

```

---

# Why is this a building?

---
# Can you think how to :-

1. Make the building out of another material  (this site might help http://www.stuffaboutcode.com/p/minecraft-api-reference.html )
2. Make it look like your house
1. Do a roof
1. Make it build near your player


Look at the other files in the folder for inspiration 


