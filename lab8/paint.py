import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'line'
    lines = []  # list with information about lines
    drawing_color = (0, 0, 255)  # color
    
    # creating a temporary surface for drawing lines
    temp_surface = pygame.Surface(screen.get_size())
    temp_surface.fill((255, 255, 255))  # fill the temporary surface with white
    
    drawing = False  # flag 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    drawing = True
                    if mode == 'circle':  # center and radius
                        lines.append({'type': 'circle', 'center': event.pos, 'radius': radius, 'color': drawing_color})
                    elif mode == 'rectangle':
                        lines.append({'type': 'rectangle', 'start': event.pos, 'end': event.pos, 'color': drawing_color})
                    else:
                        lines.append({'type': 'line', 'points': [event.pos], 'color': drawing_color})
            elif event.type == pygame.MOUSEMOTION:
                if lines and drawing:  
                    if mode == 'circle':  
                        lines[-1]['radius'] = radius  
                    elif mode == 'rectangle':
                        lines[-1]['end'] = event.pos  
                    else:
                        lines[-1]['points'].append(event.pos) 
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  
                    drawing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    drawing_color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    drawing_color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    drawing_color = (0, 0, 255)
                if event.key == pygame.K_SPACE:
                    mode = 'eraser'
                    drawing_color = (255, 255, 255)
                elif event.key == pygame.K_LEFT:
                    mode = 'circle'
                elif event.key == pygame.K_RIGHT:
                    mode = 'rectangle'
                elif event.key == pygame.K_DOWN:
                    mode = 'line'
                    
        temp_surface.fill((255, 255, 255))
        
        # Drawing all lines
        for line in lines:
            if line['type'] == 'line':
                if len(line['points']) >= 2:  # Check that there are at least two points for drawing the line
                    pygame.draw.lines(temp_surface, line['color'], False, line['points'], radius)
            elif line['type'] == 'circle':
                pygame.draw.circle(temp_surface, line['color'], line['center'], line['radius'])
            elif line['type'] == 'rectangle':
                start = line['start']
                end = line['end']
                pygame.draw.rect(temp_surface, line['color'], (start[0], start[1], end[0] - start[0], end[1] - start[1]), 2)
        
        # Displaying the temporary surface on the main screen
        screen.blit(temp_surface, (0, 0))
        
        pygame.display.flip()
        clock.tick(60)

main()