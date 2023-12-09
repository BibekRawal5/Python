import pygame

pygame.font.init()
FONT = pygame.font.SysFont('comicsans', 40)

FPS = 60

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255 , 0, 0)
GREEN = (0, 255, 0)

BACKGROUND = pygame.transform.scale(pygame.image.load('background_2.jpg'), (WIDTH, HEIGHT))
car_image = pygame.image.load('car.png')
traffic_light_image = pygame.image.load('traffic_light.png')
ROAD_IMAGE = pygame.image.load('road.png')

ROAD_IMG = pygame.transform.scale(ROAD_IMAGE, (WIDTH, 400))
CAR = pygame.transform.scale(car_image, (100, 100))
TRAFFIC_LIGHT = pygame.transform.scale(traffic_light_image, (100, 100))


ROAD = pygame.Rect(0, 490, WIDTH, 510)
POINT = pygame.Rect(WIDTH/2 - 100, 486, 5, 100)


def draw(car, traffic_light, color, reset):
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, WHITE, ROAD)
    WIN.blit(ROAD_IMG, (0,336))
    
    pygame.draw.rect(WIN, BLACK, POINT)
    # pygame.draw.rect(WIN, WHITE, pygame.Rect(0, 490, WIDTH, 510))
    
    WIN.blit(TRAFFIC_LIGHT, (traffic_light.x, traffic_light.y))
    if color == RED:
        pygame.draw.circle(WIN, RED, (100, HEIGHT - HEIGHT/3 - 119), 11)
    else:
        pygame.draw.circle(WIN, GREEN, (100, HEIGHT - HEIGHT/3 - 88), 11)
    
    WIN.blit(CAR, (car.x, car.y))
    
    WIN.blit(reset, (WIDTH - 150, 30))
    pygame.display.update()

 
def handle_lights(key_pressed):
    if(key_pressed[pygame.K_r]):
        return RED
    
    elif (key_pressed[pygame.K_g]) :
        return GREEN
    
    else:
        return None
    

def main():
    clock = pygame.time.Clock()
    run = True
    car = pygame.Rect(WIDTH-120, HEIGHT - HEIGHT/3 - 2, 100, 100)
    traffic_light = pygame.Rect(50, HEIGHT - HEIGHT/3 - 155, 100, 100)
    reset = FONT.render("RESET", 1, WHITE)
    play = False
    light = GREEN
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
        
        key_pressed = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        
        if key_pressed[pygame.K_SPACE]:
            play = True
            
        if play and car.x > 20:
            car.x -= 9
        
        val = handle_lights(key_pressed)
        if(val != None):
            light = val
        
        if(car.colliderect(POINT) and light == RED):
            draw(car, traffic_light, light, reset)
            pygame.time.delay(2000)
            light = GREEN
        
        if mouse_pressed[0] and WIDTH - 150 <= mouse_pos[0] <= WIDTH and 30 <= mouse_pos[1] <= 100:
            main()
        
        draw(car, traffic_light, light, reset)
        


if __name__ == "__main__":
    main()
    