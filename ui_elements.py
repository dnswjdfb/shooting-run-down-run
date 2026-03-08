import pygame

class InputBox:
    """A class for handling text input in pygame"""
    def __init__(self, x, y, w, h, text='', placeholder='', font_size=32):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        self.placeholder = placeholder
        self.font = pygame.font.SysFont('verdanai', font_size)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.password = False

    def handle_event(self, event):
        """Handle keyboard and mouse events for the input box"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box
            self.color = self.color_active if self.active else self.color_inactive
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text
                self.txt_surface = self.font.render(
                    '*' * len(self.text) if self.password else self.text, 
                    True, 
                    self.color
                )
        return None

    def update(self):
        """Update the width of the box if the text is too long"""
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        """Draw the input box and text to the screen"""
        # Blit the text
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the placeholder if no text and not active
        if not self.text and not self.active:
            placeholder_surface = self.font.render(self.placeholder, True, pygame.Color('grey'))
            screen.blit(placeholder_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)

class Button:
    """A class for creating buttons in pygame"""
    def __init__(self, x, y, w, h, text, font_size=32, color=(100, 100, 100), hover_color=(150, 150, 150)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = pygame.font.SysFont('verdanai', font_size)
        self.txt_surface = self.font.render(text, True, pygame.Color('white'))
        self.is_hovered = False

    def handle_event(self, event):
        """Handle mouse events for the button"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def update(self, mouse_pos):
        """Update button state based on mouse position"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        """Draw the button to the screen"""
        # Draw the button rect
        pygame.draw.rect(
            screen, 
            self.hover_color if self.is_hovered else self.color, 
            self.rect
        )
        # Draw the button text
        text_rect = self.txt_surface.get_rect(center=self.rect.center)
        screen.blit(self.txt_surface, text_rect)
        # Draw the border
        pygame.draw.rect(screen, pygame.Color('black'), self.rect, 2)

class MessageBox:
    """A class for displaying messages in pygame"""
    def __init__(self, x, y, w, h, text='', font_size=24, bg_color=(200, 200, 200), text_color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.SysFont('verdanai', font_size)
        self.set_text(text)
        self.visible = False
        self.timer = 0
        self.duration = 3000  # Display for 3 seconds by default

    def set_text(self, text):
        """Set the message text"""
        self.text = text
        # Wrap text to fit the box width
        self.wrapped_text = []
        words = text.split(' ')
        line = ''
        for word in words:
            test_line = line + word + ' '
            # If the line is too long, start a new line
            if self.font.size(test_line)[0] > self.rect.w - 20:
                self.wrapped_text.append(line)
                line = word + ' '
            else:
                line = test_line
        self.wrapped_text.append(line)  # Add the last line

    def show(self, text=None, duration=None):
        """Show the message box with optional new text and duration"""
        if text:
            self.set_text(text)
        if duration:
            self.duration = duration
        self.visible = True
        self.timer = pygame.time.get_ticks()

    def update(self):
        """Update the message box state"""
        if self.visible and pygame.time.get_ticks() - self.timer > self.duration:
            self.visible = False

    def draw(self, screen):
        """Draw the message box to the screen if visible"""
        if not self.visible:
            return
        
        # Draw the background
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, pygame.Color('black'), self.rect, 2)
        
        # Draw the text
        y_offset = 10
        for line in self.wrapped_text:
            text_surface = self.font.render(line, True, self.text_color)
            screen.blit(text_surface, (self.rect.x + 10, self.rect.y + y_offset))
            y_offset += self.font.get_height()