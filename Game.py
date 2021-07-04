import pygame
import time
import random
import pyttsx3
from tkinter import  *
from PIL import ImageTk, Image

def snakegame(e):
    base.destroy()
    bb = e.keysym
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (194, 24, 7)
    snake_colour = (182, 180, 40)

    print(bb)
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by Siddhi & Gauri')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 20)
    score_font = pygame.font.SysFont("arial", 20)


    def Your_score(score):
        value = score_font.render(" Game Score: " + str(score), True, white)
        dis.blit(value, [0, 0])


    def our_snake(snake_block, snake_list):
        ls = ['red', 'blue', 'yellow']
        for x in snake_list:
            pygame.draw.rect(dis,random.choice(ls), [x[0], x[1], snake_block, snake_block])


    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])


    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(black)
                message("OOPS! You Lost! Press C to play again or press Q to quit", white)
                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(black)

            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()

print("Welcome to the game. This Snake Xenzia Game is Developed by Siddhi and Gauri. Let's Begin")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

base = Tk()
base.geometry("800x600+290+120")
base.title("Snake_game")
my_image11 = ImageTk.PhotoImage(Image.open("1.jpeg"))
my_label11 = Label(base, image=my_image11, width=800, height=600, bg="white")
my_label11.place(x=0, y=0)
base.update()
lab=Label(base,text="Loading...",font=("arial bold",20),width=30,height=1,bg="#806909")
lab.place(x=190,y=450)
base.update()
def speak(text):
    engine.say(text)
    engine.runAndWait()
speak('Welcome to the game. This Snake Xenzia Game is Developed by Siddhi... and Gauri... Lets Begin')
time.sleep(1)
base.update()

lab.config(text="Press Enter to start the game...")
base.update()

speak('Press Enter to start the game.....')

pygame.init()
base.update()
en = Entry(base)
en.place(x=-30,y=-30)

en.focus()

en.bind("<Key>",snakegame)

base.mainloop()