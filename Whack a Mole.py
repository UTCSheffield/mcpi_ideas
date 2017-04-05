import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

mc = minecraft.Minecraft.create()
mc.postToChat ("Whack a Mole")

pos = mc.player.getTilePos()
mc.setBlocks(pos.x - 1, pos.y, pos.z + 3, pos.x + 1, pos.y + 2, pos.z + 3, block.STONE.id)

blocksLit = 0
points = 0

mc.postToChat("Get Ready")
time.sleep(2)
mc.postToChat("GO!")

while blocksLit < 9:
    time.sleep(0.2)

blocksLit = blocksLit + 1
lightCreated = False
while not lightCreated:
    xPos = pos.x + random.randint(-1,1)
    yPos = pos.y + random.randint (0,2)
    zPos = pos.z + 3
    if mc.getBlock(xPos, yPos, zPos) == block.STONE.id:
        mc.setBlock(xPos, yPos, zPos, block.GLOWSTONE_BLOCK.id)
        lightCreated = True


