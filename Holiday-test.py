import datetime
import calendar

class Holiday():
    #入力日が、日本の祝日かどうかを判定し、祝日であればTrueを返す
    seijinhi = 11
    shunbunbi = 0
    uminohi = 20
    yamanohi = 11
    shuubunhi = 20
    keironohi = 23
    sportnohi = 20
    def YoubiDay (self, HanteiBi, Youbi, ShuNum):
        indexNum = calendar.day_name[:].index(Youbi)
        WeekCount = 0
        for serchDay in range(calendar.monthrange(HanteiBi.year, HanteiBi.month)[1] - 1):
            if datetime.date(HanteiBi.year, HanteiBi.month, serchDay+1).weekday() == indexNum:
                WeekCount = WeekCount + 1
            if WeekCount == ShuNum:
                return serchDay + 1
                break
    def holidayHanteiDay (self, HanteiBi):
        Result = False
        #祝日が日と曜日で決まっているものを判定
        if HanteiBi.month == 1:
            #1月1日（元日）
            if HanteiBi.day == 1:
                Result = True
            #1月の第２月曜日（成人の日）
            self.seijinhi = self.YoubiDay(HanteiBi,'Monday',2)
            if HanteiBi.day == self.seijinhi:
                Result = True
        if HanteiBi.month == 2:
            #2月11日（建国記念の日：政令により定められる）
            if HanteiBi.day == 11:
                Result = True
            #2月23日（天皇誕生日）
            if HanteiBi.day == 23:
                Result = True
        if HanteiBi.month == 3:
            #3月3日 (春分の日)
            self.shunbunbi = int(20.8431 + 0.242194 * (HanteiBi.year - 1980)) - int((HanteiBi.year - 1980) / 4)
            if HanteiBi.day == self.shunbunbi:
                Result = True
        if HanteiBi.month == 4:
            #4月29日 (昭和の日)
            if HanteiBi.day == 29:
                Result = True
        if HanteiBi.month == 5:
            #5月3日（憲法記念日）
            if HanteiBi.day == 3:
                Result = True
            #5月4日（みどりの日）
            if HanteiBi.day == 4:
                Result = True
            #5月5日（こどもの日）
            if HanteiBi.day == 5:
                Result = True
        if HanteiBi.month == 7:
            #7月第３月曜日（海の日：ただし2020年だけは7月23日）
            if HanteiBi.year == 2020:
                self.uminohi = 23
                self.sportnohi = 24
            if HanteiBi.year == 2021:
                self.uminohi = 22
                self.sportnohi = 23
            else:
                self.uminohi = self.YoubiDay(HanteiBi,'Monday',3)
            if HanteiBi.day == self.uminohi:
                Result = True
            #2020年及2021年の特例（スポーツの日）
            if HanteiBi.year == 2020:
                if HanteiBi.day == self.sportnohi:
                    Result = True
            if HanteiBi.year == 2021:
                if HanteiBi.day == self.sportnohi:
                    Result = True
        if HanteiBi.month == 8:
            #8月11日（山の日）
            if HanteiBi.year == 2020:
                yamanohi = 23
            if HanteiBi.year == 2021:
                yamanohi = 8 
            else:
                yamanohi = 11
            if HanteiBi.day == yamanohi:
                Result = True
        if HanteiBi.month == 9:
            #秋分の日
            self.shuubunhi = int(23.2488 + 0.242194 * (HanteiBi.year - 1980)) - int(HanteiBi.year - 1980) / 4
            if HanteiBi.day == self.shuubunhi:
                Result = True
            #9月第３月曜日（敬老の日）
            self.keironohi = self.YoubiDay(HanteiBi,'Monday',3)
            if HanteiBi.day == self.keironohi:
                Result = True
        if HanteiBi.month == 10:
            #スポーツの日
            if (HanteiBi.year != 2020) or (HanteiBi.year != 2021):
                self.sportnohi = self.YoubiDay(HanteiBi, 'Monday', 2)
                if HanteiBi.day == self.sportnohi:
                    Result = True
        if HanteiBi.month == 11:
            #11月3日（文化の日）
            if HanteiBi.day == 3:
                Result = True
            #11月23日（勤労感謝の日）
            if HanteiBi.day == 23:
                Result = True
        
        return Result


def main():
    #HanteiBi = datetime.datetime.strptime("2021/3/20", "%Y/%m/%d")
    HanteiBi = datetime.date(2021,7,19)
    x = Holiday()
    print(HanteiBi)
    print(x.holidayHanteiDay(HanteiBi))

if __name__ == "__main__":
    main()

# Public Function holidayHantei2(hanteiBi As Date, holiday1 As Boolean) As Boolean
#     '国民の祝日に関する法律３条２項判定
#     Dim zenjitsu As Date
#     Dim zenhori As Date
    
#     zenjitsu = DateSerial(Year(hanteiBi), Month(hanteiBi), Day(hanteiBi) - 1)
#     If holiday1 = False Then
#         zenhori = zenjitsu
#         Do While holidayHantei1(zenhori) = True
#             If Weekday(zenhori) = vbSunday Then
#                 holidayHantei2 = True
#             End If
#             zenhori = DateSerial(Year(zenhori), Month(zenhori), Day(zenhori) - 1)
#         Loop
#     Else
#         holidayHantei2 = True
#     End If
#     '国民の祝日に関する法律３条３項判定
#     Dim yokujitsu As Date
    
#     yokujitsu = DateSerial(Year(hanteiBi), Month(hanteiBi), Day(hanteiBi) + 1)
#     If holiday1 = False Then
#         If (holidayHantei1(zenjitsu) = True) And (holidayHantei1(yokujitsu) = True) Then
#             holidayHantei2 = True
#         End If
#     End If
# End Function

# Function hizukeFind(hanteiBi As Date, youbikai As Long) As Long
# '曜日で指定されるものの日付を返す
# Dim i As Long
# Dim count As Long

#     count = 0
#     For i = 1 To 21
#         If Weekday(DateSerial(Year(hanteiBi), Month(hanteiBi), i), vbSunday) = vbMonday Then
#             count = count + 1
#             If count >= youbikai Then
#                 hizukeFind = i
#                 Exit For
#             End If
#         End If
#     Next i
# End Function



