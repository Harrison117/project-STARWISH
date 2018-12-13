
import math
import pygame

class Ship:

    def __init__( self, xpos, ypos ):
        # 40% move speed
        self.__DEF_MS = 0.25

        self.xpos = xpos
        self.ypos = ypos

        self.move_speed = self.__DEF_MS

    def changeCoords( self, coords ):
        self.xpos, self.ypos = coords

    def returnCoords( self ):
        return (self.xpos, self.ypos)

    def move( self, direction ):
        dx, dy = direction
        self.xpos += dx * self.move_speed
        self.ypos += dy * self.move_speed

    def slowMoveSpeed( self ):
        self.move_speed *= 0.5

    def normalMoveSpeed( self ):
        self.move_speed /= 0.5

class Player( Ship ):

    def __init__( self, name, xpos, ypos, sprite ):
        super().__init__( xpos, ypos )

        self.name   = name
        self.sprite = sprite

class Enemy( Ship ):

    def __init__( self, enemy_type, xpos, ypos ):
        super().__init__( xpos, ypos )
        self.enemy_type = enemy_type
