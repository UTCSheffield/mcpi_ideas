from mcpi import minecraft
from mcpi import block
import time
mc = minecraft.Minecraft.create()

#while(True):
#    pos = mc.player.getPos()
#    print(pos)
#    #mc.player.setPos(0,0,0)
#    #mc.setBlock(pos.x,pos.y-1,pos.z,block.AIR)
#    #mc.setBlocks(0,0,0,30,30,30,block.AIR) big block
#    mc.setBlocks(pos.x-1,pos.y-1,pos.z-1,pos.x+1,pos.y+2,pos.z+1,block.WOOD_PLANKS)
#    mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y+1,pos.z,block.AIR)
#    mc.setBlock(pos.x,pos.y+3,pos.z,block.WOOD_PLANKS)
#    mc.setBlocks(pos.x+1,pos.y,pos.z,pos.x+1,pos.y+1,pos.z,block.AIR)
#    time.sleep(5)

#mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y,pos.z,block.)

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

#stairs
mc.setBlocks(pos.x+4,pos.y+1,pos.z+3,pos.x+4,pos.y+2,pos.z+3,block.COBBLESTONE)
mc.setBlocks(pos.x-3,pos.y+1,pos.z+4,pos.x-3,pos.y+2,pos.z+4,block.COBBLESTONE)
mc.setBlocks(pos.x+3,pos.y+1,pos.z-4,pos.x+3,pos.y+2,pos.z-4,block.COBBLESTONE)
mc.setBlocks(pos.x-4,pos.y+1,pos.z-3,pos.x-4,pos.y+2,pos.z-3,block.COBBLESTONE)

#well
time.sleep(1)
mc.setBlocks(pos.x+1,pos.y+1,pos.z+1,pos.x-1,pos.y+3,pos.z-1,block.COBBLESTONE)
mc.setBlocks(pos.x+1,pos.y+2,pos.z,pos.x-1,pos.y+2,pos.z,block.AIR)
mc.setBlocks(pos.x,pos.y+2,pos.z-1,pos.x,pos.y+2,pos.z+1,block.AIR)
mc.setBlocks(pos.x,pos.y+1,pos.z,pos.x,pos.y+2,pos.z,block.AIR)
mc.setBlock(pos.x,pos.y+4,pos.z,block.COBBLESTONE)

#bacement
time.sleep(1)
mc.setBlocks(pos.x-5,pos.y-2,pos.z-5,pos.x+5,pos.y-6,pos.z+5,block.COBBLESTONE)
mc.setBlocks(pos.x-4,pos.y-2,pos.z-4,pos.x+4,pos.y-5,pos.z+4,block.AIR)
mc.setBlock(pos.x+4,pos.y-5,pos.z+4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x+4,pos.y-5,pos.z-4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x-4,pos.y-5,pos.z+4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x-4,pos.y-5,pos.z-4,block.GLOWSTONE_BLOCK)
mc.setBlock(pos.x,pos.y-6,pos.z,block.AIR)
mc.setBlock(pos.x,pos.y-7,pos.z,block.COBBLESTONE)
time.sleep(1)
mc.setBlock(pos.x,pos.y+1,pos.z,block.WATER)
time.sleep(1)
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y-4,pos.z,block.AIR)
