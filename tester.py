
from Ship import Player
from Ship import Enemy

def test():
	haru = Player( "Haru", 0,0 )

	print( haru.name )
	print( haru.xpos )
	print( haru.ypos )

	haru.changeCoords( (10,10) )

	print( haru.xpos )
	print( haru.ypos )

	try:
		print( haru.__DEF_MS )

	except:
		print( "Unable to print private attribute" )

test()