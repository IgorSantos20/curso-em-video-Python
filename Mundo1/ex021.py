'''Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame
pygame.init()
pygame.mixer.music.load('C:\Estudos\curso-em-video-Python\Mundo1\ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()