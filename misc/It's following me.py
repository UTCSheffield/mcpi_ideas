from mcpi import minecraft
from mcpi import block
from mcpi.vec3 import Vec3
from minecraftstuff import MinecraftShape

import time

def bitLen(int_type):
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    return(length)

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

mc = minecraft.Minecraft.create()

def buildImage(img, pos, on_block=block.GOLD_BLOCK, off_block=block.AIR, z_offset = 8):
    shape = MinecraftShape(mc, pos)
    print("The list of blocks to be printed as integer numbers", img)
    height = len(img)
    width = bitLen(max(img))

    for dy in range(height):
        #print(bin(img[dy]))
        for dx in range(width):
            if testBit(img[dy], dx) :
                shape.setBlock(dx, height - dy, z_offset, on_block)
            else:
                shape.setBlock(dx, height - dy, z_offset, off_block)
    return shape

position = mc.player.getTilePos()

image = [
    0b00011000,
    0b00111100,
    0b01111110,
    0b11011011,
    0b11111111,
    0b00100100,
    0b01011010,
    0b10100101
    ]

imgShape = buildImage(image, position)

while True :
    position2 = mc.player.getTilePos()
    #print(position2)
    imgShape.move(position2.x, position2.y, position2.z)
    #imgShape.rotateBy(5, 0, 0)
    time.sleep(1)
