import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
'''class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printing(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    
'''
pygame.init()
 


#Loop until the user clicks the close button.
done = False


# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
#textPrint = TextPrint()

direction = ""
# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed")
        print (direction)
        direction = ""
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
 
   
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()


    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
     
        
       
            
        buttons = joystick.get_numbuttons()
       


        for i in range( 4 ):
            button = joystick.get_button( i )
            #if button:
            if i==0 and button==1:
                direction =  "Top" 
            elif i==1 and button==1:
                direction =  "Right" 
            elif i==2 and button==1:
                direction =  "Down" 
            elif i==3 and button==1:
                direction =  "Left" 
          
            
        

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()