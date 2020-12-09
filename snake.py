import pygame
import random

pygame.init()                                               # Инициализация модуля pygame

width = 1280
height = 720

surface = pygame.display.set_mode((width, height))          # Создание обьекта рабочей области (окна)

block_size = 20


def setka(x=0, y=0):                                        # Функция игровой сетки не является обьектом
    while x < width:
        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, height))
        x += block_size
        pygame.draw.line(surface, (0, 0, 0), (0, y), (width, y))
        y += block_size


class snake():
    def __init__(self, x, y):                               # метод инициализатор для обьекта Snake
        self.head = [x * block_size, y * block_size]
        self.body = [[self.head[0] - block_size, self.head[1] - block_size]]
        self.apple_x = (random.randint(0, (width // block_size - 1))) * block_size + block_size // 2
        self.apple_y = (random.randint(0, (height // block_size - 1))) * block_size + block_size // 2
        self.top = False
        self.right = False
        self.left = False
        self.bottom = True

    def draw(self):                                         # метод отрисовки змеи
        for i in self.body:
            pygame.draw.rect(surface, (0, 0, 255), (i[0], i[1], block_size, block_size))
        
        if len(self.body) > 3:            
            self.body.pop()
            
        self.body.insert(0, list(self.head))


    def controler(self):                                     # метод задающая направление движения змеи
        for press in pygame.event.get():
            if press.type == pygame.KEYDOWN:
                if press.key == pygame.K_w and self.bottom == False:
                    self.top = True
                    self.right = False
                    self.left = False
                    self.bottom = False
                if press.key == pygame.K_d and self.left == False:
                    self.top = False
                    self.right = True
                    self.left = False
                    self.bottom = False
                if press.key == pygame.K_a and self.right == False:
                    self.top = False
                    self.right = False
                    self.left = True
                    self.bottom = False
                if press.key == pygame.K_s and self.top == False:
                    self.top = False
                    self.right = False
                    self.left = False
                    self.bottom = True

    def move(self):                                         # метод движения змеи
        if self.right == True:
            self.head[0] += block_size
            if self.head[0] > width:
                self.head[0] = 0
        if self.left == True:
            self.head[0] -= block_size
            if self.head[0] < 0:
                self.head[0] = width
        if self.top == True:
            self.head[1] -= block_size
            if self.head[1] < 0:
                self.head[1] = height
        if self.bottom == True:
            self.head[1] += block_size
            if self.head[1] > height:
                self.head[1] = 0

    
    def collision(self):                                    # метод сравнивающий положение головы по отношению к остальному телу
        i = 0
        for segment in self.body[1:]:
            i += 1
            if self.head[0] == segment[0] and self.head[1] == segment[1]:
                del self.body[i:]
    
    def apple_move(self):                                   # метод сравнивающий положение головы по отношению яблока
        if self.head[0] + 10 == self.apple_x and self.head[1] + 10 == self.apple_y:
            self.apple_x = (random.randint(0, (width // block_size - 1))) * block_size + block_size // 2
            self.apple_y = (random.randint(0, (height // block_size - 1))) * block_size + block_size // 2
            self.body.insert(0, list(self.head))
    
    def apple_draw(self):                                   # метод отрисовки яблока
        pygame.draw.circle(surface, (255, 0, 0), (self.apple_x, self.apple_y), block_size // 2)        




Snake = snake(20, 10)                                       # создание обьекта Snake

while True:

    surface.fill((0, 128, 0))

    setka()
    Snake.draw()
    Snake.controler()
    Snake.apple_move()
    Snake.apple_draw()
    Snake.move()
    Snake.collision()
    
    pygame.time.delay(60)                                   # FPS
    pygame.display.flip()
    
