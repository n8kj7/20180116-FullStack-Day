# Minimum number of calls to display text in pygame window
import pygame
import l26_settings as settings

# to run anything in this module, pygame must be initialized
sample_text = 'This is a text test \n this is only a text test.'

#create a screen
pygame.display.init()
pygame.font.init()
def init_modules():
    pygame.display.init()
    pygame.font.init()  # consider using this instead

def init_screen(title_bar_text, icon_img, win_dimensions):
    win_bg_rgb = (0, 0, 0)
    surface_window = pygame.display.set_mode(win_dimensions) #init window
    pygame.display.set_caption(title_bar_text) # set caption
    pygame.display.set_icon(icon_img)  # set icon
    surface_window.fill(win_bg_rgb)
    return surface_window


def set_text(surface_win, text_lines, coordinates, text_color=settings.WHITE):
    font_size = 24
    text_font = pygame.font.SysFont('couriernew', font_size, bold=True)
    antialias = False
    bg_color = settings.BLACK
    text_lines = list(text_lines)
    coordinates[1] += text_font.get_height()
    for line in text_lines:
        rendered_text = text_font.render(line, antialias, text_color, bg_color)
        surface_win.blit(rendered_text, coordinates)
        coordinates[1] += text_font.get_height()

class MessageBox:  #holds messages, displays current
    messages = []
    font_size = 24
    text_font = pygame.font.SysFont('couriernew', font_size, bold=True)
    antialias = False
    bg_color = settings.BLACK

    def __init__(self, surface):
        self.surface = surface

    def display_message(self):
        coordinates = [0, 0]
        text_color = settings.WHITE
        rendered_text = self.text_font.render(self.messages[-1], self.antialias, text_color, self.bg_color)
        self.surface.blit(rendered_text, coordinates)

class StatusBox(MessageBox):  #holds messages, displays current
    messages = []
    font_size = 24
    text_font = pygame.font.SysFont('couriernew', font_size, bold=True)
    antialias = False
    bg_color = settings.BLACK

    def __init__(self, surface):
        self.surface = surface

    def display_message(self):
        coordinates = [0, 450]
        text_color = settings.WHITE
        rendered_text = self.text_font.render(self.messages[-1], self.antialias, text_color, self.bg_color)
        self.surface.blit(rendered_text, coordinates)


def next_line(y_value, font):
    return y_value + font.get_height()

def next_letter(x_value, font_size):
    return x_value + font_size

def display_screen():
    pygame.display.update()

# just a test script for the text/graphics module
#
# surface_coordinates = [100, 100]
# text_lines = 'Testing testing testing testing', 'testing'
#
# icon = pygame.image.load ('heart.png')  # icon file in game directory
# pygame.display.init()
# pygame.font.init()
# main_win = init_screen('hello', icon, (600, 480))
# display_text(main_win, text_lines, surface_coordinates)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

