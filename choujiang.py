import pygame
import random
import threading
import time
import math
import pandas
import numpy
def resetFile():
    with open('/home/pi/Desktop/haveSelected.txt','w') as f:
        f.write('')

getM=[]

colorr=255
colorg=0
colorb=0
change=[0,0]#the color index,up down
pygame.init()
center=60

positionAll=[[140,300,0,''],[540,300,0,''],[840,300,0,'']]#position size name

sizeAll=[100,100,100]
realPeople=[2,10,20,50]
peopleUsed=[1,5,7,17]
inputLevel=int(input('input level 1 , 2 , 3 , 4'))
if inputLevel==4:
        resetFile()
        #pass

screen=pygame.display.set_mode([740,600])#,pygame.FULLSCREEN)
def showMessage(text,size,colour,p):

    fon=pygame.font.Font('/home/pi/Desktop/SimHei.ttf',int(size))

    sur=fon.render(text,True,colour)

    screen.blit(sur,p)
def changeColor(r,g,b):
    global change
    get=[r,g,b]
    if 255 in get:
        change[0]+=1 if change[1]==0 else -1
        if change[0]>=2:change[1]=1
        elif change[0]<=0:change[1]=0
    get[change[0]]+=0.5
    for i in range(len(get)):
        if get[i]!=0 and i!=change[0]:
            get[i]-=0.5
    return  get[0],get[1],get[2]

def getPeople():
    arr=[]
    for i in range(1,5):
        get=pandas.read_excel('/home/pi/Desktop/sd'+str(i)+'.xls')
        for ii in range(len(get['班级'])):
            if str(get['年级'][ii])!='nan' and str(get['班级'][ii])!='虚拟班级' and str(get['年级'][ii])!='毕业':
                #print(get['班级'][ii])
                arr.append(get['年级'][ii]+get['班级'][ii]+''+(get['学生姓名'][ii]) if get['学生姓名'][ii]!='凯迪丽娜·阿不都艾尼' else'凯迪丽娜')

    return arr
mod=False
def countTime():
        global mod
        mod=False
        time.sleep(3)
        mod=True
def selectpeople():
    #global getGiftPeople

    #getGiftPeople = 'caesar'
    iii=0
    run=True
    thread=threading.Thread(target=countTime)
    thread.start()
    while run:
        if mod==True:
            get=0.00001+(iii**2.1)*0.00000000001
            time.sleep(get)
            iii+=1
            for ii in range(len(positionAll)):
                if get>0.0013 and positionAll[ii][0]==center:
                    for clo in range(len(positionAll)):
                        if clo!=ii:
                            positionAll[clo][3]=''
                    run=False
                    createtextFile(positionAll[ii][3]+'|')
                    people.remove(positionAll[ii][3])
        else:
            time.sleep(0.000001)
        for i in range(len(positionAll)):
            positionAll[i][0]-=1
            if positionAll[i][0]<-340:
                positionAll[i][0]=720
                positionAll[i][3]=people[random.randint(0,len(people)-1)]

            positionAll[i][2]=75-math.pow((positionAll[i][0]-center)**2,1/3.4)



def reduceStudents():
    with open('/home/pi/Desktop/haveSelected.txt','r') as f:
        getTex=f.read()
    peopleArray=getTex.split('|')
    try:
        peopleArray.remove('')
    except:pass
    for i in peopleArray:
        print(i)
        try:
            people.remove(i)
        except:pass


people=getPeople()
reduceStudents()
getGiftPeople=''
img=pygame.image.load('/home/pi/Desktop/抽奖背景.jpg').convert()
img=pygame.transform.scale(img,(740,600))
def mixtri(num):
    get1=num%5
    poA=[]
    for ii in range(int(num/5)+1):
        po1=[]
        for i in range(5 if ii!=int(num/5) else get1):
            po1.append([140*i+20,30*ii+250,''])
        poA.append(po1)
    return poA
def createtextFile(text=''):
    with open('/home/pi/Desktop/haveSelected.txt','r') as f:
        getTex=f.read()
    with open('/home/pi/Desktop/haveSelected.txt','w') as f:
        f.write(getTex+text)


def first():
    while True:

        #colorr,colorg,colorb=changeColor(colorr,colorg,colorb)
        screen.fill((30,30,30))
        screen.blit(img,(0,0))
        #showMessage("托马斯新年晚会抽奖", 70, (colorr, colorg, colorb), [70, 100])
        showMessage(positionAll[0][3], positionAll[0][2], (0, 0, 0), [positionAll[0][0],positionAll[0][1]])
        showMessage(positionAll[1][3], positionAll[1][2], (0, 0, 0), [positionAll[1][0],positionAll[1][1]])
        showMessage(positionAll[2][3], positionAll[2][2], (0, 0, 0), [positionAll[2][0],positionAll[2][1]])
        showMessage("开始抽奖", 50, (225,225,225), [300, 550])
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            #print(pos)
            if event.type==pygame.QUIT:
                pygame.quit()
            if pos[0]>300 and pos[0]<500 and pos[1]>550 and pos[1]<600 and event.type ==pygame.MOUSEBUTTONDOWN:
                #getGiftPeople=people[random.randint(0,len(people)-1)]
                thr=threading.Thread(target=selectpeople)
                thr.start()
            if pos[0]>0 and pos[0]<30 and pos[1]>0 and pos[1]<30 and event.type ==pygame.MOUSEBUTTONDOWN:
                pygame.quit()

        pygame.display.flip()
def other(num,allP):
    getM=mixtri(num)
    start=False
    sunPeople=0
    TypeAppear=0
    while True:

        #colorr,colorg,colorb=changeColor(colorr,colorg,colorb)
        screen.fill((30,30,30))
        screen.blit(img,(0,0))

        for i in getM:
            for ii in i:
                name=people[random.randint(0,len(people)-1)]
                showMessage(ii[2], 15, (0,0,0), [ii[0],ii[1]])
        ###
        if TypeAppear==1 and mod==True:

            if allP-sunPeople<num and allP-sunPeople>0:
                getM=mixtri(allP-sunPeople)
            #getGiftPeople=people[random.randint(0,len(people)-1)]
            nameSum=''
            for i in range(len(getM)):
                for ii in range(len(getM[i])):
                    name=people[random.randint(0,len(people)-1)]
                    getM[i][ii][2]=name
                    people.remove(name)
                    nameSum+=name+'|'
            createtextFile(nameSum)
            sunPeople+=num
            TypeAppear=0
        elif TypeAppear==1:
            for i in range(len(getM)):
                for ii in range(len(getM[i])):
                    name=people[random.randint(0,len(people)-1)]
                    getM[i][ii][2]=name
        ###
        showMessage("开始抽奖", 50, (225,225,225), [300, 550])
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            #print(pos)
            if event.type==pygame.QUIT:
                pygame.quit()
            if pos[0]>300 and pos[0]<500 and pos[1]>550 and pos[1]<600 and event.type ==pygame.MOUSEBUTTONDOWN:
                thread=threading.Thread(target=countTime)
                thread.start()
                TypeAppear=1
            if pos[0]>0 and pos[0]<30 and pos[1]>0 and pos[1]<30 and event.type ==pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        pygame.display.flip()

if inputLevel!=1:

    other(peopleUsed[inputLevel-1],realPeople[inputLevel-1])

elif inputLevel==1:
    first()