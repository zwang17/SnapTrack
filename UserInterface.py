import os
import pygame
from ImageReader import imageReader, NutritionReader

class PygameGame(object):
    daily_progress_test = {'Vitamin C': 33, 'Iron': 24, 'Total Carbohydrate': 25, 'Total Fat': 38, 'Sugars': 20,
                           'Vitamin D': 54, 'Calcium': 30, 'Calories': 44, 'Sodium': 42, 'Saturated Fat': 34,
                           'Cholesterol': 14,
                           'Vitamin B': 3, 'Protein': 36, 'Vitamin A': 8, 'Vitamin E': 10}
    records_test = {'Vitamin C': 89, 'Iron': 88, 'Total Carbohydrate': 105, 'Total Fat': 99, 'Sugars': 110,
                           'Vitamin D': 87, 'Calcium': 70, 'Calories': 115, 'Sodium': 90, 'Saturated Fat': 80,
                           'Cholesterol': 70,
                           'Vitamin B': 43, 'Protein': 78, 'Vitamin A': 32, 'Vitamin E': 10}
    setpercentage = {'Calories': 100, 'Calories from Fat': 100, 'Total Fat': 100, 'Saturated Fat': 100, 'Cholesterol': 100, \
                 'Sodium': 100, 'Total Carbohydrate': 100, 'Sugars': 100, 'Protein': 100, 'Calcium': 100, 'Iron': 100, \
                 'Vitamin A': 100, 'Vitamin B': 100, 'Vitamin C': 100, 'Vitamin D': 100, 'Vitamin E': 100
                 }
    for elements  in setpercentage:
        setpercentage[elements] = 50
    standardcriterion = {'Calories': 2000, 'Calories from Fat': 290, 'Total Fat': 60, 'Saturated Fat': 20, 'Cholesterol': 300, \
                 'Sodium': 2400, 'Total Carbohydrate': 300, 'Sugars': 90, 'Protein': 50, 'Calcium': 1000, 'Iron': 18, \
                 'Vitamin A': 600, 'Vitamin B': 1000, 'Vitamin C': 75000, 'Vitamin D': 125, 'Vitamin E': 22058
                 }
    criterion = {'Calories': 2000, 'Calories from Fat': 290, 'Total Fat': 60, 'Saturated Fat': 20, 'Cholesterol': 300, \
                 'Sodium': 2400, 'Total Carbohydrate': 300, 'Sugars': 90, 'Protein': 50, 'Calcium': 1000, 'Iron': 18, \
                 'Vitamin A': 600, 'Vitamin B': 1000, 'Vitamin C': 75000, 'Vitamin D': 125, 'Vitamin E': 22058
                 }
    copy_criterion = {'Calories': 2000, 'Calories from Fat': 290, 'Total Fat': 60, 'Saturated Fat': 20, 'Cholesterol': 300, \
                 'Sodium': 2400, 'Total Carbohydrate': 300, 'Sugars': 90, 'Protein': 50, 'Calcium': 1000, 'Iron': 18, \
                 'Vitamin A': 600, 'Vitamin B': 1000, 'Vitamin C': 75000, 'Vitamin D': 125, 'Vitamin E': 22058
                 }

    Unit_Dict = {'Calories':'kcal','Calories from Fat': 'kJ','Total Fat': 'g','Saturated Fat': 'g','Cholesterol':'mg',\
                 'Sodium':'mg','Total Carbohydrate': 'g','Sugars':'g','Protein': 'g','Calcium':'mg','Iron':'mg',\
                 'Vitamin A':'mcg','Vitamin B':'mcg','Vitamin C':'mcg','Vitamin D':'mcg','Vitamin E':'mcg'
                }

    # Helpers
    # Init functions
    def initColor(self):
        self.white = (255,255,255)

        self.lightBlue = self.hex_to_rgb("#d7f7fd")
        self.blue = (69,160,217)
        self.fbBlue = self.hex_to_rgb("#3b5998")
        self.deepBlue= (68,118,192)
        self.darkBlue  = (51,87,117)

        self.green = self.hex_to_rgb("#44ab29")
        self.deepGreen = self.hex_to_rgb("#35830a")
        self.red = self.hex_to_rgb("#df1a06")
        self.darkRed = self.hex_to_rgb("#941a06")

        self.blueGray = self.hex_to_rgb("#343f51")
        self.deepBlueGray = self.hex_to_rgb("#2e3242")
        self.darkBlueGray = self.hex_to_rgb("#1b2331")

        self.extrGrey = (238,238,238)
        self.lightGrey = (112,112,101)
        self.grey = self.hex_to_rgb("#58584b")
        self.darkGrey = self.hex_to_rgb("#494949")
        self.deepGrey = self.hex_to_rgb("373737")

        self.orange = self.hex_to_rgb("#ff8700")
        self.darkOrange = self.hex_to_rgb("#dd6f0b")
        self.deepOrange = self.hex_to_rgb("#c16112")

        self.searchFontTable = self.deepBlueGray
        self.searchFontFood = self.deepBlueGray

    def getActualValue(self,nutrition,percent):
        return PygameGame.criterion[nutrition]*percent/100

    def within(self,left,right,down,up,x,y):
        return left < x < right and down < y < up

    def hex_to_rgb(self,value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def initStartButtons(self):
        self.btnWidth = 180
        self.btnHeight = 40
        first_button_height = 150
        self.HomeBtnSurface = [0,first_button_height,self.btnWidth,first_button_height+self.btnHeight,self.darkBlueGray]
        self.SearchBtnSurface = [0,first_button_height+40,self.btnWidth,first_button_height+40+self.btnHeight,self.blueGray]
        self.IdentifyBtnSurface = [0,first_button_height+80,self.btnWidth,first_button_height+80+self.btnHeight,self.blueGray]
        self.DailyProgressBtnSurface = [0,first_button_height+120,self.btnWidth,first_button_height+120+self.btnHeight,self.blueGray]
        self.RecordsBtnSurface = [0,first_button_height+160,self.btnWidth,first_button_height+160+self.btnHeight,self.blueGray]
        self.SettingBtnSurface = [0,first_button_height+200,self.btnWidth,first_button_height+200+self.btnHeight,self.blueGray]

    def initHomeButtons(self):
        self.btnWidthHome = 230
        self.btnHeightHome = 40
        self.interval = 20
        first_button_y = 265
        first_button_x = 430
        self.instructionBtn = [first_button_x,first_button_y, first_button_x+self.btnWidthHome ,first_button_y+self.btnHeightHome,self.darkBlueGray]
        self.logOutBtn = [first_button_x,first_button_y+self.interval+self.btnHeightHome, first_button_x+self.btnWidthHome ,first_button_y+self.interval+self.btnHeightHome*2,self.grey]
        self.shareBtn = [first_button_x,first_button_y+self.interval*2+self.btnHeightHome*2, first_button_x+self.btnWidthHome,first_button_y+self.interval*2+self.btnHeightHome*3,self.fbBlue]
        self.googleBtn = [first_button_x,first_button_y+self.interval*3+self.btnHeightHome*3, first_button_x+self.btnWidthHome,first_button_y+self.interval*3+self.btnHeightHome*4,self.red]


    def loadFont(self):
        self.myFont = pygame.font.Font(os.path.join("font", "anke.regular.ttf"), int(25 / 2))
        self.myFont25 = pygame.font.Font(os.path.join("font", "anke.regular.ttf"), 25)
        self.myFont20 = pygame.font.Font(os.path.join("font", "anke.regular.ttf"), 20)

    #########################
### Main Framework ######
#########################

    def init(self):
        self.mode = "Home"
        self.recordMode = 0
        self.initColor()
        self.initStartButtons()
        self.initHomeButtons()
        self.path = None
        self.returnFoodInfo = False
        self.returnNutritionFact = False
        self.temp_dict = {}

        self.btnWidth2 =120
        self.btnHeight2 = 55   
        self.calendarColor=[]
        for row in range(5): self.calendarColor += [[0]*7]

        self.btnWidth3 = 460
        self.btnHeight3 = 85

        self.proceed = True
        self.notProceed = True

#### Back Button #####
        self.BackBtnSurface = [80,60,40+self.btnWidth2,40+self.btnHeight2,self.lightGrey]
#### Upload Buttons
        self.UploadTableBtn = [550-self.btnWidth3/2,170,550+self.btnWidth3/2,170+self.btnHeight3,self.white]
        self.UploadFoodBtn = [550-self.btnWidth3/2,320,550+self.btnWidth3/2,320+self.btnHeight3,self.white]

        self.EatBtn = [self.btnWidth+(900-self.btnWidth)/2-100/2,520,100,50,self.orange]

        self.btnLst = [
        self.HomeBtnSurface,
        self.IdentifyBtnSurface,
        self.SearchBtnSurface,
        self.DailyProgressBtnSurface,
        self.RecordsBtnSurface,
        self.SettingBtnSurface]

        self.modeLst = ['Home','Identify','Search','Daily Progress','Records','Setting']
        self.iconPathLst = ['Home.png','Identify.png','Search.png','Daily Progress.png','Records.png','Setting.png']
        self.neuList = ['Calories','Total Fat','Saturated Fat','Cholesterol',\
                     'Sodium','Total Carbohydrate','Sugars','Protein','Calcium','Iron',\
                     'Vitamin A','Vitamin B','Vitamin C','Vitamin D','Vitamin E']

        self.week = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

        self.label = None
        self.barLst = []
        self.temp_barLst = []
        self.history_barLst = []
        self.loadIcon()
        self.loadProfile()
        self.loadLogo()
        self.loadFont()
        self.loadShareLogo()

#### MousePressed ####
    def mousePressedMainBar(self, x, y):
        for button in self.btnLst:
            if self.within(button[0],button[2],button[1],button[3],x,y):
                button[4] = self.darkBlueGray

    def mousePressedRecords(self,x,y):
        if self.mode == "Records":
            if self.recordMode != 11:
                for i in range(5):
                    for j in range(7):
                        if self.within(250 + j *70+50,  310 + j *70+50, 130 + i * 70+30,190 + i * 70+30,x,y):
                            self.recordMode = i * 7 + (j - 2)
            else:
                if not(self.within(280+50, 700+50,100+30 ,450+30,x,y)):
                    self.recordMode = 0
                    self.history_barLst = []


    def mousePressed(self,x,y):
        self.mousePressedMainBar(x,y)
        self.mousePressedRecords(x,y)

#### Open File Browser ####
    def open_file_browser(self):
        pygame.mixer.init()  # initializing the mixer

        import tkinter
        from tkinter import filedialog

        root = tkinter.Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        return root.filename

#### MouseReleased ####
    def mouseReleasedMainBar(self, x, y):
        for index in range(len(self.btnLst)):
            surface = self.btnLst[index]
            if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
                surface[4] = self.darkBlueGray
                self.mode = self.modeLst[index]
        self.mouseMotionMainBar(x,y)

    def mouseReleasedIdentify(self,x,y):
        if self.mode == "Identify":
            surface = self.EatBtn
            if self.within(surface[0], surface[0] + surface[2], surface[1], surface[1] + surface[3], x, y):
                for nutrition in self.temp_dict:
                    if nutrition in self.daily_progress_test:
                        self.daily_progress_test[nutrition] += self.temp_dict[nutrition]
                self.proceed = True
                self.temp_barLst = []
                self.mode = "Daily Progress"
                self.DailyProgressBtnSurface[4] = self.darkBlueGray

    def mouseReleasedSearch(self,x,y):
        if self.mode == "Search":
            surface = self.UploadFoodBtn
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                self.temp_barLst = []
                surface[4] = self.lightGrey
                self.path = self.open_file_browser()
                if self.path != "":
                    self.mode = "Identify"
                    self.returnFoodInfo = True
                    self.returnNutritionFact = False
                self.IdentifyBtnSurface[4] = self.deepBlueGray
            surface = self.UploadTableBtn
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                self.temp_barLst = []
                surface[4] = self.lightGrey
                self.path = self.open_file_browser()
                if self.path != "":
                    self.mode = "Identify"
                    self.returnFoodinfo = False
                    self.returnNutritionFact = True
                self.IdentifyBtnSurface[4] = self.deepBlueGray
    def mouseReleasedRecord(self,x,y):
        if self.mode == "Records":
            self.calendarColor = []
            for row in range(5): self.calendarColor += [[0]*7]

    def mouseReleasedSetting(self,x,y):
        if self.mode == 'Setting':
            pass

    def mouseReleased(self,x,y):
        self.mouseReleasedMainBar(x,y)
        self.mouseReleasedSearch(x,y)
        self.mouseReleasedIdentify(x,y)
        self.mouseReleasedRecord(x,y)
        self.mouseReleasedSetting(x,y)

#### MouseMotion ####
    def mouseMotionMainBar(self,x,y):
        for index in range(len(self.btnLst)):
            if self.within(self.btnLst[index][0], self.btnLst[index][2], self.btnLst[index][1], self.btnLst[index][3], x, y)\
                     and self.mode != self.modeLst[index]:
                self.btnLst[index][4] = self.deepBlueGray
            elif self.mode != self.modeLst[index]: self.btnLst[index][4] = self.blueGray

    def mouseMotionHome(self,x,y):
        if self.mode == "Home":
            surface = self.instructionBtn
            if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
                surface[4] = self.darkBlueGray
            else: surface[4] = self.blueGray

            surface = self.logOutBtn
            if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
                surface[4] = self.darkGrey
            else: surface[4] = self.grey

            surface = self.logOutBtn
            if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
                surface[4] = self.deepGrey
            else: surface[4] = self.grey

            surface = self.googleBtn
            if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
                surface[4] = self.darkRed
            else: surface[4] = self.red

            surface = self.shareBtn
            if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
                surface[4] = self.blueGray
            else: surface[4] = self.fbBlue

    def mouseMotionSearch(self,x,y):
        if self.mode == "Search":
            surface = self.UploadTableBtn
            if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
                surface[4] = self.deepBlueGray
                self.searchFontTable = self.white
            else:
                surface[4] = self.white
                self.searchFontTable = self.deepBlueGray


        surface = self.UploadFoodBtn
        if self.within(surface[0], surface[2], surface[1], surface[3], x, y):
            surface[4] = self.deepBlueGray
            self.searchFontFood = self.white

        else:
            surface[4] = self.white
            self.searchFontFood = self.deepBlueGray

    def mouseMotionIdentify(self,x,y):
        if self.mode == "Identify":
            surface = self.EatBtn
            if self.within(surface[0], surface[0]+surface[2], surface[1], surface[1]+surface[3], x, y):
                surface[4] = self.darkOrange
            else:
                surface[4] = self.orange
            detect = False
            for i in range(15):
                if  215 + 90 * (i % 8) <= x <= 215 + 90 * (i % 8) + 25 and 250 + (i // 8) * 220 >= y >= 250 + (i // 8) * 220 - 160:
                    self.label = (x,y,i)
                    detect = True
            if not detect:
                self.label = None

    def mouseMotionRecord(self,x,y):
        if self.mode == "Records":
            if self.recordMode != 11:
                for i in range(5):
                    for j in range(7):
                        if self.within(250 + j *70+50,  310 + j *70+50, 130 + i * 70+30,190 + i * 70+30,x,y):
                            self.calendarColor[i][j] = 1
                        else:
                            self.calendarColor[i][j] = 0
            else:
                detect = False
                for i in range(15):
                    #10,140,330+30*i,480
                    if 330 + 30 * i <= x <= 330+30*i + 10 and 480-140 - 50 <= y <= 480 + 50:
                        detect = True
                        self.label = (x, y, i)
                if not(detect):
                    self.label = None

    def mouseMotionDailyProgress(self,x,y):
        if self.mode == 'Daily Progress':
            detect = False
            for i in range(15):
                if  215 + 90 * (i % 8) <= x <= 215 + 90 * (i % 8) + 25 and 250 + (i // 8) * 220 >= y >= 250 + (i // 8) * 220 - 160:
                    self.label = (x,y,i)
                    detect = True
            if not detect:
                self.label = None

    def mouseMotionSetting(self,x,y):
        if self.mode == 'Setting':
            detect = False
            for i in range(15):
                #350, 70+ i* 35, 400 ,20
                if 350 <= x <= 700 and 70+ i* 35 <= y <= 85+ i* 35:
                    detect = True
            if detect == False:
                self.label = None    

    def mouseMotion(self, x, y):
        self.mouseMotionMainBar(x,y)
        self.mouseMotionHome(x,y)
        self.mouseMotionIdentify(x,y)
        self.mouseMotionSearch(x,y)
        self.mouseMotionRecord(x,y)
        self.mouseMotionDailyProgress(x,y)
        self.mouseMotionSetting(x,y)

    def recalculate(self):
        for nutrition in self.daily_progress_test:
            self.daily_progress_test[nutrition] = self.daily_progress_test[nutrition] * self.copy_criterion[nutrition] / self.criterion[nutrition]
            self.copy_criterion[nutrition] = self.criterion[nutrition]

    def mouseDrag(self, x, y):
        if self.mode == "Setting":
            self.recalculate()
            self.barLst = []
            self.proceed = True
            detect = False
            for i in range(15):
                #350, 70+ i* 35, 400 ,20
                if 350 <= x <= 700 and 70+ i* 35 <= y <= 85+ i* 35:
                    detect = True
                    name = self.neuList[i]
                    self.setpercentage[name] = int((x-350) / 3.5)
                    self.label = (x,y,i)
            for elements in self.criterion:
                if self.setpercentage[elements]!= 0:
                    self.criterion[elements] = self.standardcriterion[elements]/50 * self.setpercentage[elements]
                else: self.criterion[elements] = 1
            if detect == False:
                self.label = None

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

#### timerFried ####
    def timerFiredDailyProgress(self):
        if self.mode == "Daily Progress":
            for bar in self.barLst:
                bar.increment_height()

    def timerFiredIdentify(self):
        if self.mode == "Identify":
            for bar in self.temp_barLst:
                bar.increment_height()

    def timerFiredRecords(self):
        if self.mode == "Records":
            for bar in self.history_barLst:
                bar.increment_height()

    def timerFiredSetting(self):
        if self.mode == 'Setting':
            pass

    def timerFired(self, dt):
        self.timerFiredDailyProgress()
        self.timerFiredIdentify()
        self.timerFiredRecords()
        self.timerFiredSetting()

    def drawButton(self,screen,color, fontColor, a, b, c, d, text,fontNum, width = 0):
        pygame.draw.rect(screen, color, (a,b,c,d), width)
        os.path.exists(os.path.join("font", "anke.regular.ttf"))
        myFont = pygame.font.Font(os.path.join("font","anke.regular.ttf"), fontNum)
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.midleft = (a + c/3, b + d/2)
        screen.blit(textSurface, textRect1)

    def drawHomeButton(self,screen,color, fontColor, a, b, c, d, text,fontNum, width = 0):
        pygame.draw.rect(screen, color, (a,b,c,d), width)
        os.path.exists(os.path.join("font", "anke.regular.ttf"))
        myFont = pygame.font.Font(os.path.join("font","anke.regular.ttf"), fontNum)
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c/1.7, b + d/2)
        screen.blit(textSurface, textRect1)

    def drawHomeButtonCenter(self,screen,color, fontColor, a, b, c, d, text,fontNum, width = 0):
        pygame.draw.rect(screen, color, (a,b,c,d), width)
        os.path.exists(os.path.join("font", "anke.regular.ttf"))
        myFont = pygame.font.Font(os.path.join("font","anke.regular.ttf"), fontNum)
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c/2, b + d/2)
        screen.blit(textSurface, textRect1)

    def drawSearchButton(self,screen,color, fontColor, a, b, c, d, text):
        
        pygame.draw.rect(screen,(250,250,250),(a-7,b-7,c+14,d+14))
        pygame.draw.rect(screen,(240,240,240),(a-6,b-6,c+12,d+12))

        pygame.draw.rect(screen,(230,230,230),(a-5,b-5,c+10,d+10))

        pygame.draw.rect(screen,(210,210,210),(a-4,b-4,c+8,d+8))
        pygame.draw.rect(screen,(190,190,190),(a-3,b-3,c+6,d+6))
        pygame.draw.rect(screen,(170,170,170),(a-2,b-2,c+4,d+4))
        pygame.draw.rect(screen,(160,160,160),(a-1,b-1,c+2,d+2))

        pygame.draw.rect(screen, color, (a,b,c,d))
        textSurface = self.myFont25.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c / 2, b + d / 2)
        screen.blit(textSurface, textRect1)

    def drawEatButton(self,screen):
        surface = self.EatBtn
        pygame.draw.rect(screen, surface[4], (surface[0],surface[1],surface[2],surface[3]), 0)
        textSurface = self.myFont20.render("EAT", True, self.white)
        textRect1 = textSurface.get_rect()
        textRect1.center = (surface[0]+surface[2]/2,surface[1]+surface[3]/2)
        screen.blit(textSurface, textRect1)

    def drawCalendarButton(self,screen,color, fontColor, a, b, c, d, text,fontNum, width = 0):
        pygame.draw.rect(screen, color, (a,b,c,d), width)
        os.path.exists(os.path.join("font", "anke.regular.ttf"))
        myFont = pygame.font.Font(os.path.join("font","anke.regular.ttf"), fontNum)
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c/2, b + d/2)
        screen.blit(textSurface, textRect1)

    def makeABar(self,width,height,x,y,percent,name=None):
        from Shape import Bar as Bar
        self.barLst.append(Bar(width,height,self.blue,self.lightBlue,x,y,0,percent,self.darkBlue,self.red,dynamic=True,name=name,font=self.myFont))

    def makeHistoryBar(self,width,height,x,y,percent):
        from Shape import Bar as Bar
        self.history_barLst.append(Bar(width,height,self.blue,self.lightBlue,x,y,0,percent,self.darkBlue,self.red,dynamic=True))

    def makeTempBar(self,width,height,x,y,percent,already_percent,name=None):
        from Shape import Bar as Bar
        self.temp_barLst.append(Bar(width,height,self.blue,self.lightBlue,x,y,percent,already_percent,self.darkBlue,self.red,dynamic=True,name=name,font=self.myFont))

    def drawHistoryBars(self,screen):
        for bar in self.history_barLst:
            bar.drawBar(screen=screen)

    def drawBars(self,screen):
        for bar in self.barLst:
            bar.drawBar(screen=screen)

    def drawTempBars(self, screen):
        for bar in self.temp_barLst:
            bar.drawBar(screen=screen)

    def drawMainBar(self,screen,color,width,height):
        pygame.draw.rect(screen,color,(0,0,width,height), 0)

    def drawIcon(self,screen,icon,x,y):
        screen.blit(icon,(x,y))

    def drawProfile(self,screen,profile):
        screen.blit(profile, (11, -10))
        myFont = pygame.font.Font(os.path.join("font","anke.regular.ttf"), 12)
        textSurface = myFont.render("Hello, Andrew!", True, self.extrGrey)
        textRect1 = textSurface.get_rect()
        textRect1.midleft = (48,130)
        screen.blit(textSurface, textRect1)

    def drawLogo(self,screen,logo):
        screen.blit(logo,(65,-170))
    def loadIcon(self):
        self.iconLst = []
        for path in range(len(self.iconPathLst)):
            icon_home = pygame.image.load(os.path.join('icon', self.iconPathLst[path]))
            icon_home = pygame.transform.scale(icon_home, (40, 40))
            self.iconLst.append(icon_home)

    def loadProfile(self):
        profile = pygame.image.load(os.path.join("icon", 'andrew_Carnegie.png'))
        profile = pygame.transform.scale(profile, (16 * 10, 15 * 10))
        self.profile = profile

    def loadLogo(self):
        logo = pygame.image.load(os.path.join("icon", 'logo.png'))
        logo = pygame.transform.scale(logo, (int(500 * 1.7), int(337 * 1.7)))
        self.logo = logo

    def loadShareLogo(self):
        fb = pygame.image.load(os.path.join("icon", 'fb.png'))
        fb = pygame.transform.scale(fb, (40, 40))
        self.fb = fb

        google = pygame.image.load(os.path.join("icon", 'google.png'))
        google = pygame.transform.scale(google, (40, 40))
        self.google = google


    #### redraw ####
    def redrawMainBar(self, screen):
        self.drawMainBar(screen, self.blueGray, self.btnWidth, 600)
        pygame.draw.line(screen,self.darkBlueGray,(20,146),(179-20,146),1)
        pygame.draw.line(screen,self.darkBlueGray,(20,148+245),(179-20,148+245),1)

        self.drawProfile(screen,self.profile)
        textLst = ['Home','Identify','Search','Daily Progress','Records','Setting']
        for i in range(len(self.btnLst)):
            button = self.btnLst[i]
            self.drawButton(screen,button[4], self.white, button[0], button[1],self.btnWidth,self.btnHeight, textLst[i],15)
            self.drawIcon(screen,self.iconLst[i],button[0]+self.btnWidth/15,button[1])

    def redrawHome(self, screen):
        if self.mode == "Home":
            self.drawLogo(screen,self.logo)
            button = self.instructionBtn 
            self.drawHomeButtonCenter(screen,button[4], self.white, button[0], button[1],self.btnWidthHome,self.btnHeightHome,"Instruction",15)
            button = self.shareBtn
            self.drawHomeButton(screen,button[4], self.white, button[0], button[1],self.btnWidthHome,self.btnHeightHome,"Share on Facebook",15)
            self.drawIcon(screen,self.fb,button[0]+self.btnWidth/30,button[1])

            button = self.logOutBtn
            self.drawHomeButtonCenter(screen,button[4], self.white, button[0], button[1],self.btnWidthHome,self.btnHeightHome,"Log out",15)
            button = self.googleBtn
            self.drawHomeButton(screen,button[4], self.white, button[0], button[1],self.btnWidthHome,self.btnHeightHome,"Share on Google+",15)
            self.drawIcon(screen,self.google,button[0]+self.btnWidth/15,button[1])

            textSurface = self.myFont25.render("by Team Temy", True, self.deepBlueGray)
            textRect1 = textSurface.get_rect()
            textRect1.center = (545,530)
            screen.blit(textSurface, textRect1)


    def getNutritionFact(self,path):
        return NutritionReader(path)

    def getFoodInfo(self,path):
        return imageReader(path)

    def getResultDictionary(self):
        if self.returnFoodInfo == True:
            self.notProceed = False
            return self.getFoodInfo(self.path)
        elif self.returnNutritionFact == True:
            self.notProceed = False
            return self.getNutritionFact(self.path)

    def drawFoodName(self,screen):
        textSurface = self.myFont25.render("Identification result: "+self.food_name.upper(), True, self.orange)
        textRect1 = textSurface.get_rect()
        textRect1.center = (540, 50)
        screen.blit(textSurface, textRect1)

    def redrawIdentify(self, screen):
        if self.mode == "Identify":
            result = self.getResultDictionary()
            if self.notProceed == False:
                self.returnFoodInfo = self.returnNutritionFact = False
                food_name = ""
                if isinstance(result,tuple):
                    food_name = result[0]
                    result = result[1]
                print(result)
                print(food_name)
                self.temp_dict = result
                self.food_name = food_name
                i = 0
                for nutrition in self.neuList:
                    if nutrition in self.temp_dict:
                        self.makeTempBar(25, 160, 215 + 90 * (i % 8), 250 + (i // 8) * 220,self.temp_dict[nutrition],already_percent=int(self.daily_progress_test[nutrition]),name=nutrition)
                        i += 1
                self.notProceed = True
            if len(self.temp_barLst) > 0:
                self.drawTempBars(screen)
                if self.food_name != "":
                    self.drawFoodName(screen)

            if len(self.temp_barLst) != 0:
                self.drawEatButton(screen)

            if self.label != None and self.temp_dict != {}:
                x, y, i = self.label
                name = self.neuList[i]
                if name in self.temp_dict:
                    percentage = self.temp_dict[name]
                    value = percentage * self.criterion[name] / 100
                    str1 = "Expected increment: " + str(value) + self.Unit_Dict[name]
                    str2 = "Percentage: " + str(percentage) + "%"
                    self.drawCalendarButton(screen, self.white, self.blueGray, x - 60, y-40, 120, 20, str1, 13)
                    self.drawCalendarButton(screen, self.white, self.blueGray, x - 60, y-20, 120, 20, str2, 13)


    def redrawSearch(self, screen):
        if self.mode == "Search":
            button = self.UploadTableBtn
            self.drawSearchButton(screen,button[4], self.searchFontTable, button[0], button[1],self.btnWidth3,self.btnHeight3, "Upload Nutrition Facts Picture")
            button = self.UploadFoodBtn
            self.drawSearchButton(screen,button[4], self.searchFontFood, button[0], button[1],self.btnWidth3,self.btnHeight3, "Upload Food Picture")

    def redrawDailyProgress(self, screen):
        if self.mode == "Daily Progress":
            textSurface = self.myFont25.render("Daily Progress", True, self.blueGray)
            textRect1 = textSurface.get_rect()
            textRect1.center = (540, 50)
            screen.blit(textSurface, textRect1)

            i = 0
            if self.proceed == True:
                for nutrition in self.neuList:
                    if nutrition in self.daily_progress_test:
                        self.makeABar(25, 160, 215 + 90 * (i%8), 250 + (i//8)*220 , self.daily_progress_test[nutrition],name=nutrition)
                        i += 1
                self.proceed = False
            self.drawBars(screen)

            if self.label != None:
                x, y, i = self.label
                name = self.neuList[i]
                percentage = self.daily_progress_test[name]
                value = percentage * self.criterion[name] / 100
                str1 = "Current Intake: " + str(value) + self.Unit_Dict[name]
                str2 = "Percentage: " + str(percentage) + "%"
                self.drawCalendarButton(screen, self.white, self.blueGray, x - 60, y-40, 120, 20, str1, 13)
                self.drawCalendarButton(screen, self.white, self.blueGray, x - 60, y-20, 120, 20, str2, 13)

    def redrawRecords(self, screen):
        if self.mode == "Records":
            x = 50
            y = 50
            self.drawCalendarButton(screen,self.white, self.blueGray, 250+x, 10+y, 480, 50, "November", 35)
            pygame.draw.polygon(screen,self.blueGray,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
            pygame.draw.polygon(screen,self.blueGray,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
            for i in range(7):
                self.drawCalendarButton(screen, self.white, self.blueGray,250 + i * 70+x, 90+y, 60, 30, self.week[i], 20)

            day = 29
            for i in range(5):
                for j in range(7):
                    if i ==0 and j == 3:
                        day = 1
                    if i == 4 and j == 5:
                        day = 1
                    if self.calendarColor[i][j] == 0 :
                        # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                        self.drawCalendarButton(screen, self.white, self.blueGray, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                    if self.calendarColor[i][j] == 1:
                        #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                        self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                    day = day + 1

            if self.recordMode == 11:
                pygame.draw.rect(screen, self.extrGrey, (250+x, 90+y,480 ,380))
                os.path.exists(os.path.join("font", "anke rg.ttf"))
                myFont = pygame.font.Font(os.path.join("font","anke.regular.ttf"), 30)
                textSurface = myFont.render("Date: Nov." + str(self.recordMode) + 'th', True, self.blueGray)
                textRect1 = textSurface.get_rect()
                textRect1.midleft = (300+x, 150+y)
                screen.blit(textSurface, textRect1)
                #Good

                myFont1 = pygame.font.Font(os.path.join("font", "anke.regular.ttf"), 20)
                textSurface1 = myFont1.render("Condition : " + "Fair", True, self.blueGray)
                textRect2 = textSurface1.get_rect()
                textRect2.midleft = (300+x, 200+y)
                screen.blit(textSurface1, textRect2)

                i = 0
                for nutrition in self.neuList:
                    if nutrition in self.records_test:
                        self.makeHistoryBar(10,140,330+30*i,480,int(self.records_test[nutrition]))
                        i += 1
                self.drawHistoryBars(screen)

                if self.label != None:
                    x, y, i = self.label
                    self.drawCalendarButton(screen, self.white, self.blueGray,x - 60, y - 40, 120, 20, self.neuList[i], 13)
                    self.drawCalendarButton(screen, self.white, self.blueGray,x - 60, y-20, 120, 20, str(self.records_test[self.neuList[i]]) + "%", 13)


    def redrawSetting(self, screen):
        if self.mode == 'Setting':
            for i in range(15):
                name = self.neuList[i]
                self.drawButton(screen, self.white, self.blueGray, 180, 70+ i* 35, 80, 15, name + ":",15)
                pygame.draw.rect(screen, self.blueGray, (350, 70+ i* 35, 350 ,15),4)
                pygame.draw.rect(screen, self.blueGray, (350, 70+ i* 35, 3.5 *self.setpercentage[name] ,15))
                str2 = str(int(self.criterion[name]*10 )/10) + self.Unit_Dict[name]
                self.drawButton(screen, self.white, self.blueGray, 700, 70+ i* 35, 80, 15, str2,15)

            if self.label != None:
                x, y, i = self.label
                name = self.neuList[i]
                str1 = str(self.setpercentage[name] * 2) + "%"
                self.drawCalendarButton(screen,self.white, self.blueGray, x - 10, y - 20, 20, 20, str1, 10)

    def redrawAll(self, screen):
        self.redrawMainBar(screen)
        self.redrawHome(screen)
        self.redrawSearch(screen)
        self.redrawIdentify(screen)
        self.redrawDailyProgress(screen)
        self.redrawRecords(screen)
        self.redrawSetting(screen)


    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=50, title="SnapTrack"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)

        pygame.init()


    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

def main():
    game = PygameGame(900,600)
    game.run()

if __name__ == '__main__':
    main()