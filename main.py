import turtle
import time
import math

energy_display = turtle.Turtle()
energy_display.hideturtle()
energy_display.penup()
energy_display.goto(0, 200)
energy_display.color('black')
FONT = ('Times New Roman', 16, 'bold')
energy_display.write("Кинетическая энергия: 0    Потенциальная энергия: 0", align='center', font=FONT)

wn = turtle.Screen()
wn.setup(1200, 900)
#wn.bgpic('images/1.jpg')
turtle.tracer(2)
t = turtle.Turtle('turtle')
t.hideturtle()
t.color('blue')
t.penup()
t.begin_poly()
t.fd(400)
t.left(90)
t.circle(30.358)
t.fd(4)
t.left(90)
t.fd(400)
t.end_poly()
wn.addshape('pend', t.get_poly())

t1 = turtle.Turtle(shape='pend')
t1.up()
t1.color('red')
t1.showturtle()

t2 = t1.clone()
t2.goto(-120, 0)
t2.showturtle()

t3 = t1.clone()
t3.goto(120, 0)
t3.showturtle()

t4 = t1.clone()
t4.goto(-60, 0)
t4.showturtle()

t5 = t1.clone()
t5.goto(60, 0)
t5.showturtle()

g = 9.81 

FONT = ('Times New Roman', 20, 'bold')
angle = float(wn.textinput('Колебания маятника', 'Введите угол отклонения:'))
m = float(wn.textinput('Колебания маятника', 'Введите массу мяча в килограммах: '))
h = float(wn.textinput('Колебания маятника', 'Введите высоту мяча в метрах: '))


angle = -angle
if angle > 0:
    t2.right(angle)

if angle < 0:
    t3.right(angle)
q = 0
N = 110


def motion(turtle1, turtle2):
    q = 0
    for i in range(N):
        q = 0.01 * i * angle / 60
        turtle1.lt(q)
        time.sleep(0.01)

    q1 = q
    for i in range(N):
        q2 = q1 - 0.01 * i * angle / 60
        turtle2.lt(q2)
        time.sleep(0.01)
    q3 = 0
    for i in range(N):
        q3 = 0.01 * i * angle / 60
        turtle2.lt(-q3)
        time.sleep(0.01)

    q4 = q3
    for i in range(N):
        q5 = q4 - 0.01 * i * angle / 60
        turtle1.lt(-q5)
        time.sleep(0.01)
    q = 0

def calculate_kinetic_energy(m, v):
    return 0.5 * m * v**2

# Function to calculate potential energy
def calculate_potential_energy(m, h):
    return m * g * h

# Function to update energy display
def update_energy_display(kinetic_energy, potential_energy):
    energy_display.clear()
    energy_display.write(f"Кинетическая энергия: {kinetic_energy:.2f} J    Потенциальная энергия: {potential_energy:.2f} J", align='center', font=FONT)

# Function to perform the simulation and calculate energies
def task(m, h, angle):
    v = math.sqrt(2 * g * h)
    y = h * math.cos(math.radians(q))

    kinetic_energy = calculate_kinetic_energy(m, v)
    potential_energy = calculate_potential_energy(m, y)
    update_energy_display(kinetic_energy, potential_energy)

while True:
    if angle < 0:
        motion(t3, t2)
        task(m, h, angle)
    if angle > 0:
        motion(t2, t3)
        task(m, h, angle)
