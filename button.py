import pygame
import math

class Button:
    def __init__(self, rect, color, text, text_color, action, is_arrow=False):
        self.rect = rect
        self.color = color
        self.text = text
        self.text_color = text_color
        self.action = action
        self.font = pygame.font.Font(None, 25)
        self.is_hovered = False
        self.is_arrow = is_arrow

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

    def update(self):
        self.is_hovered = self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

        if self.is_arrow:
            arrow_length = min(self.rect.width, self.rect.height) - 20
            arrow_center = self.rect.center
            arrow_end = (
                arrow_center[0] + math.cos(math.radians(225)) * arrow_length,
                arrow_center[1] + math.sin(math.radians(225)) * arrow_length
            )
            pygame.draw.line(surface, (0, 0, 0), arrow_center, arrow_end, 2)
            pygame.draw.polygon(
                surface, (0, 0, 0),
                [
                    (
                        arrow_end[0] + math.cos(math.radians(225 + 15)) * 10,
                        arrow_end[1] + math.sin(math.radians(225 + 15)) * 10
                    ),
                    arrow_end,
                    (
                        arrow_end[0] + math.cos(math.radians(225 - 15)) * 10,
                        arrow_end[1] + math.sin(math.radians(225 - 15)) * 10
                    )
                ]
            )

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)


def create_buttons(panel_rect, start_action, stop_action, reset_action):
    button_width = panel_rect.width - 20
    button_height = 40
    button_margin = 10

    button_y = panel_rect.top + 20

    buttons = []

    start_button_rect = pygame.Rect(
        panel_rect.left + 10, button_y, button_width, button_height
    )
    start_button = Button(
        start_button_rect,
        (0, 0, 0),
        "Start",
        (255, 255, 255),
        start_action
    )
    buttons.append(start_button)

    button_y += button_height + button_margin

    stop_button_rect = pygame.Rect(
        panel_rect.left + 10, button_y, button_width, button_height
    )
    stop_button = Button(
        stop_button_rect,
        (0, 0, 0),
        "Stop",
        (255, 255, 255),
        stop_action
    )
    buttons.append(stop_button)

    button_y += button_height + button_margin

    reset_button_rect = pygame.Rect(
        panel_rect.left + 10, button_y, button_width, button_height
    )
    reset_button = Button(
        reset_button_rect,
        (0, 0, 0),
        "Reset",
        (255, 255, 255),
        reset_action
    )
    buttons.append(reset_button)

    button_y += button_height + button_margin

    wind_direction_button_rect = pygame.Rect(
        panel_rect.left + 10, button_y, button_width, button_height
    )
    # wind_direction_button = Button(
    #     wind_direction_button_rect,
    #     (0, 0, 0),
    #     "Wind Direction",
    #     (255, 255, 255),
    #     wind_direction_action,
    #     is_arrow=True
    # )
    # buttons.append(wind_direction_button)

    return buttons
