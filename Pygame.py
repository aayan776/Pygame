import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Setting image")
background = pygame.transform.scale(pygame.image.load('Grass_Block.png').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

boy = pygame.transform.scale(pygame.image.load('boy.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
boy_rect = boy.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
text = pygame.font.Font(None, 36).render('Hello world', True, pygame.Color("black"))
text_rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    screen.blit(background, (0, 0))
    screen.blit(boy, boy_rect)
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(1000)
  pygame.quit()
if __name__ == '__main__':
  game_loop()