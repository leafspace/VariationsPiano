import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.IN)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.IN)

print("Begining to listen ...")

while True:
    if(GPIO.input(1) == 1):
        print("播放音乐:do")
        track1 = pygame.mixer.music.load(".mp3")
        pygame.mixer.music.play()
    if(GPIO.input(2) == 1):
        print("播放音乐:re")
        track1 = pygame.mixer.music.load(".mp3")
        pygame.mixer.music.play()
    if(GPIO.input(3) == 1):
        print("播放音乐:mi")
        track1 = pygame.mixer.music.load(".mp3")
        pygame.mixer.music.play()
    if(GPIO.input(4) == 1):
        print("播放音乐:fa")
        track1 = pygame.mixer.music.load(".mp3")
        pygame.mixer.music.play()

print("programe exit .")
GPIO.cleanup()