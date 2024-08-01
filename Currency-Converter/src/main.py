import pygame

pygame.init()

from menu import Menu
from card import Card
from textbar import Textbar
from converter import change_currency

class App:
    def __init__(self):
        self.width, self.height = 800, 500
        self.win = pygame.display.set_mode((self.width, self.height))
        self.final_value = 0
        self.color = (200, 100, 100)
        self.initial_menu_card = Card(10, 10, 120, 30, "INITIAL")
        self.initial_menu = Menu((self.initial_menu_card.x + self.initial_menu_card.width//2 - 35), (self.initial_menu_card.y + self.initial_menu_card.height + 3))

        self.final_menu_card = Card(670, 10, 120, 30, "FINAL")
        self.final_menu = Menu((self.final_menu_card.x + self.final_menu_card.width//2 - 35), (self.final_menu_card.y + self.final_menu_card.height + 3))

        self.textbar = Textbar(self.initial_menu_card.x + self.initial_menu_card.width + 170, 40, 200, 50, True, 30)
        self.to_write = False

        self.initial_text = Textbar(self.textbar.x, self.textbar.y + 60, 200, 50, False, 25)
        self.final_text = Textbar(self.textbar.x, self.textbar.y + 120, 200, 50, False, 25)

    def change_currency_value(self):
        if not self.textbar.str == "" and (self.textbar.str.replace('.', '', 1).isnumeric()):
            if not (self.initial_menu_card.string == "INITIAL") and not (self.final_menu_card.string == "FINAL"):

                self.final_value = change_currency(self.initial_menu_card.string, self.final_menu_card.string, float(self.textbar.str))
                self.final_value = round(self.final_value, 3)

    def text(self):
        if not self.initial_menu_card.string == "INITIAL":
            self.initial_text.str = f"{self.textbar.str} {self.initial_menu_card.string}"
        
        if not self.final_menu_card.string == "FINAL" and not self.final_value == 0:
            self.final_text.str = f"= {self.final_value} {self.final_menu_card.string}"

    def main_function(self):

        self.initial_menu.load_list()
        self.final_menu.load_list()

        Running = True
        while Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if self.initial_menu_card.rect.collidepoint(pos):
                        self.initial_menu.show_menu = not self.initial_menu.show_menu

                    if self.final_menu_card.rect.collidepoint(pos):
                        self.final_menu.show_menu = not self.final_menu.show_menu

                    for card in self.initial_menu.card_list:
                        if card.rect.collidepoint(pos):
                            self.initial_menu_card.string = card.string

                    for card in self.final_menu.card_list:
                        if card.rect.collidepoint(pos):
                            self.final_menu_card.string = card.string

                    if self.textbar.rect.collidepoint(pos):
                        self.to_write = True
                        self.textbar.color_bg = (0, 0, 0)
                    else:
                        self.to_write = False
                        self.textbar.color_bg = self.textbar.color
                    
                if event.type == pygame.MOUSEWHEEL:
                    offset = event.y * 10
                
                    for card in self.initial_menu.card_list:
                        card.y += offset
                        card.update_rect()

                    self.initial_menu_card.y += offset
                    self.initial_menu_card.update_rect()
                
                    for card in self.final_menu.card_list:
                        card.y += offset
                        card.update_rect()

                    self.final_menu_card.y += offset
                    self.final_menu_card.update_rect()

                if event.type == pygame.KEYDOWN:

                    if self.to_write:

                        if event.key == pygame.K_BACKSPACE:
                            self.textbar.str = self.textbar.str[:-1]

                        elif event.key == pygame.K_RETURN:
                            self.change_currency_value()
                            print('enter clicked')

                        else:
                            self.textbar.str += event.unicode


            self.draw()

    def draw(self):

        self.win.fill(self.color)

        self.initial_menu_card.draw(self.win)
        self.final_menu_card.draw(self.win)

        self.initial_menu.draw(self.win)
        self.final_menu.draw(self.win)

        self.textbar.draw(self.win)
        self.initial_text.draw(self.win)
        self.final_text.draw(self.win)

        self.text()

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()