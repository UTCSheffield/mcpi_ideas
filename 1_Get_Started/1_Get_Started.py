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

mc.setBlock(pos, block.DIAMOND_BLOCK)
above = pos
above.y = above.y + 4
mc.setBlock(above, block.TNT.id, 1)


while True:
  pos = mc.player.getTilePos() 
  num = (pos.x+pos.y+pos.z) % 16
  mc.setBlock(pos, block.WOOL.id, num)
