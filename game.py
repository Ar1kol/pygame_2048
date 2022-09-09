from logics import *
import pygame
import sys
from data_base import get_best, cur, insert_result
import json
import os

COLORS = {
    0: (130, 130, 130),
    2: (98, 180, 209),
    4: (255, 255, 0),
    8: (0, 0, 255),
    16: (0, 255, 191),
    32: (255, 128, 0),
    64: (128, 255, 0),
    128: (255, 0, 191),
    256: (0, 255, 191),
    512: (0, 255, 0),
    1024: (255, 0, 0),
    # 2048: (98, 180, 209),
}

WHITE = (255, 255, 255)
SCORE_COLOR = (255, 127, 0)
BLACK = (0, 0, 0)
BLOKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOKS * SIZE_BLOCK + (BLOKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0,0, WIDTH, 110)

GEAMERS_DB = get_best()


def draw_top_gamer():
    font_top = pygame.font.SysFont('comicansms', 24)
    font_gamer = pygame.font.SysFont("comicansms", 30)
    text_head = font_top.render("Best score: ", True, SCORE_COLOR)
    screen.blit(text_head, (270, 5))
    for index, gamer in enumerate(GEAMERS_DB):
        name, score = gamer
        text = f"{index + 1}. {name} - {score}"
        text_gamer = font_gamer.render(text, True, SCORE_COLOR)
        screen.blit(text_gamer, (280, 25 + 27 * index))
        print(index, name, score)

def draw_inerface(score, delta = 0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('comicansms', 80)
    font_score = pygame.font.SysFont("comicansms", 32)
    font_delta = pygame.font.SysFont("comicansms", 24)
    text_score = font_score.render("Score: ", True, SCORE_COLOR)
    text_score_value = font_score.render(f"{score}", True, SCORE_COLOR)
    screen.blit(text_score, (20, 25))
    screen.blit(text_score_value, (175, 30))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, SCORE_COLOR)
        screen.blit(text_delta, (165, 70))
    pretty_print(game_array)
    draw_top_gamer()
    for row in range(BLOKS):
        for column in range(BLOKS):
            value = game_array[row][column]
            text = font.render(f"{value}", True, WHITE)
            weight = column*SIZE_BLOCK + (column + 1) * MARGIN
            height = row*SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (weight, height, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_weight, font_height = text.get_size()
                text_x = weight + (SIZE_BLOCK - font_weight) / 2
                text_y = height + (SIZE_BLOCK - font_height) / 2
                screen.blit(text, (text_x, text_y))

def draw_intro():
    img2048 = pygame.image.load(r"sources\2048_intro.png")
    img_arrows = pygame.image.load(r"sources\keyboard-arrow.jpg")
    font = pygame.font.SysFont('comicansms', 70)
    font_ex = pygame.font.SysFont('comicansms', 50)
    text_welcome = font.render("Welcome!", True, WHITE)
    text_explanation = font_ex.render("Use arrows for playing", True, WHITE)
    name = "Enter name"
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Enter name":
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME 
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_welcome, (230, 80))
        screen.blit(text_name, (rect_name))
        screen.blit(text_explanation, (65, 400))
        screen.blit(pygame.transform.scale(img_arrows, [300, 100]), [85, 480])

        pygame.display.update()
    screen.fill(BLACK)

def draw_game_over():
    global USERNAME, GEAMERS_DB, score, game_array
    img2048 = pygame.image.load(r"sources\2048_intro.png")
    img_enter = pygame.image.load(r"sources\enter_key.png")
    img_space = pygame.image.load(r"sources\Space_bar.png")
    font = pygame.font.SysFont('comicansms', 65)
    font_key = pygame.font.SysFont('comicansms', 50)
    text_game_over = font.render("Game Over!", True, WHITE)
    text_score = font.render(f"Your Score: {score}", True, WHITE)
    best_score = GEAMERS_DB[0][1]
    text_enter = font_key.render("Press to change player!", True, WHITE)
    text_spacebar = font_key.render("Press to continue!", True, WHITE)
    if score > best_score:
        text = "You broke the Record!"
    else:
        text = f"Current Record {best_score}"
    text_record = font.render(text, True, WHITE)
    insert_result(USERNAME, score)
    GEAMERS_DB = get_best()
    make_decision = False
    while not make_decision:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #restart game with current name
                    make_decision = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    #restart game with input new name
                    USERNAME = None
                    make_decision = True
                    init_const()
        screen.fill(BLACK)
        screen.blit(text_game_over, (220, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_enter, (30, 375))
        screen.blit(pygame.transform.scale(img_enter, [450, 50]), [10, 420])
        screen.blit(text_spacebar, (30, 490))
        screen.blit(pygame.transform.scale(img_space, [450, 50]), [10, 535])
        pygame.display.update()
    screen.fill(BLACK)


def save_game():
    data = {
        "user": USERNAME,
        "score": score,
        "arr": game_array
    }
    with open ('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def game_loop():
    global score, game_array
    draw_inerface(score)
    pygame.display.update()
    is_arr_moved = False
    while is_zero_in_arr(game_array) or able_to_move(game_array):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    game_array, delta, is_arr_moved = move_left(game_array)
                elif event.key == pygame.K_RIGHT:
                    game_array, delta, is_arr_moved = move_right(game_array)
                elif event.key == pygame.K_UP:
                    game_array, delta, is_arr_moved = move_up(game_array)
                elif event.key == pygame.K_DOWN:
                    game_array, delta, is_arr_moved = move_down(game_array)
                score += delta
                if is_zero_in_arr(game_array) and is_arr_moved:
                    empty = get_empty_list(game_array)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x,y = get_index_from_number(random_num)
                    game_array = insert_2_or_4(game_array, x, y)
                    print(f"We filled in the element numbered {random_num}")
                    is_arr_moved = False
                draw_inerface(score, delta)
                pygame.display.update()

        # print(USERNAME)


def init_const():
    global score, game_array
    game_array = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    empty = get_empty_list(game_array)
    random.shuffle(empty)
    random_num_1 = empty.pop()
    random_num_2 = empty.pop()
    x_1, y_1 = get_index_from_number(random_num_1)
    x_2, y_2 = get_index_from_number(random_num_2)
    game_array = insert_2_or_4(game_array, x_1, y_1)
    game_array = insert_2_or_4(game_array, x_2, y_2)
    score = 0


USERNAME = None
game_array = None
score = None
path = os.getcwd()
if 'data.txt' in os.listdir():
    with open('data.txt') as file:
        data = json.load(file)
        USERNAME = data["user"]
        game_array = data["arr"]
        score = data["score"]
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    init_const()

# print(get_empty_list(game_array))
# pretty_print(game_array)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


while True:
    if USERNAME == None:
        draw_intro()

    game_loop()
    draw_game_over()