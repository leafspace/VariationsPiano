import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Begining to listen ...")
pygame.mixer.init()
while True:
    if(GPIO.input(1) == True):
        print("play:do")
        track1 = pygame.mixer.music.load("a1.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        continue
    if(GPIO.input(2) == True):
        print("play:re")
        track1 = pygame.mixer.music.load("a3.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        continue
    if(GPIO.input(3) == True):
        print("play:mi")
        track1 = pygame.mixer.music.load("a4.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        continue
    if(GPIO.input(4) == True):
        print("play:fa")
        track1 = pygame.mixer.music.load("a5.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        continue

print("programe exit .")
GPIO.cleanup()
