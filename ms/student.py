#Student Work
import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from os import path
import os

#LOADING IMAGES
#loading images before main program loops makes it so images are not looped over ang over again

#loading main menu background
backImg = pygame.image.load('images/Free Pixel Art Forest/Free Pixel Art Forest/PNG/Background layers/Layer_0011_0.png')
backImg = pygame.transform.scale2x(backImg)
sceneImg = pygame.image.load('images/Free Pixel Art Forest/Free Pixel Art Forest/PNG/Background layers/Layer_0006_4.png')
sceneImg = pygame.transform.scale(sceneImg, (3000, 2700))
midImg = pygame.image.load('images/Free Pixel Art Forest/Free Pixel Art Forest/PNG/Background layers/Layer_0005_5.png')
midImg = pygame.transform.scale(midImg, (3000, 2700))
frontImg = pygame.image.load('images/Free Pixel Art Forest/Free Pixel Art Forest/PNG/Background layers/Layer_0003_6.png')
frontImg = pygame.transform.scale(frontImg, (3000, 2700))

#loading game title
titleImg = pygame.image.load('images/title.png')
titleImg = pygame.transform.scale(titleImg, (500, 150))

#loading main game background
backGroundSky = pygame.image.load('images/stringstar fields/background_0.png')
backGroundSky = pygame.transform.scale(backGroundSky, (1070, 900))
backGroundCloud = pygame.image.load('images/stringstar fields/background_1.png')
backGroundCloud = pygame.transform.scale(backGroundCloud, (1070, 900))
backGroundSmallMountain = pygame.image.load('images/BG_DesertMountains/background2.png')
backGroundSmallMountain = pygame.transform.scale2x(backGroundSmallMountain)
backGroundMountain = pygame.image.load('images/BG_DesertMountains/background3.png')
backGroundMountain = pygame.transform.scale2x(backGroundMountain)

#loading game button images
restartImage = pygame.image.load('images/restart.jpeg')
restartImage =  pygame.transform.scale(restartImage, (230, 90))
startImage = pygame.image.load('images/Startbutton.png')
startImage =  pygame.transform.scale(startImage, (230, 100))
exitImage = pygame.image.load('images/Exitbutton.png')
exitImage = pygame.transform.scale(exitImage, (230, 100))
helpImage =  pygame.image.load('images/Helpbutton.png')
helpImage = pygame.transform.scale(helpImage, (230, 100))
closeImage = pygame.image.load('images/Closebutton.png')
closeImage = pygame.transform.scale(closeImage, (60, 40))
returnImage = pygame.image.load('images/Pausebutton.png')
returnImage = pygame.transform.scale(returnImage, (60, 40))
backImage = pygame.image.load('images/returnbutton.png')
backImage = pygame.transform.scale(backImage, (60, 40))
countinueImage = pygame.image.load('images/Countinuebutton.png')
countinueImage = pygame.transform.scale(countinueImage, (170, 90))
pauseImg = pygame.image.load('images/pause.png')
pauseImg = pygame.transform.scale(pauseImg, (300, 350))

#load jump blocks
#blockImg = pygame.image.load('images/Terrain (16x16).png')
blockImg = pygame.image.load('images/grass.png')
sideImg = pygame.image.load('images/side.png')
lSideImg = pygame.image.load('images/leftside.png')
stopImg = pygame.image.load('images/stop.png')

#dead player image 
deadImg = pygame.image.load('images/stop.png')

#game mosnter image
enemy = pygame.image.load('images/Bat.png')

#moving platform image
movingPlatform = pygame.image.load('images/tileset.png')

#toxic waste iamge
toxicWaste = pygame.image.load('images/ToxicWater.png')

#crystal image
crystalImg = pygame.image.load('images/32x32pixelart_assets05_loot_png/loot02crystal.png')

#tree checkpoint image
treePoint = pygame.image.load('images/Sunnyland Trees Expansion Files/Sunnyland Trees Expansion Files/Sprites/Sliced Trees/tree.png')

#winning images
cheeringImg = pygame.image.load('images/cheering.png')
winBackGround = pygame.image.load('images/winBackGround.png')
winBackGround = pygame.transform.scale(winBackGround, (1070, 900))

#losing images
lostBackGround = pygame.image.load('images/lostBackGround.png')

#initializing music
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()


#LOADING IN BACKGROUND MUSIC
music = pygame.mixer.music.load('images/Magic-Cliffs-Environment/Magic-Cliffs-Environment/magic cliffs music/magic cliffs.ogg')
#looping music
pygame.mixer.music.play(-1, 0.0, 5000)



def main():
    '''
        This function sets all of the game assets like player and world
        This is where the user controls the charater to avoid monsters
        and collect points to reach the end of the game.
        
        Parameters
        ----------
        None
            
        Returns
        ---------
            None
        '''
    
    pygame.init()      # Prepare the pygame module for use
    surfaceWidth = 900   # Desired physical surface size, in pixels.
    surfaceHeight = 900

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
    
    #define text font and size
    fontScore = pygame.font.SysFont('Pokemon GB.ttf', 30) #score font
    font = pygame.font.SysFont('Pokemon GB.ttf', 70) #score font
    hintFont = pygame.font.SysFont('nunito', 30) #score font

    
    
    #defining game variables
    tileSize = 50 #size of each tiles
    gameOver = 0
    mainMenu = True #is the player in the main menu?
    hintScreen = False
    pauseScreen = False
    level = 1 #the level number player is currently running
    maxLevels = 5 #maximum levels in this game
    score = 0 #the player score
    
    #gettig highscore
    if os.path.exists('score.txt'):
    
        with open('score.txt', 'r') as file:
            highScore = int(file.read())
    else:
        highScore = 0
    
    #text colours
    white = (255,255,255)
    maroon = (224, 88, 131)
    black = (0,0,0)
    pink = (138, 8, 54)
    
    #loading sound effects
    crystalCollect = pygame.mixer.Sound('images/crystalCollect.wav')
    jumping = pygame.mixer.Sound('images/jump.wav')
    deathBell = pygame.mixer.Sound('images/deathBell.wav')
    winBell = pygame.mixer.Sound('images/winBell.wav')

    
    #function for drawing text 
    def drawText (text, font, textColour, x, y):
        
        '''
        This function defines the colour, font, and size of
        text used in the program
        
        Parameters
        ----------
        text : String
            What the text will display
        font : String
            The font of the text
        textColour : String
            The colour of the text
        x : int
            the value of the x-axis
        y : int
            the value of the y-axis
            
       Returns
            ---------
                None
            ''' 
        img = font.render(text, True, textColour)
        mainSurface.blit(img, (x,y))
    

    #function to reset the level
    def resetLevel(level):
        '''
        This function resets the game level and
        clears all previous objects before loading
        in a new map. It also resets the player position.
        
        Parameters
        ----------
        level : int
            What the current level should be
            
       Returns
            ---------
                world
                    The level outlay
            ''' 
        player.reset(100, surfaceHeight - 130)
        #clearing all previous assets of the game
        batGroup.empty()
        toxicGroup.empty()
        treePointGroup.empty()
        platformGroup.empty()
        crystalGroup.empty()
        
        #loading new level
        if path.exists(f'level{level}_data'): #checking if the level number actually exists
        
            PickleIn = open(f'level{level}_data', 'rb') #add dirrent name later possibly
            worldData = pickle.load(PickleIn)
        
        world = World(worldData)
        
        return world
    
    #game button class
    class Button():
        #setting up buttons
        def __init__(self, x, y, image):
            
            '''
            This function sets the button
            
            Parameters
            ----------
            x : int
                The x position of the button
            y : int
                 The y position of the button
            image : list
                The image for the button
                
            Returns
            ---------
                None
                '''
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.clicked = False
        
        #when drawing buttons
        def draw(self):
            
            '''
                This function gets what action is being done when
                a button is drawn
                
                Parameters
                ----------
                    None
                    
               Returns
                    ---------
                        action
                            What action was done
                ''' 
            action = False
            #get mouse pos
            pos = pygame.mouse.get_pos()
            
            #check mouse and clicked condistion
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
                    
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            #draw button
                 
            mainSurface.blit(self.image, self.rect)
            
            return action

    
    #main player class 
    class Player():  # Pygame Platformer Game Tutorial pt. 2
        def __init__(self, x, y): 
            '''
                This function defines the player loaction and movement
                
                Parameters
                ----------
                x : int
                    the value of the x-axis
                y : int
                    the value of the y-axis
                    
               Returns
                    ---------
                        None
                ''' 
            self.reset(x, y)
            
        def update(self, gameOver):
            
            '''
                This function moves the player dependig on what keys are pressed
                
                Parameters
                ----------
                gameOver : int
                    Tells if the player is playing the game, dead, or reached the end of the game
                    
               Returns
                    ---------
                        gameOver
                            Has the player died
                ''' 
           
           #player displacment and speed
            dx = 0
            dy = 0
            walkCoolDown = 0.7
            colThresh = 20
            
            
            #if the game is running
            if gameOver == 0:
                    
                #get keypresses
                key = pygame.key.get_pressed()
             
                if key[pygame.K_SPACE] and self.jumped == False and self.inAir == False:
                    jumping.play()
                    self.velY = -15 # y cord increasing going down neg means char jumps up
                    self.jumped = True
                if key[pygame.K_SPACE] == False:
                    self.jumped = False
                    
                #going left
                if key[pygame.K_LEFT]:
                    dx -= 13 #player speed
                    self.counter += 1
                    self.direction = -1
                 
                #going right 
                if key[pygame.K_RIGHT]:
                    dx += 13 #player speed
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                if self.direction == 1:
                    self.image = self.imagesMoveRight[self.index]
                if self.direction == -1:
                    self.image = self.imagesMoveLeft[self.index]
                
                #adding animation
                if self.counter > walkCoolDown:
                    self.counter = 0
                    self.index += 1
                if self.index >= len(self.imagesMoveRight):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.imagesMoveRight[self.index]
                if self.direction == -1:
                    self.image = self.imagesMoveLeft[self.index]
                
                #Gravity
                self.velY += 1
                if self.velY > 10:
                    self.velY = 10
                dy += self.velY
                
                #check for collision
                self.inAir = True
                for tile in world.tileList:
                    #check for collision on the x-axis
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0
                    #check for collision on y-axis
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        
                        #checking if the player is under the block [jumping]
                        if self.velY < 0:
                            dy = tile[1].bottom - self.rect.top #top of the player
                            self.velY = 0
                        
                        #if above the ground
                        elif self.velY >= 0:
                            dy = tile[1].top - self.rect.bottom #top of the player
                            self.velY = 0
                            self.inAir = False
                            
                #check for collision with enemy
                if pygame.sprite.spritecollide(self, batGroup, False):
                    gameOver = -1
                    deathBell.play()
                    #stopping music
                    pygame.mixer.music.pause()
                    
                #check collision with toxic waste
                if pygame.sprite.spritecollide(self, toxicGroup, False):
                    gameOver = -1
                    deathBell.play()
                    #stopping music
                    pygame.mixer.music.pause()
              
                #checking if player landed on checkpoint tree
                if pygame.sprite.spritecollide(self, treePointGroup, False):
                    gameOver = 1 #player has won!
                    winBell.play()
                  
                  #check collision with platform  
                for platform in platformGroup:
                    #collision in the x direction
                    if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height): #checking collision
                       dx = 0
                       
                    #check for y collision
                    if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): #checking collision
                       #check if the player is below the platform
                        if abs((self.rect.top + dy) - platform.rect.bottom) < colThresh:
                            self.velY = 0 # stopping velocity
                            dy = platform.rect.bottom - self.rect.top
                        elif abs((self.rect.bottom + dy) - platform.rect.top) < colThresh:
                            self.rect.bottom = platform.rect.top - 1 #put player 1 pixel above platform
                            self.inAir = False
                            dy = 0
                        #move with platform
                        if platform.moveX != 0:
                            self.rect.x += platform.moveDirection
                       
                self.rect.x += dx
                self.rect.y += dy
                
            elif gameOver == -1:
                #if player has died
                
                self.image = self.deadImage                
                
            #draw player
            mainSurface.blit(self.image, self.rect)            
            return gameOver
        
        #resetting player actions
        def reset(self, x, y):
            '''
                This function resets the player action
                
                Parameters
                ----------
                x : int
                    the value of the x-axis
                y : int
                    the value of the y-axis
                    
               Returns
                    ---------
                        None
                ''' 
            self.imagesMoveRight = []
            self.imagesMoveLeft = []

            self.index = 0
            self.counter = 0
                       
            for num in range(1, 10):
                imgRight = pygame.image.load(f'images/Warrior-V1.3/Run/Warrior_Run_{num}.png')
                
                imgRight = pygame.transform.scale2x(imgRight)
                imgLeft = pygame.transform.flip(imgRight, True, False)
                self.imagesMoveRight.append(imgRight)
                self.imagesMoveLeft.append(imgLeft)
           
            self.deadImage =  pygame.transform.scale(deadImg, (140, 90))
            self.image = self.imagesMoveRight[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.velY = 0
            self.jumped = False
            self.direction = 0
            self.inAir = True
            
    #world creation class    
    class World():  #Pygame platformer tutorial pt. 1
        def __init__(self, data):
            '''
                This function creates the world level of the game byt
                reading it off of a list
                
                Parameters
                ----------
                data : List
                    The contents of the list that assigns a sprite for each area
                    
               Returns
                    ---------
                        None
                ''' 
            self.tileList = []
    
            #setting up the level creation 
            rowCount = 0
            for row in data:
                colCount = 0
                for tile in row:
                    #every value with 1 is dirt block
                    if tile == 1:
                        img = pygame.transform.scale(blockImg, (tileSize, tileSize))
                        imgRect = img.get_rect()
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    #making side grass image
                    if tile == 2:
                        img = pygame.transform.scale(sideImg, (tileSize, tileSize))
                        imgRect = img.get_rect()
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    #making invisable barriers
                    if tile == 9:
                        img = pygame.transform.scale(stopImg, (tileSize // 20, tileSize // 20))
                        imgRect = img.get_rect()
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    #monster drawings 
                    if tile == 3:
                        bat = Enemy(colCount * tileSize, rowCount * tileSize + 5)
                        batGroup.add(bat) # groups are .add
                    #moving platform that goes left and right
                    if tile == 4:
                        platform = Platform(colCount * tileSize, rowCount * tileSize, 1, 0) #x is moving y is not moving
                        platformGroup.add(platform)
                    #moving platform that goes up and down
                    if tile == 5:
                        platform = Platform(colCount * tileSize, rowCount * tileSize, 0, 1) #y is moving x is not moving
                        platformGroup.add(platform)
                    #toxic waste 
                    if tile == 6:
                        toxic = Toxic(colCount * tileSize, rowCount * tileSize + (tileSize // 2))
                        toxicGroup.add(toxic)
                    #game crystal display
                    if tile == 7:
                        crystal = Crystal(colCount * tileSize + (tileSize // 2), rowCount * tileSize + 37) #adjusting crystal height
                        crystalGroup.add(crystal)
                    #tree checkpoint displays
                    if tile == 8:
                        moveOn = TreePoint(colCount * tileSize, rowCount * tileSize - (tileSize // 2)) #creating the size of the exit
                        treePointGroup.add(moveOn)
                        
                    colCount += 1
                rowCount += 1
                
         #drawing all of the tiles and objects       
        def draw(self):
            '''
                This functiondraws all the tile into the game
                
                Parameters
                ----------
                    None
               Returns
                    ---------
                        None
                ''' 
            for tile in self.tileList:
                mainSurface.blit(tile[0], tile[1])
                
    #Monster behaviour class 
    class Enemy(pygame.sprite.Sprite): #pygame tutorial pt. 5 enemies 
        def __init__(self, x, y):
            '''
                This function defines the scale, location, and direction the
                playe charater moves in.
                
                Parameters
                ----------
                x : int
                    the value of the x-axis
                y : int
                    the value of the y-axis
                    
               Returns
                    ---------
                        None
                ''' 
            pygame.sprite.Sprite.__init__(self)
            
            self.image = pygame.transform.scale2x(enemy)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.moveDirection = 1
            self.moveCounter = 0
         
         #moving enemy
        def update(self):
            '''
                This function updates the player movement and direction.
                
                Parameters
                ----------
                    None
                
               Returns
                    ---------
                        None
                ''' 
            self.rect.x += self.moveDirection
            self.moveCounter += 1
            if abs(self.moveCounter) > 50:
                self.moveDirection *= -1
                self.moveCounter *= -1
                
    #platform behaviour class            
    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, moveX, moveY):
            '''
                This function updates the movement of platforms 
                Parameters
                ----------
                text : String
                    What the text will display
                font : String
                    The font of the text
                textColour : String
                    The colour of the text
                x : int
                    the value of the x-axis
                y : int
                    the value of the y-axis
                    
               Returns
                    ---------
                        None
                ''' 
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(movingPlatform, (tileSize, tileSize // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.moveCounter = 0
            self.moveDirection = 1
            self.moveX = moveX
            self.moveY = moveY
            
        #updating direction
        def update(self):
            '''
            This function resets the game level and
            clears all previous objects before loading
            in a new map. It also resets the player position.
            
            Parameters
            ----------
            level : int
                What the current level should be
                
           Returns
                ---------
                    world
                        The level outlay
                ''' 
            self.rect.x += self.moveDirection * self.moveX #moving horazontal
            self.rect.y += self.moveDirection * self.moveY
            self.moveCounter += 1
            if abs(self.moveCounter) > 50:
                self.moveDirection *= -1
                self.moveCounter *= -1   
    
    #toxic waste class behaviour 
    class Toxic(pygame.sprite.Sprite):
        
        '''
            This function helps initiate the toxic waste obstical.
            It scales the image and creates sprites. 
            
            Parameters
            ----------
            pygame.sprite.Sprite : class
                The sprite class in pygames
                
           Returns
                ---------
                   None
                ''' 
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(toxicWaste, (tileSize, tileSize // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x #top and center of image
            self.rect.y = y
            
    #crystal class behaviour        
    class Crystal(pygame.sprite.Sprite):
        '''
            This function helps initiate the crystals in the game for points.
            It scales the image and creates sprites. 
            
            Parameters
            ----------
            pygame.sprite.Sprite : class
                The sprite class in pygames
                
           Returns
                ---------
                   None
                ''' 
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(crystalImg, (tileSize // 2, tileSize // 2)) #scalign crystal height
            self.rect = self.image.get_rect()
            self.rect.center = (x, y) #midpoint of image

    #Tree checkpoint behaviour 
    class TreePoint(pygame.sprite.Sprite):
        '''
            This function helps initiate the tree checkpoints.
            It scales the image and creates sprites. 
            
            Parameters
            ----------
            pygame.sprite.Sprite : class
                The sprite class in pygames
                
           Returns
                ---------
                   None
                ''' 
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(treePoint, (tileSize *2, int(tileSize * 2.5)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    
    #displaying the main menu background
    def ScreenDisplay():
        
        '''
            This function displays the game background
            images.
            
            Parameters
            ----------
                None
                
           Returns
                ---------
                   None
            ''' 
    #make this into a class and call the class
        #clearly display the background image
        mainSurface.blit(backImg, (0,0))
        mainSurface.blit(sceneImg, (-500,-1580))
        mainSurface.blit(midImg, (-350,-1580))
        mainSurface.blit(frontImg, (-350,-1580))
    
    #text used in the hintscreen
    def HintText():
        
        '''
            This function holds ands and displays all the text that
            will be present in the hint screen. 
            
            Parameters
            ----------
                None
           Returns
                ---------
                   None
                ''' 
        #displaying text for the rules
        drawText('Rules:', hintFont, white, 10, 150)
        drawText('1. To make it to the next level you need to touch the tree', hintFont, white, 10, 195)
        drawText('2. Jump on platforms to advance', hintFont, white, 10, 235)
        drawText('3. Avoid green acid and moving monsters', hintFont, white, 10, 275)
        drawText('4. Collect the crystals on the ground to gain points', hintFont, white, 10, 315)
        drawText('5. Jump on moving platforms to advance to areas where you cannot jump', hintFont, white, 10, 360)
        
        #displayig hints
        drawText('Hints:', hintFont, white, 10, 410)
        drawText('1. Wait until enemy starts moving towards you then jump', hintFont, white, 10, 455)
        drawText('2. Click the "pause" button on the top left to pause the game', hintFont, white, 10, 500)
        drawText('3. Click the "close" button on the top left to exit the game', hintFont, white, 10, 545)
        drawText('4. Press the arrow key while jumping to move in that direction', hintFont, white, 10, 590)
        
        drawText('Controls', hintFont, white, 10, 660)
        drawText('Jump: Space Key', hintFont, white, 10, 705)
        drawText('Run Left: Left arrow key', hintFont, white, 10, 750)
        drawText('Run Right: Right arrow key', hintFont, white, 10, 795)


    

    #creating an instance of the classes     
    player = Player(100, surfaceHeight - 120)
    batGroup = pygame.sprite.Group()
    platformGroup = pygame.sprite.Group()
    toxicGroup = pygame.sprite.Group()
    crystalGroup = pygame.sprite.Group()
    treePointGroup = pygame.sprite.Group()

    #load in level data and create world
    if path.exists(f'level{level}_data'): #checking if the level number actually exists
        
        PickleIn = open(f'level{level}_data', 'rb')
        worldData = pickle.load(PickleIn)
    world = World(worldData)
    
    #create button
    restartButton = Button(surfaceWidth // 2 - 170, surfaceHeight // 2 + 10, restartImage)
    startButton = Button(surfaceWidth // 2 - 350, surfaceHeight // 2 , startImage) # the subtracting 350 and plus 100 are adjusting the placcement of the button
    exitButton = Button(surfaceWidth // 2 + 90, surfaceHeight // 2 , exitImage)
    helpButton = Button(surfaceWidth // 2 - 130, surfaceHeight // 2 + 170, helpImage)
    closeButton = Button(750,5, closeImage)
    returnButton = Button(835,5, returnImage)
    backButton = Button(835,5, backImage)
    countinueButton = Button(surfaceWidth // 2 - 350, surfaceHeight // 2 , countinueImage)
    
    
    #This is the main game loop. This is where most of the game takes place 
    run = True
    while run:
        
        #displaying game background
        mainSurface.blit(backGroundSky, (0,0))
        mainSurface.blit(backGroundCloud, (0,30))
        mainSurface.blit(backGroundSmallMountain, (0,30))
        mainSurface.blit(backGroundMountain, (0,20))
        
        #Main Menu of the program
        if mainMenu == True:
            
            #call screen display
            ScreenDisplay()
            
            #now display title
            mainSurface.blit(titleImg, (170,150))
            
            #loading button here
            #creating a hint menu
            if helpButton.draw():
                mainMenu = False
                hintScreen = True

            if exitButton.draw():
                run = False
                
            if startButton.draw():
                mainMenu = False
                hintScreen = False
                pauseScreen = False
                
        #drawing hint screen        
        elif hintScreen == True:
            #if true draw the background
            ScreenDisplay()
            
            HintText()
            
            #if the back button is pressed go back to main menu
            if backButton.draw():
                hintScreen = False
                mainMenu = True
        
        #drawing pause screen
        elif pauseScreen == True:
            #first display
            ScreenDisplay()
            
            #then display
            mainSurface.blit(pauseImg, (280,150))
            #loading button here
            #creating a hint menu
            if exitButton.draw():
                run = False
            if countinueButton.draw():
                pauseScreen = False
                
        else:
                
           #game logic drawing in buttons in-game for player
            world.draw()
            if closeButton.draw():
                run = False
            elif returnButton.draw():
                pauseScreen = True
            
             #game logic where the player moves ect.    
            if gameOver == 0: #game is running
                
                drawText(f'Current Level: {level}', fontScore, white, tileSize - 35, 50)
                drawText(f'Highest Level {maxLevels}', fontScore, white, tileSize - 35, 80)
                batGroup.update()
                platformGroup.update()
                
                #creat the display crystal group
                displayCrystal = Crystal(tileSize // 2, tileSize//2)
                crystalGroup.add(displayCrystal)
                #update score checking if player has collected crystal
                if pygame.sprite.spritecollide(player, crystalGroup, True): #checking collision between player and crystal/ True means sprite will dissapear once colision happnens
                    score += 1
                    crystalCollect.play()
                drawText('X ' + str(score), fontScore, white, tileSize - 5, 20)
               
               
               
            #updating the overworld sprites
            batGroup.draw(mainSurface)
            platformGroup.draw(mainSurface)
            toxicGroup.draw(mainSurface)
            crystalGroup.draw(mainSurface)
            treePointGroup.draw(mainSurface)
            
            gameOver = player.update(gameOver)
            
            #looking for if the player has died
            if gameOver == -1:
                mainSurface.blit(lostBackGround, (0,0))
                if score > highScore:
                        highScore = score
                        with open('score.txt', 'w') as file:
                            file.write(str(highScore))
                #game over test
                drawText('You Died!', font, maroon, (surfaceWidth // 2) - 140, surfaceHeight // 2 - 300)
                drawText('Your score: ' + str(score), font, white, (surfaceWidth // 2) - 170, (surfaceHeight // 2  - 245))
                readHigh = open('score.txt', 'r')
                drawText('Your high score: ' + (readHigh.read()), font, white, (surfaceWidth // 2) - 210, (surfaceHeight // 2 - 190))
                
                if restartButton.draw():
                    #clear world data and make a new instance of it
                    #this helps reset everything within the level including thigns like collectables
                    #countinue background music 
                    pygame.mixer.music.unpause()
                    
                    worldData = [] #empty world data so you can load in new values in its place
                    world = resetLevel(level) #give function new level and deletes all data from old level
                    #update highscore
                    if score > highScore:
                        highScore = score
                        with open('score.txt', 'w') as file:
                            file.write(str(highScore))
                    gameOver = 0
                    score = 0 #resetting player score
                    
            #looking at if the player has won    
            if gameOver == 1:
                #clear screen and move on the next level
                level += 1
                if level <= maxLevels:
                    #reset level
                    worldData = [] #empty world data so you can load in new values in its place
                    world = resetLevel(level) #give function new level and deletes all data from old level
                    gameOver = 0 #resetting game over back to zero so player can continue playing
                    #dont reset score since player is still playing
                else:
                    mainSurface.blit(winBackGround, (0,0))
                    mainSurface.blit(cheeringImg, (440,450))
                    if score > highScore:
                        highScore = score
                        with open('score.txt', 'w') as file:
                            file.write(str(highScore))
                    drawText('You finished!', font, maroon, (surfaceWidth // 2) - 180, surfaceHeight // 2 - 300)
                    drawText('Your score: ' + str(score), font, pink, (surfaceWidth // 2) - 170, (surfaceHeight // 2  - 245))
                    readHigh = open('score.txt', 'r')
                    drawText('Your high score: ' + (readHigh.read()), font, pink, (surfaceWidth // 2) - 210, (surfaceHeight // 2 - 190))
                        #restart game
                    if restartButton.draw():
                        level = 1 #start from beginning
                        #reset level
                        worldData = [] #empty world data so you can load in new values in its place
                        world = resetLevel(level) #give function new level and deletes all data from old level
                        gameOver = 0 #resetting game over back to zero so player can continue playing
                        score = 0
                    if exitButton.draw():
                        run = False
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #making sure highscore saves when player exit game without dying
                if score > highScore:
                        highScore = score
                        with open('score.txt', 'w') as file:
                            file.write(str(highScore))
                run = False
                
        pygame.display.update()
                # Now the surface is ready, tell pygame to display it!
            
                
        clock.tick(160) #Frame rate this effects the player and mosnter sprites 

    pygame.quit()     # Once we leave the loop, close the window.

main()
