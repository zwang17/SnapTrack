"""
Example:
Broccoli = Food('broccoli')
print(Broccoli.getNutrition())
# pass in "with_unit = True" into getNutrition() will return a dictionary of nutritions with units.
"""
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
        number_dict = self.getNDBNumber(self.food_name)
        num = 0
        for i in number_dict:
            num = number_dict[i]
        report = self.getReport(num)
        result_dict = {}
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

if __name__ == '__main__':
    pass