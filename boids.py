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
        self.velocity.setMag(random(0.5,1))
        self.acceleration = createVector()
        self.max_force = 1
        self.max_speed = 4
        #print(f'velocity {self.velocity} acceleration {self.acceleration}')
        
    def update(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.max_speed)
        
    def show(self):
        fill("blue")
        diameter = 10#sin(frameCount / 60) * 50 + 10
        x, y = self.position.x, self.position.y
        ellipse(x, y, diameter, diameter)
    
    def wrap_around(self):
        if self.position.x > 600: self.position.x = 0
        elif self.position.x < 0: self.position.x = 600
        if self.position.y > 400: self.position.y = 0
        elif self.position.y < 0: self.position.y = 400
        
    def align(self, boids):
        perception_radius = 10
        steering = createVector()
        total = 0
        for other_boid in boids:
            d = dist(self.position.x,
                    self.position.y,
                    other_boid.position.x,
                    other_boid.position.y)
            if other_boid == self or d > perception_radius: continue
            steering.add(other_boid.velocity)
            total+=1
            
        if total > 0:
            steering.div(total)
            steering.setMag(self.max_speed)
            steering.sub(self.velocity)
            alignment_force = steering.limit(self.max_force)
            self.acceleration.add(alignment_force)
            
    def cohesion(self, boids):
        perception_radius = 1
        steering = createVector()
        total = 0
        for other_boid in boids:
            d = dist(self.position.x,
                    self.position.y,
                    other_boid.position.x,
                    other_boid.position.y)
            if other_boid == self or d > perception_radius: continue
            steering.add(other_boid.position)
            total+=1
            
        if total > 0:
            steering.div(total)
            steering.sub(self.position)
            steering.setMag(self.max_speed)
            steering.sub(self.velocity)
            cohesion_force = steering.limit(self.max_force)
            self.acceleration.add(cohesion_force)
            
    def separation(self, boids):
        perception_radius = 100
        steering = createVector()
        total = 0
        for other_boid in boids:
            d = dist(self.position.x,
                    self.position.y,
                    other_boid.position.x,
                    other_boid.position.y)
            if other_boid == self or d > perception_radius: continue
            diff = p5.Vector.sub(self.position, other_boid.position)
            diff.div(d)
            steering.add(diff)
            total+=1
            
        if total > 0:
            steering.div(total)
            steering.setMag(self.max_speed)
            steering.sub(self.velocity)
            cohesion_force = steering.limit(self.max_force)
            self.acceleration.add(cohesion_force)
            
    def reset_acceleration(self):
        self.acceleration.mult(0)
            
    
    
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
        boid.reset_acceleration()
        boid.align(flock)
        boid.cohesion(flock)
        boid.separation(flock)
        boid.wrap_around()
        boid.update()
        boid.show()