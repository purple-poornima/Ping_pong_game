import pygame #import the pygame files
pygame.init() #link up every files from pygame 
#declare height and width
height=600 
width=900
#screen
screen = pygame.display.set_mode((width,height)) #height and width of the screen
pygame.display.set_caption("ping pong") #the caption at the top of screen
#clock from 0
clock=pygame.time.Clock()
#font size and style
font=pygame.font.SysFont("Arial",50)
#background for the board
background=pygame.image.load("pingpong_board.png")
background=pygame.transform.scale(background,(900,600))

#paddles dimension and its coordinates
pad_height=200
pad_width=20

left_pad_x=0
left_pad_y=height/2

right_pad_x=width-pad_width
right_pad_y=height/2

#total score to win
max_score=10

#winner
winner=None

#run is true for loop
run=True 

#ball coordinates and the speed
ball_x=width/2
ball_y=height/2

ball_speed_x=5
ball_speed_y=5

#score for player 1 and player 2

score1=0;
score2=0;

#start of ai speed
increase=0.2
while run:
    #catastrophe is the each event from the pygame.event
    for catastrophe in pygame.event.get():
        #quit statement
        if catastrophe.type==pygame.QUIT:
            run=False #false if the cross button chosen
        
    #draw the initialized background
    screen.blit(background,(0,0))#out of loop give green colour
    #draw the paddles and the circle
    pygame.draw.rect(screen,"red",(left_pad_x,left_pad_y,pad_width,pad_height))
    pygame.draw.rect(screen,"red",(right_pad_x,right_pad_y,pad_width,pad_height))
    pygame.draw.circle(screen,"red",(ball_x,ball_y),7)
    #give the scores
    text_surface=font.render(f"{score1}:{score2} ",True,"green")
    screen.blit(text_surface,(width/2-30,2))
    #ball speed increase by increase int the coordinates
    ball_x=ball_x+ball_speed_x
    ball_y=ball_y+ball_speed_y
    #ball speed and collisions at top bottom 
    if ball_y<=0 or ball_y>=height:
        ball_speed_y=ball_speed_y*-1
  
    
    
 #when keys get pressed at w and s
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s] and right_pad_y<=height-pad_height:
        right_pad_y=right_pad_y+4
    if keys[pygame.K_w] and right_pad_y-4>=0:
        right_pad_y=right_pad_y-4
#collision at the paddle
    if ball_x + 7>=right_pad_x and ball_y>=right_pad_y and ball_y<=right_pad_y+pad_height:
         ball_speed_x=ball_speed_x*-1


    if ball_x-7<=left_pad_x+pad_width and ball_y>=left_pad_y and ball_y<=left_pad_y+pad_height:
         ball_speed_x=ball_speed_x*-1    
#score
    if ball_x<0:
        score2 +=1
    # if score increases for me then i will increase the speed for ai paddle
        increase=increase+0.3
        ball_x=width/2
        ball_y=height/2
        ball_speed_x=4
    
    if ball_x>width:
        score1 +=1
        ball_x=width/2
        ball_y=height/2
        ball_speed_x=-4
    

    # winner determined
    if score1>=max_score:
        winner="AI wins"
    if score2>=max_score:
        winner="You win"
        #--ai paddle is done here--
    ai_speed=1+increase
    center_pad=left_pad_y+ pad_height/2
    if ball_speed_x<0:  #when ball moves towards the ai paddle
        if ball_y<center_pad:
            left_pad_y-=ai_speed
        elif ball_y>center_pad:
            left_pad_y+=ai_speed
    if left_pad_y < 0:
        left_pad_y = 0

    if left_pad_y > height - pad_height:
        left_pad_y = height - pad_height    

    if winner is not None:
        winner_text=font.render(winner,True,"white")
        restart_text=font.render("Press R to Resart",False,"yellow")

        screen.blit(winner_text,(100,height/2-70))
        screen.blit(restart_text,(100,height/2-20))

        ball_speed_x=0
        ball_speed_y=0

        if keys[pygame.K_r]:
            left_pad_x=0
            left_pad_y=height/2

            right_pad_x=width-pad_width
            right_pad_y=height/2
            
            winner=None

            ball_x=width/2
            ball_y=height/2

            ball_speed_x=5
            ball_speed_y=5

            score1=0;
            score2=0;

            increase=0.1

            
    
    
    pygame.display.update()#update the screen each time
    clock.tick(60)# frame rate values to 60 frames per cycle
pygame.quit()#after the while loop is finished finish pygame 