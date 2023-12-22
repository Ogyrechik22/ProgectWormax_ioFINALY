img = 0
bb = 300
ee = 25
cc = 700
dd = 25
rr = 100
vv = 25
x = 25
s = 150
y = 25
z = 875
l = 25
v = 0
dirb = 3.2
dira = 2.9
dirc = 2.7
dird = 3
dirs = 2
zz = 0
rer = 0
def setup():
    global img
    size(900,900)
    background(0,5,5)
    frameRate(1000)
    textMode(CENTER)
    img = loadImage('23.jpg')
def draw():
    global x,y,z,l,s,dirs,dira,dirb,dirc,dird,ee,bb,cc,dd,rr,vv,zz,rer
    background(1)
    fill(54,255,0)
    textSize(20)
    ellipse(bb,ee,35,35)
    fill(1)
    text(+3,bb - 6,ee + 7)
    ee = ee + 1.7
    if ee > 875:
        ee = 25
        bb = random(25,875)
    fill(255,142,3)
    ellipse(cc,dd,35,35)
    fill(1)
    text("-",cc - 6,dd + 7)
    dd = dd + 1.7
    if dd > 875:
        dd = 25
        cc = random(25,875)
    fill(255,235,3)
    ellipse(rr,vv,35,35)
    fill(1)
    text("+",rr - 6,vv + 7)
    vv = vv + 1.7
    if vv > 875:
        vv = 25
        rr = random(25,875)
    fill(255)
    rect(mouseX,750,200,17)
    ellipse(x,y,50,50)
    x = x + dira
    y = y + dirb
    if x > 875:
        dira = -3.2
    if x < 25:
        dira = 3.2
    if y > 1100:
        x = random(25,875)
        y = 25
    if y < 25:
        dirb = 2.9
    ellipse(z,l,50,50)
    z = z + dirc
    l = l + dird
    if z > 875:
        dirc = -2.7
    if z < 25:
        dirc = 2.7
    if l > 1100:
        l = 25
        z = random(25,875)
    if l < 25:
        dird = 3
    text("score:", 730,100)
    text(zz,800,100)
    if x > mouseX and x < mouseX + 200 and y > 735 and y < 755:
        dirb = -2.9
        zz = zz + 7
    if z > mouseX and z < mouseX + 200 and l > 735 and l < 755:
        dird = -3
        zz = zz + 7
    if bb > mouseX and bb < mouseX + 200 and ee > 735 and ee < 755:
        bb = random(25,875)
        ee = 25
        zz = zz + 2
    if cc > mouseX and cc < mouseX + 200 and dd > 735 and dd < 755:
        cc = random(25,875)
        dd = 25
        zz = zz - 50
    if rr > mouseX and rr < mouseX + 200 and vv > 735 and vv < 755:
        rr = random(25,875)
        vv = 25
        zz = zz + 3
    fill(62,83,116)
    textSize(70)
    text("wormax.io",280,200)
    textSize(120)
    fill(130)
    ellipse(450,340,340,180)
    fill(255,23,31)
    text("PLAY",305,380)
    fill(255)
def mouseClicked():
    noLoop()
    fill(1)
    global img
    image(img,0,0,900,900)
    stroke(255)
    line(0,75,900,75)
    line(0,150,900,150)
    line(0,225,900,225)
    line(0,300,900,300)
    line(0,375,900,375)
    line(0,450,900,450)
    line(0,525,900,525)
    line(0,600,900,600)
    line(0,675,900,675)
    line(0,750,900,750)
    line(0,825,900,825)
    fill(255)
    textSize(30)
    text(u"Уровень от Knobelboy. Сложность 6/10. Играть!",100,50)
    text(u"Уровень от ItsDolphy Сложность 7/10. Играть!",100,125)
    text(u"Уровень от Trusta. Сложность 4/10. Играть!",100,200)
    text(u"Уровень от DragonVAC. Сложность 0/10. Играть!",100,275)
    text(u"Уровень от Zoink. Сложность 10/10. Играть!",100,350)
    text(u"Уровень от Trick. Сложность 9/10. Играть!",100,425)
    text(u"Уровень от Doggie. Сложность 9/10. Играть!",100,500)
    text(u"Уровень от Viprin. Сложность 4/10. Играть!",100,575)
    text(u"Уровень от Cursed. Сложность 8/10. Играть!",100,650)
    text(u"Уровень от ItsVeryZGD. Сложность 3/10. Играть!",100,725)
    text(u"Уровень от Manix. Сложность 5/10. Играть!",100,800)
    text(u"Уровень от Eandis. Сложность 9/10. Играть!",100,875)



    
