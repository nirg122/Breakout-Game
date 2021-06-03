import turtle as tr
from ball import Ball
from time import sleep
from block_manager import BlockManager
from paddle import Paddle
from lives import Lives

def motion(event):
    global x
    x = event.x

screen = tr.Screen()
screen.setup(width=1400, height=800)
screen.bgcolor("grey")
screen.title("Python Turtle Movement")
screen.tracer(0)
screen.listen()
canvas = tr.getcanvas()

paddle = Paddle()
blocks = BlockManager()

ball = Ball()
x = 0
brick_hit_counter = 0
lives = Lives()

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.01)
    canvas.bind('<Motion>', motion) # controlling the paddle with mouse movement

    n = -40 # for making space between paddle pixel
    for pixel in paddle.paddle_list:
        pixel.setx((x - 700) - n)
        n += 20
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 360:
        ball.bounce_y()

    if ball.xcor() > 656:
        ball.bounce_x()

    if ball.xcor() < -660:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle.paddle_list[0]) < 20:
        ball.x_move = 15
        ball.y_move = 5

    if ball.distance(paddle.paddle_list[1]) < 20:
        ball.x_move = 12
        ball.y_move = 7

    if ball.distance(paddle.paddle_list[2]) < 20:
        ball.x_move = 10
        ball.y_move = 10

    if ball.distance(paddle.paddle_list[3]) < 20:
        ball.x_move = -10
        ball.y_move = 10

    if ball.distance(paddle.paddle_list[4]) < 20:
        ball.x_move = -12
        ball.y_move = 7

    if ball.distance(paddle.paddle_list[5]) < 20:
        ball.x_move = -15
        ball.y_move = 5

    # Detect paddle miss
    if ball.ycor() < -400:
        lives.life -= 1
        ball.reset_position()
        lives.clear()
        lives.write(f'♥\n{lives.life}', align="center", font=("Courier", 25, "bold"))

    # Detect block hit
    for row in blocks.all_rows:
        for block in row:
            if ball.distance(block) < 27:
                ball.bounce_y()
                block.goto(2000, 2000) # block goes off the screen
                brick_hit_counter += 1

    # Detect paddle goes off right side screen
    pixel_xcor = 660
    for pixel in paddle.paddle_list:
        if pixel.xcor() > pixel_xcor:
            pixel.goto(pixel_xcor, pixel.ycor())
            pixel_xcor -= 20

    # Detect paddle goes off left side screen
    pixel_xcor = -674
    for pixel in paddle.paddle_list[::-1]:
        if pixel.xcor() < pixel_xcor:
            pixel.goto(pixel_xcor, pixel.ycor())
            pixel_xcor += 20

    # Lost of lives
    if lives.life < 1:
        canvas.create_text(0, 0, text="You Have Lost\n   Game Over", font=('Helvetica', 50, 'bold'), fill='red')
        game_is_on = False

    # Detect all blocks has been hit
    if brick_hit_counter == 192:
        canvas.create_text(0, 0, text=" You Have WON\n    Game Over", font=('Helvetica', 50, 'bold'), fill='green')
        game_is_on = False

screen.exitonclick()
