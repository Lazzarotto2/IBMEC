import os.path
import random

from ..mecanicas import som
from jogo.gui.cores import CORES #Usei para dar cor pro npc
import pygame

class NPC:
    def __init__(self, tesouro):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if [x, y] not in [tesouro.posicao, [0, 0]]:
                break
        self.cor = CORES.branco
        self.posicao = [x, y]
        self.char = "&"
        self.mensagem = "Olá! Eu sou um NPC!"

    @staticmethod
    def falar():
        oi = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "npc.wav"))
        pygame.mixer.Sound.play(oi)
