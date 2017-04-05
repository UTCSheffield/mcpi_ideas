from mcpi import minecraft
from mcpi import block
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

print(pos)

mc.player.setPos(0,53,0)

mc.setBlocks(-128,0,-128,128,50,128,block.AIR)
mc.setBlocks(0,0,0,12,12,12,block.WOOD_PLANKS)
mc.setBlocks(1,1,1,11,11,11,block.AIR)
mc.setBlocks(11,0,0,11,2,0,block.AIR)
mc.setBlocks(11,1,5,11,1,5,int(block.STAIRS_COBBLESTONE.id),2)
mc.setBlocks(11,2,6,11,2,6,int(block.STAIRS_COBBLESTONE.id),2)
mc.setBlocks(11,3,7,11,3,7,int(block.STAIRS_COBBLESTONE.id),2)
mc.setBlocks(11,4,8,11,4,8,int(block.STAIRS_COBBLESTONE.id),2)
mc.setBlocks(11,5,9,11,5,9,int(block.STAIRS_COBBLESTONE.id),2)
mc.setBlocks(11,6,10,11,6,10,int(block.STAIRS_COBBLESTONE.id),2)


mc.setBlocks(11,1,6,11,1,11,block.WOOD_PLANKS)
mc.setBlocks(11,2,7,11,2,11,block.WOOD_PLANKS)
mc.setBlocks(11,3,8,11,3,11,block.WOOD_PLANKS)
mc.setBlocks(11,4,9,11,4,11,block.WOOD_PLANKS)
mc.setBlocks(11,5,10,11,5,11,block.WOOD_PLANKS)
mc.setBlock(11,1,6,block.GLOWSTONE_BLOCK)

mc.setBlock(11,6,11,block.WOOD_PLANKS)
mc.setBlocks(0,6,0,10,6,11,block.WOOD_PLANKS)
mc.setBlocks(1,11,1,11,11,11,block.GLOWSTONE_BLOCK)
mc.setBlocks(10,11,10,10,11,2,block.WOOD_PLANKS)
mc.setBlocks(10,11,10,2,11,10,block.WOOD_PLANKS)
mc.setBlocks(2,11,2,2,11,10,block.WOOD_PLANKS)
mc.setBlocks(2,11,2,10,11,2,block.WOOD_PLANKS)
mc.setBlocks(11,3,1,11,3,2,block.WOOD_PLANKS)
mc.setBlocks(8,2,0,2,3,0,block.GLASS_PANE)
mc.setBlock(11,0,0,int(block.STAIRS_COBBLESTONE.id),2)

mc.setBlock(11,1,6,block.GLOWSTONE_BLOCK)
mc.setBlock(11,2,7,block.GLOWSTONE_BLOCK)
mc.setBlock(11,3,8,block.GLOWSTONE_BLOCK)
mc.setBlock(11,4,9,block.GLOWSTONE_BLOCK)
mc.setBlock(11,5,10,block.GLOWSTONE_BLOCK)
mc.setBlock(11,4,9,block.GLOWSTONE_BLOCK)

mc.setBlock(11,1,8,block.GLOWSTONE_BLOCK)
mc.setBlock(11,2,9,block.GLOWSTONE_BLOCK)
mc.setBlock(11,3,10,block.GLOWSTONE_BLOCK)
mc.setBlock(11,4,11,block.GLOWSTONE_BLOCK)
mc.setBlock(11,5,12,block.GLOWSTONE_BLOCK)
mc.setBlock(11,4,13,block.GLOWSTONE_BLOCK)

mc.setBlock(11,1,10,block.GLOWSTONE_BLOCK)
mc.setBlock(11,2,11,block.GLOWSTONE_BLOCK)

mc.setBlock(11,3,0,block.GLOWSTONE_BLOCK)
mc.setBlocks(10,1,1,10,3,2,block.WOOD_PLANKS)
mc.setBlocks(11,6,1,11,6,4,block.WOOD_PLANKS)
mc.setBlocks(2,8,0,10,10,0,block.GLASS_PANE)

mc.setBlocks(2,1,10,8,1,10,int(block.STAIRS_COBBLESTONE.id),2)
mc.setBlocks(2,1,10,2,1,4,int(block.STAIRS_COBBLESTONE.id),1)

"""mc.setBlock(5,1,2,block.STONE_BRICK)
mc.setBlock(6,1,3,block.STONE_BRICK)
mc.setBlock(6,1,3,block.STONE_BRICK)
mc.setBlock(7,1,1,block.STONE_BRICK)"""

mc.setBlocks(11,4,1,11,5,1,block.GLOWSTONE_BLOCK)
mc.setBlocks(10,4,1,10,5,2,block.GLASS)
mc.setBlocks(11,4,2,11,5,2,block.GLASS)

mc.setBlocks(13,12,0,13,12,12,int(block.STAIRS_COBBLESTONE.id),1)
mc.setBlocks(13,12,-1,0,12,-1,int(block.STAIRS_COBBLESTONE.id),2)


