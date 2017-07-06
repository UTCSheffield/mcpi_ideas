from mcpi import minecraft
from mcpi import block

# Store the connection to Minecraft in a variable called mc
ip_addr = "192.168.1.30"
mc = minecraft.Minecraft.create(ip_addr)

# Store the position player is standing in a variable called pos 
pos = mc.player.getTilePos() 

newpos = pos
newpos.y += 4000
mc.player.setTilePos(newpos)
