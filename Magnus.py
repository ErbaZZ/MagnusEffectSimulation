from visual import *
from visual.controls import *
from visual.graph import *

scene = display()
scene.height = 600
scene.width = 600
scene.background = (1, 1, 1)
scene.center = (0, 0, 0)
scene.background = (0, 0, 0)
scene.range = (20, 10, 50)
scene.ambient = 0.5
scene.title = "Magnus Effect"
scene.forward = -scene.range

w = 300
h = 600
x = 600
y = 0

running = 0

basketballpattern = ((1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
basketball = materials.texture(data=basketballpattern, mapping="spherical", interpolate=True)  # Basketball texture
sloc = vector(0, 0, 0)  # Starting location

dt = 0.005  # Time changed per loop

# Starting Velocity
vx = 50
vy = 40
vz = 30

ballCd = 0.54  # Drag Coefficient of a basketball
ballCl = 0.25  # Lift Coefficient of a basketball
ballmass = 0.6237  # Mass of a basketball
ballr = 0.5  # For graphical purpose only, real radius of basketball = 12.13 cm
airD = 1.225  # Density of air
ballCSA = 0.046  # Cross section area of a basketball
fd = vector(0., 0., 0.)  # Drag Force
fm = vector(0., 0., 0.)  # Magnus Force
g = vector(0, -9.8, 0)  # Acceleration from gravity
rx = 30 # Rotational speed in x axis (rad/s)
ry = -10  # Rotational speed in y axis (rad/s)
rz = 80  # Rotational speed in z axis (rad/s)
RPMx = rx * 9.54929659643
RPMy = ry * 9.54929659643
RPMz = rz * 9.54929659643
rotation = vector(rx, ry, rx)  # Rotation vector of the ball
a = vector(0, 0, 0)
time = 0

ball = sphere(pos=sloc, radius=ballr, color=(0.94, 0.51, 0.03), material=basketball, make_trail=True)
analytic = curve(color=(1, 0, 0))
floor = box(pos=(20, -0.5 - (ballr), 0), size=(150, 1, 200), material=materials.wood)
wall = box(pos=(20, 24 + ballr, -100), size=(150, 50, 1), material=materials.wood)

ball.velocity = vector(vx, vy, vz)  # Set the starting velocity vector of the ball

arrowlenmult = 0.2
global varrow
varrow = arrow(pos=(0, 0, 0), axis=ball.velocity * arrowlenmult, shaftwidth=0.2, color=(1, 0, 0))


# Controlling Functions
def setvx(val):
    global vx
    vx = val
    vxlabel.text = '%d m/s' % vx
    varrow.axis = (vx * arrowlenmult, vy * arrowlenmult, vz * arrowlenmult)


def setvy(val):
    global vy
    vy = val
    vylabel.text = '%d m/s' % vy
    varrow.axis = (vx * arrowlenmult, vy * arrowlenmult, vz * arrowlenmult)


def setvz(val):
    global vz
    vz = val
    vzlabel.text = '%d m/s' % vz
    varrow.axis = (vx * arrowlenmult, vy * arrowlenmult, vz * arrowlenmult)


def setrxspeed(val):
    global rx
    global rotation
    global RPMx
    rx = val
    RPMx = rx * 9.54929659643
    rotation = vector(rx, ry, rz)
    rotxsplabel.text = '%d rad/s' % rx
    rpmxlabel.text = '%d RPM' % RPMx


def setryspeed(val):
    global ry
    global rotation
    global RPMy
    ry = val
    RPMy = ry * 9.54929659643
    rotation = vector(rx, ry, rz)
    rotysplabel.text = '%d rad/s' % ry
    rpmylabel.text = '%d RPM' % RPMy


def setrzspeed(val):
    global rz
    global rotation
    global RPMz
    rz = val
    RPMz = rz * 9.54929659643
    rotation = vector(rx, ry, rz)
    rotzsplabel.text = '%d rad/s' % rz
    rpmzlabel.text = '%d RPM' % RPMz


# Main loop
def launch():
    global running
    global rotation
    if (running == 0):  # Prevent launching again mid-air
        ball.velocity = vector(vx, vy, vz)
        time = 0
        varrow.visible = false
        controlw.display._destroy()


        # Graphs
        vxplot = gdisplay(x=600,y=0,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'vx(t)',xtitle = 't (s)',ytitle='vx(m/s)')
        vxcurve = gcurve(display=vxplot,color=(1,0,0))
        vyplot = gdisplay(x=850,y=0,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'vy(t)',xtitle = 't (s)',ytitle='vy(m/s)')
        vycurve = gcurve(display=vyplot,color=(1,0,0))
        vzplot = gdisplay(x=1100,y=0,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'vz(t)',xtitle = 't (s)',ytitle='vz(m/s)')
        vzcurve = gcurve(display=vzplot,color=(1,0,0))
        Fdxplot = gdisplay(x=600,y=200,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'Fdx(t)',xtitle = 't (s)',ytitle='Fdx(N)')
        Fdxcurve = gcurve(display=Fdxplot,color=(1,0,0))
        Fdyplot = gdisplay(x=850,y=200,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'Fdy(t)',xtitle = 't (s)',ytitle='Fdy(N)')
        Fdycurve = gcurve(display=Fdyplot,color=(1,0,0))
        Fdzplot = gdisplay(x=1100,y=200,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'Fdz(t)',xtitle = 't (s)',ytitle='Fdz(N)')
        Fdzcurve = gcurve(display=Fdzplot,color=(1,0,0))
        Fmxplot = gdisplay(x=600,y=400,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'Fmx(t)',xtitle = 't (s)',ytitle='Fmx(N)')
        Fmxcurve = gcurve(display=Fmxplot,color=(1,0,0))
        Fmyplot = gdisplay(x=850,y=400,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'Fmy(t)',xtitle = 't (s)',ytitle='Fmy(N)')
        Fmycurve = gcurve(display=Fmyplot,color=(1,0,0))
        Fmzplot = gdisplay(x=1100,y=400,width = 250,height=200,background = (1,1,1),foreground=(0,0,0),title = 'Fmz(t)',xtitle = 't (s)',ytitle='Fmz(N)')
        Fmzcurve = gcurve(display=Fmzplot,color=(1,0,0))

        while (ball.pos.y >= 0):
            running = 1
            rate(1 / dt)
            fd = -(
            1. / 2.) * ballCd * airD * ballCSA * ball.velocity.mag2 * ball.velocity.norm()  # Drag force from the air
            fm = (1. / 2.) * ballCl * airD * ballCSA * ball.velocity.mag2 * (
            cross(rotation / (2 * pi) * dt, ball.velocity))  # Magnus force from the rotation of the ball
            a = (fd + fm+(ballmass*g)) / ballmass  # Acceleration of the ball
            ball.velocity += a * dt
            ball.pos += ball.velocity * dt

            # Rotating the ball in each axes
            ball.rotate(angle=rx * dt, axis=(1, 0, 0))
            ball.rotate(angle=ry * dt, axis=(0, 1, 0))
            ball.rotate(angle=rz * dt, axis=(0, 0, 1))

            # Turn the camera to follows the ball
            scene.forward = (ball.pos/2 - scene.range)
            scene.center = (ball.pos.x * 0.75, ball.pos.y, ball.pos.z)

            time += dt

            # Plotting graphs
            vxcurve.plot(pos=(time,ball.velocity.x))
            vycurve.plot(pos=(time,ball.velocity.y))
            vzcurve.plot(pos=(time,ball.velocity.z))
            Fdxcurve.plot(pos=(time,fd.x))
            Fdycurve.plot(pos=(time,fd.y))
            Fdzcurve.plot(pos=(time,fd.z))
            Fmxcurve.plot(pos=(time,fm.x))
            Fmycurve.plot(pos=(time,fm.y))
            Fmzcurve.plot(pos=(time,fm.z))

            if (sloc.y + vy * time + 0.5 * g.y * time * time >= 0):
                # Analytic movement line of the ball without the effect of drag force and magnus force (Moving in vacuum)
                analytic.append(
                    pos=(sloc.x + vx * time, sloc.y + vy * time + 0.5 * g.y * time * time, sloc.z + vz * time))
        while (
                    sloc.y + vy * time + 0.5 * g.y * time * time >= 0):  # Continue the analytic line if it hasn't reached the floor yet
            rate(1 / dt)
            time += dt
            analytic.append(pos=(sloc.x + vx * time, sloc.y + vy * time + 0.5 * g.y * time * time, sloc.z + vz * time))


# Controls Window and controlling elements
controlw = controls(x=600, y=0, width=300, height=600, title="Controls", background=(0, 0.3, 0.3))
b1 = button(pos=(0, -80), width=30, height=15, text='Launch', action=lambda: launch(), color=(0.8, 0.8, 0.8))
vxslider = slider(pos=(-35, 75), width=5, height=10, value=vx, length=60, text='x velocity',
                  action=lambda: setvx(vxslider.value), color=(1, 0.8, 0.8), min=0, max=50)
vyslider = slider(pos=(-35, 55), width=5, height=10, value=vy, length=60, text='y velocity',
                  action=lambda: setvy(vyslider.value), color=(1, 0.8, 0.8), min=0, max=50)
vzslider = slider(pos=(-35, 35), width=5, height=10, value=vz, length=60, text='z velocity',
                  action=lambda: setvz(vzslider.value), color=(1, 0.8, 0.8), min=0, max=50)
xlabel = label(pos=(-43, 75), text='vx', display=controlw.display, box=false, opacity=0)
ylabel = label(pos=(-43, 55), text='vy', display=controlw.display, box=false, opacity=0)
zlabel = label(pos=(-43, 35), text='vz', display=controlw.display, box=false, opacity=0)
vxlabel = label(pos=(40, 75), text='%d m/s' % vx, display=controlw.display, box=false)
vylabel = label(pos=(40, 55), text='%d m/s' % vy, display=controlw.display, box=false)
vzlabel = label(pos=(40, 35), text='%d m/s' % vz, display=controlw.display, box=false)
vtitlelabel = label(pos=(0, 90), text='Velocity', display=controlw.display)
rotlable = label(pos=(0, 10), text='Angular Velocity', display=controlw.display)
rotxslider = slider(pos=(-35, -5), width=5, height=10, value=rx, length=60, text='rotational speed',
                    color=(1, 0.8, 0.8), min=-100, max=100, action=lambda: setrxspeed(rotxslider.value))
rotxsplabel = label(pos=(39, -2), text='%d rad/s' % rx, display=controlw.display, box=false, opacity=0)
rpmxlabel = label(pos=(39, -8), text='%d RPM' % RPMx, display=controlw.display, box=false, opacity=0)
rotyslider = slider(pos=(-35, -25), width=5, height=10, value=ry, length=60, text='rotational speed',
                    color=(1, 0.8, 0.8),
                    min=-100, max=100, action=lambda: setryspeed(rotyslider.value))
rotysplabel = label(pos=(39, -22), text='%d rad/s' % ry, display=controlw.display, box=false, opacity=0)
rpmylabel = label(pos=(39, -28), text='%d RPM' % RPMy, display=controlw.display, box=false, opacity=0)
rotzslider = slider(pos=(-35, -45), width=5, height=10, value=rz, length=60, text='rotational speed',
                    color=(1, 0.8, 0.8), min=-100, max=100, action=lambda: setrzspeed(rotzslider.value))
rotzsplabel = label(pos=(39, -42), text='%d rad/s' % rz, display=controlw.display, box=false, opacity=0)
rpmzlabel = label(pos=(39, -48), text='%d RPM' % RPMz, display=controlw.display, box=false, opacity=0)

axlabel = label(pos=(-43, -5), text='rx', display=controlw.display, box=false, opacity=0)
aylabel = label(pos=(-43, -25), text='ry', display=controlw.display, box=false, opacity=0)
azlabel = label(pos=(-43, -45), text='rz', display=controlw.display, box=false, opacity=0)
