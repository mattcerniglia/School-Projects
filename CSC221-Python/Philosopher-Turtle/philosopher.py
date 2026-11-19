def philosopher():
	import turtle
	t=turtle
	t.Turtle()
	t.speed(0)
	t.goto(0,0)
	t.bgcolor("black")
	t.pencolor("red")
#sped pen up, changed background color, pen color and moved it to center
	t.circle(100)
	t.forward(100)
	for i in range(4):
		t.left(90)
		t.forward(200)
		i += 1
#making the square, using range to stop when its completed
	t.forward(200)
	t.left(135)
	t.forward(425)
	t.left(90)
	t.forward(425)
	t.left(135)
	t.forward(600)
#making triangle
	t.left(90)
	t.circle(300)
#making sure the circle is in the right place, going the right direction
	t.done()

philosopher()
