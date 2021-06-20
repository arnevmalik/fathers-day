from ursina import *
import random
app= Ursina()
speed=0.1
speed2= -0.1
speed3=0.1
speed4=-0.1
def update() :
 
    global speed
    global speed2
    global speed3
    global speed4
    cube2.rotation_x+=1
    cube2.rotation_y+=1
    cube.x+=speed
    if abs(cube.x)>=6:
        speed *= -1
    cube3.x+=speed4
    if abs(cube3.x)>=6 :
        speed4 *= -1

    
  
 


    
    

cube= Entity(model="cube",texture="hfd.png",scale=2)
cube2= Entity(model="cube",texture="father.jpeg",scale=3,rotation_x=1,rotation_y=1)
cube3= Entity(model="cube",texture="hfd.png",scale=2)

app.run()