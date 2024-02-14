import turtle as tu
import time
import random
#move
wn = tu.Screen()
wn.setup(1200,700)
wn.title("SnakeGame")
wn.bgpic("Jogo em python/snake.png")
wn.bgcolor("orange")
 

#
score = 0
draw = tu.Turtle()
draw.speed(0)
draw.penup()
draw.goto(0,250)
draw.hideturtle()
draw.write("Score: {}".format(score),align="center",font=("arial",24,"bold"))
#snake
snk = tu.Turtle()
snk.shape("triangle")
snk.color("green")
snk.speed(0)
snk.penup()
pos_x= snk.xcor()
pos_y = snk.ycor()

#food
fd = tu.Turtle()
fd.shape("square")
fd.color("red")
fd.penup()
fd.speed(0)
def spawn_food():
  y_food = random.randint(-330,330)
  x_food = random.randint(-580,580)
  fd.setpos(x_food,y_food)
spawn_food()
key = -1
delay = 0.1
def move_up():
 global key
 if key != 2:
  key = 0

def move_left():
 global key
 if key != 3:
  key = 1

def move_down():
 global key
 if key != 0:
  key = 2
  
def move_right():
 global key
 if key != 1:
  key = 3
 
def move():
 global key,pos_x,pos_y
 print(key)
 if key == 0:
  pos_y = pos_y + 30
  snk.setheading(90)
  snk.setpos(pos_x,pos_y)
 if key == 1:
  pos_x = pos_x - 30
  snk.setheading(180)
  snk.setpos(pos_x,pos_y)
 if key == 2:
  pos_y = pos_y - 30
  snk.setheading(270)
  snk.setpos(pos_x,pos_y)
 if key == 3:
  pos_x+=30
  snk.setheading(360)
  snk.setpos(pos_x,pos_y)  

wn.listen()
wn.onkeypress(move_up,"Up")
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_down,"Down")
wn.onkeypress(move_right,"Right")
colors = ["red","green","yellow","blue","black","brown"]
snks = []
i=0
while True:
  wn.update()
  if pos_x > 580 or pos_x < -580 or pos_y > 330 or pos_y < -330:
   pen = tu.Turtle()
   pen.speed(0)
   pen.hideturtle()
   pen.penup()
   pen.write("GAME OVER",align="center",font=("arial",60,"bold"))
   wn.exitonclick()
  for index in range (0,len(snks),+1):
   if(pos_x == snks[index].xcor() and pos_y == snks[index].ycor()):
    wn.exitonclick() 
  if snk.distance(fd)<30:
   snks.append( tu.Turtle() )
   snks[i].color(colors[random.randint(0,5)])
   snks[i].shape("square")
   snks[i].penup()
   snks[i].speed(0)
   i+=1
   delay/=3
   score+=1
   draw.clear()
   draw.write("Score: {}".format(score),align="center",font=("arial",24,"bold"))
   spawn_food()
  for index in range(len(snks)-1,0,-1):
     tempx = snks[index-1].xcor()
     tempy = snks[index-1].ycor()
     snks[index].setpos(tempx,tempy)
  if len(snks)> 0:
    snks[0].setpos(pos_x,pos_y)
   
  move()
  
  time.sleep(delay)
