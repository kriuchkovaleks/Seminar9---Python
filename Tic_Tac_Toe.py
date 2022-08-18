
import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Piece'
    return False


pygame.init()
size_block = 100
margin = 15
width = heigth = size_block*3 + margin*4


size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Tic Tac Toe')
backgroud_color = (187, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (82, 89, 59)

mas = [[0]*3 for i in range(3)]
query = 0
game_over = False

while True:

    screen.fill(backgroud_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse//(size_block + margin)
            row = y_mouse//(size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = '0'
            query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            query = 0
            screen.fill(backgroud_color)

    for row in range(3):
        for col in range(3):
            if mas[row][col] == 'x':
                color = red
            elif mas[row][col] == '0':
                color = green
            else:
                color = white
            x = col*size_block + (col+1)*margin
            y = row*size_block + (row+1)*margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))

    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, '0')

    if game_over:
        if game_over == 'x':
            screen.fill(red)
        elif game_over == '0':
            screen.fill(green)
        else:
            screen.fill(black)

  
    pygame.display.update()
