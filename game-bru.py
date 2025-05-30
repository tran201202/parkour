import sys
import pygame
import time

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("My game")
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.dash = False

    def main_menu(self):
        self.background_image = pygame.image.load("start.png")
        
        self.start_button_image = pygame.image.load("start_button.png")
        # self.start_button_image = pygame.transform.scale(self.start_button_image, (250, 250))
        self.start_button_rect = self.start_button_image.get_rect(center = (650, 500))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(event.pos):
                        self.tutorial_screen()
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.start_button_image, self.start_button_rect)
            pygame.display.update()
            self.clock.tick(60)




    def Start_screen(self):
        self.background_image = pygame.image.load("background.png")
        self.character_image = pygame.image.load("Character.png")

        self.character_image = pygame.transform.scale(self.character_image, (25, 50))
        self.fcharge_image = pygame.image.load("5_rcharge.png")

        self.r_recharge = pygame.image.load("rush_recharge.png")
        self.r_recharge = pygame.transform.scale(self.r_recharge, (200, 200))  
        

        self.done_image = pygame.image.load("endscreen.png")
        self.done_image = pygame.transform.scale(self.done_image, (200, 100))
        self.endit_image = pygame.image.load("finish.png")
        self.endit_image = pygame.transform.scale(self.endit_image, (100, 200))
        self.floor_image = pygame.image.load("Floor.png")
        self.floor_image = pygame.transform.scale(self.floor_image, (200, 50))  
        self.left = pygame.image.load('HandL.png')
        self.left = pygame.transform.scale(self.left, (12, 10))
        self.right = pygame.image.load('HandR.png')
        self.right = pygame.transform.scale(self.right, (12, 10))
        self.jumpx2_symbol = pygame.image.load('double_jump_symbol.png')
        self.jumpx2_symbol = pygame.transform.scale(self.jumpx2_symbol, (12, 10))
        self.dash_symbol = pygame.image.load('dash_symbol.png')
        self.dash_symbol = pygame.transform.scale(self.dash_symbol, (12, 10))
        self.all_rect = {'rect1': [300, 700, 200, 50], 'rect2': [650, 700, 400, 50], 'rect3': [1200, 600, 200, 300], 'rect4': [1700, 700, 500, 50], 'rect5': [2250, 675, 150, 60], 'rect6': [2450, 650, 150, 70], 'rect6': [2450, 650, 150, 70], 'rect6': [2450, 650, 150, 70], 'rect6': [2450, 600, 150, 70], 'rect7': [2650, 550, 150, 70], 'rect8': [2850, 500, 150, 70], 'rect9': [3050, 450, 150, 70], 'rect10': [3250, 400, 150, 70]}
        
        for k, v in self.all_rect.items():
            a = k + "_image"
            setattr(self, a , pygame.transform.scale(self.floor_image, (v[-2], v[-1])))
            # self.floor_image = pygame.transform.scale(self.floor_image, (v[-2], v[-1]))
            setattr(self, k, self.floor_image.get_rect(topleft=(v[0], v[1])))



        # Character properties
        char_x, char_y = 400, 600 
        end_x, end_y = 3550, 500 
        char_velocity_x = 0
        char_velocity_y = 0
        gravity = 1
        jump_power = -15
        on_floor = False
        self.direction = 'right'
        dash_speed = 12
        dash_up_boost = -8
        dash_duration = 10
        dash_timer = 0
        jump_counter = 2
        gear_id = 1
        glove_id = 1
        rush = 0
        rush_count = 5
        FPS = 60
        rushed = False
        rushing = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        char_velocity_x = 5 + rush
                        self.direction = 'right'
                    if event.key == pygame.K_LEFT:
                        char_velocity_x = -5 - rush
                        self.direction = 'left' 
                    if event.key == pygame.K_SPACE and (jump_counter > 0):  
                        char_velocity_y = jump_power
                        jump_counter -= 1
                    if event.key == pygame.K_r:
                        gear_id += 1
                        if gear_id > 2:
                            gear_id = 1
                        if gear_id == 2:
                            rushed = True
                        else:
                            rushed = False
                    if event.key == pygame.K_t:
                        glove_id += 1
                        if glove_id > 2:
                            glove_id = 1
                        print(glove_id)
                    if event.key == pygame.K_e and self.dash and gear_id == 1:
                        if self.direction =='right':
                            char_velocity_x = dash_speed
                        elif self.direction == 'left':
                            char_velocity_x = - dash_speed
                        char_velocity_y = dash_up_boost
                        dash_timer = dash_duration
                        self.dash = False
                    if event.key == pygame.K_e and gear_id == 2 and rush_count > 0 and rushing == False:
                        rush = 6.5
                        rush_count -= 1
                        rushing = True
                        print(rush_count)
                        
                    elif gear_id != 2 or rush_count == 0:
                        rush = 0
                        rushing = False
                        



                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                        char_velocity_x = 0  

            
            char_velocity_y += gravity

            
            if char_y > 800:
                self.gameover()
            char_x -= char_velocity_x
            for k, v in self.all_rect.items():
                v[0] -= char_velocity_x

            if dash_timer > 0:
                dash_timer -= 1
                if dash_timer == 0:
                    if self.direction == 'right':
                        char_velocity_x = 5
                    else:
                        char_velocity_x = -5


            char_y += char_velocity_y
            end_x -= char_velocity_x
            

            on_floor = False
            
            for k, v in self.all_rect.items():
                char_y, char_velocity_y, a = self.check_collision(char_x, char_y, char_velocity_y, v[0], v[1], v[2], v[3])
                on_floor = on_floor or a

                    
                if self.dash != True:
                    if glove_id != 1:
                        pass
                    else:
                        self.dash = on_floor
            if on_floor == True and glove_id == 1:
                jump_counter = 2
            elif on_floor == True and glove_id == 2:
                jump_counter = 1


            char_x = max(400, 400)  

            self.screen.blit(self.background_image, (0, 0))
            for k,v in self.all_rect.items():
                a = k + '_image'
                self.screen.blit(getattr(self, a), (v[0], v[1]))

            self.screen.blit(self.character_image, (char_x, char_y))
            self.screen.blit(self.left, (char_x-15, char_y+20))
            self.screen.blit(self.right, (char_x+27.5, char_y+20))
            self.screen.blit(self.jumpx2_symbol, (char_x-15, char_y+20))
            self.screen.blit(self.dash_symbol, (char_x+27.5, char_y+20))   
            self.screen.blit(self.endit_image, (end_x, end_y))  
            if rushed == True:
                if rush_count == 5:
                    self.fcharge_image = pygame.image.load("5_rcharge.png")
                elif rush_count == 4:
                    self.fcharge_image = pygame.image.load("4_rcharge.png")
                elif rush_count == 3:
                    self.fcharge_image = pygame.image.load("3_rcharge.png")
                elif rush_count == 2:
                    self.fcharge_image = pygame.image.load("2_rcharge.png")
                elif rush_count == 1:
                    self.fcharge_image = pygame.image.load("1_rcharge.png")
                else:
                    self.fcharge_image = pygame.image.load("0_rcharge.png")

                self.screen.blit(self.fcharge_image, (50, 50))

            if self.win(char_x, char_y, end_x, end_y):
                self.game_win()

            pygame.display.update()
            self.clock.tick(FPS)

    def game_win(self):
        self.background_image = pygame.image.load('endscreen.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 800))
        self.retry_image = pygame.image.load('retry.png')
        self.retry_image = pygame.transform.scale(self.retry_image, (250, 150))
        self.retry_rect = self.retry_image.get_rect(topleft = (300, 600))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.retry_rect.collidepoint(event.pos):
                        self.Start_screen()
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.retry_image, self.retry_rect)
            pygame.display.update()
            self.clock.tick(60)

    def win(self, char_x, char_y, end_x, end_y):
        win = False
        if end_x <= char_x <= end_x + 100 or \
            end_x + 100 >= char_x + 25 >= end_x:
            if end_y <= char_y <= end_y + 200 or \
            end_y + 200 >= char_y >= end_y:
                win = True
        return win






    def gameover(self):
        self.background_image = pygame.image.load('gameover.png')
        self.retry_image = pygame.image.load('retry.png')
        self.retry_image = pygame.transform.scale(self.retry_image, (250, 150))
        self.retry_rect = self.retry_image.get_rect(topleft = (300, 600))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.retry_rect.collidepoint(event.pos):
                        self.Start_screen()
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.retry_image, self.retry_rect)
            pygame.display.update()
            self.clock.tick(60)

            


    def tutorial_screen(self):
        self.tutorial_image = pygame.image.load("Tutorial.png")
        self.tutorial_image = pygame.transform.scale(self.tutorial_image, (800, 800))
        self.close_image = pygame.image.load("Close.png")
        self.close_image = pygame.transform.scale(self.close_image, (250, 150))
        self.close_rect = self.close_image.get_rect(topleft = (300, 600))
                    
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.close_rect.collidepoint(event.pos):
                        self.Start_screen()
                
            self.screen.blit(self.tutorial_image, (0, 0))
            self.screen.blit(self.close_image, self.close_rect)
            pygame.display.update()
            self.clock.tick(60)

           


    def check_collision(self, char_x, char_y, char_velocity_y, rectx, recty, sizex, sizey):
        on_floor = False
        
        if recty < char_y + 50 < recty + 20:
            if rectx <= char_x <= rectx + sizex or \
               rectx <= char_x + 50 <= rectx + sizex:
                char_y = recty  - 50
                char_velocity_y = 0
                
                on_floor = True
            else:
                on_floor = False
        elif recty + 20 < char_y + 50 < recty + sizey:
            if rectx < char_x + 50 < rectx + (sizex / 2):
                char_x  = rectx - 50
            else:
                char_x = rectx + sizex
            on_floor = False
        
        return char_y, char_velocity_y, on_floor
Game().main_menu()
# Game().Start_screen()

