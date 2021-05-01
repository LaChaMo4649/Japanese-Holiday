class Holiday():
    #祝日のデータベース作成、祝日判定
    import datetime
    import calendar
    def YoubiDay (self, HanteiBi, Youbi, ShuNum):
        #HanteiBi:判定日の年と月において、ShuNum:第何周かの番号で示されるYoubi:指定曜日の日にちを返す。　
        indexNum = calendar.day_name[:].index(Youbi) #Monday:0 〜 Sunday:6
        WeekCount = 0
        for serchDay in range(calendar.monthrange(HanteiBi.year, HanteiBi.month)[1] - 1):
            if datetime.date(HanteiBi.year, HanteiBi.month, serchDay+1).weekday() == indexNum:
                WeekCount = WeekCount + 1
            if WeekCount == ShuNum:
                return serchDay + 1
                break
    def _HolidayDataBase(self, nen):
        #nen：年で指定する年の日付が一義的に指定できる祝日の辞書型を返す。
        holidayData = {}
        #nen = datetime.date(today()).year
        #1月1日（元日）
        holidayData[datetime.date(nen,1,1)] = "元日"
        #１月の第２月曜日（成人の日）
        holidayData[datetime.date(nen,1,self.YoubiDay(datetime.date(nen,1,1),"Monday",2))] = "成人の日"
        #2月11日（建国記念の日：政令で定める日）
        holidayData[datetime.date(nen,2,11)] = "建国記念の日"
        #2月23日（天皇誕生日）
        holidayData[datetime.date(nen,2,23)] = "天皇誕生日"
        #春分日（春分の日）
        shunbunhi = int(20.8431 + 0.242194 * (nen - 1980)) - int((nen - 1980) / 4)
        holidayData[datetime.date(nen,3,shunbunhi)] = "春分の日"
        #4月29日（昭和の日）
        holidayData[datetime.date(nen,4,29)] = "昭和の日"
        #5月3日（憲法記念日）
        holidayData[datetime.date(nen,5,3)] = "憲法記念日"
        #5月4日（みどりの日）
        holidayData[datetime.date(nen,5,4)] = "みどりの日"
        #5月5日（子供の日）
        holidayData[datetime.date(nen,5,5)] = "こどもの日"
        #7月の第３月曜日：2020年は7月23日、2021年は7月22日（海の日）
        if nen == 2020:
            holidayData[datetime.date(nen,7,23)] = "海の日"
        if nen == 2021:
            holidayData[datetime.date(nen,7,22)] = "海の日"
        else:
            holidayData[datetime.date(nen,7,self.YoubiDay(datetime.date(nen,7,1),'Monday',3))] = "海の日"
        #8月11日（山の日）
        if nen == 2020:
            holidayData[datetime.date(nen,8,10)] = "山の日"
        if nen == 2021:
            holidayData[datetime.date(nen,8,8)] = "山の日"
        else:
            holidayData[datetime.date(nen,8,11)] = "山の日"
        #9月の第3月曜日（敬老の日）
        holidayData[datetime.date(nen,9,self.YoubiDay(datetime.date(nen,9,1),"Monday",3))] = "敬老の日"
        #秋分日（秋分の日）
        shunbunhi = int(23.2488 + 0.242194 * (nen - 1980)) - int((nen - 1980) / 4)
        holidayData[datetime.date(nen,9,shunbunhi)] = "秋分の日"
        #10月の第２月曜日（スポーツの日）
        if nen == 2020:
            holidayData[datetime.date(nen,7,24)] = "スポーツの日"
        if nen == 2021:
            holidayData[datetime.date(nen,7,23)] = "スポーツの日"
        else:holidayData[datetime.date(nen,1,self.YoubiDay(datetime.date(nen,10,1),"Monday",2))] = "スポーツの日"
        #11月3日（文化の日）
        holidayData[datetime.date(nen,11,3)] = "文化の日"
        #11月23日（勤労感謝の日）
        holidayData[datetime.date(nen,11,23)] = "勤労感謝の日"
        return holidayData
    def HolidayJudge(self, HanteiBi):
        HoliHan = False
        HoliBase = self._HolidayDataBase(HanteiBi.year)
        if HanteiBi in HoliBase:
            HoliHan = True
        #国民の祝日に関する法律３条２項判定
        else:
            zenjitsu = HanteiBi - datetime.timedelta(days=1)
            while (zenjitsu in HoliBase): #前日が祝日である限りループ
                if zenjitsu.weekday() == 6: #前日が祝日で日曜日
                    HoliHan = True
                    break
                else:
                    zenjitsu = zenjitsu - datetime.timedelta(days=1)
            else:
                HoliHan = False
        #国民の祝日に関する法律３条３項判定
        zenjitsu = HanteiBi - datetime.timedelta(days=1)
        yokujitsu = HanteiBi + datetime.timedelta(days=1)
        if (zenjitsu in HoliBase) and (yokujitsu in HoliBase):
            HoliHan = True
        return HoliHan

import datetime
import calendar
x = Holiday()
print(x.HolidayJudge(datetime.date(2021,1,1)))
# print(x.HolidayJudge(datetime.date(2021,1,11)))
# print(x.HolidayJudge(datetime.date(2021,2,11)))
# print(x.HolidayJudge(datetime.date(2021,2,23)))
# print(x.HolidayJudge(datetime.date(2021,3,20)))
# print(x.HolidayJudge(datetime.date(2021,4,29)))
# print(x.HolidayJudge(datetime.date(2021,5,3)))
# print(x.HolidayJudge(datetime.date(2021,5,4)))
# print(x.HolidayJudge(datetime.date(2021,5,5)))
# print(x.HolidayJudge(datetime.date(2021,7,22)))
# print(x.HolidayJudge(datetime.date(2021,8,8)))
# print(x.HolidayJudge(datetime.date(2021,8,9)))
# print(x.HolidayJudge(datetime.date(2021,9,20)))
# print(x.HolidayJudge(datetime.date(2021,9,23)))
# print(x.HolidayJudge(datetime.date(2021,11,3)))
# print(x.HolidayJudge(datetime.date(2021,11,23)))