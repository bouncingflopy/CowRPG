import pygame
import random
from client_files.code.settings import *
from client_files.code.tile import Tile
from client_files.code.world import GroupYSort
from client_files.code.enemy import TitleEnemy


class Title:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(ppppo9, pppppo78)
        self.max_length = 14

        self.username = r""
        self.password = r""
        self.running = True
        self.quit = False

        self.release_mouse = False

        # BANK
        self.box_width = 400
        self.box_height = 350
        self.boxx = int(kljh / 2) - int(self.box_width / 2)
        self.boxy = int(faaasd / 2) - int(self.box_height / 2)
        self.box = pygame.Rect(self.boxx, self.boxy, self.box_width, self.box_height)

        # sevret
        self.username_title_text = self.font.render("Username", False, iuyweriuywer)
        self.username_title_text_rect = self.username_title_text.get_rect(topleft=(self.boxx + 50, self.boxy + 50))
        self.username_rect = pygame.Rect(self.boxx + 50, self.boxy + 80, 300, 50)
        self.username_text = None
        self.username_text_rect = None
        # sbd
        self.password_title_text = self.font.render("Password", False, iuyweriuywer)
        self.password_title_text_rect = self.password_title_text.get_rect(topleft=(self.boxx + 50, self.boxy + 150))
        self.password_rect = pygame.Rect(self.boxx + 50, self.boxy + 180, 300, 50)
        self.password_text = None
        self.password_text_rect = None

        # Get a life
        self.button_rect = pygame.Rect(self.boxx + 145, self.boxy + 270, 100, 50)
        self.button_text = self.font.render("Join", False, ggggg)
        self.button_text_rect = self.button_text.get_rect(topleft=(self.boxx + 152, self.boxy + 280))

        # Get a life
        self.username_selected = False
        self.password_selected = False

        # Get a life
        self.visible_sprites = GroupYSort()
        self.enemies = []
        self.background_setup()

    def background_setup(self):
        # sdf
        surface = pygame.image.load('../graphics/tiles/10.png').convert_alpha()
        for y in range(12):
            for x in range(20):
                Tile((x * osahkjfgaohf, y * osahkjfgaohf), (self.visible_sprites,), 'floor', True, 0, surface)

    def background(self):
        self.visible_sprites.custom_draw(pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0))

        # AAAA
        side = random.randrange(-1, 2, 2)
        x = (kljh if side == 1 else 0) + (side * osahkjfgaohf)
        y = random.randint(-osahkjfgaohf, faaasd + osahkjfgaohf)
        self.enemies.append(TitleEnemy("white_cow", (x, y), (self.visible_sprites,), (-side, 0)))


        for enemy in self.enemies:
            if enemy.vbvbv.x + enemy.dfhjhe[0] > kljh + osahkjfgaohf or enemy.vbvbv.x + enemy.dfhjhe[0] < -osahkjfgaohf:
                enemy.kill()

            enemy.title_move()

    def display(self):
        self.background()

        pygame.draw.rect(self.display_surface, kjfgh, self.box)

        self.display_surface.blit(self.username_title_text, self.username_title_text_rect)
        pygame.draw.rect(self.display_surface, cvmnv, self.username_rect)
        if self.username_selected:
            pygame.draw.rect(self.display_surface, kopkop, self.username_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, weoir8, self.username_rect, 3)
        self.display_surface.blit(self.username_text, self.username_text_rect)

        # y
        self.display_surface.blit(self.password_title_text, self.password_title_text_rect)
        pygame.draw.rect(self.display_surface, cvmnv, self.password_rect)
        if self.password_selected:
            pygame.draw.rect(self.display_surface, kopkop, self.password_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, weoir8, self.password_rect, 3)
        self.display_surface.blit(self.password_text, self.password_text_rect)

        # Button
        pygame.draw.rect(self.display_surface, fhdfhjdf, self.button_rect)
        self.display_surface.blit(self.button_text, self.button_text_rect)

    def mouse(self):
        mouse = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.release_mouse and not mouse_click[0]:
            self.release_mouse = False

        if mouse_click[0]:
            if self.username_rect.collidepoint(mouse[0], mouse[1]):
                self.username_selected = True
            else:
                self.username_selected = False

            if self.password_rect.collidepoint(mouse[0], mouse[1]):
                self.password_selected = True
            else:
                self.password_selected = False

            if self.button_rect.collidepoint(mouse[0], mouse[1]):
                self.running = False

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE or 'a' <= event.unicode <= 'z' or 'A' <= event.unicode <= 'Z' or '0' <= event.unicode <= '9':
                    if self.username_selected:
                        if event.key == pygame.K_BACKSPACE:
                            self.username = self.username[:-1]
                        elif len(self.username) < self.max_length:
                            self.username += str(event.unicode)

                    if self.password_selected:
                        if event.key == pygame.K_BACKSPACE:
                            self.password = self.password[:-1]
                        elif len(self.password) < self.max_length:
                            self.password += str(event.unicode)

        # Update text on screen
        # Username
        self.username_text = self.font.render(self.username, False, iuyweriuywer)
        self.username_text_rect = self.username_text.get_rect(topleft=(self.boxx + 60, self.boxy + 90))
        # Password
        self.password_text = self.font.render(self.password, False, iuyweriuywer)
        self.password_text_rect = self.password_text.get_rect(topleft=(self.boxx + 60, self.boxy + 190))

    def run(self):
        self.mouse()
        self.input()
        self.display()

        # Delete all enemies if join button is pressed
        if not self.running:
            for sprite in self.visible_sprites:
                sprite.kill()

        return self.quit, self.running, self.username, self.password
