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

def buildImage(img, pos, on_block = block.GOLD_BLOCK, off_block = block.AIR, z_offset = 4):
	print("The list of blocks to be printed as integer numbers", img)
	height = len(img)
	width = bitLen(max(img))

	for dy in range(height):
		#print(bin(img[dy]))
		for dx in range(width):
			relativePos = Vec3(dx, height - dy, z_offset)
			point = pos + relativePos
			if testBit(img[dy], dx) :
				mc.setBlock(point, on_block)
			else:
				mc.setBlock(point, off_block)

position = mc.player.getPos()



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
buildImage(image  , position)



image2 = [24, 60, 126, 219, 255, 36, 90, 165]
buildImage(image2  , position, on_block=block.DIAMOND_BLOCK, z_offset = 5)
