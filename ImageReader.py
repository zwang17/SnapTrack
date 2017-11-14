import io
import os


from google.cloud import vision
from google.cloud.vision import types

def imageReader(path):

    def detect_labels(path):
        result = []
        """Detects labels in the file."""
        client = vision.ImageAnnotatorClient()

        file_name = os.path.join(
            os.path.dirname(__file__),
             path)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        for label in labels:
            if label.score > 0.7:
                result.append(label.description)

        return result

    class Food(object):
        Nutrition_Name_Dict = {'Energy':'Calories','Total lipid (fat)':'Total Fat','Fatty acids, total saturated':'Saturated Fat',\
                          'Cholesterol':'Cholesterol','Sodium, Na':'Sodium','Carbohydrate, by difference':'Total Carbohydrate',\
                          'Sugars, total':'Sugars','Protein':'Protein','Calcium, Ca':'Calcium','Iron, Fe':'Iron',\
                          'Vitamin A, RAE':'Vitamin A','Vitamin B-6':'Vitamin B','Vitamin C, total ascorbic acid':'Vitamin C',\
                               'Vitamin D':'Vitamin D','Vitamin E (alpha-tocopherol)':'Vitamin E'}
        Unit_Dict = {'Calories':'kcal','Calories from Fat': 'kJ','Total Fat': 'g','Saturated Fat': 'g','Cholesterol':'mg',\
                     'Sodium':'mg','Total Carbohydrate': 'g','Sugars':'g','Protein': 'g','Calcium':'mg','Iron':'mg',\
                     'Vitamin A':'mcg','Vitamin B':'mcg','Vitamin C':'mcg','Vitamin D':'mcg','Vitamin E':'mcg'
                    }
        def __init__(self,food_name):
            self.food_name = food_name
            self.Value_Dict = {}
            for name in Food.Nutrition_Name_Dict:
                self.Value_Dict[name] = '0'
            self.nutrition_Dict = self.getNutritions()

        def getNutritions(self,with_unit=False):
            criterion = {'Calories':2000,'Calories from Fat': 290,'Total Fat': 60,'Saturated Fat': 20,'Cholesterol':300,\
                 'Sodium':2400,'Total Carbohydrate': 300,'Sugars': 90,'Protein': 50,'Calcium':1000,'Iron':18,\
                 'Vitamin A':600,'Vitamin B':1000,'Vitamin C':75000,'Vitamin D':125,'Vitamin E':22058
                }
            number_dict = self.getNDBNumber(self.food_name)
            num = 0
            for i in number_dict:
                num = number_dict[i]
            report = self.getReport(num)

            result_dict = {'Calories':'0','Calories from Fat': '0','Total Fat': '0','Saturated Fat': '0','Cholesterol':'0',\
                     'Sodium':'0','Total Carbohydrate':'0','Sugars':'0','Protein': '0','Calcium':'0','Iron':'0',\
                     'Vitamin A':'0','Vitamin B':'0','Vitamin C':'0','Vitamin D':'0','Vitamin E':'0'
                    }

            if with_unit:
                for nutrition in report:
                    if nutrition in Food.Nutrition_Name_Dict:
                        result_dict[Food.Nutrition_Name_Dict[nutrition]] = [report[nutrition][0],Food.Unit_Dict[Food.Nutrition_Name_Dict[nutrition]]]
                result_dict['Calories'][0] = str(int(int(result_dict['Calories'][0]) * 0.239))

            else:
                for nutrition in report:
                    if nutrition in Food.Nutrition_Name_Dict:
                        result_dict[Food.Nutrition_Name_Dict[nutrition]] = report[nutrition][0]
                result_dict['Calories'] = str(int(int(result_dict['Calories']) * 0.239))

            for cr in result_dict:
                s = result_dict[cr]
                num = int(eval(s) * 100 / criterion[cr])
                result_dict[cr] = num * 2
            return result_dict

        @staticmethod
        def getNDBNumber(food_name, num_output=1):
            # return a dictionary with food_name as keys and corresponding ndb number as values
            import requests
            url = "https://api.nal.usda.gov/ndb/search/"

            querystring = {"format":"json","q": food_name,"sort":"n","max":str(num_output),"offset":"0",\
                           "api_key":"dCkqkzaw600McBG3V20U8HgiBAEy7NC3Lq8DCQq1","ds":"Standard Reference","sort":"r"}

            headers = {
                'cache-control': "no-cache",
                'postman-token': "fa8dcb05-9be4-c6ad-c161-d3bd766bc35f"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            result = response.json()
            items = result['list']['item']
            NDBDict = {}
            for item in items:
                NDBDict[item['name']] = item['ndbno']
            return NDBDict

        @staticmethod
        def getReport(NDBNumber):
            # NDBNumber is a string
            # return a dictionary with nutrient names as keys and amount+unit as values
            import requests
            url = "https://api.nal.usda.gov/ndb/reports/"
            querystring = {"format": "json", "api_key": "dCkqkzaw600McBG3V20U8HgiBAEy7NC3Lq8DCQq1", "ndbno": NDBNumber,
                           "type": "s"}
            headers = {
                'cache-control': "no-cache",
                'postman-token': "85d74a47-1176-52fc-77d5-28581fdf962e"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            result = response.json()
            nutrient_list = result['report']['food']['nutrients']
            result = {}
            for nutrient in nutrient_list:
                result[nutrient['name']] = [nutrient['value'],nutrient['unit']]
            return result

    result = detect_labels(path)
    for food in result:
        try:
            if food not in ['dessert','dish','fruit']:
                a = Food(food)
                return (food, a.getNutritions())
        except:
            continue

def NutritionReader(path):

    def getMidpoint(Vertices):
        x1,y1 = Vertices[0]
        x2,y2 = Vertices[1]
        x3,y3 = Vertices[2]
        x4,y4 = Vertices[3]
        midX = (x1 + x2 + x3 + x4) / 4
        midY = (y1 + y2 + y3 + y4) / 4
        return midX, midY

    def textIdentify(path):

        client = vision.ImageAnnotatorClient()

        file_name = os.path.join(
            os.path.dirname(__file__),
             path)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        result = []
        for text in texts:

            vertices = ([(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])
            midPoint = getMidpoint(vertices)
            result.append([text.description, midPoint])
        return result

    def switch(result, i ,j):
        result[i], result[j] = result[j], result[i]

    def arrange(result):
        for i in range(1,len(result)):
            for j in range(i+1, len(result)):
                text1, pos1 = result[i]
                pos1x, pos1y = pos1
                text2, pos2 = result[j]
                pos2x, pos2y = pos2
                if (pos2y - pos1y) < -10:
                    switch(result,i,j)
                elif abs(pos2y - pos1y) < 10 and pos1x > pos2x:
                    switch(result,i,j)
        return result

    def connect(result):
        text = ''
        for i in range(1, len(result)):
            t, pos = result[i]
            text += ' ' + t
        return text

    def getTheText(path):
        pic = textIdentify(path)
        arranged = arrange(pic)
        return connect(arranged)

    def type1Search(file, name):
        pos = file.find(name)
        if pos == -1:
            return 0
        else:
            if name == "Calories" or name == "Calories from Fat":
                subFile = file[pos + len(name):]
                result = ""
                i = 1
                while subFile[i] != " ":
                    if subFile[i] == 'O':
                        result = result + '0'
                    else: result = result + subFile[i]
                    i = i + 1
                return eval(result)
            else:
                subFile = file[pos + len(name):]
                posg = subFile.find("g")
                result = ""
                for i in range(posg):
                    if subFile[i] == 'O':
                        result = result + '0'
                    elif (subFile[i].isdigit()) or subFile[i] == ".":
                        result = result + subFile[i]
                return eval(result)  


    def type2Search(file, name):
        pos = file.find(name)
        if pos == -1:
            return 0
        else:
            subFile = file[pos + len(name):]
            posg = subFile.find("%")
            result = ""
            for i in range(3):
                if subFile[posg - 1 - i] == 'O':
                    result = '0' + result
                elif (subFile[posg - 1 - i].isdigit()) or subFile[posg - 1 - i] == ".":
                    result = subFile[posg - 1 - i] + result
            return eval(result) 

    def getResult(path):
        text  = getTheText(path)
        print(text)
        result = {}
        criterion = {'Calories':2000,'Calories from Fat': 290,'Total Fat': 60,'Saturated Fat': 20,'Cholesterol':300,\
                 'Sodium':2400,'Total Carbohydrate': 300,'Sugars': 90,'Protein': 50,'Calcium':1000,'Iron':18,\
                 'Vitamin A':600,'Vitamin B':1000,'Vitamin C':75000,'Vitamin D':125,'Vitamin E':22058
                }
        type1 = ['Calories','Calories from Fat','Total Fat','Saturated Fat','Cholesterol',\
                         'Sodium','Total Carbohydrate','Sugars','Protein']
        type2 = ['Calcium','Iron','Vitamin A','Vitamin B','Vitamin C','Vitamin D','Vitamin E']

        for nut in type1:
            a = type1Search(text, nut)
            result[nut] = int(a / criterion[nut] *100)

        for nut in type2:
            result[nut] = int(type2Search(text, nut))

        return result

    return getResult(path)






if __name__ == '__main__':
    path = "Nutrition Fact1.jpg"
    print(NutritionReader(path))
    # path1 = "10.jpeg"
    # print(imageReader(path1))




