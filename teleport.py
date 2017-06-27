from mcpi import minecraft
from mcpi import block

# Store the connection to Minecraft in a variable called mc
ip_addr = "127.0.0.1"
mc = minecraft.Minecraft.create(ip_addr)

# Store the position player is standing in a variable called pos 
pos = mc.player.getTilePos() 

newpos = pos
newpos.y += 20
mc.player.setTilePos(newpos)

