import pygame
import Ship

class PygView(object):

    def __init__(self, width=640, height=200, fps=60):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)

        self.move_up    = False
        self.move_down  = False
        self.move_left  = False
        self.move_right = False
        self.isSlow     = False

        playerSprite = pygame.Surface((40,20))
        playerSprite.fill( (255,255,255) )

        self.player  = Ship.Player( "Haru", 0, 0, playerSprite )


    def run(self):
        """The mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                running = self.handle_quitEvent( event )

                self.handle_playerMovementEvent( event )
            
            self.handle_playerMovement()

            self.screen.fill((0,0,0))
            self.screen.blit(self.player.sprite, self.player.returnCoords())
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()

    def handle_playerMovementEvent( self, event ):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.move_up = True

            if event.key == pygame.K_s:
                self.move_down = True

            if event.key == pygame.K_a:
                self.move_left = True

            if event.key == pygame.K_d:
                self.move_right = True

            if event.key == pygame.K_LSHIFT:
                self.player.slowMoveSpeed()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.move_up = False

            if event.key == pygame.K_s:
                self.move_down = False

            if event.key == pygame.K_a:
                self.move_left = False

            if event.key == pygame.K_d:
                self.move_right = False

            if event.key == pygame.K_LSHIFT:
                self.player.normalMoveSpeed()


    def handle_playerMovement( self ):

        if self.move_up:
            self.player.move( (0,-1) )

        if self.move_down:
            self.player.move( (0,1) )

        if self.move_left:
            self.player.move( (-1,0) )

        if self.move_right:
            self.player.move( (1,0) )


    def handle_quitEvent( self, event ):
        if event.type == pygame.QUIT \
                or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return False

        return True
####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(640, 400).run()
