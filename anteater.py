import pygame
import random
import time
pygame.init()

# main stuff
height,width = 700,700
screen = pygame.display.set_mode((height,width))
green = (0,255,0)
black = (100,55,55)
red = (255,50,50)
blue = (255,50,255)
font = pygame.font.SysFont('Corbel',30)
score = 1
text = (score)
scoretext = font.render(str(text), True,blue)

# snake stuff
x = 50
y = 50
direction = ("right")

# apple stuff
ax1 = random.randint(1,700)
ay1 = random.randint(1,700)
ax = int(ax1) - int(ax1) % 50
ay = int(ay1) - int(ay1) % 50
running = True
while running == True:
  pygame.time.Clock().tick(60)
  screen.fill(green)
  if x == ax:
    if y == ay:
      score += 1
      ax1 = random.randint(1,700)
      ay1 = random.randint(1,700)
      ax = int(ax1) - int(ax1) % 50
      ay = int(ay1) - int(ay1) % 50
  if direction == ("up"):
    y = y - 50
  elif direction == ("down"):
    y = y + 50
  elif direction == ("left"):
    x = x - 50
  elif direction == ("right"):
    x = x + 50
  pygame.draw.rect(screen,red,pygame.Rect(ax+13,ay+13,25,25))
  pygame.draw.rect(screen,black,pygame.Rect(x,y,50,50))
  text = (score)
  scoretext = font.render(str(text), True,blue)
  screen.blit(scoretext,(50,50))
  pygame.display.update()
  time.sleep(1/score)
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        if direction == ("down"):
          pass
        else:
          direction = ("up")
      elif event.key == pygame.K_s:
        if direction == ("up"):
          pass
        else:
          direction = ("down")
      elif event.key == pygame.K_a:
        if direction == ("right"):
          pass
        else:
          direction = ("left")
      elif event.key == pygame.K_d:
        if direction ==("left"):
          pass
        else:
          direction = ("right")
  if 0 > x < 700:
    score = 0
    running = False
  if 0 < y > 700:
    score = 0
    running = False
pygame.display.quit()
pygame.quit()
