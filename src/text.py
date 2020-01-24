import pygame

#create list of available anchors for text
available_anchors = ('topleft', 'bottomleft', 'topright', 'bottomright',
                     'midtop', 'midleft', 'midbottom', 'midright', 'center')

#create text for use in game
class Text(object):
    def __init__(self, position=(0, 0), text='', colour=(0, 0, 0), size=36, font='Lucida Sans', anchor='topleft'):
        self.position = position
        self.size = size
        self.colour = colour
        self.font = font
        self.text = str(text)
        self.anchor = anchor
        
        self.font_type = pygame.font.SysFont(self.font, self.size)
        self.surface = self.font_type.render(self.text, 1, self.colour)

        if anchor in available_anchors:
            exec('self.rect = self.surface.get_rect(' + self.anchor + '=self.position)')
        else:
            raise Exception('Invalid Anchor Point')

    def set_text(self, *text):
        self.text = ''

        for item in text:
            self.text += str(item) + ' '

        self.surface = self.font_type.render(self.text, 1, self.colour)

        if self.anchor in available_anchors:
            exec('self.rect = self.surface.get_rect(' + self.anchor + '=self.position)')
        else:
            raise Exception('Invalid Anchor Point')

    def update_settings(self, **settings):
        self.__dict__.update(settings)

        self.font_type = pygame.font.SysFont(self.font, self.size)
        self.surface = self.font_type.render(self.text, 1, self.colour)

        if self.anchor in available_anchors:
            exec('self.rect = self.surface.get_rect(' + self.anchor + '=self.position)')
        else:
            raise Exception('Invalid Anchor Point')

    def render(self, surface):
        surface.blit(self.surface, self.rect)


