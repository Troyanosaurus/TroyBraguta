# 🚀 5. Rocket Launch Pad
# Concept: Draw a rocket and simulate a simple liftoff with key press.

# ✅ Drawing:

# Triangle top, rectangle body

# Fire using small triangles

# 💡 Effects:

# Press space to move rocket upward

# Add a countdown or rocket sound

import pygame
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Ship launch")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_rocket():
    # Setting
    screen.fill((135, 206, 235)) # Sky
    
    # Fire
    pygame.draw.ellipse(screen, (255, 153, 28), (350, RocketY - 30, 100, 140)) # Big Fire
    pygame.draw.ellipse(screen, (255, 255, 0), (370, RocketY - 30, 60, 110)) # Small Fire
    
    pygame.draw.rect(screen, (134, 222, 80), (0, 450, 1000, 150)) # Land

    # Rocket Ship
    pygame.draw.polygon(screen, (255, 0, 0), [(400, RocketY - 300), (250, RocketY - 100), (550, RocketY - 100)]) # Wings
    pygame.draw.polygon(screen, (58, 58, 58), [(400, RocketY - 130), (330, RocketY), (470, RocketY)]) # Booster
    pygame.draw.polygon(screen, (211, 211, 211), [(400, RocketY - 370), (330, RocketY - 200), (470, RocketY - 200)]) # Tip
    pygame.draw.ellipse(screen, (211, 211, 211), (325, RocketY - 320, 150, 250)) # Rocket Ship Base
    pygame.draw.ellipse(screen, (255, 0, 0), (365, RocketY - 260, 70, 70)) # Window Base
    pygame.draw.ellipse(screen, (255, 255, 255), (370, RocketY - 255, 60, 60)) # Window
    
    # Sign
    pygame.draw.rect(screen, (58, 58, 58), (0, 50, 120, 70)) # Sign Base
    pygame.draw.rect(screen, (0, 0, 0), (0, 55, 115, 60)) # Sign Screen

    
    pygame.display.update()


text_font2 = pygame.font.SysFont("Courier", 60)
counter = 5
RocketY = 450

running = True
while running:
    draw_rocket()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while counter > 0:
                    draw_rocket()
                    draw_text(f"{counter}", text_font2, (255, 0, 0), 43, 55)
                    counter -= 1
                    pygame.display.update()
                    time.sleep(1)
                        
               
                draw_rocket()
                draw_text("Go!", text_font2, (0, 255, 0), 10, 55)
                pygame.display.update()
                time.sleep(1)
                    
                while RocketY > -150:
                    RocketY -= 2
                    draw_rocket()
    
pygame.quit()
