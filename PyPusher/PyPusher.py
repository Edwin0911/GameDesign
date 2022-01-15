import pygame, sys, os, time

class Player():
    def __init__(self,pos):
        self.pos = pos

class Star():
    def __init__(self,pos):
        self.pos = pos

class Selector():
    def __init__(self,pos):
        self.pos = pos

dir_path = os.path.dirname(os.path.abspath(__file__))

pygame.init()

game_map = [ [' ',' ',' ',' ',' ',' ',' '],
           ['x','#','#','#','#','x',' '],
           ['#','o','o','o','o','#','x'],
           ['#','o','o','o','o','o','#'],
           ['#','o','o','o','o','o','#'],
           ['#','o','o','o','o','o','#'],
           ['#','o','o','o','o','o','#'],
           ['x','#','#','#','#','o','x']]

TILE_WIDTH = 50
TILE_HEIGHT = 85
TILE_FLOOR_HEIGHT = 40
MAP_WIDTH = len(game_map[0])
MAP_HEIGHT = len(game_map)

IMAGES = {'star': pygame.image.load(dir_path+'\\Star.png'),
              'selector': pygame.image.load(dir_path+'\\Selector.png'),
              'corner': pygame.image.load(dir_path+'\\Wall_Block_Tall.png'),
              'wall': pygame.image.load(dir_path+'\\Wood_Block_Tall.png'),
              'inside floor': pygame.image.load(dir_path+'\\Plain_Block.png'),
              'outside floor': pygame.image.load(dir_path+'\\Grass_Block.png'),
              'boy': pygame.image.load(dir_path+'\\boy.png'),
              'rock': pygame.image.load(dir_path+'\\Rock1.png'),
              'solved': pygame.image.load(dir_path+'\\star_solved.png')
          }

TILE_DEFINITION = {'x': IMAGES['corner'],
               '#': IMAGES['wall'],
               'o': IMAGES['inside floor'],
               ' ': IMAGES['outside floor'],
               '1': IMAGES['rock'],
               }

def set_state():


    return player, selectors, stars

def draw_map(game_map, player, stars, selectors):
    """Draws the map to a Surface object, including the player's position"""

    # map_surf will be the single Surface object that the tiles are drawn on,
    # by doing so it is easy to position the entire map on the BASE_SURF object

    # First, the width and height must be calculated.    
    map_surf_w = MAP_WIDTH * TILE_WIDTH
    map_surf_h = (MAP_HEIGHT-1) * TILE_FLOOR_HEIGHT + TILE_HEIGHT
    map_surf = pygame.Surface((map_surf_w, map_surf_h))
    map_surf.fill((0, 170, 255)) # start with a blank color on the surface.

    # Draw the tile sprites onto this surface.
    for r in range(len(game_map)):
        for c in range(len(game_map[r])):
            space_rect = pygame.Rect((c * TILE_WIDTH, r * TILE_FLOOR_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

            if game_map[r][c] in TILE_DEFINITION:
                base_tile = TILE_DEFINITION[game_map[r][c]]

            # First draw the base ground/wall tile.
            map_surf.blit(base_tile, space_rect)

            for item in selectors:
                if (r, c) == item.pos:
                    map_surf.blit(IMAGES['selector'], space_rect)

            for item in stars:
                if (r, c) == item.pos:
                    map_surf.blit(IMAGES['star'], space_rect)
                    
            # Last draw the player on the board.
            if (r, c) == player.pos:
                map_surf.blit(IMAGES['boy'], space_rect)

    return map_surf

def make_move(game_map, player, stars, move_to):
    offset = (0,0)

    if move_to == 'UP':
        offset = (-1,0)
    elif move_to == 'DOWN':
        offset = (1,0)
    elif move_to == 'LEFT':
        offset = (0,-1)
    elif move_to == 'RIGHT':
        offset = (0,1)

    newplayer_x = player.pos[0]+offset[0]
    newplayer_y = player.pos[1]+offset[1]
    
    if game_map[newplayer_x][newplayer_y] == 'o':
        if (newplayer_x, newplayer_y) != stars[0].pos and (newplayer_x, newplayer_y) != stars[1].pos:
            player.pos = (newplayer_x,newplayer_y)
        elif (newplayer_x, newplayer_y) == stars[0].pos:
            newstar_x = stars[0].pos[0]+offset[0]
            newstar_y = stars[0].pos[1]+offset[1]
            if game_map[newstar_x][newstar_y] == 'o' and (newstar_x,newstar_y) != stars[1].pos:
                stars[0].pos = (newstar_x,newstar_y)
                player.pos = (newplayer_x,newplayer_y)            
        elif (newplayer_x, newplayer_y) == stars[1].pos:
            newstar_x = stars[1].pos[0]+offset[0]
            newstar_y = stars[1].pos[1]+offset[1]
            if game_map[newstar_x][newstar_y] == 'o' and (newstar_x,newstar_y) != stars[0].pos:
                stars[1].pos = (newstar_x,newstar_y)
                player.pos = (newplayer_x,newplayer_y)  
    # TODO: compute the position that the player want to move   
    # TODO: check if that position is on the floor
    # TODO: check if there is a star on that position 
    # TODO: if the star can be pushed, push that star and move player to that position

def is_solved(selectors, stars):
    if selectors[0].pos == stars[0].pos and selectors[1].pos == stars[1].pos:
        return True
    else:
        return False
    # TODO: check if the puzzle is solved
    
while True:
    
    BASE_SURF = pygame.display.set_mode((800, 600))
    
    
    player = Player((5,4))
    selectors = [Selector((2,3)),Selector((2,4))]
    stars = [Star((4,2)),Star((4,4))]
        
    restart = 0
    while restart == 0:
        
        move_to = None
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    move_to = 'LEFT'
                if e.key == pygame.K_RIGHT:
                    move_to = 'RIGHT'
                if e.key == pygame.K_UP:
                    move_to = 'UP'
                if e.key == pygame.K_DOWN:
                    move_to = 'DOWN'
                if e.key == pygame.K_r:
                    restart = 1
                    # reset game state at current level    
        
        make_move(game_map, player, stars, move_to)

        BASE_SURF.fill((0, 170, 255))
        
        map_surf = draw_map(game_map, player, stars, selectors)
        map_surf_rect = map_surf.get_rect()
        map_surf_rect.center = BASE_SURF.get_rect().center
        BASE_SURF.blit(map_surf, map_surf_rect)

        if is_solved(selectors, stars):
            BASE_SURF.blit(IMAGES['solved'], (160,220))   
            
        # TODO: if the puzzle is solved, display a message to indicate user
        # TODO: render a text to indicate user  how to reset the game
        
        font = pygame.font.Font(None, 50)
        imgText = font.render("Press R to Restart", True, (255,255,255))
        BASE_SURF.blit(imgText, (250, 50)) 

        pygame.display.update()
