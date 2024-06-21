# two player chess in python with Pygame!
# part one, set up variables images and game loop

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

# game variables and images
captured_pieces_white = []
captured_pieces_black = []

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
valid_rig = []
valid_targets = []
valid_glocations = []
valid_slocations = []
s_options = []
g_options = []
s_array = []
g_array = []
s_targets = []
g_targets = []

facts = []

# Define colors
BLACK = (0, 0, 0)
WHITE = (236, 236, 236)
SILVER = (150, 150, 253)
DARK_GREY = (54, 54, 54)
LIGHT_GREY = (160, 160, 160)
BABY_BLUE = (0, 127, 255)
DEEP_BLUE = (27, 27, 255)
RED = (255, 0, 0)
PINK = (255, 125, 125)
DARK_RED = (154, 0, 80)
TEAL = (0, 255, 255)
GOLD = (255, 192, 0)
DEEP_PURPLE = (100, 0, 255)
BRICK =  (180, 10, 0)
WOOD =  (165, 10, 0)
PAPER_BROWN = (255, 225, 178)
WINE = (76, 7, 9)
BRICK_BROWN =  (204, 63, 0)
VIOLET = (255, 0, 255)
TANGERINE = (255, 128, 0)

l_padx = 650 
l_pady = 625
l_buttonwidth = 100
l_buttonheight = 50

# Load Piece images

# Gold Piece images

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

# Gold Skipper
r_skipper = pygame.image.load("g_Shell.png")
red_skipper = pygame.transform.scale(r_skipper, (pl_width, pl_height))
o_skipper = pygame.transform.scale(r_skipper, (major_width, major_height))

# Gold Rigger
r_rigger = pygame.image.load("g_Rigger.png")
red_rigger = pygame.transform.scale(r_rigger, (pl_width, pl_height))
o_rigger = pygame.transform.scale(r_rigger, (major_width, major_height))

# Gold Rover
r_rover = pygame.image.load("g_Rover.png")
red_rover = pygame.transform.scale(r_rover, (n_width, n_height))
o_rover = pygame.transform.scale(r_rover, (n_width, n_height))

#Gold Drone
r_drone = pygame.image.load("g_Drone.png")
red_drone = pygame.transform.scale(r_drone, (pl_width, pl_height))
o_drone = pygame.transform.scale(r_drone, (major_width, major_height))

# Gold Mine
r_mine = pygame.image.load("g_Mine.png")
gold_mine = pygame.transform.scale(r_mine, (hamper_width, hamper_height))
o_mine = pygame.transform.scale(r_mine, (major_width, major_height))

# Gold Qbit
r_qbit = pygame.image.load("g_qbit.png")
gold_qbit = pygame.transform.scale(r_qbit, (hamper_width, hamper_height))
o_qbit = pygame.transform.scale(r_qbit, (major_width, major_height))



# Silver Piece Images

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

# Silver Skipper
s_skipper = pygame.image.load("s_Shell.png")
silver_skipper = pygame.transform.scale(s_skipper, (pl_width, pl_height))
i_skipper = pygame.transform.scale(s_skipper, (major_width, major_height))

# Silver Rigger 
s_rigger = pygame.image.load("s_Rigger.png")
silver_rigger = pygame.transform.scale(s_rigger, (pl_width, pl_height))
i_rigger = pygame.transform.scale(s_rigger, (major_width, major_height))

#Silver Rover
s_rover = pygame.image.load("s_Rover.png")
silver_rover = pygame.transform.scale(s_rover, (pl_width, pl_height))
i_rover = pygame.transform.scale(s_rover, (major_width, major_height))

#Silver Drone
s_drone = pygame.image.load("s_Drone.png")
silver_drone = pygame.transform.scale(s_drone, (pl_width, pl_height))
i_drone = pygame.transform.scale(s_drone, (major_width, major_height))

#Silver Target
s_qbit = pygame.image.load("s_qbit.png")
silver_qbit = pygame.transform.scale(s_qbit, (hamper_width, hamper_height))
i_qbit = pygame.transform.scale(s_qbit, (major_width, major_height))

# Silver Mine
s_mine = pygame.image.load("s_mine.png")
silver_mine = pygame.transform.scale(s_mine, (hamper_width, hamper_height))
i_mine = pygame.transform.scale(s_mine, (major_width, major_height))


#define boards


#Create Local Buttons
aerial_view = pygame.Rect(50, l_pady, l_buttonwidth, l_buttonheight)
board_view = pygame.Rect(200, l_pady, l_buttonwidth, l_buttonheight)
mine_field = pygame.Rect(350, l_pady, l_buttonwidth, l_buttonheight)

commence = pygame.Rect(500, l_pady, l_buttonwidth, l_buttonheight)

stop_game = pygame.Rect((G_WIDTH - 150), l_pady, 100, l_buttonheight)
set_plants = pygame.Rect((G_WIDTH - 150), (l_pady - 100), l_buttonwidth, l_buttonheight)
set_pieces = pygame.Rect((G_WIDTH - 150), (l_pady - 200), l_buttonwidth, l_buttonheight)

# Define button colors
button_color = WHITE
button_hover_color = BABY_BLUE

# Define button text colors
text_color = WHITE
text_hover_color = BLACK

# Define button text font
button_font = pygame.font.Font('freesansbold.ttf', 24)

# Piece lists
g_images = [o_queen, o_skipper, o_rigger, o_drone, o_rover, o_seeker, o_streamer]
s_images = [i_queen, i_skipper, i_rigger, i_drone, i_rover, i_seeker, i_streamer]

g_locations = []
s_locations = []

g_pieces = ['queen', 'skipper', 'rigger', 'drone', 'rover', 'seeker', 'seeker']
s_pieces = ['queen', 'skipper', 'rigger', 'drone', 'rover', 'seeker', 'seeker']

piece_list = ['queen', 'skipper', 'rigger', 'drone', 'rover', 'seeker', 'seeker']

g_planters = [ 'rigger', 'skipper', 'queen']
s_planters = [ 'rigger', 'skipper', 'queen']

#Plants lists
pict = [o_qbit, o_mine, i_qbit, i_mine]

plant_list = ['target', 'mine']

g_target_counter = [o_qbit, o_qbit]
s_target_counter = [i_qbit, i_qbit]
g_mine_counter = [o_mine, o_mine, o_mine, o_mine]
s_mine_counter = [i_mine, i_mine, i_mine, o_mine]

g_mine_coords = []
s_mine_coords = []
g_target_coords = []
s_target_coords = []

g_placed_mines = []
s_placed_mines = []

g_mines = [o_mine, o_mine, o_mine, o_mine, o_mine, o_mine, o_mine, o_mine, o_mine, o_mine]
s_mines = [i_mine, i_mine, i_mine, i_mine, i_mine, i_mine, i_mine, i_mine, i_mine, i_mine]

g_target = [o_qbit]
s_target = [i_qbit]

g_plants = ['target', 'mine']
s_plants = ['target', 'mine']

set_target = True

background_home = pygame.image.load("neutral.png")
background_home = pygame.transform.scale(background_home, (global_width, global_height))

background_game = pygame.image.load("pop.png")
background_game = pygame.transform.scale(background_game, (local_width, local_height))

background_board = pygame.image.load("neutral.png")
background_board = pygame.transform.scale(background_board, (local_width, local_height))

# check variables/ flashing counter
counter = 0
winner = ''

# Function to draw buttons with text
def draw_button(rect, text, hover=False):
    # Draw the button rectangle
    if hover:
        pygame.draw.rect(screen, button_color, rect)
    else:
        pygame.draw.rect(screen, DEEP_PURPLE, rect)
    
    # Render the text
    text_surface = button_font.render(text, True, text_hover_color if hover else text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    
    # Draw the text on the button
    screen.blit(text_surface, text_rect)

def display_button(rect, text, hover=False):
    
    if hover:
        pygame.draw.rect(screen, button_color, rect)
    else:
        pygame.draw.rect(screen, DARK_RED, rect)
    
    # Render the text
    text_surface = button_font.render(text, True, text_hover_color if hover else text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    
    # Draw the text on the button
    screen.blit(text_surface, text_rect)

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
                    

def draw_planters():
    if g_locations and s_locations:
        for i in range(len(g_planters)):
            index = piece_list.index(g_planters[i])
            screen.blit(g_images[index], (g_local[i][0] * c_width, g_local[i][1] * c_height))
            if turn_step < 2 and greyscale:  # Only draw selection in board_view
                if selection == i:
                    pygame.draw.rect(screen, 'red', [g_local[i][0] * c_width + 1, g_local[i][1] * c_height + 1,
                                                     pc_width, pc_height], 2)
                    
        for i in range(len(s_planters)):
            index = piece_list.index(s_planters[i])
            screen.blit(s_images[index], (s_local[i][0] * c_width  , s_local[i][1] * c_height))
            if turn_step >= 2 and greyscale:
                if selection == i:
                    pygame.draw.rect(screen, 'blue', [s_local[i][0] * c_width + 1, s_local[i][1] * c_height + 1,
                                                      pc_width, pc_height], 2)

def draw_plants():
        if set_target == False:
            if turn_step <= 1:
                if g_mine_coords:
                    index = plant_list.index(g_plants[1])
                    i = -1
                    while i < len(g_mine_coords):
                        if len(g_mine_counter) > 0:
                            screen.blit(g_mines[index], (g_mine_coords[i][0] * c_width , g_mine_coords[i][1] * c_height ))
                            i += 1

            else:
                if s_mine_coords:
                    index = plant_list.index(s_plants[1])
                    i = -1
                    while i < len(s_mine_coords):
                        if len(s_mine_counter) > 0:
                            screen.blit(s_mines[index], (s_mine_coords[i][0] * c_width , s_mine_coords[i][1] * c_height ))
                            i += 1

        else:
            if turn_step <= 1:
                if g_target_coords and click_coords != g_mine_coords:
                    index = plant_list.index(g_plants[0])
                    screen.blit(g_target[index], (g_target_coords[-1][0] * c_width , g_target_coords[-1][1] * c_height ))
            else:
                if s_target_coords:
                    index = plant_list.index(s_plants[0])
                    screen.blit(s_target[index], (s_target_coords[-1][0] * c_width , s_target_coords[-1][1] * c_height ))

            

                          
# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'drone':
            moves_list = check_drone(location, turn)
        elif piece == 'rover':
            moves_list = check_rover(location, turn)
        elif piece == 'streamer':
            moves_list = check_streamstep(location, turn)
        elif piece == 'seeker':
            moves_list = check_edgacent_seekset(location, turn)
        elif piece == 'rigger':
            moves_list = check_edgacent_moveset(location, turn)
        elif piece == 'skipper':
            moves_list = check_skipstep(location, turn)
        elif piece == 'queen':
            moves_list = check_queens_english(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


def check_array(planters, local, turn):
    rig_list = []
    all_rig_list = []
    for i in range((len(planters))):
        location = local[i]
        piece = planters[i]
        if piece == 'queen':
            rig_list = check_edgacent_mineset(location,turn)
        elif piece == 'skipper':
            rig_list = check_edgacent_mineset(location,turn)
        elif piece == 'rigger':
            rig_list = check_rigger(location, turn)
        all_rig_list.append(rig_list)
    return all_rig_list



def check_targets(planters, locations, turn):
    rig_list = []
    all_rig_list = []
    for i in range((len(planters))):
        location = locations[i]
        piece = planters[i]
        if piece == 'queen':
            rig_list = check_queens_spanish(location,turn)
        elif piece == 'seeker':
            pass
        elif piece == 'skipper':
            pass
        elif piece == 'rigger':
            pass
        all_rig_list.append(rig_list)
    return all_rig_list


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


def check_queens_spanish(position, color):
    rig_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
    else:
        friends_list = s_locations
        enemies_list = g_locations
    universal_list = enemies_list + friends_list
    for i in range(2):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 2
            y = 0
        elif i == 1:
            x = -2
            y = 0
        while path:
            if 0 <= position[0] + (chain * x) <= 14 and 0 <= position[1] + (chain * y) <= 6:
                rig_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                chain += 1
            else:
                path = False
    return rig_list

    
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

def check_edgacent_mineset(position,color):
    rig_list = []
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
            rig_list.append(target)
    return rig_list

def check_rigger(position, color):
    rig_list = check_edgacent_moveset(position, color)
    second_list = check_thecorners_moveset(position, color)
    third_list = check_skipstep(position, color)
    for i in range(len(second_list)):
        rig_list.append(second_list[i])
    for i in range(len(third_list)):
        rig_list.append(third_list[i])
    return rig_list
    

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

def check_edgacent_seekset(position, color):
    moves_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
        d_coords = s_mine_coords
        d_target = s_target_coords
    elif color == 'silver':
        friends_list = s_locations
        enemies_list = g_locations
        d_coords =  g_mine_coords
        d_target = g_target_coords
    universal_list = enemies_list + friends_list + d_coords
    # 8 squares to check for kings, they can go one square any direction
    targets = [(2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-2, 0)]
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in universal_list and 0 <= target[0] <= 14 and 0 <= target[1] <= 6:
            moves_list.append(target)
        if d_target:
            if target == d_target [-1]:
                facts.append(target)
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

def check_streamstep(position, color):
    moves_list = []
    path_coords = (position[0], position[1])
        
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
        d_mine_coords = s_mine_coords
    else:
        friends_list = s_locations
        enemies_list = g_locations
        d_mine_coords = g_mine_coords
    universal_list = enemies_list + friends_list
    for i in range(6):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        elif i == 3:
            x = -2
            y = 0
        elif i == 4:
            x = 2
            y = 0
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in universal_list and \
                    0 <= position[0] + (chain * x) <= 14 and 0 <= position[1] + (chain * y) <= 6:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                chain += 1
                
            else:
                path = False
    return moves_list


def check_skipstep(position, color):
    moves_list = []
    if color == 'gold':
        enemies_list = s_locations
        friends_list = g_locations
    else:
        friends_list = s_locations
        enemies_list = g_locations
    universal_list = enemies_list + friends_list
    # 8 squares to check for kings, they can go one square any direction
    targets = [(4, 0), (2, 2), (2, -2), (-2, 2), (-2, -2), (-4, 0)]
    for i in range(6):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in universal_list and 0 <= target[0] <= 14 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if set_up_phase == False:
        if turn_step < 2:
            options_list = g_options
        else:
            options_list = s_options
        valid_options = options_list[selection]
        print("Valid options for the selected piece:", valid_options)
        return valid_options

def check_valid_rig():
    if turn_step < 2:
        array_list = g_array
    else:
        array_list = s_array
    valid_array = array_list[selection]
    return valid_array

def check_valid_targets():
    if turn_step < 2:
            target_list = g_targets
    else:
            target_list = s_targets
    valid_targets = target_list[selection]
    return valid_targets


def display_valid(targets):
    #set target has been set
    if set_target == True:
        if turn_step < 2:
            color = TANGERINE
        else:
            color = DEEP_BLUE
    #mine view has been set 
    else:
        if turn_step < 2:
            color = RED
        else:
            color = DEEP_PURPLE
            
    for i in range(len(targets)):
            pygame.draw.circle(screen, color, (targets[i][0] * c_width + 40, targets[i][1] * c_height + 40), 5)

def place_pieces():
    for x in range(15):
        for y in range(7):
            if (x + y) % 2 != 0: 
                if turn_step < 2:
                        if y == 0:
                            valid_glocations.append((x,y))
    display_valid(valid_glocations)

def place_s_piece():
    for x in range(15):
        for y in range(7):
            if (x + y) % 2 != 0:
                if turn_step >= 2:
                        if y == 6:
                            valid_slocations.append((x,y))
    display_valid(valid_slocations)

def set_mines():
    for x in range(15):
        for y in range(7):
            if y != 6 and  y != 0 and (x + y) % 2 != 0:                
            # Remember to implement the turn step
                valid_rig.append((x,y))
    display_valid(valid_rig)

def declare_target():
    for x in range(15):
        for y in range(7):
            if 5 > y > 1 and (x + y) % 2 != 0:
                        valid_targets.append((x, y))
    display_valid(valid_targets)
                        
# draw valid moves on screen
def draw_valid(moves):
    if greyscale == False:
        if turn_step < 2:
            color = GOLD
        else:
            color = SILVER
    for i in range(len(moves)):
            pygame.draw.circle(screen, color, (moves[i][0] * c_width + 40, moves[i][1] * c_height + 40), 5)

def draw_checker(moves):
    if greyscale == False:
        if turn_step < 2:
            color = BLACK
        else:
            color = WHITE
    for i in range(len(moves)):
            pygame.draw.circle(screen, color, (moves[i][0] * c_width + 40, moves[i][1] * c_height + 40), 5)


def add_mine():
    if mis_step == False:
        if turn_step >= 2:
            item = o_mine
            g_mine_counter.append(item)
        else:
            item = i_mine
            s_mine_counter.append(item)
    else:
        if turn_step >= 2:
            item = i_mine
            s_mine_counter.append(item)
        else:
            item = o_mine
            g_mine_counter.append(item)

def add_target():
    if turn_step >= 2:
        item = o_qbit
        g_target_counter.append(item)
    else:
        item = i_qbit
        s_target_counter.append(item)

def drop_mine():
    if turn_step < 2:
        if g_mine_counter:
            g_mine_counter.pop()
    else:
        if s_mine_counter:
            s_mine_counter.pop()

def drop_target():
    if turn_step < 2:
        if g_target_counter:
            g_target_counter.pop()
    else:
        if s_target_counter:
            s_target_counter.pop()

def display_counter():
    if turn_step < 2:
        color = GOLD
        if set_target == False:
            counter_string = "Gold Mines"
            counter = g_mine_counter
            index = 1
        else:
            counter_string = "Gold Targets"
            counter = g_target_counter
            index = 0
    if turn_step >= 2:
        color = SILVER
        if set_target == False:
            counter_string = "Silver Mines"
            counter = s_mine_counter
            index = 3
        else:
            counter_string = "Silver Targets"
            counter = s_target_counter
            index = 2
        
    # Draw the counter text
    font = pygame.font.Font(None, 36)
    counter_text = font.render(f"{counter_string}: {(len(counter)-1)}", True, color)
    counter_text_rect = counter_text.get_rect()
    counter_text_rect.center = (G_WIDTH - 100, 50)
    screen.blit(counter_text, counter_text_rect)
    screen.blit(pict[index], (G_WIDTH - 200 , (G_HEIGHT / 2) - 250 ))

def display_command():
    if turn_step < 2:
        color = WHITE
        string = "Gold Player"
        nex_line = "Declare your target"
        if g_target_coords:
            nex_line = "Place your mines"
    if turn_step >= 2:
        color = LIGHT_GREY
        string = "Silver Player"
        nex_line = "Declare your target"
        if s_target_coords:
            string = "Place your mines"

    # Draw the counter text
    font = pygame.font.Font(None, 30)
    counter_text = font.render(f"{string} ", True, color)
    nexline = font.render(f"{nex_line} ", True, color)
    counter_text_rect = counter_text.get_rect()
    nexline_rect = nexline.get_rect()
    counter_text_rect.center = (G_WIDTH - 100, 350)
    nexline_rect.center = (G_WIDTH - 100, 380)
    screen.blit(counter_text, counter_text_rect)
    screen.blit(nexline, nexline_rect)
    

#Show the aerial view
def show_area():

    global board_display

    board_display=background_game

#Show the board view
def show_board():

    global board_display

    board_display=background_board


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


    

# main game loop

run = True
mis_step = False
game_over = False

set_up_phase = True
mining_phase = True

game_phase = True

greyscale = True


placing_pieces = False

piece_rotation = False

# Additional Flags
greyscale = True  # Indicates whether the game is in greyscale mode

# Commence Button Flag
commence_pressed = False  # Indicates whether the Commence button has been pressed

# You can use these flags to control the flow of the game and the phases



    
board_display = background_game
draw_game_screen()

while run:
    screen.fill('#222222')
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if aerial_view.collidepoint(event.pos):
                    if greyscale == False:
                        greyscale = True
                        show_board()
                    else:
                        greyscale = False
                        show_area()
                    
                if mine_field.collidepoint(event.pos):
                    if set_target == True:
                        set_target = False
                    else:
                        set_target = True
                if set_plants.collidepoint(event.pos):
                    if turn_step == 0:
                        set_target = True
                        turn_step = 2
                        
                if set_pieces.collidepoint(event.pos):
                    if turn_step >= 2:
                        mining_phase = False
                        greyscale = False
                        turn_step = 0
                        placing_pieces = True
                    else:
                        turn_step = 2
                        placing_pieces = True
                    
                if commence.collidepoint(event.pos):
                    placing_pieces = True
                    greyscale = False
                    set_up_phase = False
                    turn_step = 0
                if stop_game.collidepoint(event.pos):
                    running_game = False
                    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            y_coord = event.pos[1] // c_height
            x_coord = ( event.pos[0] ) // (c_width )
            click_coords = (x_coord, y_coord)


            #Rememver to use the names of the pieces and not their locations to get their locations on the mine view

            if set_up_phase == False:
                
                s_options = check_options(s_pieces, s_locations, 'silver')
                g_options = check_options(g_pieces, g_locations, 'gold')

                g_local = [ g_locations [2], g_locations [1],  g_locations [0]]
                s_local = [ s_locations [2], s_locations [1],  s_locations [0]]

                s_targets = check_targets(s_planters, s_local, 'silver')
                g_targets = check_targets(g_planters, g_local, 'gold')

                s_array = check_array(s_planters, s_local, 'silver')
                g_array = check_array(g_planters, g_local, 'gold')
            

            #Over board Main Game Screeen
            if set_up_phase == True:
                
                if greyscale == False:
                            if turn_step <= 1:
                                if click_coords in valid_glocations:#also try valid_rig or valid_spots or something if valid_moves doesn't work
                                        if click_coords not in g_locations:
                                            g_locations.append(click_coords)
                                            if len(g_locations) == 7:
                                                turn_step = 2
                            else:
                                if click_coords in valid_slocations:#also try valid_rig or valid_spots or something if valid_moves doesn't work
                                    if click_coords not in s_locations:
                                        s_locations.append(click_coords)
                                        # Where you handle piece selection
                                        print("Selected piece index:", selection)
                                        if len(s_locations) == 7:
                                            turn_step = 0
                                            set_up_phase = False

                else:
                        # It's all mines now
                        if set_target == False:
                            valid = valid_rig
                            if turn_step <= 1:
                                d_coords = g_mine_coords
                                e_coords = g_target_coords
                                union = d_coords + e_coords
                            else:
                                d_coords = s_mine_coords
                                e_coords = s_target_coords
                                union =d_coords + e_coords
                                
                            if click_coords in valid:
                                if click_coords not in union:
                                    d_coords.append(click_coords)
                                    drop_mine()
                                        
                                    selection = 100
                                    valid_moves = []
                                else:
                                    pass
                                    
                        #set target has been set to true
                        else:
                                valid = valid_targets
                                if turn_step <= 1:
                                    d_coords = g_target_coords
                                    m_coords = g_mine_coords
                                    union = d_coords + m_coords
                                else:
                                    d_coords = s_target_coords
                                    m_coords = s_mine_coords
                                    union = d_coords + m_coords
                                    
                                    
                                if click_coords in valid :
                                    if click_coords not in union:
                                        d_coords.append(click_coords)
                                        drop_target()
                                            
                                        selection = 100
                                        valid_moves = []

                                    else:
                                        pass

            #Set Up Phase is over
            else:
                if greyscale == False:
                            s_options = check_options(s_pieces, s_locations, 'silver')
                            g_options = check_options(g_pieces, g_locations, 'gold')
                            if turn_step <= 1:
                                d_locations = g_locations
                                e_locations = s_locations
                                d_pieces = g_pieces
                                e_pieces = s_pieces
                                e_local = s_local
                                d_planters = g_planters
                                e_planters = s_planters
                                e_mine_coords = s_mine_coords
                                e_target_coords = s_target_coords
                                orient = 'gold'
                                a = 0
                                b = 1
                                c = 2
                            else:
                                d_locations = s_locations
                                e_locations = g_locations
                                d_pieces = s_pieces
                                e_pieces = g_pieces
                                e_local = g_local
                                d_planters = s_planters
                                e_planters = g_planters
                                e_mine_coords = g_mine_coords
                                e_target_coords = g_target_coords
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
                                    e_planters.pop(e_piece)
                                    e_locations.pop(e_piece)
                                    e_local.pop(e_piece)
                                    add_target()
                                    add_mine()
                                    
                                if click_coords in e_mine_coords:
                                    e_minor = e_mine_coords.index(click_coords)
                                    mis_step = True
                                    d_pieces.pop(selection)
                                    d_locations.pop(selection)
                                    d_local.pop(selection)
                                    e_mine_coords.pop(e_minor)
                                    add_target()
                                    add_mine()

                                if click_coords in e_target_coords:
                                    winner = orient

                                #if mining_phase == False and placing_pieces == False:
                                        
                                turn_step = c
                                selection = 100
                                valid_moves = []

           
                # Set up phase concluded
                else:
                    valid = valid_rig
                    if set_target == False:
                        s_array = check_array(s_planters, s_local, 'silver')
                        g_array = check_array(g_planters, g_local, 'gold')
                    else:
                        g_targets = check_targets(g_planters, g_local, 'gold')
                        s_targets = check_targets(s_planters, s_local, 'silver')
                    if turn_step <= 1:
                            d_local = g_local
                            e_local = s_local
                            d_coords = g_mine_coords
                            m_coords = g_target_coords
                            e_coords = s_mine_coords
                            n_coords = s_target_coords

                    else:
                            d_local = s_local
                            e_local = g_local
                            d_coords = s_mine_coords
                            m_coords = s_target_coords
                            e_coords = g_mine_coords
                            n_coords = g_target_coords

                    if set_target == False:
                            union = d_local + e_local + d_coords + m_coords
                            
                            if click_coords in d_local:
                                selection = d_local.index(click_coords)
                                
                            if click_coords in valid and selection != 100:
                                if click_coords not in union:
                                    d_coords.append(click_coords)
                                    drop_mine()
                                        
                                    selection = 100
                                    valid_moves = []
                                else:
                                    pass

                    else:
                            union = d_coords + m_coords
                            if click_coords in d_local:
                                selection = d_local.index(click_coords)
                                
                            if click_coords in valid and selection != 100 :
                                if click_coords not in union:
                                    m_coords.append(click_coords)
                                    drop_target()
                                        
                                    selection = 100
                                    valid_moves = []

                                else:
                                    pass


    if greyscale == True:
        show_board()
        draw_game_screen()
        draw_planters()
        draw_plants()
        display_counter()
        display_command()
        if set_up_phase == False:
                if set_target == False:
                    if selection != 100:
                        if turn_step <= 1:
                            if len(g_mine_counter) != 1:
                                valid_rig  = check_valid_rig()
                                display_valid(valid_rig)
                            
                        else:
                            if len(s_mine_counter) !=1:
                                valid_rig  = check_valid_rig()
                                display_valid(valid_rig)
                            
                else:
                    if selection != 100:
                        if len(g_locations) < 7:
                            if len(g_target_counter) !=1:
                                valid_rig  = check_valid_targets()
                                display_valid(valid_rig)
                            
                        elif len(s_locations) < 7:
                            if len(s_target_counter) !=1:
                                valid_rig  = check_valid_targets()
                                display_valid(valid_rig)
                            
        else:
                if set_target == False:
                    set_mines()
                else:
                    declare_target()
                  
    
    if greyscale == False:
        show_area()
        draw_game_screen()
        draw_pieces()
        if set_up_phase == True:
            if placing_pieces == True:
                if len(g_locations) < 7:
                    place_pieces()
                elif len(s_locations) < 7:
                    place_s_piece()
        else:
            if selection != 100:
                valid_moves = check_valid_moves()
                draw_valid(valid_moves)
                draw_checker(facts)
    else:
        draw_button(mine_field, "Mine Field", set_target)
   
    if winner != '':
        game_over = True
        draw_game_over()

    if set_up_phase:
        if mining_phase:
            if turn_step <= 1:
                if g_target_coords:
                    set_target = False
                    display_button(set_plants, "Change Player", turn_step >= 2)
            if turn_step > 1:
                if s_target_coords:
                    set_target = False
                    display_button(set_pieces, "Set pieces", turn_step < 2)


    draw_button(aerial_view, "Board View", greyscale)
    draw_button(stop_game, "Stop Game")
    # Update the display
    
    pygame.display.update()
pygame.quit()
