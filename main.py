import pygame, sys, time, random
from pygame.locals import *

BLOCK_SIZE = 40

class Food:         
    def __init__(self, surface):
        self.list_of_food = ['src/chocolate.png', 'src/meat.png', 'src/hot-dog.png','src/poultry-leg.png',]
        self.food = pygame.image.load(random.choice(self.list_of_food))
        self.surface = surface
        self.x = 120
        self.y = 120
        pygame.display.flip()

    def draw_chocolate(self):
        self.surface.blit(self.food,(self.x, self.y))
        pygame.display.flip()

    def move(self): #floats(uniform) doesn't work best, tryed
        self.y = random.randint(0,11)*BLOCK_SIZE
        self.x = random.randint(0,21)*BLOCK_SIZE


class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        self.block = pygame.image.load('src/block.jpg').convert() 
        self.x = [BLOCK_SIZE]*length
        self.y = [BLOCK_SIZE]*length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def draw_length(self):
        self.parent_screen.fill((0, 102, 51))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()

    def glides(self):
        for i in range(self.length -1, 0, -1):
            self.x[i] = self.x[i -1]
            self.y[i] = self.y[i -1]

        if self.direction == 'left':
            self.x[0] -= BLOCK_SIZE
        if self.direction == 'right':
            self.x[0] += BLOCK_SIZE
        if self.direction == 'up':
            self.y[0] -= BLOCK_SIZE
        if self.direction == 'down':
            self.y[0] += BLOCK_SIZE

        self.draw_length()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((900, 500))
        self.snake = Snake(self.surface, 3)
        self.snake.draw_length()
        self.food = Food(self.surface)
        self.food.draw_chocolate()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + BLOCK_SIZE:
            if y1 >= y2 and y1 < y2 + BLOCK_SIZE:
                return True
        return False

    def play(self):
        self.snake.glides()
        self.food.draw_chocolate()
        self.display_score()
        pygame.display.flip()


        if self.is_collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.increase_length()
            self.food.move()

    def display_score(self):
        font = pygame.font.Font('src/Gilroy-Semibold.ttf', 33)
        score = font.render(f"Score: {self.snake.length -3}", True, (12, 3, 74))
        self.surface.blit(score,(750,10))


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT or event.key == ord('a'):
                        self.snake.move_left()

                    if event.key == K_RIGHT or event.key == ord('d'):
                        self.snake.move_right()

                    if event.key == K_UP or event.key == ord('w'):
                        self.snake.move_up()

                    if event.key == K_DOWN or event.key == ord('s'):
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False
                    sys.exit()
                    
            self.play()

            time.sleep(0.3)

if __name__ == '__main__':
    game = Game()
    game.run()
