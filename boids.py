#import random
#import numpy as np
#from js import p5

class Boid:
    def __init__ (self):
        #self.x = random.randrange(0+radius,600-radius)
        #self.y = random.randrange(0+radius,400-radius)
        self.position = createVector(random(0,600),random(0,400))
        #self.position = p5.Vector([100], [1])
        self.velocity = p5.Vector.random2D()
        self.velocity.setMag(random(0.5,1.5))
        print(f'velocity {self.velocity}')
        self.acceleration = createVector()
        
    def update(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        
    def show(self):
        fill("blue")
        diameter = 10#sin(frameCount / 60) * 50 + 50
        x, y = self.position.x, self.position.y
        ellipse(x, y, diameter, diameter)
        #print(self.position)
        #print(f'position {self.position.x}')
        
        
diameter=100
#diameter = sin(frameCount / 60) * 50 + 50
radius=diameter/2
flock = []

def setup():
    createCanvas(600, 400)
    for i in range(10):
        flock.append(Boid())

def draw():
    background(200)
    for boid in flock:
        boid.update()
        boid.show()