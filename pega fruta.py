import random
import pygame
from pygame.locals import (
    K_BACKSPACE,
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
)

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super(Jogador, self).__init__()
        self.superf = pygame.image.load("sprites/combuca.png")
        self.superf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.superf.get_rect(center=((LARGURA_TELA)/2,ALTURA_TELA-(self.superf.get_height()/2)))
    
    def movimenta(self, teclada):
        if teclada[K_LEFT]:
            self.rect.move_ip(-10,0)
        if teclada[K_RIGHT]:
            self.rect.move_ip(10,0)
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= LARGURA_TELA:
            self.rect.right = LARGURA_TELA

class Fruta(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruta, self).__init__()
        self.superf = pygame.image.load("sprites/"+random.choice(["banana","maca","maracuja"])+'.png')
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
            
        


pygame.init()
pygame.font.init()
LARGURA_TELA = 1080
ALTURA_TELA = 720
ICONE = pygame.image.load('sprites/combuca.png')
pygame.display.set_icon(ICONE)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Cata Fruta')

background = pygame.image.load("sprites/background.png").convert()
def fonte(x):
    return pygame.font.Font('fontes/Kemco Pixel Bold.ttf',x)
textoperdeu = fonte(100).render("Voce Perdeu!",True,(255,255,0))

ADICIONARFRUTA = pygame.USEREVENT + 1
pygame.time.set_timer(ADICIONARFRUTA, 1000)

jogador = Jogador()




relogio = pygame.time.Clock()


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
                    return frutascoletadas
            elif event.type == QUIT:
                rodando = False
                return frutascoletadas
            elif event.type == ADICIONARFRUTA:
                novo_fruta = Fruta()
                frutas.add(novo_fruta)
                todos_sprites.add(novo_fruta)
        
        teclada = pygame.key.get_pressed()
        jogador.movimenta(teclada)
        print(frutas)
        # frutas.update()
        for fruta in frutas:
            if fruta.movimentaemorre():
                rodando = False
                return frutascoletadas

        tela.blit(background,(0,-200))

        for ser in todos_sprites:
            tela.blit(ser.superf,ser.rect)
        
        if pygame.sprite.spritecollideany(jogador, frutas):
            pygame.sprite.spritecollide(jogador,frutas,True)
            frutascoletadas +=1

        texto = fonte(50).render("Frutas: "+str(frutascoletadas),True,(255,255,255))
        tela.blit(texto, (20,20))
        
        pygame.display.flip()
        relogio.tick(60)




def jogarnovamente():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
            elif event.type == QUIT:
                return False


def digitarnome(offsety):
    superftela = pygame.display.get_surface().copy()
    digitando = True
    nomedigitando = str()
    while digitando:
        tela.blit(superftela,(0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return nomedigitando
                elif event.key == K_RETURN:
                    return nomedigitando
                elif event.key == K_BACKSPACE:
                    if len(nomedigitando)>0:
                        nomedigitando = nomedigitando[:-1]
                else:
                    if len(nomedigitando) <=3:
                        nomedigitando += event.unicode
                    print(nomedigitando)
            elif event.type == QUIT:
                digitando = False
                return nomedigitando
        textonovo = fonte(50).render(nomedigitando,True,(255,255,0))
        tela.blit(textonovo,(LARGURA_TELA/10,(ALTURA_TELA)/2+offsety))
        pygame.display.flip()
        #FAZER DESENHAR NA TELA O TEXTO DIGITADO--------------------------------------
        
        
        
        #tela.blit()
        
            

        # teclada = pygame.key.get_pressed()
        
        # print(teclada.description)




def leleaderboard():
    leaderboard = list()
    with open("highscore.txt", "r") as highscore:
        linhas = highscore.read().split("/n")
        for linha in linhas:
            itens = linha.split(' - ')
            leaderboard.append(itens)
    return leaderboard



# S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/11 - Desenvolvimento de Sistemas 2023/Maycon Bruno Bertulino/aulas python/Aula 2 - NumPY/data


jogar = True


while jogar:
    pontuacao = jogo()
    tela.blit(textoperdeu,((LARGURA_TELA-textoperdeu.get_width())/2,
                        (ALTURA_TELA-textoperdeu.get_height())/2))
    pygame.display.flip()
    print(pontuacao)

    input("teste")
    leaderboard = leleaderboard()
    print(leaderboard)
    input("teste")
    offsety = 50
    for linhalb in leaderboard:

        nomellb = fonte(50).render(linhalb[0],True,(255,255,0))
        pontllb = fonte(50).render(linhalb[1],True,(255,255,0))
        print(linhalb)
        print(type(linhalb[1]))
        print(int(linhalb[1]))
        input("posentra loop")
        if pontuacao > int(linhalb[1]):
            input("teste")
            textonome = digitarnome(offsety)
            # tela.blit(fonte(50).render(pontuacao,True,(255,255,0)), (LARGURA_TELA/2,(ALTURA_TELA)/2+offsety))
            # tela.blit(fonte(50).render(textonome,True,(255,255,0)), (LARGURA_TELA/10,(ALTURA_TELA)/2+offsety))
        else:
            print("Pontuação menor")
            tela.blit(pontllb, (LARGURA_TELA/2,(ALTURA_TELA)/2+offsety))
            tela.blit(nomellb, (LARGURA_TELA/10,(ALTURA_TELA)/2+offsety))
            pygame.display.flip()
        offsety += 50


    # if leaderboard[0][0] <= pontuacao:
    #     offsety = 100
    #     linhahighscore = fonte(50).render(linhalb,True,(255,255,0))
    #     tela.blit(linhahighscore,((LARGURA_TELA-linhahighscore.get_width())/2,
    #                         ((ALTURA_TELA-linhahighscore.get_height())/2)+offsety))


        # for linha in highscore:
        #     linhahighscore = fonte(50).render(linha,True,(255,255,0))
        #     tela.blit(linhahighscore,((LARGURA_TELA-textoperdeu.get_width())/2,
        #                             ((ALTURA_TELA-textoperdeu.get_height())/2)+offsety))
        # offsety += 50
    jogar = jogarnovamente()


