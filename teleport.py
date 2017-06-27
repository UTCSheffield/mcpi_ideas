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
<<<<<<< HEAD

=======
>>>>>>> 4ffd885c095b2974d117df9903eb4e16d8bff10b
