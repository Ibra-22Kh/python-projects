import random
import turtle
# s = 5 
# print(s)

# b ="hello"
# print(b)

# name = input("Enter your name")
# age = input("Enter your age")

# print("Name: " + name)
# print("Age: " + age)


# x = random.randint(0,100)
# print("x: " , x)

skillpoints = 15
# if skillpoints < 16:
#     print("You have less points")
# else:
#     print("You have more points")

# shoppingCarts =  []
# item = input("Enter the name of the product")
# shoppingCarts.append(item)
# print("list", shoppingCarts)


#
#Finite State Machine 

# state = 1
# while(1):
#     transit = input("Enter your alphabet")
#     print("you have entered the state:",state)
#     if state == 1:
#         if transit == 'W':
#             state = 2

#     elif state == 2:
#         if transit == 'G':
#             state = 3
#         elif transit == 'S':
#             state = 1
    
#     elif state == 3:
#         if transit == 'L':
#             state = 1

#     print("maintenent tu es le state ici:",state)


l = ["apple","peer","mango","orange"]

# for elment in l:
#     print(elment)

# array=[1,23,4,56,7,8,9]

# for element in array:
#     print(element+2)
# for i in range (0,len(array)):
#     array[i] = array[i]+ i
    
# print(array)
# for i, items in enumerate(l):
#     print(items)

# shapes = ["Square", "Circle", "Triangle"]
# centers =[(10,10),(50,50), (100,100)]

# #loop in the ordinary range
# for i in range(0,len(shapes)):
#     print(shapes[i],centers[i])

# #loop in zip function for many arrays on each other for not having error overlaping
# for shape, center in zip(shapes,centers):
#     print(shape,center)


# List comprehension
# s = "This is nice"

# s= [x for x in s if x!=' ']
# print(s)

# lifOfNumber = [x for x in range(10) if x%2 == 0]
# print(lifOfNumber)

#16px x 16px image coordinates shift Using for loop


# imagePixels = [ 
#                 [0,0], [1,0], [2,0], [3,0],
#                 [0,1], [1,1], [2,1], [3,1],
#                 [0,2], [1,2], [2,2], [3,2],
#                 [0,3], [1,3], [2,3], [3,3],
#             ]
# for i in range(0,len(imagePixels)):
#     imagePixels[i][0] = imagePixels[i][0] + 3
#     print(imagePixels)
# #shift Y axis 2 pixels downwards
# for i in range(0,len(imagePixels)):
#     imagePixels[i][0] = imagePixels[i][1] + 3
#     print(imagePixels)


#function and return type with different uses:
# db = ["hassan", "jack", "jonas"]
# def addTo(name):
#     db.append(name)

# addTo("John")
# addTo("Coral")
# print("Db is : ",db)

# def pwr2(num):
#     pw2 = num*num
#     div = num/num
#     return pw2,div

# pw2 , div = pwr2(5)
# print("pwr is", pw2)
# print("div is",div)


# #Square
# farouq_turtle = turtle.Turtle()


# screen = turtle.Screen()
# screen.title("PingPong")
# screen.bgcolor("Blue")
# screen.setup(width=800, height=600)
# screen.tracer(0)


# paddle_1 = turtle.Turtle()
# paddle_1.shape("square")
# paddle_1.color("white")
# paddle_1.shapesize(stretch_wid=5, stretch_len=1)
# paddle_1.penup()
# paddle_1.goto(-350,0)


# paddle_2 = turtle.Turtle()
# paddle_2.shape("square")
# paddle_2.color("white")
# paddle_2.shapesize(stretch_wid=5, stretch_len=1)
# paddle_2.penup()
# paddle_2.goto(350,0)

# ball = turtle.Turtle()
# ball.shape("circle")
# ball.color("Green")
# ball.penup()
# ball.goto(0,0)
# ball.dx = 0.1
# ball.dy = -0.1

# score1= 0
# score2= 0
# scoreText = turtle.Turtle()

# scoreText.color("white")
# scoreText.hideturtle()
# scoreText.penup()
# scoreText.goto(0,260)
# scoreText.write("Player 1 : 0  Player 2 : 0", align="center", font=("Courier",22,"normal"))
# step = 10

# def moveBall():
#     ball.setx(ball.xcor()+ball.dx)
#     ball.sety(ball.ycor()+ ball.dy)
    
#     x = ball.xcor()
#     y = ball.ycor()
    
#     if x>390:
#         ball.setx(390)
#         ball.dx = ball.dx * -1
#     if x <-390:
#         ball.setx(-390)
#         ball.dx = ball.dx * -1
    
#     if y >290:
#         ball.sety(290)
#         ball.dy = ball.dy * -1
        
#     if y <-290:
#         ball.sety(-290)
#         ball.dy =ball.dy * -1
        
        

  
    

# def paddle_1_up():
#     y = paddle_1.ycor()
#     y = y+step
#     paddle_1.sety(y)
#     if  y > 240:
#         paddle_1.sety(240)
    
# def paddle_1_down():
#     y = paddle_1.ycor()
#     y = y-step
#     paddle_1.sety(y)
#     if y<-240:
#         paddle_1.sety(-240)
        
# def paddle_1_right():
#     x =  paddle_1.xcor()
#     x= x+step
#     paddle_1.setx(x) 
#     if x >-10:
#         paddle_1.setx(-10)

# def paddle_1_left():
#     x =  paddle_1.xcor()
#     x= x-step
#     paddle_1.setx(x) 
#     if x <-350:
#         paddle_1.setx(-350)

# def paddle_2_left():
#     x =  paddle_2.xcor()
#     x= x-step
#     paddle_2.setx(x) 
#     if x <10:
#         paddle_2.setx(10)

# def paddle_2_right():
#     x =  paddle_2.xcor()
#     x= x+step
#     paddle_2.setx(x) 
#     if x >350:
#         paddle_2.setx(350)        


# def paddle_2_down():
#     y = paddle_2.ycor()
#     y = y-step
#     paddle_2.sety(y)
#     if y<-240:
#         paddle_2.sety(-240)

# def paddle_2_up():
#     y = paddle_2.ycor()
#     y = y+10
#     paddle_2.sety(y)
#     if  y > 240:
#         paddle_2.sety(240)
        
        

# def checkCollision():
#     if (paddle_1.xcor()+20 >=  ball.xcor() >= paddle_1.xcor()-20) and (paddle_1.ycor()+60 >=  ball.ycor() >= paddle_1.ycor()-60):
#         ball.dx = ball.dx*-1
#         ball.dy = ball.dy *-1
        
#         x = ball.xcor()
#         x= x+10
#         ball.setx(x)
    
#     if (paddle_2.xcor()+20 >=  ball.xcor() >= paddle_2.xcor()-20) and (paddle_2.ycor()+60 >=  ball.ycor() >= paddle_2.ycor()-60):
#         ball.dx = ball.dx*-1
#         ball.dy = ball.dy *-1
        
#         x = ball.xcor()
#         x= x-10
#         ball.setx(x)  
    
    
# screen.listen()
# screen.onkeypress(paddle_1_up,"w")
# screen.onkeypress(paddle_1_down,"s")
# screen.onkeypress(paddle_1_right,"d")
# screen.onkeypress(paddle_1_left,"a")
# screen.onkeypress(paddle_2_up,"Up") 
# screen.onkeypress(paddle_2_down,"Down")
# screen.onkeypress(paddle_2_right,"Right")
# screen.onkeypress(paddle_2_left,"Left")
# while(1):
#     screen.update()
#     moveBall()
#     checkCollision()
#     if ball.xcor()>=350:
#         score1 = score1 +1
#         scoreText.clear()
#         scoreText.write("Player 1 : {}  Player 2 : {}".format(score1,score2), align="center", font=("Courier",22,"normal"))
#         ball.goto(0,0)
#         ball.dx = ball.dx *-1
        
#     if ball.xcor()<-350:
#         score2 = score2 +1
#         scoreText.clear()
#         scoreText.write("Player 1 : {}  Player 2 : {}".format(score1,score2), align="center", font=("Courier",22,"normal"))
#         ball.goto(0,0)
#         ball.dx = ball.dx *-1      


#dictionaries and how to use them

# db = {"name":"john","age": 27 , "birthdate": "1/1/2101" }
# print(db["age"])
# print(db.keys())

# DB = {"name":["John","Messiah","Hassan"],
#     "age":[27,29,30]}
# print(DB["name"][0])


# db ={}
# if"names" in db:
#     del db["names"]

# db["names"]="Mr.White"
# db["age"]=28

# db.update({"names":["John","Parker"]})
# db.update({"age":[27,29]})

# db["names"].append("Sofia")
# db["age"].append(26)


# print(db)


# db ={}


# db.update({"names":["John","Parker"]})
# db.update({"age":[27,29]})

# index = db["names"].index("John")

# for value in db.values():
#     for subvalue in value:
#         print(subvalue)

def xx (par):
    return par/10

x  = lambda x: x/10

print(x(50))

print(xx(50))

# for key in db.keys():
#     del db[key][index]

# def square():
#   farouq_turtle.forward(100)
#   farouq_turtle.right(90)
#   farouq_turtle.forward(100)
#   farouq_turtle.right(90)
#   farouq_turtle.forward(100)
#   farouq_turtle.right(90)
#   farouq_turtle.forward(100)

# square()
# farouq_turtle.forward(100)
# square()