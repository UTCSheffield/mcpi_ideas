from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

print(pos)

#mc.player.setPos(0,50,0)
#mc.setBlocks(0,-1,0,11,8,11,block.STONE_BRICK)
#mc.setBlocks(1,0,1,9,9,10,b

mc.setBlocks(0,-1,0,12,5,5,block.STONE_BRICK)
mc.setBlocks(0,1,1,11,4,4,block.AIR)
#mc.setBlocks(0,-1,0,5,6,5,block.STONE_BRICK)
#mc.setBlock(pos.x+6,pos.y+5,pos.z+3,block
#mc.setBlocks(-128,-1,-128,128,50,128,block.AIR)
