import pygame
import os

class Bar():
    def __init__(self, width, height, middle_color, top_color, x, y, delta_percent, already_percent = 0, bottom_color = None, warning_color = None, dynamic = False,name=None, font = None):
        self.width = width
        self.height = height
        
        self.bottom_color = bottom_color
        self.middle_color = middle_color
        self.top_color = top_color
        
        self.x = x
        self.y = y

        self.already_percent = min(already_percent,100)
        self.new_percent = delta_percent + already_percent

        if dynamic == True:
            self.current_percent = 0
        else:
            self.current_percent = 100
        self.lower_height = self.new_percent / 100 * self.height
        self.upper_height = self.height - self.lower_height
        self.warning_color = warning_color
        self.with_name = False
        if name!= None:
            self.name = name
            self.with_name = True
            self.text_color = self.hex_to_rgb("#343f51")
            self.load_font()

    def load_font(self):
        self.myFont = pygame.font.Font(os.path.join("font", "anke.regular.ttf"), int(self.width / 2))

    def hex_to_rgb(self,value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def increment_height(self):
        if self.current_percent < max(100,self.new_percent):
            self.current_percent += 2

    def drawBar(self, screen):
        if self.current_percent <= 100:
            if self.current_percent <= self.already_percent:
                lower_height = self.current_percent/100*self.height
                pygame.draw.rect(screen, self.bottom_color,
                                 (self.x, self.y - lower_height, self.width, lower_height+0.5), 0)
            elif self.current_percent <= self.new_percent:
                lower_height = self.already_percent/100*self.height
                middle_height = (self.current_percent-self.already_percent)/100*self.height
                pygame.draw.rect(screen, self.bottom_color,
                                 (self.x, self.y - lower_height,self.width,lower_height+0.5), 0)
                pygame.draw.rect(screen, self.middle_color,
                                 (self.x, self.y - lower_height - middle_height, self.width, middle_height+0.5), 0)
            elif self.current_percent >= self.new_percent:
                lower_height = self.already_percent/100*self.height
                middle_height = (self.new_percent-self.already_percent)/100*self.height
                upper_height = (self.current_percent-self.new_percent)/100*self.height
                pygame.draw.rect(screen, self.bottom_color,
                                 (self.x, self.y - lower_height,self.width,lower_height+0.5), 0)
                pygame.draw.rect(screen, self.middle_color,
                                 (self.x, self.y - lower_height - middle_height, self.width, middle_height+0.5), 0)
                pygame.draw.rect(screen, self.top_color,
                                 (self.x, self.y - lower_height - middle_height - upper_height, self.width, upper_height+0.5), 0)
        if self.current_percent > 100:
            lower_height = self.already_percent / 100 * self.height
            middle_height = (100 - self.already_percent) / 100 * self.height
            upper_height = (self.current_percent - 100) / 100 * self.height
            pygame.draw.rect(screen, self.bottom_color,
                             (self.x, self.y - lower_height, self.width, lower_height + 0.5), 0)
            pygame.draw.rect(screen, self.middle_color,
                             (self.x, self.y - lower_height - middle_height, self.width, middle_height + 0.5), 0)
            pygame.draw.rect(screen, self.warning_color,
                             (self.x, self.y - lower_height - middle_height - upper_height, self.width,
                              upper_height + 0.5), 0)
        if self.with_name:
            self.drawName(screen)

    def drawName(self, screen):
        textSurface = self.myFont.render(self.name, True, self.text_color)
        textRect1 = textSurface.get_rect()
        textRect1.center = (self.x + self.width / 2, self.y + 10)
        screen.blit(textSurface, textRect1)
