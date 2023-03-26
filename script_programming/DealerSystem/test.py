# import json
# from datetime import date, timedelta,datetime
# # file to test different things
# file = open('data.json')

# data = json.load(file)


# # for i in data["cars"]:
# #     if i["brand"] == "bmw" and i["number"] > 0:
# #         i["number"] -= 1
# #         print(i["number"])

# mydata = ["sebastianek", "bmw"]

# data['clients'].append({
#                         "name": mydata[0],
#                         "car": mydata[1],
#                         "transaction": "sell",
#                         "sum": 22
#                     })
# # print(data['clients'])
# # print(data['cars'])

# # mydate = date.today()
# # resultdate = mydate + timedelta(days=3)
# # print(mydate)
# # print(resultdate)
# # print(date(2022, 10, 31))
# # x = date.today()
# # print(x)
# # # print("seba".capitalize())

# seba = 0
# print(bool(seba))


# # for i in data['clients']:
# #     if i["name"] == "Sebastian":
# #         print(i["car"])



class S():
    def prinnin(self):
        return 's'

    def trying(self):
        # print(hasattr(obje,seba))
        if hasattr(S,'seba'):
            x = getattr(S,'seba')
            setattr(S,'seba', x + 12)
        else:
            S.seba = 20
        print(S.seba)
        

obje = S()
obje.trying()
obje.trying()
obje.trying()
