#import random
#import numpy as np
#from js import p5

class Boid:
    def __init__ (self):
        #self.x = random.randrange(0+radius,600-radius)
        #self.y = random.randrange(0+radius,400-radius)
        self.position = createVector(random(0,width),random(0,height))
        #self.position = p5.Vector([100], [1])
        self.velocity = p5.Vector.random2D()
        self.velocity.setMag(random(0.1,0.2))
        self.acceleration = createVector()
        #print(f'velocity {self.velocity} acceleration {self.acceleration}')
        
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
    
    def wrap_around(self):
        if self.position.x > 600: self.position.x = 0
        elif self.position.x < 0: self.position.x = 600
        if self.position.y > 400: self.position.y = 0
        elif self.position.y < 0: self.position.y = 400
            
        
        
    def align(self, boids):
        perception_radius = 50
        steering = createVector()
        total = 0
        for other_boid in boids:
            d = dist(self.position.x,
                    self.position.y,
                    other_boid.position.x,
                    other_boid.position.y)
            if d == 0: continue
            elif d < perception_radius:
                steering.add(other_boid.velocity)
                total+=1
            
        if total > 0:
            steering.div(total)
            self.acceleration = steering.sub(self.velocity)
            
    
    
diameter=100
#diameter = sin(frameCount / 60) * 50 + 50
radius=diameter/2
flock = []
width, height = 1200, 800

def setup():
    createCanvas(600, 400)
    for i in range(20):
        flock.append(Boid())

def draw():
    background(200)
    for boid in flock:
        boid.wrap_around()
        boid.align(flock)
        boid.update()
        boid.show()