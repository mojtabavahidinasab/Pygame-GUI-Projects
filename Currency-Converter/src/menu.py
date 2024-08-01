import pygame

from card import Card

class Menu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list = ["INR", "USD", "GBP", "EUR", "JPY", "CAD", "AUD", "HKD", "ILS", "KES", "MYR", "PKR", "LKR", "SEK", "TRY", "AED"]
        self.card_list = []
        self.show_menu = False

    def load_list(self):

        for index, str in enumerate(self.list):
            card = Card(self.x, (self.y + (index * 33)), 70, 30, str)
            self.card_list.append(card)

    def draw(self, win):

        if self.show_menu:
            for card in self.card_list:
                card.draw(win)
