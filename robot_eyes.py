import pygame
import random
import sys
import time

# Constants for colors
BGCOLOR = (0, 0, 0)  # Background color (black)
MAINCOLOR = (255, 255, 255)  # Drawing color (white)

# Mood constants
DEFAULT, TIRED, ANGRY, HAPPY = 0, 1, 2, 3

# Predefined positions
N, NE, E, SE, S, SW, W, NW = 1, 2, 3, 4, 5, 6, 7, 8

class RoboEyes:
    def __init__(self, width=800, height=480, frame_rate=50):
        self.screen_width = width
        self.screen_height = height
        self.frame_interval = 1 / frame_rate
        self.start_time = time.time()
        
        self.tired = False
        self.angry = False
        self.happy = False
        self.curious = False
        self.cyclops = False
        self.eyeL_open = False
        self.eyeR_open = False

        # EYE LEFT - size and border radius
        self. eyeLwidthDefault = 200
        self. eyeLheightDefault = 300
        self. eyeLwidthCurrent = self.eyeLwidthDefault
        self. eyeLheightCurrent = 1 # start with closed eye, otherwise set to eyeLheightDefault
        self. eyeLwidthNext = self.eyeLwidthDefault
        self. eyeLheightNext = self.eyeLheightDefault
        self. eyeLheightOffset = 0
        # Border Radius
        self. eyeLborderRadiusDefault = 20
        self. eyeLborderRadiusCurrent = self.eyeLborderRadiusDefault
        self. eyeLborderRadiusNext = self.eyeLborderRadiusDefault

        # EYE RIGHT - size and border radius
        self. eyeRwidthDefault = self.eyeLwidthDefault
        self. eyeRheightDefault = self.eyeLheightDefault
        self. eyeRwidthCurrent = self.eyeRwidthDefault
        self. eyeRheightCurrent = 1 # start with closed eye, otherwise set to eyeRheightDefault
        self. eyeRwidthNext = self.eyeRwidthDefault
        self. eyeRheightNext = self.eyeRheightDefault
        self. eyeRheightOffset = 0
        # Border Radius
        self. eyeRborderRadiusDefault = 20
        self. eyeRborderRadiusCurrent = self.eyeRborderRadiusDefault
        self. eyeRborderRadiusNext = self.eyeRborderRadiusDefault

        # Space between eyes
        self. spaceBetweenDefault = 150
        self. spaceBetweenCurrent = self.spaceBetweenDefault
        self. spaceBetweenNext = 150

        # EYE LEFT - Coordinates
        self. eyeLxDefault = ((self.screen_width)-(self.eyeLwidthDefault+self.spaceBetweenDefault+self.eyeRwidthDefault))/2
        self. eyeLyDefault = ((self.screen_height-self.eyeLheightDefault)/2)
        self. eyeLx = self.eyeLxDefault
        self. eyeLy = self.eyeLyDefault
        self. eyeLxNext = self.eyeLx
        self. eyeLyNext = self.eyeLy

        # EYE RIGHT - Coordinates
        self. eyeRxDefault = self.eyeLx+self.eyeLwidthCurrent+self.spaceBetweenDefault
        self. eyeRyDefault = self.eyeLy
        self. eyeRx = self.eyeRxDefault
        self. eyeRy = self.eyeRyDefault
        self. eyeRxNext = self.eyeRx
        self. eyeRyNext = self.eyeRy

        # BOTH EYES 
        # Eyelid top size
        self. eyelidsHeightMax = self.eyeLheightDefault/2 # top eyelids max height
        self. eyelidsTiredHeight = 0
        self. eyelidsTiredHeightNext = self.eyelidsTiredHeight
        self. eyelidsAngryHeight = 0
        self. eyelidsAngryHeightNext = self.eyelidsAngryHeight
        # Bottom happy eyelids offset
        self. eyelidsHappyBottomOffsetMax = (self.eyeLheightDefault/2)+3
        self. eyelidsHappyBottomOffset = 0
        self. eyelidsHappyBottomOffsetNext = 0
        


        #*********************************************************************************************
        #  Macro Animations
        #*********************************************************************************************

        # Animation - horizontal flicker/shiver
        self. hFlicker = False
        self. hFlickerAlternate = False
        self. hFlickerAmplitude = 2

        # Animation - vertical flicker/shiver
        self. vFlicker = False
        self. vFlickerAlternate = False
        self. vFlickerAmplitude = 10

        # Animation - auto blinking
        self. autoblinker = False # activate auto blink animation
        self. blinkInterval = 1 # basic interval between each blink in full seconds
        self.blinkIntervalVariation = 4 # interval variaton range in full seconds, random number inside of given range will be add to the basic blinkInterval, set to 0 for no variation
        self. blinktimer = 0 # for organising eyeblink timing

        # Animation - idle mode: eyes looking in random directions
        self. idle = False
        self.idleInterval = 1 # basic interval between each eye repositioning in full seconds
        self. idleIntervalVariation = 3 # interval variaton range in full seconds, random number inside of given range will be add to the basic idleInterval, set to 0 for no variation
        self. idleAnimationTimer = 0 # for organising eyeblink timing

        # Animation - eyes confused: eyes shaking left and right
        self. confused = False
        self.confusedAnimationTimer = 0
        self. confusedAnimationDuration = 500
        self. confusedToggle = True

        # Animation - eyes laughing: eyes shaking up and down
        self. laugh = False
        self.laughAnimationTimer = 0
        self. laughAnimationDuration = 500
        self. laughToggle = True



        


















        
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("RoboEyes")

        #*********************************************************************************************
    #  SETTERS METHODS
    #*********************************************************************************************

    # Calculate frame interval based on defined frameRate
    def setFramerate(self,fps):
        self.frameInterval = 1000/fps
    

    def setWidth(self, leftEye,  rightEye):
        self.eyeLwidthNext = leftEye
        self.eyeRwidthNext = rightEye
        self.eyeLwidthDefault = leftEye
        self.eyeRwidthDefault = rightEye
    

    def setHeight(self, leftEye,  rightEye) :
        self.eyeLheightNext = leftEye
        self.eyeRheightNext = rightEye
        self.eyeLheightDefault = leftEye
        self.eyeRheightDefault = rightEye
    

    # Set border radius for left and right eye
    def setBorderradius( self,leftEye,  rightEye) :
        self.eyeLborderRadiusNext = leftEye
        self.eyeRborderRadiusNext = rightEye
        self.eyeLborderRadiusDefault = leftEye
        self.eyeRborderRadiusDefault = rightEye
        

    # Set space between the eyes, can also be negative
    def setSpacebetween( self,space) :
        self.spaceBetweenNext = space
        self.spaceBetweenDefault = space
    

    def set_mood(self, mood):
        if mood == TIRED:
            self.tired = True
            self.angry = self.happy = False
        elif mood == ANGRY:
            self.angry = True
            self.tired = self.happy = False
        elif mood == HAPPY:
            self.happy = True
            self.tired = self.angry = False
        else:
            self.tired = self.angry = self.happy = False
    # # Set mood expression
    # def setMood(unsigned char mood):
    #     switch (mood)
    #     :
    #     case TIRED:
    #     tired=1 
    #     angry=0 
    #     happy=0
    #     break
    #     case ANGRY:
    #     tired=0 
    #     angry=1 
    #     happy=0
    #     break
    #     case HAPPY:
    #     tired=0 
    #     angry=0 
    #     happy=1
    #     break
    #     default:
    #     tired=0 
    #     angry=0 
    #     happy=0
    #     break
        
    

    # # Set predefined position
    # def setPosition(unsigned char position)
    # :
    #     switch (position)
    #     :
    #     case N:
    #     # North, top center
    #     eyeLxNext = getScreenConstraint_X()/2
    #     eyeLyNext = 0
    #     break
    #     case NE:
    #     # North-east, top right
    #     eyeLxNext = getScreenConstraint_X()
    #     eyeLyNext = 0
    #     break
    #     case E:
    #     # East, middle right
    #     eyeLxNext = getScreenConstraint_X()
    #     eyeLyNext = getScreenConstraint_Y()/2
    #     break
    #     case SE:
    #     # South-east, bottom right
    #     eyeLxNext = getScreenConstraint_X()
    #     eyeLyNext = getScreenConstraint_Y()
    #     break
    #     case S:
    #     # South, bottom center
    #     eyeLxNext = getScreenConstraint_X()/2
    #     eyeLyNext = getScreenConstraint_Y()
    #     break
    #     case SW:
    #     # South-west, bottom left
    #     eyeLxNext = 0
    #     eyeLyNext = getScreenConstraint_Y()
    #     break
    #     case W:
    #     # West, middle left
    #     eyeLxNext = 0
    #     eyeLyNext = getScreenConstraint_Y()/2
    #     break
    #     case NW:
    #     # North-west, top left
    #     eyeLxNext = 0
    #     eyeLyNext = 0
    #     break
    #     default:
    #     # Middle center
    #     eyeLxNext = getScreenConstraint_X()/2
    #     eyeLyNext = getScreenConstraint_Y()/2
    #     break
    def millis(self):
        return int((time.time() - self.start_time) * 1000)
    

    # Set automated eye blinking, minimal blink interval in full seconds and blink interval variation range in full seconds
    def setAutoblinker1(self, active, interval, variation):
        self.autoblinker = active
        self.blinkInterval = interval
        self.blinkIntervalVariation = variation
        
    def setAutoblinker(self,active):
        self.autoblinker = active
        

    # Set idle mode - automated eye repositioning, minimal time interval in full seconds and time interval variation range in full seconds
    def setIdleMode1(self, active, interval, variation):
        self.idle = active
        self.idleInterval = interval
        self.idleIntervalVariation = variation
        
    def setIdleMode(self, active) :
        self.idle = active
        

    # Set curious mode - the respectively outer eye gets larger when looking left or right
    def setCuriosity(self, curiousBit) :
        self.curious = curiousBit
        

    # Set cyclops mode - show only one eye 
    def setCyclops(self, cyclopsBit) :
        self.cyclops = cyclopsBit
        

    # Set horizontal flickering (displacing eyes left/right)
    def setHFlicker (self, flickerBit,  Amplitude) :
        self.hFlicker = flickerBit # turn flicker on or off
        self.hFlickerAmplitude = Amplitude # define amplitude of flickering in pixels
        
    def setHFlicker (self, flickerBit) :
        self.hFlicker = flickerBit # turn flicker on or off
        


    # Set vertical flickering (displacing eyes up/down)
    def setVFlicker1 (self, flickerBit,  Amplitude) :
        self.vFlicker = flickerBit # turn flicker on or off
        self.vFlickerAmplitude = Amplitude # define amplitude of flickering in pixels
    
    def setVFlicker (self, flickerBit) :
        self.vFlicker = flickerBit # turn flicker on or off
    


    #*********************************************************************************************
    #  GETTERS METHODS
    #*********************************************************************************************

    # Returns the max x position for left eye
    def getScreenConstraint_X(self):
        return self.screen_width-self.eyeLwidthCurrent-self.spaceBetweenCurrent-self.eyeRwidthCurrent
        

    # Returns the max y position for left eye
    def getScreenConstraint_Y(self):
        return self.screen_height-self.eyeLheightDefault # using default height here, because height will vary when blinking and in curious mode
        


    #*********************************************************************************************
    #  BASIC ANIMATION METHODS
    #*********************************************************************************************

    # BLINKING FOR BOTH EYES AT ONCE
    # Close both eyes
    def close(self) :
        self.eyeLheightNext = 1 # closing left eye
        self.eyeRheightNext = 1 # closing right eye
        self.eyeL_open = False # left eye not opened (=closed)
        self.eyeR_open = False # right eye not opened (=closed)
    

    # Open both eyes
    def open(self):
        self.eyeL_open = True # left eye opened - if true, drawEyes() will take care of opening eyes again
        self.eyeR_open = True # right eye opened
    

    # Trigger eyeblink animation
    def blink(self):
        self.close()
        self.open()
        

    # BLINKING FOR SINGLE EYES, CONTROL EACH EYE SEPARATELY
    # Close eye(s)
    def close1(self, left,  right) :
        if(left):
            self.eyeLheightNext = 1 # blinking left eye
            self.eyeL_open = 0 # left eye not opened (=closed)
        
        if(right):
            self.eyeRheightNext = 1 # blinking right eye
            self.eyeR_open = 0 # right eye not opened (=closed)
        
    

    # Open eye(s)
    def open1(self, left,  right) :
        if(left):
            self.eyeL_open = 1 # left eye opened - if true, drawEyes() will take care of opening eyes again
        
        if(right):
            self.eyeR_open = 1 # right eye opened
        
    

    # Trigger eyeblink(s) animation
    def blink1(self, left,  right) :
        self.close1(left, right)
        self.open1(left, right)
    
    #*********************************************************************************************
    #  MACRO ANIMATION METHODS
    #*********************************************************************************************

    # Play confused animation - one shot animation of eyes shaking left and right
    def anim_confused(self):
        self.confused = True

    # Play laugh animation - one shot animation of eyes shaking up and down
    def anim_laugh(self):
        self.laugh = True
    
        
        
    
    def draw_eyes(self):
        if(self.curious):
            if(self.eyeLxNext<=10):
                self.eyeLheightOffset=8
            elif (self.eyeLxNext>=(self.getScreenConstraint_X()-10) and self.cyclops):
                self.eyeLheightOffset=8    
            else:
                self.eyeLheightOffset=0
             # left eye
            if(self.eyeRxNext>=self.screen_width-self.eyeRwidthCurrent-10):
                self.eyeRheightOffset=8
            else:
                self.eyeRheightOffset=0
             # right eye
        




        # Left eye height
        self.eyeLheightCurrent = (self.eyeLheightCurrent + self.eyeLheightNext + self.eyeLheightOffset)/2
        self.eyeLy+= ((self.eyeLheightDefault-self.eyeLheightCurrent)/2) # vertical centering of eye when closing
        self.eyeLy-= self.eyeLheightOffset/2
        # Right eye height
        self.eyeRheightCurrent = (self.eyeRheightCurrent + self.eyeRheightNext + self.eyeRheightOffset)/2
        self.eyeRy+= (self.eyeRheightDefault-self.eyeRheightCurrent)/2 # vertical centering of eye when closing
        self.eyeRy-= self.eyeRheightOffset/2


        # Open eyes again after closing them
        if(self.eyeL_open):
            if(self.eyeLheightCurrent <= 1 + self.eyeLheightOffset):
                self.eyeLheightNext = self.eyeLheightDefault
            
        
        if(self.eyeR_open):
            if(self.eyeRheightCurrent <= 1 + self.eyeRheightOffset):
                self.eyeRheightNext = self.eyeRheightDefault 
        

        # Left eye width
        self.eyeLwidthCurrent = (self.eyeLwidthCurrent + self.eyeLwidthNext)/2
        # Right eye width
        self.eyeRwidthCurrent = (self.eyeRwidthCurrent + self.eyeRwidthNext)/2


        # Space between eyes
        self.spaceBetweenCurrent = (self.spaceBetweenCurrent + self.spaceBetweenNext)/2

        # Left eye coordinates
        self.eyeLx = (self.eyeLx + self.eyeLxNext)/2
        self.eyeLy = (self.eyeLy + self.eyeLyNext)/2
        # Right eye coordinates
        self.eyeRxNext = self.eyeLxNext+self.eyeLwidthCurrent+self.spaceBetweenCurrent # right eye's x position depends on left eyes position + the space between
        self.eyeRyNext = self.eyeLyNext # right eye's y position should be the same as for the left eye
        self.eyeRx = (self.eyeRx + self.eyeRxNext)/2
        self.eyeRy = (self.eyeRy + self.eyeRyNext)/2

        # Left eye border radius
        self.eyeLborderRadiusCurrent = (self.eyeLborderRadiusCurrent + self.eyeLborderRadiusNext)/2
        # Right eye border radius
        self.eyeRborderRadiusCurrent = (self.eyeRborderRadiusCurrent + self.eyeRborderRadiusNext)/2
        

        ## APPLYING MACRO ANIMATIONS ##

        if(self.autoblinker):
            if(self.millis() >= self.blinktimer):
                self.blink()
                self.blinktimer = self.millis()+(self.blinkInterval*1000)+(random.uniform(3,self.blinkIntervalVariation)*1000) # calculate next time for blinking
                
            

        # Laughing - eyes shaking up and down for the duration defined by laughAnimationDuration (default = 500ms)
        if(self.laugh):
            if(self.laughToggle):
                self.setVFlicker1(3, 10)
                self.laughAnimationTimer = self.millis()
                self.laughToggle = False
            elif(self.millis() >= self.laughAnimationTimer+self.laughAnimationDuration):
                self.setVFlicker1(0, 0)
                self.laughToggle = True
                self.laugh= False
            
        

        # Confused - eyes shaking left and right for the duration defined by confusedAnimationDuration (default = 500ms)
        if(self.confused):
            if(self.confusedToggle):
                self.setHFlicker(1, 20)
                self.confusedAnimationTimer = self.millis()
                self.confusedToggle = False
            elif(self.millis() >= self.confusedAnimationTimer+self.confusedAnimationDuration):
                self.setHFlicker(0, 0)
                self.confusedToggle = True
                self.confused= False
            
        

        # Idle - eyes moving to random positions on screen
        if(self.idle):
            if(self.millis() >= self.idleAnimationTimer):
                self.eyeLxNext = random.uniform(0,self.getScreenConstraint_X())
                self.eyeLyNext = random.uniform(0,self.getScreenConstraint_Y())
                self.idleAnimationTimer = self.millis()+(self.idleInterval*1000)+(random.uniform(0,self.idleIntervalVariation)*1000) # calculate next time for eyes repositioning
            
        

        # Adding offsets for horizontal flickering/shivering
        if(self.hFlicker):
            if(self.hFlickerAlternate) :
                self.eyeLx += self.hFlickerAmplitude
                self.eyeRx += self.hFlickerAmplitude
            else :
                self.eyeLx -= self.hFlickerAmplitude
                self.eyeRx -= self.hFlickerAmplitude
            
            self.hFlickerAlternate = not self.hFlickerAlternate
        

        # Adding offsets for horizontal flickering/shivering
        if(self.vFlicker):
            if(self.vFlickerAlternate) :
                self.eyeLy += self.vFlickerAmplitude
                self.eyeRy += self.vFlickerAmplitude
            else :
                self.eyeLy -= self.vFlickerAmplitude
                self.eyeRy -= self.vFlickerAmplitude
            
            self.vFlickerAlternate = not self.vFlickerAlternate
        

        # Cyclops mode, set second eye's size and space between to 0
        if(self.cyclops):
            self.eyeRwidthCurrent = 0
            self.eyeRheightCurrent = 0
            self.spaceBetweenCurrent = 0
        

        ## ACTUAL DRAWINGS ##

        self.screen.fill(BGCOLOR)

        # Draw basic eye rectangles
        pygame.draw.rect(self.screen, MAINCOLOR, (self.eyeLx, self.eyeLy, self.eyeLwidthCurrent, self.eyeLheightCurrent), border_radius=int(self.eyeLborderRadiusCurrent)) # left eye
        if not(self.cyclops):
            pygame.draw.rect(self.screen, MAINCOLOR, (self.eyeRx, self.eyeRy, self.eyeRwidthCurrent, self.eyeRheightCurrent), border_radius=int(self.eyeRborderRadiusCurrent)) #right eye

        # Prepare mood type transitions
        if (self.tired):
            self.eyelidsTiredHeightNext = self.eyeLheightCurrent/2 
            self.eyelidsAngryHeightNext = 0 
        else:
            self.eyelidsTiredHeightNext = 0
        if (self.angry):
            self.eyelidsAngryHeightNext = self.eyeLheightCurrent/2 
            self.eyelidsTiredHeightNext = 0 
        else:
            self.eyelidsAngryHeightNext = 0
        if (self.happy):
            self.eyelidsHappyBottomOffsetNext = self.eyeLheightCurrent/2 
        else:
            self.eyelidsHappyBottomOffsetNext = 0

        # Draw tired top eyelids 
        self.eyelidsTiredHeight = (self.eyelidsTiredHeight + self.eyelidsTiredHeightNext)/2
        if not(self.cyclops):
            pygame.draw.polygon(self.screen,BGCOLOR, [(self.eyeLx, self.eyeLy-1),(self.eyeLx+self.eyeLwidthCurrent, self.eyeLy-1),(self.eyeLx, self.eyeLy+self.eyelidsTiredHeight-1)])
            pygame.draw.polygon(self.screen,BGCOLOR, [(self.eyeRx, self.eyeRy-1),(self.eyeRx+self.eyeRwidthCurrent, self.eyeRy-1),(self.eyeRx+self.eyeRwidthCurrent, self.eyeRy+self.eyelidsTiredHeight-1)])

            
            # display.fillTriangle(eyeLx, eyeLy-1, eyeLx+eyeLwidthCurrent, eyeLy-1, eyeLx, eyeLy+eyelidsTiredHeight-1, BGCOLOR) # left eye 
            # display.fillTriangle(eyeRx, eyeRy-1, eyeRx+eyeRwidthCurrent, eyeRy-1, eyeRx+eyeRwidthCurrent, eyeRy+eyelidsTiredHeight-1, BGCOLOR) # right eye
        else :
        # Cyclops tired eyelids
            pygame.draw.polygon(self.screen,BGCOLOR, [(self.eyeLx, self.eyeLy-1),(self.eyeLx+(self.eyeLwidthCurrent)/2, self.eyeLy-1),(self.eyeLx, self.eyeLy+self.eyelidsTiredHeight-1)])
            pygame.draw.polygon(self.screen,BGCOLOR, [(self.eyeLx+(self.eyeLwidthCurrent/2), self.eyeLy-1),(self.eyeLx+self.eyeLwidthCurrent, self.eyeLy-1),(self.eyeLx+self.eyeLwidthCurrent, self.eyeLy+self.eyelidsTiredHeight-1)])

            
            # display.fillTriangle(eyeLx, eyeLy-1, eyeLx+(eyeLwidthCurrent/2), eyeLy-1, eyeLx, eyeLy+eyelidsTiredHeight-1, BGCOLOR) # left eyelid half
            # display.fillTriangle(eyeLx+(eyeLwidthCurrent/2), eyeLy-1, eyeLx+eyeLwidthCurrent, eyeLy-1, eyeLx+eyeLwidthCurrent, eyeLy+eyelidsTiredHeight-1, BGCOLOR) # right eyelid half
            

        # Draw angry top eyelids 
        self.eyelidsAngryHeight = (self.eyelidsAngryHeight + self.eyelidsAngryHeightNext)/2
        if not(self.cyclops): 
            pygame.draw.polygon(self.screen,BGCOLOR,[(self.eyeLx, self.eyeLy-1),(self.eyeLx+self.eyeLwidthCurrent, self.eyeLy-1),(self.eyeLx+self.eyeLwidthCurrent, self.eyeLy+self.eyelidsAngryHeight-1)])
            pygame.draw.polygon(self.screen,BGCOLOR,[(self.eyeRx, self.eyeRy-1),(self.eyeRx+self.eyeRwidthCurrent, self.eyeRy-1),(self.eyeRx, self.eyeRy+self.eyelidsAngryHeight-1)])
            
            # self.display.fillTriangle(eyeLx, eyeLy-1, eyeLx+eyeLwidthCurrent, eyeLy-1, eyeLx+eyeLwidthCurrent, eyeLy+eyelidsAngryHeight-1, BGCOLOR) # left eye
            # self.display.fillTriangle(eyeRx, eyeRy-1, eyeRx+eyeRwidthCurrent, eyeRy-1, eyeRx, eyeRy+eyelidsAngryHeight-1, BGCOLOR) # right eye
        else :
        # Cyclops angry eyelids
            pygame.draw.polygon(self.screen,BGCOLOR,)

            pygame.draw.polygon(self.screen, BGCOLOR, [(self.eyeLx, self.eyeLy-1), (self.eyeLx + (self.eyeLwidthCurrent / 2), self.eyeLy - 1), (self.eyeLx + (self.eyeLwidthCurrent / 2), self.eyeLy + self.eyelidsAngryHeight - 1)])
            pygame.draw.polygon(self.scree, BGCOLOR, [(self.eyeLx + (self.eyeLwidthCurrent / 2), self.eyeLy - 1), (self.eyeLx + self.eyeLwidthCurrent, self.eyeLy - 1), (self.eyeLx + (self.eyeLwidthCurrent / 2), self.eyeLy + self.eyelidsAngryHeight - 1)])
            

        # Draw happy bottom eyelids
        self.eyelidsHappyBottomOffset = (self.eyelidsHappyBottomOffset + self.eyelidsHappyBottomOffsetNext)/2
        pygame.draw.rect(self.screen, BGCOLOR, (self.eyeLx - 1, (self.eyeLy + self.eyeLheightCurrent) - self.eyelidsHappyBottomOffset + 1, self.eyeLwidthCurrent + 2, self.eyeLheightDefault), border_radius=int(self.eyeLborderRadiusCurrent))
        if not(self.cyclops): 
            pygame.draw.rect(self.screen, BGCOLOR, (self.eyeRx - 1, (self.eyeRy + self.eyeRheightCurrent) - self.eyelidsHappyBottomOffset + 1, self.eyeRwidthCurrent + 2, self.eyeRheightDefault), border_radius=int(self.eyeRborderRadiusCurrent))
            
        pygame.display.flip()
        pygame.display.update()


   

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # self.update()
            self.draw_eyes()
            clock.tick(60)  # Maintain a frame rate of 60 FPS

if __name__ == "__main__":
    robo_eyes = RoboEyes()
    # robo_eyes.set_mood(HAPPY)  # Example: set to happy mood
    robo_eyes.run()
