import re
class number2:
    def __init__(self):
        self.num = 0

    def dest(num):
        num+= 1



str = "(int))"

arr_temp = re.split('(\)+?)', str)
for item in (arr_temp):
    if item != None and bool(item.strip()):
        print(item)

# print (arr_temp)