import json
import turtle
import urllib.request
import time
url= 'http://api.open-notify.org/astros.json' 
response=urllib.request.urlopen(url)
result=json.loads(response.read())
people=result['people']
print('people in Space :',result['number'])
people =result['people']
for p in people:
    print(p['name']+" in "+p['craft'])
url='http://api.open-notify.org/iss-now.json'
response=urllib.request.urlopen(url)
result=json.loads(response.read())
location=result['iss_position']
lat=location['latitude']
lon=location['longitude']
print("longitude is : ",lon)
print("latitude is : ",lat)
screen=turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.jpg')
screen.register_shape('iss.png')
iss=turtle.Turtle()
#lat=29.05502
#lon=-100.097
iss.shape('iss.png')
iss.setheading(90)
iss.penup()
iss.goto(lon,lat)
#lat=29.55502
#lon=-95.097
location=turtle.Turtle()
location.penup()
location.color('red')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()
url=' http://api.open-notify.org/iss-pass.json'
url=url+'?lat='+str(lat)+'&lon='+str(lon)
response=urllib.request.urlopen(url)
result=json.loads(response.read())
over=result['response'][1]['risetime']
print(over)
style=('Arial',6,'bold')
location.write(time.ctime(over),font=style)