# Buildings

![UTC Logo](images/UTC_Logo.png)

# First Steps

1. Open up the "mcpi_ideas" folder
1. Double click on "3_Buildings.py" and Python will open.

# Code Explained

Same code at the top.

```python
pos = mc.player.getPos() #Find the players position

print(pos) # print the position

mc.player.setPos(0,50,0) # Teleport Steve into the sky in the centre of the world.
mc.setBlocks(0,-1,0,6,6,6,block.STONE_BRICK) # Make a solid box of blocks between 0,-1,0 and 6,6,6 
mc.setBlocks(1,0,1,5,5,5,block.AIR)

```

# Can you think how to :-

1. Make the building out of another material (this site might help http://www.stuffaboutcode.com/p/minecraft-api-reference.html )
2. Make it look like your house
3. Do a roof
4. Make it build near your player

Look at the "Castle.py" and "Large Tower.py" in the "misc" folder for inspiration. 
