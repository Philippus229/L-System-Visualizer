import pygame, math

windowsize = [int(input("Enter the window width:")), int(input("Enter the window height:"))]
axiom = str(input("Enter axiom:"))
sentence = axiom
gen = 0
length = int(input("Enter line length:"))
angle = float(input("Enter angle:"))
savedata = []
rules = []
number_of_rules = int(input("Enter number of rules:"))
for x in range(number_of_rules):
    tmp_rule = [str(input("Enter character to replace:")), str(input("Enter what to replace character with:"))]
    rules.append(tmp_rule)
left_at = str(input("Enter at which character to turn left:"))
right_at = str(input("Enter at which character to turn right:"))
num_of_fwd_chars = int(input("Enter how many characters are for going forward:"))
fwd_chars = []
for x in range(num_of_fwd_chars):
    fwd_at = str(input("Enter at which character to go forward:"))
    fwd_chars.append(fwd_at)
startpos = [int(input("Enter the starting position x:")), int(input("Enter the starting position y:"))]
startrot = float(input("Enter starting rotation:"))

def cos_deg(x):
    return math.cos(x*(math.pi/180))

def sin_deg(x):
    return math.sin(x*(math.pi/180))

class turtle:
    def __init__(self, start_pos, start_rot):
        self.position = start_pos
        self.rotation = start_rot

    def rotate(self, deg):
        self.rotation += deg
        if self.rotation < 0:
            self.rotation += 360
        elif self.rotation > 360:
            self.rotation -= 360

    def move(self, dist):
        new_pos = [self.position[0]+cos_deg(self.rotation)*dist, self.position[1]+sin_deg(self.rotation)*dist]
        pygame.draw.lines(screen, (255, 255, 255), self.position, new_pos)
        self.position = new_pos

def next_gen(s, g):
    new_sentence = ""
    for char in s:
        found_rule = False
        for rule in rules:
            if char == rule[0]:
                found_rule = True
                new_sentence += rule[1]
        if not found_rule:
            new_sentence += char
    return [new_sentence, g+1]
    
def draw_current_gen():
    tmp_turtle = turtle(startpos, startrot)
    for char in sentence:
        if char in fwd_chars:
            tmp_turtle.move(length)
        elif char == left_at:
            tmp_turtle.rotate(-angle)
        elif char == right_at:
            tmp_turtle.rotate(angle)
        elif char == '[':
            savedata = [tmp_turtle.position, tmp_turtle.rotation]
        elif char == ']':
            tmp_turtle.position = savedata[0]
            tmp_turtle.rotation = savedata[1]

pygame.init()
screen = pygame.display.set_mode(windowsize)
pygame.display.set_caption("L-System Visualizer")
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sentence, gen = next_gen(sentence, gen)
    screen.fill((0, 0, 0))
    draw_current_gen()
    pygame.display.flip()
pygame.quit()
