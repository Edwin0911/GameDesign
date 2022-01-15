import random
import time
import sys
import pygame


pygame.init()
window_surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')
window_surface.fill((255, 255, 255))
head_font = pygame.font.SysFont(None, 60)

image1 = pygame.image.load("O.PNG")
image1.convert()
image2 = pygame.image.load("X.PNG")
image2.convert()

def input_player_letter():
    """
    let the player type which letter they want to be.
    Returns a list with the player's letter as the first item and the
    computer's letter as the second.
    """
    while True:

        '''display_message('choose your symbol: (O or X)')'''
        text_surface = head_font.render('choose your symbol', True, (0, 0, 0))
        window_surface.blit(text_surface, (100, 50))

        
        window_surface.blit(image1, (100,300))

        window_surface.blit(image2, (400,300))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.MOUSEBUTTONUP:            
                if 100 < pygame.mouse.get_pos()[0] < 200 and 300 < pygame.mouse.get_pos()[1] < 400:
                    return ['O','X']
                elif 400 < pygame.mouse.get_pos()[0] < 500 and 300 < pygame.mouse.get_pos()[1] < 400:
                    return ['X','O']

def who_goes_first():
    # Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'

def draw_board(board):
    window_surface.fill((255, 255, 255))
    # 畫網格線 豎線
    pygame.draw.line(window_surface,(0, 0, 0), (200,0), (200,600), 2)
    pygame.draw.line(window_surface,(0, 0, 0), (400,0), (400,600), 2)
    # 畫網格線 橫線
    pygame.draw.line(window_surface,(0, 0, 0), (0,200), (600,200), 2)
    pygame.draw.line(window_surface,(0, 0, 0), (0,400), (600,400), 2)
    # 畫O
    if board[7] == 'O':
        window_surface.blit(image1, (50,50))
    if board[8] == 'O':
        window_surface.blit(image1, (250,50))
    if board[9] == 'O':
        window_surface.blit(image1, (450,50))
    if board[4] == 'O':
        window_surface.blit(image1, (50,250))
    if board[5] == 'O':
        window_surface.blit(image1, (250,250))
    if board[6] == 'O':
        window_surface.blit(image1, (450,250))
    if board[1] == 'O':
        window_surface.blit(image1, (50,450))
    if board[2] == 'O':
        window_surface.blit(image1, (250,450))
    if board[3] == 'O':
        window_surface.blit(image1, (450,450))
    # 畫X
    if board[7] == 'X':
        window_surface.blit(image2, (50,50))
    if board[8] == 'X':
        window_surface.blit(image2, (250,50))
    if board[9] == 'X':
        window_surface.blit(image2, (450,50))
    if board[4] == 'X':
        window_surface.blit(image2, (50,250))
    if board[5] == 'X':
        window_surface.blit(image2, (250,250))
    if board[6] == 'X':
        window_surface.blit(image2, (450,250))
    if board[1] == 'X':
        window_surface.blit(image2, (50,450))
    if board[2] == 'X':
        window_surface.blit(image2, (250,450))
    if board[3] == 'X':
        window_surface.blit(image2, (450,450))
    pygame.display.update()

def is_winner(bd, lt):
    # Given a board and a player's letter, this function returns True if
    #  that player has won.
    # We use "bd" instead of "board" and "lt" instead of "letter" so we
    # don't have to type as much.
    return ((bd[7] == lt and bd[8] == lt and bd[9] == lt) or 
            (bd[4] == lt and bd[5] == lt and bd[6] == lt) or 
            (bd[1] == lt and bd[2] == lt and bd[3] == lt) or 
            (bd[7] == lt and bd[4] == lt and bd[1] == lt) or 
            (bd[8] == lt and bd[5] == lt and bd[2] == lt) or 
            (bd[9] == lt and bd[6] == lt and bd[3] == lt) or 
            (bd[7] == lt and bd[5] == lt and bd[3] == lt) or 
            (bd[9] == lt and bd[5] == lt and bd[1] == lt)) 

def is_space_free(board, move):
    if board[move] == ' ':
        return True
    return False

def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise,
    # return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

def get_player_move(board):
    # Let the player enter their move.
    move = ' '
    while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or \
    not is_space_free(board, int(move)):
        '''display_message('What is your next move? (1-9)')'''
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.MOUSEBUTTONUP:            
                if 0 < pygame.mouse.get_pos()[0] < 200 and 0 < pygame.mouse.get_pos()[1] < 200:
                    move = 7
                elif 200 < pygame.mouse.get_pos()[0] < 400 and 0 < pygame.mouse.get_pos()[1] < 200:
                    move = 8
                elif 400 < pygame.mouse.get_pos()[0] < 600 and 0 < pygame.mouse.get_pos()[1] < 200:
                    move = 9
                elif 0 < pygame.mouse.get_pos()[0] < 200 and 200 < pygame.mouse.get_pos()[1] < 400:
                    move = 4
                elif 200 < pygame.mouse.get_pos()[0] < 400 and 200 < pygame.mouse.get_pos()[1] < 400:
                    move = 5
                elif 400 < pygame.mouse.get_pos()[0] < 600 and 200 < pygame.mouse.get_pos()[1] < 400:
                    move = 6
                elif 0 < pygame.mouse.get_pos()[0] < 200 and 400 < pygame.mouse.get_pos()[1] < 600:
                    move = 1
                elif 200 < pygame.mouse.get_pos()[0] < 400 and 400 < pygame.mouse.get_pos()[1] < 600:
                    move = 2
                elif 400 < pygame.mouse.get_pos()[0] < 600 and 400 < pygame.mouse.get_pos()[1] < 600:
                    move = 3
    return move

def make_move(board, letter, move):
    board[move] = letter

def random_choose(board):
    """Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move."""
    print('computer is thinking...')
    time.sleep(0.5)
    
    possible_moves = []
    # TODO: check valid locations and randomly pick one.


def find_winning_move(board, computer_letter):
    """For every possible move, check if it can win with that move."""
    for i in range(len(board)):
        boardcopy = board.copy()
        if is_space_free(boardcopy, i):
            make_move(boardcopy, computer_letter, i)
            if is_winner(boardcopy, computer_letter):
                return i
    return None

def block_player_move(board, player_letter):
    """try to block a player's move"""
    for i in range(len(board)):
        boardcopy = board.copy()
        if is_space_free(boardcopy, i):
            make_move(boardcopy, player_letter, i)
            if is_winner(boardcopy, player_letter):
                return i
    return None

def choose_corner(board):
    """choose a corner move if possible"""
    possible_moves = []
    if is_space_free(board, 1):
        possible_moves.append(1)
    if is_space_free(board, 3):
        possible_moves.append(3)
    if is_space_free(board, 7):
        possible_moves.append(7)
    if is_space_free(board, 9):
        possible_moves.append(9)
    i = random.choice(possible_moves)
    return i

def choose_center(board):
    """choose the center if possible"""
    i = 5
    if is_space_free(board, i):
       return i 
    return None
    
def choose_side(board):
    """choose side positions if possible"""
    possible_moves = []
    if is_space_free(board, 2):
        possible_moves.append(2)
    if is_space_free(board, 4):
        possible_moves.append(4)
    if is_space_free(board, 6):
        possible_moves.append(6)
    if is_space_free(board, 8):
        possible_moves.append(8)
    i = random.choice(possible_moves)
    return i

def get_computer_move(board, computer_letter, player_letter):
    move = find_winning_move(board, computer_letter)
    if move != None: return move
    move = block_player_move(board, player_letter)
    if move != None: return move
    move = choose_corner(board)
    if move != None: return move
    move = choose_center(board)
    if move != None: return move
    return choose_side(board)

def display_message(msg):
    """display some texts."""
    draw_board(board)
    text_surface = head_font.render(msg, True, (0, 0, 255))
    window_surface.blit(text_surface, (250, 220))
    pygame.display.update()
        
board = [' '] * 10
player_letter, computer_letter = input_player_letter()
turn = who_goes_first()
'''display_message('init')'''
is_playing = True

while is_playing:
    draw_board(board)
    '''display_message('it\'s '+turn+'\'s turn.')'''
    if turn == 'player':
        move = get_player_move(board)
        make_move(board, player_letter, move)

        if is_winner(board, player_letter):
            draw_board(board)
            display_message('Win')
            is_playing = False
            
        elif is_board_full(board):
            display_message('Draw')
            break
        
        else:
            turn = 'computer'
    else:
        # AI 1: random choose
        # AI 2: stragetic move
        move = get_computer_move(board, computer_letter, player_letter)
        make_move(board, computer_letter, move)
        
        if is_winner(board, computer_letter):
            draw_board(board)
            display_message('Lose')
            is_playing = False
            
        elif is_board_full(board):
            display_message('Draw')
            break
        
        else:
            turn = 'player'

