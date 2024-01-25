import game_parameters
from game_display import GameDisplay
from board import *
from apple import *


def main_loop(gd: GameDisplay) -> None:
    """this function starts a game of snake. it constructs a board with a
    snake and bomb, and apples. and then starts a round of the game"""
    score = 0
    board = Board(gd)
    snake = board.get_snake()
    while board.number_of_apples() < 3:
        apple = Apple()
        while not board.can_place_apple(apple):
            apple = Apple()
        board.add_apple(apple)
    gd.show_score(score)
    board.draw_board()
    gd.end_round()
    game_round = True
    while game_round is True:
        # stars round of game
        key_clicked = gd.get_key_clicked()
        snake.set_direction(key_clicked)
        if not snake.eat_apple():  # checks if snake needs to grow in space,
            # and if so, adds space in head in snakes direction
            snake.move_snake()  # if snake does not need to grow, snake moves
            # one space
        if board.snake_out_of_board():  # checks if snake is out of head, and
            # if is ends game
            snake.remove_head()
            board.draw_board()
            gd.end_round()
            break
        if snake.snake_eats_himself() or board.snake_hits_bomb():  # checks if
            # snake hit himself of a bomb, and if true - ends game
            game_round = False
        apple_score = board.snake_eats_apple()  # checks if snake ate apple,
        # and adds points of apple to score, and adds 3 to last apple so snake
        # grows in 3 spaces
        if apple_score is not False:
            score += apple_score
            snake.add_last_apple()
            gd.show_score(score)
        check_apple_crash = board.blast_crashed_apple()
        if check_apple_crash:  # checks if bomb blast hit apple, if did,
            # removes apple and places a new one
            board.remove_apple(check_apple_crash)
        while board.number_of_apples() < 3:  # checks if there are less than 3
            # apples in board, if true adds apples
            if board.is_full_board():  # if board is full and there are less
                # then 3 apples in board, ends game
                game_round = False
            apple = Apple()
            while not board.can_place_apple(apple):
                apple = Apple()
            board.add_apple(apple)
        if board.get_bomb().shock_wave():  # if bombs shock wave started,
            # function enlarges radius of shock wave
            board.get_bomb().add_temp_radius()
        (board.get_bomb()).reduce_time()  # reduces time until bomb explodes
        if board.snake_hits_blast():  # ends game if bomb blast hits snake
            game_round = False
        if board.get_bomb().get_temp_radius() > board.get_bomb().get_radius():
            # if bomb finished exploding, removes bomb and sets a new one
            board.set_bomb()
        if board.blast_out_board():
            board.set_bomb()
        board.draw_board()
        gd.end_round()
