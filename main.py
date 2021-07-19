import bezier, numpy, pygame
import mouse, curve, button, key
from threading import Thread

# Bezier - https://pypi.org/project/bezier/ & https://javascript.info/bezier-curve (reference)
# Numpy - https://numpy.org/doc/stable/index.html (tbh, i don't think i ended up using this)
# Pygame - https://www.pygame.org/docs/


# This project untilizes pygame to make all the drawing & perform all the action
pygame.init()

# Creates new mouse & key object 
m = mouse.Mouse()
f = key.Key()
r = key.Key() # i did not think this through

# Set up the drawing window
sideLength = 650
screen = pygame.display.set_mode([sideLength, sideLength])

# Base nodes (for setup)
nodes = [
    [100, 200],
    [100, 200]
]

# Starter buttons (im very organized, your welcom)
b1 = button.Button(screen, button.ButtonShape.CIRCLE, (150, 255, 150), (nodes[0][0], nodes[1][0]), (10, 10), 0)
b2 = button.Button(screen, button.ButtonShape.CIRCLE, (150, 255, 150), (nodes[0][1], nodes[1][1]), (10, 10), 0)
b_test = button.Button(screen, button.ButtonShape.RECTANGLE, (0, 0, 0), (250, 250), (25, 25), 0)
b_test.draw()

# List for all them buttons
buttons = [
    b1, 
    b2
]

for i in buttons:
    i.draw()

# CONSTANTS
curveDegree = 1

# Gets nodes
print('Hello and welcome to the Bezier generator!')
print('Left click to move nodes around and right click to add nodes')
print('The blue point is the first point')
print('Happy coding!')
print('---------------------------------------------------')
print('Press F to output nodes')
print('---------------------------------------------------')
print('Origin currently at the TOP LEFT corner')

# Create "Field"
box = 108.333
origin = 0
origins = [
    'TOP LEFT', 
    'TOP RIGHT',
    'BOTTOM LEFT',
    'BOTTOM RIGHT'
]

# Run until the user asks to quit
running = True

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Creates field
    for i in range(6):
        pygame.draw.line(screen, (200, 200, 200), (box*i, 0), (box*i, sideLength))
        pygame.draw.line(screen, (200, 200, 200), (0, box*i), (sideLength, box*i))

    # When you right click, you create new nodes along the curve
    if m.isPressed(mouse.MouseButton.RIGHT, True):
        curveDegree += 1
        nodes[0].append(m.pose(mouse.PoseType.ABSOLUTE)[0])
        nodes[1].append(m.pose(mouse.PoseType.ABSOLUTE)[1])
        buttons.append(button.Button(screen, button.ButtonShape.CIRCLE, (150, 250, 150), (nodes[0][len(nodes[0])-1], nodes[1][len(nodes[0])-1]), (10, 10), 0))

    # Displays & controls all the buttons/bezier nodes
    for i in buttons:
        i.draw()
        # i.drag(m, mouse.MouseButton.LEFT, m.pose())
        if i.drag(m, mouse.MouseButton.LEFT, (nodes[0][buttons.index(i)], nodes[1][buttons.index(i)])):
            i.setColor((255, 150, 150))
            nodes[0][buttons.index(i)] = m.pose(mouse.PoseType.ABSOLUTE)[0]
            nodes[1][buttons.index(i)] = m.pose(mouse.PoseType.ABSOLUTE)[1]
        else:
            i.setColor((150, 255, 150))
            buttons[0].setColor((0, 0, 255))
            i.move((nodes[0][buttons.index(i)], nodes[1][buttons.index(i)]))
    
    # Creates connector lines
    for i in range(len(nodes[0])-1):
        pygame.draw.line(screen, (150, 150, 150), (nodes[0][i], nodes[1][i]), (nodes[0][i+1], nodes[1][i+1]))

    # Draws the curve
    curve.draw(screen, nodes, curveDegree, 0.001, True, 2, (0, 0, 0))

    # Ouput
    if f.isPressed(pygame.K_f, True):
        for i in range(len(nodes[0])):
            if origin == 0:
                print('P'+str(i)+': '+'['+str((nodes[0][i])*(144/sideLength))+', '+str((nodes[1][i])*(144/sideLength))+']')
            elif origin == 1:
                print('P'+str(i)+': '+'['+str((sideLength-nodes[0][i])*(144/sideLength))+', '+str((nodes[1][i])*(144/sideLength))+']')
            elif origin == 2:
                print('P'+str(i)+': '+'['+str((nodes[0][i])*(144/sideLength))+', '+str((sideLength-nodes[1][i])*(144/sideLength))+']')
            else:
                print('P'+str(i)+': '+'['+str((sideLength-nodes[0][i])*(144/sideLength))+', '+str((sideLength-nodes[1][i])*(144/sideLength))+']')
        print('---------------------------------------------------')

    if r.isPressed(pygame.K_r, True):
        origin += 1
        origin %= 4
        print('Origin set to '+origins[origin])
        
    # Refreshes pygame
    pygame.display.update()

# Done! Time to quit.
pygame.quit()