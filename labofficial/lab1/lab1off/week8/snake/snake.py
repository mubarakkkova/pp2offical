import pygame  # Импорт модуля pygame для работы с графикой и управлением
import sys  # Импорт модуля sys для работы с системными функциями
import random  # Импорт модуля random для генерации случайных чисел

pygame.init()  # Инициализация всех импортированных модулей pygame

# Основные параметры экрана
width, height = 640, 480  # Установка размеров экрана
screen = pygame.display.set_mode((width, height))  # Создание окна игры с заданными размерами
clock = pygame.time.Clock()  # Создание объекта для отслеживания времени

# Цвета
black = (0, 0, 0)  # Цвет фона
green = (0, 255, 0)  # Цвет тела змейки
red = (255, 0, 0)  # Цвет еды
white = (255, 255, 255)  # Цвет текста
blue = (0, 0, 255)  # Цвет головы змейки

# Шрифт для счета
font = pygame.font.Font(None, 36)  # Создание объекта шрифта для отображения текста

# Параметры змейки и еды
cell_size = 20  # Размер одной клетки на игровом поле
snake = [(width // 2, height // 2)]  # Начальное положение змейки в центре экрана
direction = (0, -cell_size)  # Начальное направление движения змейки вверх
food = (random.randint(0, (width-cell_size)//cell_size) * cell_size,  # Случайное расположение еды по горизонтали
        random.randint(0, (height-cell_size)//cell_size) * cell_size)  # Случайное расположение еды по вертикали
score = 0  # Начальное значение счета

# Параметр скорости
speed = 10  # Скорость обновления кадров в игре

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Событие закрытия окна
            running = False
        elif event.type == pygame.KEYDOWN:  # Событие нажатия клавиши
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
        snake.pop()  # Удаление последнего элемента

    # Отрисовка элементов игры
    screen.fill(black)
    for index, segment in enumerate(snake):
        color = blue if index == 0 else green  # Использование синего цвета для головы
        pygame.draw.rect(screen, color, (segment[0], segment[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))

    # Отображение счета
    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()