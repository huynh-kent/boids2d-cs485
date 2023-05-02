#import random
#import numpy as np
#from js import p5

class Boid:
    def __init__ (self):
        #self.x = random.randrange(0+radius,600-radius)
        #self.y = random.randrange(0+radius,400-radius)
        self.position = createVector([100],[100])
        #self.position = p5.Vector([100], [1])
        self.velocity = p5.Vector.random2D()
        self.velocity.setMag(1,1)
        #self.acceleration = createVector(1,1)
        
        
    def show(self):
        fill("blue")
        diameter = sin(frameCount / 60) * 50 + 50
        ellipse(self.position.x, self.position.y, diameter, diameter)
        #print(self.position)
        #print(f'position {self.position.x}')
        
diameter=100
#diameter = sin(frameCount / 60) * 50 + 50
radius=diameter/2

def setup():
    createCanvas(600, 400)
    flock = [Boid() for i in range(10)]

def draw():
    background(200)
    
    #diameter = sin(frameCount / 60) * 50 + 50
    #fill("blue")
    #ellipse(100, 100, diameter, diameter)
    for boid in flock:
        boid.show()