import datetime
import calendar

nen = 2021
gantan = datetime.date(nen,1,1)
tennoutan = datetime.date(nen, 2,23)
holidayData = {gantan:'元旦',tennoutan:'天皇誕生日'}

findDay = datetime.date(nen,1,1)
print(findDay in holidayData.keys())
print(holidayData[findDay])