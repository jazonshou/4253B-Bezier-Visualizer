import bezier, numpy, pygame

# Draws a bezier curve
# (i don't want to hear it ryan)
def draw(display, nodes, degree, precision=float, delete=bool, width=float, color=()):
    tempCurve = bezier.Curve(nodes, degree)
    points=[]
    i = 0.0
    # for i in range(0, 1, precision):
    #     points.append(tempCurve.evaluate(i))
    while i < 1:
        points.append(tempCurve.evaluate(i))
        i += precision

    for i in range(len(points)-1):
        pygame.draw.line(display, color, (points[i][0][0], points[i][1][0]), (points[i+1][0][0], points[i+1][1][0]), width)

    if delete:
        del(tempCurve)


# class Curve():
#     def __init__(self, curve=bezier, ):

#     def draw(self, )