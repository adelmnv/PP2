import os
import pygame

def list_files(path):
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            files.append(os.path.join(path, f))
    return files

pygame.init()
pygame.mixer.init() 
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont("comicsansms", 12)


song_list = list_files("music/")
num = 0

pygame.mixer.music.load(song_list[num])
pygame.mixer.music.play()
song_name = os.path.basename(song_list[num])
is_changed = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_LEFT:
                is_changed = True
                num = (num - 1) % len(song_list)
                pygame.mixer.music.load(song_list[num])
                pygame.mixer.music.play()
                
            elif event.key == pygame.K_RIGHT:
                is_changed = True
                num = (num + 1) % len(song_list)
                pygame.mixer.music.load(song_list[num])
                pygame.mixer.music.play()
        
        if is_changed:
            screen.fill((255, 255, 255))
            song_name = os.path.basename(song_list[num])  
            text = font.render("Currently playing: "+song_name, True, (0, 0, 0))  
            instructions = font.render("Pause = space, next = right arrow, previous = left arrow", True, (0,0,0))
            screen.blit(text, (100, 120))
            screen.blit(instructions,(10,10))
            is_changed = False  
        pygame.display.flip()
            
            


    
