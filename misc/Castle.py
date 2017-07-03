#castle script for minecraft by joshua cartwright

from mcpi import minecraft
from mcpi import block
import time
mc = minecraft.Minecraft.create()


#castle
pos = mc.player.getPos()

#clear
mc.setBlocks(pos.x-5,pos.y-1,pos.z-5,pos.x+5,pos.y+50,pos.z+5,block.AIR)
#floor
mc.setBlocks(pos.x-5,pos.y-1,pos.z-5,pos.x+5,pos.y,pos.z+5,block.COBBLESTONE)
#walls
mc.setBlocks(pos.x-5,pos.y,pos.z-5,pos.x+5,pos.y+4,pos.z-5,block.COBBLESTONE)
mc.setBlocks(pos.x-5,pos.y,pos.z+5,pos.x+5,pos.y+4,pos.z+5,block.COBBLESTONE)
mc.setBlocks(pos.x-5,pos.y,pos.z-5,pos.x-5,pos.y+4,pos.z+5,block.COBBLESTONE)
mc.setBlocks(pos.x+5,pos.y,pos.z-5,pos.x+5,pos.y+4,pos.z+5,block.COBBLESTONE)
#walkway
mc.setBlocks(pos.x-4,pos.y+3,pos.z-4,pos.x+4,pos.y+3,pos.z+4,block.COBBLESTONE)
mc.setBlocks(pos.x-3,pos.y+3,pos.z-3,pos.x+3,pos.y+3,pos.z+3,block.AIR)

#door
mc.setBlocks(pos.x+5,pos.y+1,pos.z,pos.x+5,pos.y+2,pos.z,block.AIR)

#stairs
mc.setBlocks(pos.x+4,pos.y+1,pos.z+3,pos.x+4,pos.y+2,pos.z+3,block.COBBLESTONE)
mc.setBlocks(pos.x+3,pos.y+1,pos.z+3,pos.x+3,pos.y+2,pos.z+3,block.COBBLESTONE)
mc.setBlock(pos.x+3,pos.y+3,pos.z+3,67,0)
mc.setBlock(pos.x+2,pos.y+1,pos.z+3,block.COBBLESTONE)
mc.setBlock(pos.x+2,pos.y+2,pos.z+3,67,0)
mc.setBlock(pos.x+1,pos.y+1,pos.z+3,67,0)

mc.setBlocks(pos.x-3,pos.y+1,pos.z+4,pos.x-3,pos.y+2,pos.z+4,block.COBBLESTONE)
mc.setBlocks(pos.x-3,pos.y+1,pos.z+3,pos.x-3,pos.y+2,pos.z+3,block.COBBLESTONE)
mc.setBlock(pos.x-3,pos.y+3,pos.z+3,67,2)
mc.setBlock(pos.x-3,pos.y+1,pos.z+2,block.COBBLESTONE)
mc.setBlock(pos.x-3,pos.y+2,pos.z+2,67,2)
mc.setBlock(pos.x-3,pos.y+1,pos.z+1,67,2)

mc.setBlocks(pos.x+3,pos.y+1,pos.z-4,pos.x+3,pos.y+2,pos.z-4,block.COBBLESTONE)
mc.setBlocks(pos.x+3,pos.y+1,pos.z-3,pos.x+3,pos.y+2,pos.z-3,block.COBBLESTONE)
mc.setBlock(pos.x+3,pos.y+3,pos.z-3,67,3)
mc.setBlock(pos.x+3,pos.y+1,pos.z-2,block.COBBLESTONE)
mc.setBlock(pos.x+3,pos.y+2,pos.z-2,67,3)
mc.setBlock(pos.x+3,pos.y+1,pos.z-1,67,3)

mc.setBlocks(pos.x-4,pos.y+1,pos.z-3,pos.x-4,pos.y+2,pos.z-3,block.COBBLESTONE)
mc.setBlocks(pos.x-3,pos.y+1,pos.z-3,pos.x-3,pos.y+2,pos.z-3,block.COBBLESTONE)
mc.setBlock(pos.x-3,pos.y+3,pos.z-3,67,1)
mc.setBlock(pos.x-2,pos.y+1,pos.z-3,block.COBBLESTONE)
mc.setBlock(pos.x-2,pos.y+2,pos.z-3,67,1)
mc.setBlock(pos.x-1,pos.y+1,pos.z-3,67,1)

#holes
mc.setBlock(pos.x+4,pos.y+2,pos.z+5,block.FENCE)
mc.setBlock(pos.x+2,pos.y+2,pos.z+5,block.FENCE)
mc.setBlock(pos.x,pos.y+2,pos.z+5,block.FENCE)
mc.setBlock(pos.x-2,pos.y+2,pos.z+5,block.FENCE)
mc.setBlock(pos.x-4,pos.y+2,pos.z+5,block.FENCE)

mc.setBlock(pos.x+4,pos.y+2,pos.z-5,block.FENCE)
mc.setBlock(pos.x+2,pos.y+2,pos.z-5,block.FENCE)
mc.setBlock(pos.x,pos.y+2,pos.z-5,block.FENCE)
mc.setBlock(pos.x-2,pos.y+2,pos.z-5,block.FENCE)
mc.setBlock(pos.x-4,pos.y+2,pos.z-5,block.FENCE)

mc.setBlock(pos.x+5,pos.y+2,pos.z+4,block.FENCE)
mc.setBlock(pos.x+5,pos.y+2,pos.z+2,block.FENCE)
mc.setBlock(pos.x+5,pos.y+2,pos.z-2,block.FENCE)
mc.setBlock(pos.x+5,pos.y+2,pos.z-4,block.FENCE)

mc.setBlock(pos.x-5,pos.y+2,pos.z+4,block.FENCE)
mc.setBlock(pos.x-5,pos.y+2,pos.z+2,block.FENCE)
mc.setBlock(pos.x-5,pos.y+2,pos.z,block.FENCE)
mc.setBlock(pos.x-5,pos.y+2,pos.z-2,block.FENCE)
mc.setBlock(pos.x-5,pos.y+2,pos.z-4,block.FENCE)

#holes roof
mc.setBlock(pos.x+4,pos.y+4,pos.z+5,block.AIR)
mc.setBlock(pos.x+2,pos.y+4,pos.z+5,block.AIR)
mc.setBlock(pos.x,pos.y+4,pos.z+5,block.AIR)
mc.setBlock(pos.x-2,pos.y+4,pos.z+5,block.AIR)
mc.setBlock(pos.x-4,pos.y+4,pos.z+5,block.AIR)

mc.setBlock(pos.x+4,pos.y+4,pos.z-5,block.AIR)
mc.setBlock(pos.x+2,pos.y+4,pos.z-5,block.AIR)
mc.setBlock(pos.x,pos.y+4,pos.z-5,block.AIR)
mc.setBlock(pos.x-2,pos.y+4,pos.z-5,block.AIR)
mc.setBlock(pos.x-4,pos.y+4,pos.z-5,block.AIR)

mc.setBlock(pos.x+5,pos.y+4,pos.z+4,block.AIR)
mc.setBlock(pos.x+5,pos.y+4,pos.z+2,block.AIR)
mc.setBlock(pos.x+5,pos.y+4,pos.z,block.AIR)
mc.setBlock(pos.x+5,pos.y+4,pos.z-2,block.AIR)
mc.setBlock(pos.x+5,pos.y+4,pos.z-4,block.AIR)

mc.setBlock(pos.x-5,pos.y+4,pos.z+4,block.AIR)
mc.setBlock(pos.x-5,pos.y+4,pos.z+2,block.AIR)
mc.setBlock(pos.x-5,pos.y+4,pos.z,block.AIR)
mc.setBlock(pos.x-5,pos.y+4,pos.z-2,block.AIR)
mc.setBlock(pos.x-5,pos.y+4,pos.z-4,block.AIR)

#well
time.sleep(.25)
mc.setBlocks(pos.x+1,pos.y+1,pos.z+1,pos.x-1,pos.y+3,pos.z-1,block.COBBLESTONE)
mc.setBlocks(pos.x+1,pos.y+2,pos.z,pos.x-1,pos.y+2,pos.z,block.AIR)
mc.setBlocks(pos.x,pos.y+2,pos.z-1,pos.x,pos.y+2,pos.z+1,block.AIR)
mc.setBlocks(pos.x,pos.y+1,pos.z,pos.x,pos.y+2,pos.z,block.AIR)
mc.setBlock(pos.x,pos.y+4,pos.z,block.COBBLESTONE)
mc.setBlock(pos.x+1,pos.y+1,pos.z,63,4)
#mc.setBlock(pos.x+2,pos.y,pos.z,block.AIR)

#bacement
time.sleep(.25)
mc.setBlocks(pos.x-5,pos.y-2,pos.z-5,pos.x+5,pos.y-6,pos.z+5,block.COBBLESTONE)
mc.setBlocks(pos.x-4,pos.y-2,pos.z-4,pos.x+4,pos.y-5,pos.z+4,block.AIR)
mc.setBlocks(pos.x-4,pos.y-5,pos.z-4,pos.x+4,pos.y-5,pos.z+4,block.BOOKSHELF)
mc.setBlocks(pos.x-3,pos.y-5,pos.z-3,pos.x+3,pos.y-5,pos.z+3,block.AIR)
mc.setBlocks(pos.x+1,pos.y-5,pos.z-1,pos.x+3,pos.y-5,pos.z+1,35,2)
mc.setBlocks(pos.x+4,pos.y-5,pos.z-1,pos.x+4,pos.y-5,pos.z+1,35,0)
mc.setBlock(pos.x+4,pos.y-5,pos.z+4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x+4,pos.y-5,pos.z-4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x-4,pos.y-5,pos.z+4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x-4,pos.y-5,pos.z-4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x,pos.y-6,pos.z,block.AIR)
mc.setBlock(pos.x,pos.y-7,pos.z,block.COBBLESTONE)
time.sleep(.25)
mc.setBlock(pos.x,pos.y+1,pos.z,block.WATER)
time.sleep(.25)
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y-4,pos.z,block.AIR)

#set location
mc.setBlock(pos.x+6,pos.y,pos.z,block.COBBLESTONE)
mc.setBlocks(pos.x+6,pos.y+1,pos.z,pos.x+6,pos.y+2,pos.z,block.AIR)
time.sleep(.25)
mc.player.setPos(pos.x+6,pos.y+1,pos.z)


