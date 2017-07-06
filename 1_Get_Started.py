from mcpi import minecraft
from mcpi import block

# Store the connection to Minecraft in a variable called mc
mc = minecraft.Minecraft.create()


while True:
    pos = mc.player.getTilePos()
    num = (pos.x+pos.y+pos.z) % 16
    tempy = pos.y - 1
    pos.y = tempy
    mc.setBlock(pos, block.WOOL.id, num)
