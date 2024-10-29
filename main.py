import pygame

pygame.init()

width = 1000
height = 900

screen = pygame.display.set_mode([width , height])
pygame.display.set_caption("CHESS GAME")
font = pygame.font.Font('freesansbold.ttf' , 20)
big_font = pygame.font.Font('freesansbold.ttf' , 50)
timer = pygame.time.Clock()
fps = 60

white = ['rook' , 'knight' ,'bishop' , 'king' , 'queen' , 'bishop' , 'knight' , 'rook' , 
         'pawn' , 'pawn' ,'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' ,'pawn']
white_location = [(0,0) ,(1,0),(2,0) , (3,0) , (4,0) ,(5,0) , (6,0) ,(7,0),
                  (0,1) , (1,1) , (2,1) , (3,1) , (4,1) , (5,1) , (6,1) , (7,1)]
black = ['rook' , 'knight' ,'bishop' , 'king' , 'queen' , 'bishop' , 'knight' , 'rook' , 
         'pawn' , 'pawn' ,'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' ,'pawn']
black_location = [(0,7) ,(1,7),(2,7) , (3,7) , (4,7) ,(5,7) , (6,7) ,(7,7),
                  (0,6) , (1,6) , (2,6) , (3,6) , (4,6) , (5,6) , (6,6) , (7,6)]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []

black_queen = pygame.image.load('assets/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

def draw_board():
    for i in range(32):
        column = i%4
        row = i//4
        if row%2 == 0:
            pygame.draw.rect(screen , 'light gray' , [600-(column *200),row*100,100,100])
        else:
            pygame.draw.rect(screen , 'light gray' , [700-(column *200),row*100,100,100])
        pygame.draw.rect(screen , 'gray' , [0 , 800 , width ,100])
        pygame.draw.rect(screen , 'gold' , [0 , 800 , width ,100] , 5)
        pygame.draw.rect(screen , 'gold' , [800 , 0 , 200 ,height] , 5)
        status_text = ['White : Select a Piece to Move' , 'White : Select a Destination' ,
                       'Black : Select a Piece to Move' , 'Black : Select a Destination'  ]
        screen.blit(big_font.render(status_text[turn_step] , True , 'black') , (20 , 820))

        for i in range(9):
            pygame.draw.line(screen , 'black' , (0 , 100*i) , (800 , 100*i) , 2)
            pygame.draw.line(screen , 'black' , (100*i , 0) , (100*i , 800) , 2)

def draw_pieces():
    for i in range(len(white)):
        index = piece_list.index(white[i])
        if white[i] == 'pawn':
            screen.blit(white_pawn , (white_location[i][0] * 100 +22 , white_location[i][1]*100 + 30))
        else:
            screen.blit(white_images[index] ,(white_location[i][0] * 100 +10 , white_location[i][1]*100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen , 'red' , [white_location[i][0]*100+1 , white_location[i][1]*100+1 ,100 ,100] , 2)
    for i in range(len(black)):
        index = piece_list.index(black[i])
        if black[i] == 'pawn':
            screen.blit(black_pawn , (black_location[i][0] * 100 +22 , black_location[i][1]*100 + 30))
        else:
            screen.blit(black_images[index] ,(black_location[i][0] * 100 +10 , black_location[i][1]*100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen , 'blue' , [black_location[i][0]*100+1 , black_location[i][1]*100+1 ,100 ,100] , 2)
def check_options(pieces , locations , turn):
    moves_list = []
    all_moves_list = []
    for i in range((pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location , turn)
        elif piece == 'rook':
            moves_list = check_rook(location , turn)
        elif piece == 'knight':
            moves_list = check_knight(location , turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location , turn)
        elif piece == 'king':
            moves_list = check_king(location , turn)
        elif piece == 'queen':
            moves_list = check_queen(location , turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_location and \
                (position[0], position[1] + 1) not in black_location and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_location and \
                (position[0], position[1] + 2) not in black_location and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_location:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_location:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_location and \
                (position[0], position[1] - 1) not in black_location and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_location and \
                (position[0], position[1] - 2) not in black_location and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_location:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_location:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def draw_valid():
    pass

run = True
while run:
    timer.tick(fps)
    screen.fill('dark grey')
    draw_board()
    draw_pieces()
    if selection!=100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord , y_coord)
            if turn_step <= 1:
                if click_coords in white_location:
                    selection = white_location.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                    if click_coords in valid_moves and selection!=100:
                        white_location[selection] = click_coords
                        if click_coords in black_location:
                            black_piece = black_location.index(click_coords)
                            captured_pieces_white.append(black[black_piece])
                            black_piece.pop(black_piece)
                            black_location.pop(black_piece)
                        black_options = check_options(black , black_location , 'black')
                        white_options = check_options(white , white_location , 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []
            if turn_step > 1:
                if click_coords in black_location:
                    selection = black_location.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                    if click_coords in valid_moves and selection!=100:
                        black_location[selection] = click_coords
                        if click_coords in white_location:
                            white_piece = white_location.index(click_coords)
                            captured_pieces_black.append(white[black_piece])
                            white_piece.pop(white_piece)
                            white_location.pop(white_piece)
                        black_options = check_options(black , black_location , 'black')
                        white_options = check_options(white , white_location , 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []
    pygame.display.flip()  

pygame.quit()