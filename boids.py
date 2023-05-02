import random
class Boid:
    def __init__ (self):
        self.x = random.randrange(0+radius,600-radius)
        self.y = random.randrange(0+radius,400-radius)
        
    def show(self):
        fill("blue")
        diameter = sin(frameCount / 60) * 50 + 50
        ellipse(self.x, self.y, diameter, diameter)
        
diameter=100
#diameter = sin(frameCount / 60) * 50 + 50
radius=diameter/2
flock = [Boid() for i in range(10)]

def setup():
    createCanvas(600, 400)

def draw():
    background(200)
    
    #diameter = sin(frameCount / 60) * 50 + 50
    #fill("blue")
    #ellipse(100, 100, diameter, diameter)
    for boid in flock:
        boid.show()