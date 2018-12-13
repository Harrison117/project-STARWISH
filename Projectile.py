
import pygame 

class Projectile:

	def __init__( self, xpos, ypos ):

		self.xpos = xpos
		self.ypos = ypos


class Weapon( Projectile ):

	def __init__( self ):
		self.weapons = {}

		default_weapon_sprite = pygame.Surface((5,2))
		default_weapon = {
			"bullet":
			{
				"dmg": (10,),
				"speed": (0.25,),
				"sprite": default_weapon_sprite
			}
		}

		self.curr_weapon = default_weapon
		self.weapons.update( self.curr_weapon )

	def generateProjectile( self ):
		pass

	def switchWeapon( self, weapon_type ):
		self.weapon_type = weapon_type
		self.curr_weapon = self.weapons[ weapon_type ]
