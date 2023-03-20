# forestimage = pygame.Surface.convert(pygame.image.load("forest.png"))
import random
import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_KP_ENTER,
    KEYDOWN,
    QUIT,
)

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super(Jogador, self).__init__()
        self.superf = pygame.image.load("combuca.png")
        self.superf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.superf.get_rect(center=((LARGURA_TELA)/2,ALTURA_TELA-(self.superf.get_height()/2)))
    
# -self.superf.get_width()
# -self.superf.get_height()
    def movimenta(self, teclada):
        # if teclada[K_UP]:
        #     self.rect.move_ip(0,-5)
        # if teclada[K_DOWN]:
        #     self.rect.move_ip(0,5)
        if teclada[K_LEFT]:
            self.rect.move_ip(-10,0)
        if teclada[K_RIGHT]:
            self.rect.move_ip(10,0)
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        # if self.rect.bottom >= ALTURA_TELA:
        #     self.rect.bottom = ALTURA_TELA
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= LARGURA_TELA:
            self.rect.right = LARGURA_TELA

# class Texto(pygame.font.Font):
#     def __init__(self):
#         super(Texto, self).__init__()
#         self.





class Fruta(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruta, self).__init__()
        self.superf = pygame.image.load(random.choice(["banana","maca","maracuja"])+'.png')
        self.superf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.superf.get_rect(
            center=(random.randint(0,LARGURA_TELA),
                    random.randint(0-100, 0-20))
        )
        self.speed = random.randint(2, 6)
    
    def movimentaemorre(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.top > ALTURA_TELA:
            self.kill()
            return True
        else:
            return False
    # def morreencosta(self):
    #     pygame.sprite.spritecollide(jogador,self,1)
            
        


pygame.init()
pygame.font.init()
LARGURA_TELA = 1080
ALTURA_TELA = 720
ICONE = pygame.image.load('combuca.png')
pygame.display.set_icon(ICONE)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Cata Fruta')

background = pygame.image.load("background.png").convert()


ADICIONARFRUTA = pygame.USEREVENT + 1
pygame.time.set_timer(ADICIONARFRUTA, 1000)

jogador = Jogador()




relogio = pygame.time.Clock()
# fonte = pygame.font.SysFont("Commodore 64",50)
fonte = pygame.font.Font("./Commodore.ttf",50)
def jogo():
    frutas = pygame.sprite.Group()
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)
    frutascoletadas=0
    rodando = True
    while rodando:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    rodando = False
            elif event.type == QUIT:
                rodando = False
            elif event.type == ADICIONARFRUTA:
                novo_fruta = Fruta()
                frutas.add(novo_fruta)
                todos_sprites.add(novo_fruta)
        
        teclada = pygame.key.get_pressed()
        jogador.movimenta(teclada)
        print(frutas)
        frutas.update()
        for fruta in frutas:
            if fruta.movimentaemorre():
                rodando = False
                break

        tela.blit(background,(0,-200))

        for ser in todos_sprites:
            tela.blit(ser.superf,ser.rect)
        
        if pygame.sprite.spritecollideany(jogador, frutas):
            # for fruta in range(len(frutas)):
            pygame.sprite.spritecollide(jogador,frutas,True)
            frutascoletadas +=1
            # jogador.kill()
            # rodando=False
        
        texto = fonte.render("Frutas: "+str(frutascoletadas),True,(255,255,255))
        tela.blit(texto, (20,20))
        # superf = pygame.Surface((50,50))
        # superf.fill((0,0,0))
        # quadr = superf.get_rect()
        # centrotelasuperf = ((LARGURA_TELA-superf.get_width())/2,
        #      (ALTURA_TELA-superf.get_height())/2)
        
        #                        (LARGURA_TELA/2,ALTURA_TELA/2)
        
        pygame.display.flip()
        relogio.tick(60)



fonteperdeu = pygame.font.Font("Commodore.ttf",100)
textoperdeu = fonteperdeu.render("Voce Perdeu!",True,(255,255,0))
def jogarnovamente():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
            elif event.type == QUIT:
                return False


jogar = True


while jogar:
    jogo()
    tela.blit(textoperdeu,((LARGURA_TELA-textoperdeu.get_width())/2,
            (ALTURA_TELA-textoperdeu.get_height())/2))
    pygame.display.flip()
    jogar = jogarnovamente()

