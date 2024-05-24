#Fiona Magee qgt8xq, Izzy Teinfalt rhh5rb

#We created Flappy Bird which consists of pressing the space bar to make the bird(chracter) jump between
#tubes that are randomly generated throughout the game. This game also has coins inbetween the tubes to
#calculate points and a keep score.

#3 Basic Features:
#1. There is user input by taping the space bar to make the bird jump.
#2. There is a game over when the bird touches the ground or tubes with a screen that displays game over
#3. There are grahpics similar to the orginal flappy bird game incorperated in our game

#4 Additional Features:
#1. We have a restart from gameover with a restart button that will restart the game when pressed
#2. We use sprite animation to make the bird flap it's wings throughout the game
#3. There are collectible coins throughout the game that keep score
#4. There is a scrolling level with randomly generated tubes as the bird moves

#Changes from Checkpoint 2:
#-Completed importing pngs and sprite sheet animation
#-Added collision dectecion
#-Added a gameover function and restart button
#-Added coins and now keeps score when coins are collected

import uvage
import random
camera = uvage.Camera(800,600)
background = uvage.from_image(400,200,'flappybird_BKGRND1.png')
background.scale_by(6)
flappyimages = uvage.load_sprite_sheet('flappybirds.png',1,3)
flappy = uvage.from_image(300,300,flappyimages[-1])
flappy.scale_by(2)
timercounter = 0
currentframe = 0
game_on = True
gameover = False
yaxis = 600
newyaxis = 600

pipe2 = uvage.load_sprite_sheet('pipe2.png',1,1)
pipe1 = uvage.load_sprite_sheet('pipe1.png',1,1)
walls = [uvage.from_image(600,0,pipe2[-1]), uvage.from_image(600,800,pipe1[-1])]

coins = [uvage.from_image(600,400,'flappybird_COIN.png')]
startscreen = uvage.from_image(400,2000,'flappybird_PLAY.png')
startscreen.scale_by(3)
gameoverscreen = uvage.from_image(400,2000,'flappybird_GAMEOVER.png')
gameoverscreen.scale_by(2.3)
endgamewall = uvage.from_color(400, 625, 'green', 800, 1)
score = 0

#Allows the birds movement when the space bar is pressed and game_on is true
def bounce():
    if uvage.is_pressing('space') and game_on == True:
        flappy.y -= 40
    if flappy.y > 14:
        flappy.y += 5

#Makes walls and coins move with the flappybird in the oppisite direction
#Appends to the orginal pipes (callled walls) list in a randomized
def wallmovingandcoins():
    global yaxis
    global newyaxis
    global game_on
    if game_on == True:
        for wall in walls:
            wall.x -= 5
    randomwalls = random.randint(200, 600)
    if game_on == True:
        yaxis += 300
        walls.append(uvage.from_image(yaxis, randomwalls - 400, pipe2[-1]))
        walls.append(uvage.from_image(yaxis, randomwalls + 400,pipe1[-1]))
    if game_on == True:
        newyaxis += 300
        for coin in coins:
            coin.x -=5
        coins.append(uvage.from_image(newyaxis, randomwalls-60, 'flappybird_COIN.png'))

#When the bird hits a wall it ends the game but also displays a gameover and restart button allowing the game
#to restart
def collsions():
    global game_on
    global game_over
    global walls
    global score
    global newyaxis
    global yaxis
    global coins
    for wall in walls:
        if flappy.touches(wall):
            game_on = False
            game_over = True
            flappy.y = 800
            startscreen.y = 300
            gameoverscreen.y = 150
            if camera.mouseclick:
                game_on = True
                game_over = False
                flappy.y = 300
                flappy.x = 300
                startscreen.y = 2000
                gameoverscreen.y = 2000
                score = 0
                yaxis = 600
                newyaxis = 600
                walls = [uvage.from_image(600, 0, 'pipe2.png'), uvage.from_image(600, 800, 'pipe1.png')]
                coins = [uvage.from_image(600, 400, 'flappybird_COIN.png')]

#When the bird hits the ground this function stops the game with a gameover title and option to restart the game
def gameground():
    global game_on
    global game_over
    global walls
    global score
    global newyaxis
    global yaxis
    global coins
    if flappy.touches(endgamewall):
        game_on = False
        game_over = True
        flappy.y = endgamewall.y
        startscreen.y = 300
        gameoverscreen.y = 150
        if camera.mouseclick:
            game_on = True
            game_over = False
            flappy.y = 300
            flappy.x = 300
            startscreen.y = 2000
            gameoverscreen.y = 2000
            score = 0
            yaxis = 600
            newyaxis = 600
            walls = [uvage.from_image(600, 0, 'pipe2.png'), uvage.from_image(600, 800, 'pipe1.png')]
            coins = [uvage.from_image(600, 400, 'flappybird_COIN.png')]

#Displays everything created and also keeps score of coins collected and contains the sprite sheet
#animation to make the bird move it's wings
def tick():
    global score
    global timercounter
    global currentframe
    camera.clear('light blue')
    camera.draw(background)
    camera.draw(flappy)
    camera.draw(endgamewall)
    flappy.move_speed()
    flappy.yspeed += 0.001

    bounce()
    wallmovingandcoins()
    collsions()
    gameground()
    for coin in coins:
        if flappy.touches(coin) and game_on == True:
            score += 1
            coin.y = 2000
    for wall in walls:
        camera.draw(wall)
    for coin in coins:
        camera.draw(coin)

    timercounter += 1
    if timercounter % 7 == 0 and game_on == True:
        flappy.image = flappyimages[currentframe]
        currentframe += 1
        if currentframe >= 2:
            currentframe = 0



    camera.draw(uvage.from_text(300, 50, str(score), 50, "red", bold=True))
    camera.draw(startscreen)
    camera.draw(gameoverscreen)
    camera.display()

uvage.timer_loop(30, tick)



