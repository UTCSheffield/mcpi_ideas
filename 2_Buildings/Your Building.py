from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

print(pos)

mc.player.setPos(0,50,0)
mc.setBlocks(0,-1,0,6,6,6,block.STONE_BRICK)
mc.setBlocks(1,0,1,5,5,5,block.AIR)
