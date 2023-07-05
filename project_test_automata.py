import pygame
import random
from button import Button
from PIL import Image

# Load the JPG image
image = Image.open("map.jpg")

# Resize the image
image = image.resize((800, 1200))

# Convert the image to a pixel array
pixel_array = image.load()




# Colors
COLORS = {
    'EMPTY': (0, 0, 0),
    'TREE': (0, 255, 0),
    'BURNING': (255, 0, 0),
    'BURNING_DURATION': (255, 165, 0),
    'WATER': (0, 0, 255)  # New color for water
}

# Cell size
CELL_SIZE = 2
scale_factor = 2

# States
STATES = {
    'EMPTY': 'EMPTY',
    'TREE': 'TREE',
    'BURNING': 'BURNING',
    'BURNING_DURATION': 'BURNING_DURATION',
    'WATER': 'WATER'  # New state for water
}

# Neighbors
NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),          (1, 0),
    (-1, 1), (0, 1), (1, 1),
]

# Wind direction
wind_direction = (0, 0)

def rgb(r, g, b):
    for value in (r, g, b):
        if value < 0 or value > 255:
            raise ValueError("Color components must be in the range [0, 255].")
    return r, g, b


def neighborhood_on_fire(data, row, col, threshold):
    burning_count = 0
    for neighbor in NEIGHBORS:
        neighbor_row = (row + neighbor[1]) % len(data)
        neighbor_col = (col + neighbor[0]) % len(data[0])
        if data[neighbor_row][neighbor_col] in [STATES['BURNING'], STATES['BURNING_DURATION']]:
            burning_count += 1
            if burning_count >= threshold:
                return True
    return False


def count_burning_neighbors(data, row, col):
    count = 0
    for neighbor in NEIGHBORS:
        neighbor_row = (row + neighbor[1]) % len(data)
        neighbor_col = (col + neighbor[0]) % len(data[0])
        if data[neighbor_row][neighbor_col] == STATES['BURNING']:
            count += 1
    return count


def generate_forest(rows, cols, p_growth):
    return [[STATES['TREE'] if random.random() < p_growth else STATES['EMPTY'] for _ in range(cols)] for _ in range(rows)]


def generate_water_bodies(data, num_bodies):
    for _ in range(num_bodies):
        body_size = random.randint(7, 14)  # Randomize the size of the water body
        patch_row = random.randint(0, len(data) - body_size)
        patch_col = random.randint(0, len(data[0]) - body_size)

        # Set the entire area as water
        for row in range(patch_row, patch_row + body_size):
            for col in range(patch_col, patch_col + body_size):
                data[row][col] = STATES['WATER']

        # Create irregularity along the edges
        for row in range(patch_row, patch_row + body_size):
            for col in range(patch_col, patch_col + body_size):
                if (
                    (row == patch_row or row == patch_row + body_size - 1 or row >= len(data) - 5)
                    or (col == patch_col or col == patch_col + body_size - 1 or col >= len(data[0]) - 5)
                ) and data[row][col] == STATES['WATER']:
                    # Introduce randomness to create irregularity along the edges
                    if random.random() < 0.7:  # Adjust the probability to control irregularity
                        if random.random() < 0.3:  # Adjust the probability to control empty vs tree cells
                            data[row][col] = STATES['EMPTY']
                        else:
                            data[row][col] = STATES['TREE']

# Generate the initial forest based on the pixel colors
data = []
for row in range(rows):
    row_data = []
    for col in range(cols):
        r, g, b = pixel_array[col, row]
        if (r, g, b) == COLORS['TREE']:
            row_data.append(STATES['TREE'])
        elif (r, g, b) == COLORS['WATER']:
            row_data.append(STATES['WATER'])
        else:
            row_data.append(STATES['EMPTY'])
    data.append(row_data)



def wind_direction_action():
    global wind_direction

    # Set the wind direction based on the desired values
    wind_direction = (1, 0)  # Example wind direction: right (1, 0)



def update(data, p_growth, p_lightning, threshold, wind_direction, wind_speed):
    new_data = [[STATES['EMPTY'] for _ in row] for row in data]
    for row in range(len(data)):
        for col in range(len(data[row])):
            current_state = data[row][col]
            new_state = STATES['EMPTY']

            if current_state == STATES['TREE']:
                # Spread fire to neighboring cells
                burning_neighbors = 0
                for neighbor in NEIGHBORS:
                    neighbor_row = (row + neighbor[1]) % len(data)
                    neighbor_col = (col + neighbor[0]) % len(data[0])
                    neighbor_state = data[neighbor_row][neighbor_col]

                    if (neighbor_state in [STATES['BURNING'], STATES['BURNING_DURATION']]) or (random.random() < p_lightning):
                        burning_neighbors += 1

                if burning_neighbors >= threshold:
                    new_state = STATES['BURNING']
                else:
                    new_state = STATES['TREE']

                # Apply wind effects
                if wind_speed > 0:
                    wind_row, wind_col = wind_direction
                    wind_row = int(wind_row * wind_speed)
                    wind_col = int(wind_col * wind_speed)
                    wind_neighbor_row = (row + wind_row) % len(data)
                    wind_neighbor_col = (col + wind_col) % len(data[0])
                    wind_neighbor_state = data[wind_neighbor_row][wind_neighbor_col]

                    if wind_neighbor_state in [STATES['BURNING'], STATES['BURNING_DURATION']]:
                        new_state = STATES['BURNING']

            elif current_state == STATES['BURNING']:
                new_state = STATES['BURNING_DURATION']
            elif current_state == STATES['BURNING_DURATION']:
                # Keep the BURNING_DURATION state for a longer duration
                if random.random() < 0.2:  # Adjust the probability to control the duration
                    new_state = STATES['EMPTY']
                else:
                    new_state = STATES['BURNING_DURATION']
            elif current_state == STATES['WATER']:
                new_state = STATES['WATER']

            new_data[row][col] = new_state
    return new_data

def draw_panel(surface, screen_width, screen_height, buttons):
    panel_width = 200  # Width of the side panel
    panel_color = (100, 100, 100)  # Color of the side panel

    panel_rect = pygame.Rect(screen_width - panel_width, 0, panel_width, screen_height)
    pygame.draw.rect(surface, panel_color, panel_rect)

    for button in buttons:
        button.draw(surface)


def draw(data, surface):
    for row in range(len(data)):
        for col in range(len(data[row])):
            color = COLORS[data[row][col]]
            for x in range(CELL_SIZE):
                for y in range(CELL_SIZE):
                    rect = pygame.Rect(
                        col * CELL_SIZE * scale_factor + x * scale_factor,
                        row * CELL_SIZE * scale_factor + y * scale_factor,
                        scale_factor,
                        scale_factor
                    )
                    pygame.draw.rect(surface, color, rect)



def start_simulation():
    global running
    running = True


def stop_simulation():
    global running
    running = False


def reset_simulation():
    global data
    data = generate_forest(rows, cols, p_growth)
    generate_water_bodies(data, num_water_bodies)  # Regenerate water bodies


def main():
    global running, rows, cols, data, p_growth, p_lightning, threshold, num_water_bodies, wind_direction

    pygame.init()

    # Calculate rows and columns based on window size
    rows = pygame.display.Info().current_h // (CELL_SIZE * scale_factor)
    cols = pygame.display.Info().current_w // (CELL_SIZE * scale_factor)

    # Set up the window
    screen_width = 1200  # Set the desired width of the window
    screen_height = 600  # Set the desired height of the window
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the window title
    pygame.display.set_caption("Forest Fire Simulator")

    # Probability values
    p_growth = 6e-1
    p_lightning = 0
    threshold = 2  # Number of burning cells required to ignite a tree
    num_water_bodies = 10  # Number of water bodies to generate
    wind_speed = 3  # Initial wind speed value
    wind_direction = (0, 1)  # Initial wind direction (right direction)

    # Generate the initial forest
    data = generate_forest(rows, cols, p_growth)
    generate_water_bodies(data, num_water_bodies)

    clock = pygame.time.Clock()

    # Create buttons
    panel_rect = pygame.Rect(screen_width - 200, 0, 200, screen_height)

    start_button = Button(
        pygame.Rect(panel_rect.left + 10, 50, 160, 40),
        (0, 255, 0),
        "Start",
        (0, 0, 0),
        start_simulation
    )

    stop_button = Button(
        pygame.Rect(panel_rect.left + 10, 100, 160, 40),
        (255, 0, 0),
        "Stop",
        (0, 0, 0),
        stop_simulation
    )

    reset_button = Button(
        pygame.Rect(panel_rect.left + 10, 150, 160, 40),
        (255, 165, 0),
        "Reset",
        (0, 0, 0),
        reset_simulation
    )

    wind_direction_button = Button(
        pygame.Rect(panel_rect.left + 10, 200, 160, 40),
        (0, 0, 0),
        "Wind Direction",
        (255, 255, 255),
        wind_direction_action,
        is_arrow=True
    )

    buttons = [start_button, stop_button, reset_button, wind_direction_button]

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:  # Check for left mouse button click
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    col = mouse_x // (CELL_SIZE * scale_factor)
                    row = mouse_y // (CELL_SIZE * scale_factor)
                    if 0 <= row < rows and 0 <= col < cols:
                        data[row][col] = STATES['BURNING']  # Set the clicked cell state to 'BURNING'

            for button in buttons:
                button.handle_event(event)

        if running:
            # Update the forest state with wind direction and speed
            data = update(data, p_growth, p_lightning, threshold, wind_direction, wind_speed)

        screen.fill((0, 0, 0))
        draw(data, screen)
        draw_panel(screen, screen_width, screen_height, buttons)
        pygame.display.flip()

        clock.tick(100)

        # Control the duration of the BURNING_DURATION state
        if running and pygame.time.get_ticks() % 500 == 0:
            for row in range(len(data)):
                for col in range(len(data[row])):
                    if data[row][col] == STATES['BURNING_DURATION']:
                        data[row][col] = STATES['EMPTY']


if __name__ == "__main__":
    main()
