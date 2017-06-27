from mcpi import minecraft
from mcpi import block

# Store the connection to Minecraft in a variable called mc
mc = minecraft.Minecraft.create("127.0.0.1")

# Store the position player is standing in a variable called pos 
pos = mc.player.getTilePos() 

newpos = pos
newpos.y += 20
mc.player.setTilePos(newpos)
