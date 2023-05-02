def setup():
    createCanvas(800, 600)
    global flock, max_speed_slider, max_force_slider, bounce_checkbox
    global alignment_slider, cohesion_slider, separation_slider
    global a_percept_slider, c_percept_slider, s_percept_slider
    alignment_slider = createSlider(0,5,1,0.2)
    cohesion_slider = createSlider(0,5,1,0.2)
    separation_slider = createSlider(0,5,1,0.2)
    a_percept_slider = createSlider(0,500,100,5)
    c_percept_slider = createSlider(0,500,100,5)
    s_percept_slider = createSlider(0,500,100,5)
    max_speed_slider = createSlider(0.1,10,5,0.1)
    max_force_slider = createSlider(0.1,5,1,0.1)
    bounce_checkbox = createCheckbox('Wallbounce', False)
    add_boid_button = createButton('Add Boid')
    sub_boid_button = createButton('Del Boid')

    flock = [Boid() for i in range(20)]
    add_boid_button.mousePressed(add_boid)
    sub_boid_button.mousePressed(del_boid)

def draw():
    background(200)
    textAlign(LEFT, BOTTOM)
    textStyle(BOLD)
    fill("black")
    text(f"Alignment Value: {alignment_slider.value()}\t\t\t\t Cohesion Value: {cohesion_slider.value()}\t\t\t Separation Value: {separation_slider.value()}",
        15, 580)
    text(f"Alignment Radius: {a_percept_slider.value()}\t\t Cohesion Radius: {c_percept_slider.value()}\t\t Separation Radius: {s_percept_slider.value()}",
        380, 600)
    text(f"Max Speed: {max_speed_slider.value()}\t\t\t\t\t\t\t\t Max Force: {max_force_slider.value()}\t\t\t\t\t\t\t # Boids: {len(flock)}",
        30, 600)
    
    global max_speed, max_force
    max_speed = max_speed_slider.value()
    max_force = max_force_slider.value()
    
    for boid in flock:
        boid.reset_acceleration()
        boid.align(flock)
        boid.cohesion(flock)
        boid.separation(flock)
        if bounce_checkbox.checked(): boid.wall_bounce()
        else: boid.wrap_around()
        boid.update()
        boid.show()
        
def add_boid():
    flock.append(Boid())

def del_boid():
    flock.pop()

class Boid:
    def __init__ (self):
        self.position = createVector(random(0,800),random(0,500))
        self.velocity = p5.Vector.random2D()
        self.velocity.setMag(random(0.5,1))
        self.acceleration = createVector()
        
    def update(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limit(max_speed)
        
    def show(self):
        fill("white")
        diameter = 20 #(sin(frameCount / 60) * 10) + 20
        x, y = self.position.x, self.position.y
        ellipse(x, y, diameter, diameter)
    
    def wall_bounce(self):
        if self.position.x > 800:
            self.position.x = 790
            self.velocity.mult(-1)
        if self.position.x < 0:
            self.position.x = 10
            self.velocity.mult(-1)
        if self.position.y > 550:
            self.position.y = 540
            self.velocity.mult(-1)
        if self.position.y < 0: 
            self.positiony = 10
            self.velocity.mult(-1)
    
    def wrap_around(self):
        if self.position.x > 800: self.position.x = 0
        elif self.position.x < 0: self.position.x = 800
        if self.position.y > 550: self.position.y = 0
        elif self.position.y < 0: self.position.y = 550
        
    def align(self, boids):
        perception_radius = a_percept_slider.value()
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
            steering.setMag(max_speed)
            steering.sub(self.velocity)
            alignment_force = steering.limit(max_force)
            alignment_force.mult(alignment_slider.value())
            self.acceleration.add(alignment_force)
            
    def cohesion(self, boids):
        perception_radius = c_percept_slider.value()
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
            steering.setMag(max_speed)
            steering.sub(self.velocity)
            cohesion_force = steering.limit(max_force)
            cohesion_force.mult(cohesion_slider.value())
            self.acceleration.add(cohesion_force)
            
    def separation(self, boids):
        perception_radius = s_percept_slider.value()
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
            steering.setMag(max_speed)
            steering.sub(self.velocity)
            separation_force = steering.limit(max_force)
            separation_force.mult(separation_slider.value())
            self.acceleration.add(separation_force)
            
    def reset_acceleration(self):
        self.acceleration.mult(0)
        
