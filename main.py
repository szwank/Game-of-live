from World import World
from time import sleep
import pygame

def main():
    world = World(20, 20)
    pygame.display.set_mode((200, 600))
    sleep(5)

if __name__ == '__main__':
    main()