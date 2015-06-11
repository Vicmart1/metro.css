import sys

central_line = []

def drawLine(line, f):
    global central_line
    data_points = line.split(":")
    if len(data_points) > 1:
        f.write("<div class='center' style='height:" + data_points[len(data_points) - 1][:-1] + "px'>")
    
    color = "background:" + central_line[1]
    css = ""

    if len(data_points) == 4:
        for i in range(0,3):
            if data_points[i] != "":
                central_line[i] = data_points[i]
        color = "background:" + central_line[1]
    elif len(data_points) == 3:
        css = "width:0px; border-left: 12.5px dotted "
    elif len(data_points) == 2 and data_points[0] != "":
        if central_line[1] != "-":
            color = "background: -webkit-linear-gradient( " + central_line[1] + ", " + data_points[0] + "); background: -o-linear-gradient(" + central_line[1] + ", " + data_points[0] + ");background: -moz-linear-gradient(" + central_line[1] + ", " + data_points[0] + ");background: linear-gradient(" + central_line[1] + ", " + data_points[0] + ");"
            central_line[1] = data_points[0]
        else:
            central_line[1] = data_points[0]
            color = "background:" + central_line[1]
    elif len(data_points) == 1:
        central_line[1] = data_points[0]

    if len(data_points) > 1:
        if central_line[2] != '-':
            f.write("<div class='center " + (central_line[2] if len(data_points) != 3 else "") + " rectangle right-line' style='" + (css + central_line[2] if len(data_points) == 3 else "") + "'></div>")
        if central_line[0] != '-':
            f.write("<div class='center " + (central_line[0] if len(data_points) != 3 else "") + " rectangle left-line' style='" + (css + central_line[0] if len(data_points) == 3 else "") + "'></div>")
        f.write("<div class='center rectangle' style='" + css + (color if len(data_points) != 3 else central_line[1]) + "'></div>")
    
        f.write("</div>")

def createDescription(line, junction, f):
    data_points = line.split(":")
    f.write("<div class='right rotated" + ("-junction" if junction else " ")+ "'><p class='vertical-center text'><b>" + data_points[0] + "</b></br>" + (" " if len(data_points) == 1 else data_points[1]) + "</p></div>")

def createStation(line, f):
    f.write("<div class='center " + central_line[1] + " full-circle'><div class='center white mid-circle vertical-center'></div></div>")

def drawJunction(line, f):
    global central_line
    data_points = line.split(":")
    f.write("<div class='center'><div class='center " + ((central_line[2] if data_points[0][0] == '>' else central_line[0]) if len(data_points) == 1 else data_points[0][1:]) + ('-fade' if len(data_points) > 2 and data_points[1]=='fade' else "") + " rectangle rotated-" + ('right' if data_points[0][0] == '>' else 'left') + (" " if len(data_points) < 3 else ("-" + data_points[2][:-1])) + ("" if len(data_points) < 2 else ("-solid" if data_points[1] == 'solid' else "")) + "'></div></div>")
    if (data_points[0][0] == '>' or data_points[0][1:] == central_line[2]) and len(data_points) < 3:
        central_line[2] = '-'
    elif (data_points[0][0] == '<' or data_points[0][1:] == central_line[0]) and len(data_points) < 3:
        central_line[0] = '-'

def createRuler(line, f):
    data_points = line.split(':')
    remainder = float(data_points[1])%1.0
    for i in range(0,int(float(data_points[1]) - float(data_points[0]))):
        f.write("<div class='gray ruler-rectangle' style='width:100px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>" + str(int(float(data_points[0])) + i) + "</p></div></div>")
        f.write("<div class='gray ruler-rectangle' style='width:25px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>Mar</p></div></div>")
        f.write("<div class='gray ruler-rectangle' style='width:50px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>June</p></div></div>")
        f.write("<div class='gray ruler-rectangle' style='width:25px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>Sept</p></div></div>")
    if remainder > 0.0:
        f.write("<div class='gray ruler-rectangle' style='width:100px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>" + str(int(float(data_points[1]))) + "</p></div></div>")
    
    if remainder >= 0.25:
        f.write("<div class='gray ruler-rectangle' style='width:25px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>Mar</p></div></div>")
    
    if remainder >= 0.5:
        f.write("<div class='gray ruler-rectangle' style='width:50px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>June</p></div></div>")
    
    if remainder >= 0.75:
        f.write("<div class='gray ruler-rectangle' style='width:25px;'><div class='right ruler-rotated'><p class='vertical-center text'></br>Sept</p></div></div>")


def error(str):
    print str
    raise SystemExit(0)


#-----------------------#
if len(sys.argv) < 3:
    error("Usage: python metro.py [read file] [write file]")

f = open(sys.argv[2],'w')
f.write("<html><head><style>@font-face { font-family: KeepCalm; src: url(http://ff.static.1001fonts.net/k/e/keep-calm.regular.ttf); } html { overflow-x: hidden; } body { padding: 0px; margin: 0px; } .all-lines { position:absolute; top:0px; width:100%; left: 0; margin-left:-50%; /* half of the width */ } .ruler { position: absolute; left:0px; top:0px; width:100%; z-index: 2; } .line { width: 418px; } .major-right-line { position: absolute; left: calc(50% + 12px); } .major-left-line { position: absolute; left: calc(50% - 418px - 12px); } .center { margin-left: auto; margin-right: auto; } .left { float: left; } .right { float: right; } .red { background: red; } .red-fade { background: -webkit-linear-gradient(left,rgba(255,255,255,0), red); /*Safari 5.1-6*/ background: -o-linear-gradient(right,rgba(255,255,255,0), red); /*Opera 11.1-12*/ background: -moz-linear-gradient(right,rgba(255,255,255,0), red); /*Fx 3.6-15*/ background: linear-gradient(to right, rgba(255,255,255,0), red); /*Standard*/ } .pink { background: pink; } .pink-fade { background: -webkit-linear-gradient(left,rgba(255,255,255,0), pink); /*Safari 5.1-6*/ background: -o-linear-gradient(right,rgba(255,255,255,0), pink); /*Opera 11.1-12*/ background: -moz-linear-gradient(right,rgba(255,255,255,0), pink); /*Fx 3.6-15*/ background: linear-gradient(to right, rgba(255,255,255,0), pink); /*Standard*/ } .orange { background: orange; } .orange-fade { background: -webkit-linear-gradient(left,rgba(255,255,255,0), orange); /*Safari 5.1-6*/ background: -o-linear-gradient(right,rgba(255,255,255,0), orange); /*Opera 11.1-12*/ background: -moz-linear-gradient(right,rgba(255,255,255,0), orange); /*Fx 3.6-15*/ background: linear-gradient(to right, rgba(255,255,255,0), orange); /*Standard*/ } .black { background: black; } .black-fade { background: -webkit-linear-gradient(left,rgba(255,255,255,0), black); /*Safari 5.1-6*/ background: -o-linear-gradient(right,rgba(255,255,255,0), black); /*Opera 11.1-12*/ background: -moz-linear-gradient(right,rgba(255,255,255,0), black); /*Fx 3.6-15*/ background: linear-gradient(to right, rgba(255,255,255,0), black); /*Standard*/ } .gray { background: gray; } .gray-fade { background: -webkit-linear-gradient(left,rgba(255,255,255,0), gray); /*Safari 5.1-6*/ background: -o-linear-gradient(right,rgba(255,255,255,0), gray); /*Opera 11.1-12*/ background: -moz-linear-gradient(right,rgba(255,255,255,0), gray); /*Fx 3.6-15*/ background: linear-gradient(to right, rgba(255,255,255,0), gray); /*Standard*/ } .blue { background: blue; } .blue-fade { background: -webkit-linear-gradient(left,rgba(255,255,255,0), blue); /*Safari 5.1-6*/ background: -o-linear-gradient(right,rgba(255,255,255,0), blue); /*Opera 11.1-12*/ background: -moz-linear-gradient(right,rgba(255,255,255,0), blue); /*Fx 3.6-15*/ background: linear-gradient(to right, rgba(255,255,255,0), blue); /*Standard*/ } .green { background: green; } .green-fade { background: -webkit-linear-gradient(left,rgba(255,255,255,0), green); /*Safari 5.1-6*/ background: -o-linear-gradient(right,rgba(255,255,255,0), green); /*Opera 11.1-12*/ background: -moz-linear-gradient(right,rgba(255,255,255,0), green); /*Fx 3.6-15*/ background: linear-gradient(to right, rgba(255,255,255,0), green); /*Standard*/ } .gray-red-fade { background: -webkit-linear-gradient(gray, red); /*Safari 5.1-6*/ background: -o-linear-gradient(gray, red); /*Opera 11.1-12*/ background: -moz-linear-gradient( gray, red); /*Fx 3.6-15*/ background: linear-gradient( gray, red); /*Standard*/ } .red-blue-fade { background: -webkit-linear-gradient( red, blue); /*Safari 5.1-6*/ background: -o-linear-gradient( red, blue); /*Opera 11.1-12*/ background: -moz-linear-gradient( red, blue); /*Fx 3.6-15*/ background: linear-gradient( red, blue); /*Standard*/ } .white { background: white; } .full-circle { width: 50px; height: 50px; -moz-border-radius: 25px; -webkit-border-radius: 25px; border-radius: 25px; } .mid-circle { width: 25px; height: 25px; -moz-border-radius: 12.5px; -webkit-border-radius: 12.5px; border-radius: 12.5px; } .vertical-center { position: relative; top: 50%; -webkit-transform: translateY(-50%); -ms-transform: translateY(-50%); transform: translateY(-50%); } div{ position: relative; font-family: KeepCalm; font-size: 92.5%; } .ruler-rectangle { width: 100%; height: 2px; margin-bottom:100px; } .rectangle { width: 12.5px; height: calc(100% + 20px); -webkit-transform: translateY(-10px); -ms-transform: translateY(-10px); transform: translateY(-10px); position: absolute; margin-left: auto; margin-right: auto; left: 0; right: 0; top:0px; z-index: -1; } .dotted-rectangle { width: 0px; border-right: 12.5px dotted; height: calc(100% + 20px); -webkit-transform: translateY(-10px); -ms-transform: translateY(-10px); transform: translateY(-10px); position: absolute; margin-left: auto; margin-right: auto; left: 0; right: 0; top:0px; z-index: -1; } .right-line { left: 25px; } .left-line { right: 25px; } .text { padding: 5px; padding-left: 10px; } .ruler-rotated { -ms-transform: translateY(-5px) translateX(25px) rotate(45deg); -webkit-transform: translateY(-5px) translateX(25px) rotate(45deg); transform: translateY(-5px) translateX(25px) rotate(45deg); } .rotated { -ms-transform: translateY(95px) translateX(15px) rotate(45deg); -webkit-transform: translateY(95px) translateX(15px) rotate(45deg); transform: translateY(95px) translateX(15px) rotate(45deg); width: calc(50% + 40px); padding: 5px; } .rotated-up { -ms-transform: translateY(-95px) translateX(-210px) rotate(45deg); -webkit-transform: translateY(-95px) translateX(-210px) rotate(45deg); transform: translateY(-90px) translateX(-205px) rotate(45deg); padding-left: 0px; width: calc(50% + 40px); } .rotated-junction { -ms-transform: translateY(85px) translateX(20px) rotate(45deg); -webkit-transform: translateY(85px) translateX(20px) rotate(45deg); transform: translateY(85px) translateX(20px) rotate(45deg); width: calc(50% + 40px); } .rotated-left { -ms-transform: translateY(85px) translateX(-40%) rotate(-45deg); -webkit-transform: translateY(85px) translateX(-40%) rotate(-45deg); transform: translateY(85px) translateX(-40%) rotate(-45deg); height: 12.5px; width: calc(1.414 * 50%); z-index: -2; } .rotated-left-up-solid { -ms-transform: translateY(-100px) translateX(-40%) rotate(45deg); -webkit-transform: translateY(-100px) translateX(-40%) rotate(45deg); transform: translateY(-100px) translateX(-40%) rotate(45deg); height: 12.5px; width: calc(1.414 * 50%); z-index: -2; } .rotated-right { -ms-transform: translateY(85px) translateX(40%) rotate(45deg); -webkit-transform: translateY(85px) translateX(40%) rotate(45deg); transform: translateY(85px) translateX(40%) rotate(45deg); height: 12.5px; width: calc(1.414 * 50%); z-index: -2; } .rotated-left-up { -ms-transform: translateY(-65px) translateX(-39%) rotate(45deg); -webkit-transform: translateY(-65px) translateX(-39%) rotate(45deg); transform: translateY(-65px) translateX(-39%) rotate(45deg); height: 12.5px; width: calc(50%); z-index: -2; } .rotated-left-down { -ms-transform: translateY(50px) translateX(-39%) rotate(-45deg); -webkit-transform: translateY(50px) translateX(-39%) rotate(-45deg); transform: translateY(50px) translateX(-39%) rotate(-45deg); height: 12.5px; width: calc(50%); z-index: -2; } .rotated-right-up { -ms-transform: translateY(-115px) translateX(39%) rotate(135deg); -webkit-transform: translateY(-115px) translateX(39%) rotate(135deg); transform: translateY(-115px) translateX(39%) rotate(135deg); height: 12.5px; width: calc(50%); z-index: -2; } .rotated-right-down { -ms-transform: translateY(50px) translateX(39%) rotate(225deg); -webkit-transform: translateY(50px) translateX(39%) rotate(225deg); transform: translateY(50px) translateX(39%) rotate(225deg); height: 12.5px; width: calc(50%); z-index: -2; } </style></head><body><div class='body center'>")
f.write("<div class='ruler'>")
line_count = 0

for i in range(0,3):
    central_line.append("-")

with open(sys.argv[1], 'r+') as r:
    lines = r.readlines()
    i = 0
    while i<len(lines):
        line = lines[i]
        if line[0] == '#':
            line_count+=1
            if line_count == 1:
                f.write("</div>")
                f.write("<div class='all-lines center content'><div class='left line major-left-line'>")
            elif line_count == 2:
                f.write("</div>")
                f.write("<div class='right line major-right-line'>")
                for j in range(0,3):
                    central_line[j] = "-"
            elif line_count == 3:
                f.write("</div>")
                f.write("<div class='center line' id='central-line'>")
                for j in range(0,3):
                    central_line[j] = "-"    
        elif line[0] == '>' or line[0] == '<':
            drawJunction(line, f)
        elif line[0] == '\"':
            try:
                createDescription(line.split('\"')[1], lines[i+1][0]=='>' or lines[i+2][0]=='>' or lines[i+3][0]=='>' or lines[i+4][0]=='>', f)
            except:
                createDescription(line.split('\"')[1], 0, f)
            if lines[i+1][0] == '<' and len(lines[i+1].split(":")) > 2 and lines[i+1].split(":")[2] == 'up\n':
                drawJunction(lines[i+1], f)
                i+=1
            createStation(line, f)
        else:
            if line_count == 0:
                try:
                    createRuler(line, f)
                except:
                    error("Syntax for timeline bounds - [Beginning Year]:[End Year (can be decimal)]")
            else:
                drawLine(line, f)
        i+=1

f.write("</div></div></div>")
f.write("</body></html>")
f.close()
print "Done..."
