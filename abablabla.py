import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Cria a janela do jogo
tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela)

# Cria um objeto de fonte
fonte = pygame.font.Font(None, 36)

# Renderiza o texto em uma nova superfície de texto
texto = fonte.render("Olá, mundo!", True, BRANCO)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpa a tela
    tela.fill(PRETO)

    # Desenha o texto na tela
    tela.blit(texto, (10, 10))

    # Atualiza a tela
    pygame.display.flip()