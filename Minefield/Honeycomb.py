import os
import pygame

pygame.init()

G_WIDTH = 850
G_HEIGHT = 690

global_width = 800
global_height = 700

local_height = 590
local_width = 600

WIDTH = 690
HEIGHT = 650
b_width = 600 
b_height = 590
c_width = (b_width/15) + 3
c_height = (b_height/7) + 3
pc_width = WIDTH/7
pc_height = HEIGHT/7

board_marginx = 45
board_marginy = 20

screen = pygame.display.set_mode([G_WIDTH, G_HEIGHT])
pygame.display.set_caption('Minefield')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
logo = pygame.image.load('ghostface.png')
pygame.display.set_icon(logo)

major_height = 90
major_width = 90
hamper_height = 200
hamper_width = 200
minor_height = 30
minor_width = 30
n_width = 95
n_height = 100

l_padx = 650 
l_pady = 625
l_buttonwidth = 100
l_buttonheight = 50

p_width = minor_width
p_height = minor_height

pl_width = minor_width
pl_height = minor_height

# Gold Queen
r_queen = pygame.image.load("g_Queen.png")
red_queen = pygame.transform.scale(r_queen, (p_width, p_height))
o_queen = pygame.transform.scale(r_queen, (major_width, major_height))

# Gold Streamer
r_streamer = pygame.image.load("g_Skipper.png")
red_streamer = pygame.transform.scale(r_streamer, (pl_width, pl_height))
o_streamer = pygame.transform.scale(r_streamer, (major_width, major_height))

# Gold Seeker
r_seeker = pygame.image.load("g_Seeker.png")
red_seeker = pygame.transform.scale(r_seeker, (p_width, p_height))
o_seeker = pygame.transform.scale(r_seeker, (major_width, major_height))


# Silver Queen
s_queen = pygame.image.load("s_Queen.png")
silver_queen = pygame.transform.scale(s_queen, (p_width, p_height))
i_queen = pygame.transform.scale(s_queen, (major_width, major_height))

# Silver Seeker
s_seeker = pygame.image.load("s_Seeker.png")
silver_seeker = pygame.transform.scale(s_seeker, (p_width, p_height))
i_seeker = pygame.transform.scale(s_seeker, (major_width, major_height))

# Silver Streamer
s_streamer = pygame.image.load("s_Skipper.png")
silver_streamer = pygame.transform.scale(s_streamer, (pl_width, pl_height))
i_streamer = pygame.transform.scale(s_streamer, (major_width, major_height))


# Define button text font
button_font = pygame.font.Font('freesansbold.ttf', 24)


# Piece lists
g_images = [o_queen, o_seeker, o_streamer, o_seeker, o_streamer, o_seeker, o_streamer,]
s_images = [i_queen, i_seeker, i_streamer, i_seeker, i_streamer, i_seeker, i_streamer,]

g_locations = [(7,0), (5,0), (3,0), (1,0), (9,0), (11,0), (13,0)]
s_locations = [(7,6), (5,6), (3,6), (1,6), (9,6), (11,6), (13,6)]

g_pieces = ['queen', 'drone', 'seeker', 'drone', 'seeker', 'drone', 'seeker']
s_pieces = ['queen', 'drone', 'seeker', 'drone', 'seeker', 'drone', 'seeker']

piece_list = ['queen', 'drone', 'seeker']



background_home = pygame.image.load("neutral.png")
background_home = pygame.transform.scale(background_home, (global_width, global_height))

background_game = pygame.image.load("pop.png")
background_game = pygame.transform.scale(background_game, (local_width, local_height))

background_board = pygame.image.load("neutral.png")
background_board = pygame.transform.scale(background_board, (local_width, local_height))

turn_step = 0
click_coords = 100
valid_moves = []

selection = 100

# draw main game board
def draw_game_screen():
    screen.blit(board_display, (board_marginx, board_marginy))


# draw pieces onto board
def draw_pieces():
    if g_locations:
        for i in range(len(g_pieces)):
            for i in range(len(g_locations)):
                index = piece_list.index(g_pieces[i])
                screen.blit(g_images[index], (g_locations[i][0] * c_width , g_locations[i][1] * c_height ))
            if turn_step < 2:
                if selection == i:
                    pygame.draw.rect(screen, 'white', [g_locations[i][0] * c_width + 1, g_locations[i][1] * c_height + 1,
                                                     pc_width, pc_height], 2)

    if s_locations :
        for i in range(len(s_pieces)):
            for i in range(len(s_locations)):
                index = piece_list.index(s_pieces[i])
                screen.blit(s_images[index], (s_locations[i][0] * c_width , s_locations[i][1] * c_height ))
            if turn_step >= 2:
                if selection == i:
                    pygame.draw.rect(screen, 'white', [s_locations[i][0] * c_width + 1, s_locations[i][1] * c_height + 1,
                                                     pc_width, pc_height], 2)

# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'drone':
            moves_list = check_drone(location, turn)
        elif piece == 'seeker':
            moves_list = check_rover(location, turn)
        elif piece == 'queen':
            moves_list = check_queens_english(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_queens_english(position, color):
    moves_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
    elif color == 'silver':
        friends_list = s_locations
        enemies_list = g_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-2, 0)]
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 14 and 0 <= target[1] <= 6:
            moves_list.append(target)
    return moves_list

def check_drone(position, color):
    moves_list = check_thecorners_moveset(position, color)
    second_list = check_edgacent_killset(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_rover(position, color):
    moves_list = check_edgacent_moveset(position, color)
    second_list = check_thecorners_killset(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_edgacent_moveset(position, color):
    moves_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
    elif color == 'silver':
        friends_list = s_locations
        enemies_list = g_locations
    universal_list = enemies_list + friends_list
    # 8 squares to check for kings, they can go one square any direction
    targets = [(2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-2, 0)]
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in universal_list and 0 <= target[0] <= 14 and 0 <= target[1] <= 6:
            moves_list.append(target)
    return moves_list

def check_edgacent_killset(position, color):
    moves_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
    elif color == 'silver':
        friends_list = s_locations
        enemies_list = g_locations
    universal_list = enemies_list + friends_list
    targets = [(2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-2, 0)]
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target in enemies_list and 0 <= target[0] <= 14 and 0 <= target[1] <= 6:
            moves_list.append(target)
    return moves_list

def check_thecorners_moveset(position, color):
    moves_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
    else:
        friends_list = s_locations
        enemies_list = g_locations
    universal_list = enemies_list + friends_list
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(0, 2), (0, -2), (3, 1), (3, -1), (-3, 1), (-3, -1)]
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in universal_list and 0 <= target[0] <= 14 and 0 <= target[1] <= 6:
            moves_list.append(target)
    return moves_list

def check_thecorners_killset(position, color):
    moves_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
    else:
        friends_list = s_locations
        enemies_list = g_locations
    universal_list = enemies_list + friends_list
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(0, 2), (0, -2), (3, 1), (3, -1), (-3, 1), (-3, -1)]
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target in enemies_list and 0 <= target[0] <= 14 and 0 <= target[1] <= 6:
            moves_list.append(target)
    return moves_list

def check_valid_moves():
        if turn_step < 2:
            options_list = g_options
        else:
            options_list = s_options
        valid_options = options_list[selection]
        print("Valid options for the selected piece:", valid_options)
        return valid_options

def draw_valid(moves):
    if turn_step < 2:
            color = '#88ff00'
    else:
            color = '#00ff88'
    for i in range(len(moves)):
            pygame.draw.circle(screen, color, (moves[i][0] * c_width + 40, moves[i][1] * c_height + 40), 5)

def check_win_condition():
    if "queen" not in g_pieces:
        return "Silver"
    elif "queen" not in s_pieces:
        return "Gold"
    else:
        return None
    


run = True
game_over = False

board_display = background_game
draw_game_screen()

while run:
    screen.fill('#222222')
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            y_coord = event.pos[1] // c_height
            x_coord = (event.pos[0]) // (c_width)
            click_coords = (x_coord, y_coord)

            # Update selection regardless of whose piece is clicked
            if click_coords in g_locations or click_coords in s_locations:
                selection = g_locations.index(click_coords) if click_coords in g_locations else s_locations.index(click_coords)
                print("Selected piece index:", selection)

            s_options = check_options(s_pieces, s_locations, 'silver')
            g_options = check_options(g_pieces, g_locations, 'gold')

            if turn_step <= 1:
                                    d_locations = g_locations
                                    e_locations = s_locations
                                    d_pieces = g_pieces
                                    e_pieces = s_pieces
                                    orient = 'gold'
                                    a = 0
                                    b = 1
                                    c = 2
            else:
                                    d_locations = s_locations
                                    e_locations = g_locations
                                    d_pieces = s_pieces
                                    e_pieces = g_pieces
                                    orient = 'silver'
                                    a = 2
                                    b = 3
                                    c = 0

            if click_coords in d_locations:
                                    selection = d_locations.index(click_coords)
                                    # Where you handle piece selection
                                    print("Selected piece index:", selection)
                                    if turn_step == a:
                                        turn_step = b
                                             
                                
            if click_coords in valid_moves and selection != 100:
                                    d_locations[selection] = click_coords
                                    if click_coords in e_locations:
                                        e_piece = e_locations.index(click_coords)
                                        mis_step = False
                                        e_pieces.pop(e_piece)
                                        e_locations.pop(e_piece)
                                        

                                    #if mining_phase == False and placing_pieces == False:
                                            
                                    turn_step = c
                                    selection = 100
                                    valid_moves = []
                                    
                                    winner = check_win_condition()
                                    if winner:
                                        print("Winner:", winner)
                                        game_over = True
   
    draw_game_screen()
    draw_pieces()

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    pygame.display.update()
pygame.quit()
