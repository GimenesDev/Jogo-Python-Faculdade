#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from Code.CONST import entity_health
import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple) -> None:
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed= 0
        self.health = entity_health[self.name]


    @abstractmethod
    def move(self, ):
        pass
