yo_dict = {1: "One", 2: "Two", 3: "Three"}

for value in yo_dict:
    print(value)


def funktion():

    x = 1
    return x

num = funktion()

print(num)


print('Next')
import pygame
pygame.init()

# Get Mouse Position
pos = pygame.mouse.get_pos()
x, y = pos

print(pos)
print(x)
print(y)