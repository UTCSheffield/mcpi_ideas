from mcpi import minecraft
from mcpi import block
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

#print (pos)

#mc.player.setPos (12,00,12)
mc.player.setting("autojump", False)

#mc.setBlocks (-128,0,-128,128,70,128,block.AIR)
#mc.setBlocks (-128,-1,-128,128,-1,128,block.CLAY)
mc.setBlocks (-10,0,-10,25,60,25,block.STONE_BRICK)
mc.setBlocks (-11,-1,-11,26,-1,26,block.STONE_BRICK)
mc.setBlocks (-9,0,-9,24,59,24,block.AIR)

start =-10
end =25

for a in range(start,end+1):
    if(a==start or a==end or a%3==0):
        #print (a)
        #Quartz pillar
        mc.setBlocks (25,0,a,25,60,a,155,2)
        mc.setBlocks (-10,0,a,-10,60,a,155,2)
        mc.setBlocks (a,0,25,a,60,25,155,2)
        mc.setBlocks (a,0,-10,a,60,-10,155,2)
    else:
        #Bottom floor glazing
        mc.setBlocks (25,0,a,25,7,a,block.GLASS)
        mc.setBlocks (-10,0,a,-10,7,a,block.GLASS)
        mc.setBlocks (a,0,25,a,7,25,block.GLASS)
        mc.setBlocks (a,0,-10,a,7,-10,block.GLASS)

#Doors
mc.setBlocks (25,0,11,25,1,10,block.DOOR_IRON)
mc.setBlocks (25,0,8,25,1,7,block.DOOR_IRON)

for j in range(8,57, 7):
    #ground floor celing first floor ground         
    mc.setBlocks (-9,j,-9,24,j+1,24,block.STONE_BRICK)

    for b in range(start,end+1):
        if(not(b==start or b==end or b%3==0)):
            #2nd floor glazing
            mc.setBlocks (25,j+1,b,25,j+6,b,block.GLASS)
            mc.setBlocks (-10,j+1,b,-10,j+6,b,block.GLASS)
            mc.setBlocks (b,j+1,25,b,j+6,25,block.GLASS)
            mc.setBlocks (b,j+1,-10,b,j+6,-10,block.GLASS)
for k in range(8,33, 7):
    mc.setBlocks (1,k+2,1,14,k+3,14,block.GLASS_PANE)

mc.setBlocks (2,1,2,13,33,13,block.AIR)

