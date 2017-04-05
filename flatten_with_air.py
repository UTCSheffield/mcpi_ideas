from mcpi import minecraft
from mcpi import block
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

print(pos)

#mc.player.setPos(128,128,128)

mc.setBlocks(-128,0,-128,128,50,128,block.AIR)
