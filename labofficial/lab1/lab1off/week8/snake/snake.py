import pygame  
import sys  
import random  

pygame.init()  

width, height = 640, 480  
screen = pygame.display.set_mode((width, height))  
clock = pygame.time.Clock()  # Создание объекта для отслеживания времени

black = (0, 0, 0)  # Цвет фона
green = (0, 255, 0)  # Цвет тела змейки
red = (255, 0, 0)  # Цвет еды
white = (255, 255, 255)  # Цвет текста
blue = (0, 0, 255)  # Цвет головы змейки


font = pygame.font.Font(None, 36) 

cell_size = 20  
snake = [(width // 2, height // 2)]  
direction = (0, -cell_size)  
food = (random.randint(0, (width-cell_size)//cell_size) * cell_size,  
        random.randint(0, (height-cell_size)//cell_size) * cell_size)  
score = 0  

speed = 10  # Скорость обновления кадров в игре

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # Событие закрытия окна
            running = False
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP and direction != (0, cell_size):
                direction = (0, -cell_size)
            elif event.key == pygame.K_DOWN and direction != (0, -cell_size):
                direction = (0, cell_size)
            elif event.key == pygame.K_LEFT and direction != (cell_size, 0):
                direction = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and direction != (-cell_size, 0):
                direction = (cell_size, 0)

    # Перемещение змейки
    new_head = ((snake[0][0] + direction[0]) % width, (snake[0][1] + direction[1]) % height)
    if new_head in snake:
        running = False  # Столкновение с самой собой

    snake.insert(0, new_head)  # Добавление новой головы
    if snake[0] == food:
        score += 10  # Увеличение счета
        food = (random.randint(0, (width-cell_size)//cell_size) * cell_size,
                random.randint(0, (height-cell_size)//cell_size) * cell_size)
    else:
        snake.pop()  


    screen.fill(black)
    for index, segment in enumerate(snake):
        color = blue if index == 0 else green  
        pygame.draw.rect(screen, color, (segment[0], segment[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))

    # Отображение счета
    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()