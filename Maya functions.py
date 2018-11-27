
##import maya.cmds as mc
##import math
##
###This is a test
###for i in range(10):
##    #mc.sphere()
##    # move -r 2.974305 0 0 ;
##    #mc.move((2*i), 0, 0)
##    
###google search: change number range python (stackoverflow) 
####OldRange = (OldMax - OldMin)  
####NewRange = (NewMax - NewMin)  
####NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
##
##def reRange(oldValue):
##    oldRange = (1 - (-1))  #red color 
##    newRange = (1 - 0)  
##    newValue = (((oldValue - (-1)) * newRange) / oldRange) + 0
##    return newValue
##
##for i in range(1, 73):
##    mc.sphere(radius =.5)
##    
##    #Moves the Sphere
##    #move -r 0 0 -13.259078 ;
##    mc.move(0, 0, -10, relative = True)  
##    
##    #Moves the pivot to the origin 
##    mc.move(0, 0, 10, ('nurbsSphere' + str(i) + '.scalePivot'), ('nurbsSphere' + str(i) + '.rotatePivot'), relative = True)
##    mc.rotate(0, (5 * i), 0, r = True, os = True)
##    
##    redVal = reRange(math.sin(math.radians(i * 5))) #<-- Old value 
##    greenVal = reRange(math.sin(math.radians(i * 5 + 120)))
##    blueVal = reRange(math.sin(math.radians(i * 5 + 240)))
##    
##    mc.polyColorPerVertex( rgb=(redVal, greenVal, blueVal), cdo = True ) #adds colors
##
##
##
##
##def makeUI():
##    # Make a new window
##    window = cmds.window( title="Long Name", iconName='Short Name', widthHeight=(200, 55) )
##    cmds.columnLayout( adjustableColumn=True )
##    cmds.button( label='Do Nothing' )
##    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
##    cmds.setParent( '..' )
##    cmds.showWindow( window )
        



import maya.cmds as mc
import math
import random

#colors
def reRange(oldValue):
    oldRange = (1 - (-1))  
    newRange = (1 - 0)  
    newValue = (((oldValue - (-1)) * newRange) / oldRange) + 0
    return newValue


for i in range (72):
    
    #YOu can addjust the intensity of the color by chaning the values ( i * (5,10,20) for each one
    r1 = reRange( math.sin(math.radians(i * 5)) )
    g1 = reRange( math.sin(math.radians(i * 5 + 120)))
    b1 = reRange( math.sin(math.radians(i * 5 + 240)))
    
    #RGB2
    r2 = reRange( math.sin(math.radians((i+10) * 5)) )
    g2 = reRange( math.sin(math.radians((i+10) * 5 + 120)))
    b2 = reRange( math.sin(math.radians((i+10) * 5 + 240)))
    #RGB3
    r3 = reRange( math.sin(math.radians((i+20) * 5)) )
    g3 = reRange( math.sin(math.radians((i+20) * 5 + 120)))
    b3 = reRange( math.sin(math.radians((i+20) * 5 + 240)))
    
    #This will randomize the  radius of the spheres
    rad1 = random.uniform(-.75,.75)
    rad2 = random.uniform(-.5,.5)
    rad3 = random.uniform(-.25,.25)


##    def makeSpheres():
##        red_numSpheres = mc.intField('numSpheres', query = True, value = True)
##        green_numSpheres = mc.intField('numSpheres', query = True, value = True)
##        blue_numSpheres = mc.intField('numSpheres', query = True, value = True)
##        
##        for i in range of (0, red_numSpheres):
##            mc.polySphere(n = 'sphere_a_' + str(i), r = 1.5 + rad1)
##            mc.move(1,0,0)
##            mc.polyColorPerVertex( rgb=(r1, g1, b1), cdo = True )
##            
##            for j in range of (0, green_numSpheres):
##                mc.polySphere(n = 'sphere_b_' + str(i), r = .75 + rad2)
##                mc.rotate(0,120, 0, r = True, ws = True)
##                mc.move(3,0,0, os = True)
##                mc.polyColorPerVertex( rgb=(r2, g2, b2), cdo = True )
##                
##                for k in range of (0, blue_numSpheres):
##                    mc.polySphere(n = 'sphere_c_' + str(i), r = .5 + rad3)
##                    mc.rotate(0,240, 0, r = True, ws = True)
##                    mc.move(6,0,0, os= True)
##                    mc.polyColorPerVertex( rgb=(r3, g3, b3), cdo = True )

    
   
    #first sphere
    mc.polySphere(n = 'sphere_a_' + str(i), r = 1.5 + rad1)
    mc.move(1,0,0)
    #use the RGB color values from above
    mc.polyColorPerVertex( rgb=(r1, g1, b1), cdo = True )
    
    #second sphere
    mc.polySphere(n = 'sphere_b_' + str(i), r = .75 + rad2)
    #rotate the sphere 120 degrees on the Y axis
    mc.rotate(0,120, 0, r = True, ws = True)
    #move it in object space
    mc.move(3,0,0, os = True)
    #use the RGB color values from above
    mc.polyColorPerVertex( rgb=(r2, g2, b2), cdo = True )
    
    #third sphere
    mc.polySphere(n = 'sphere_c_' + str(i), r = .5 + rad3)
    mc.rotate(0,240, 0, r = True, ws = True)
    mc.move(6,0,0, os= True)
    mc.polyColorPerVertex( rgb=(r3, g3, b3), cdo = True )
    
    #group the spheres and name
    mc.select('sphere_a_' + str(i), 'sphere_b_' + str(i), 'sphere_c_' + str(i), replace = True)
    mc.group(n = 'group_a_' + str(i) )


    #this gives the spiral look
    mc.rotate(0,(45 * i), 0, r = True, os = True)
    mc.makeIdentity( apply = True, t = True, r = True, s = True, n = False,pn = True)
    
    mc.move(12, 0, 0)
    
    #spins
    if i % 5 == 0:
        mc.expression( s = 'group_a_' + str(i) + '.rotateY = time * 30;',  o = 'group_a_' + str(i), ae = True, uc = 'all' )
    else:
        mc.expression( s = 'group_a_' + str(i) + '.rotateY = time * 5;',  o = 'group_a_' + str(i), ae = True, uc = 'all' )
        
    #grouping
    mc.group(empty = True, n = 'group_b_' + str(i))
    
    #new group from the old group
    mc.select('group_a_' + str(i), r = True)
    mc.select('group_b_' + str(i), tgl = True)
    mc.parent()
    
    #select parent group and rotate (5*i) degrees in z
    mc.select('group_b_' + str(i), r = True)
    mc.rotate(0, 0, (5*i), r = True, os = True)
    
def makeUI():
    if (mc.window("Colorful Spheres", exists = True)):
        mc.deleteUI("Colorful Spheres")
    # Make a new window
    window = mc.window("colors", title="Colorful Spheres", widthHeight=(200, 55) )

    #mc.columnLayout( adjustableColumn=True )
    #mc.text(label="Number of Red Spheres on the screen")
    #mc.intField('red_numSpheres', minValue=1, maxValue=100, value=1)
    
    #mc.text(label="Number of Green Spheres on the screen")
    #mc.intField('green_numSpheres', minValue=1, maxValue=100, value=1)
    
    #mc.text(label="Number of Blue Spheres on the screen")
    #mc.intField('blue_numSpheres', minValue=1, maxValue=100, value=1)
    
makeUI()
#makeSpheres()
