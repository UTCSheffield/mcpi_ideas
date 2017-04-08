from mcpi import minecraft
from mcpi import block
from mcpi.vec3 import Vec3
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
pos = mc.player.getPos()

img = [ 0x18, 0x3C, 0x7E, 0xDB, 0xFF, 0x24, 0x5A, 0xA5 ]
img = [24, 60, 126, 219, 255, 36, 90, 165]
img = [
    0b11000,
    0b111100,
    0b1111110,
    0b11011011,
    0b11111111,
    0b100100,
    0b1011010,
    0b10100101
    ]


img = [
    0b00011000,
    0b00111100,
    0b01111110,
    0b11011011,
    0b11111111,
    0b00100100,
    0b01011010,
    0b10100101
    ]

print(img)

dz = 4
height = len(img)
width = bitLen(max(img))

for dy in range(height):
    print(bin(img[dy]))
    for dx in range(width):
        relativePos = Vec3(dx, height - dy, dz)
        point = pos + relativePos
        if testBit(img[dy], dx) :
            mc.setBlock(point, block.GOLD_BLOCK)
        else:
            mc.setBlock(point, block.AIR)
