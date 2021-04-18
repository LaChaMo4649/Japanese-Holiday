class Holiday():
    #祝日のデータベース作成、祝日判定
    import datetime
    import calendar
    def YoubiDay (self, HanteiBi, Youbi, ShuNum):
        #HanteiBi:判定日の年と月において、ShuNum:第何周かの番号で示されるYoubi:指定曜日の日にちを返す。　
        indexNum = calendar.day_name[:].index(Youbi)
        WeekCount = 0
        for serchDay in range(calendar.monthrange(HanteiBi.year, HanteiBi.month)[1] - 1):
            if datetime.date(HanteiBi.year, HanteiBi.month, serchDay+1).weekday() == indexNum:
                WeekCount = WeekCount + 1
            if WeekCount == ShuNum:
                return serchDay + 1
                break
    def HolidayDataBase():
        #日付が一義的に指定できる祝日の辞書型を返す。
        holidayData = {}
        nen = datetime.date(today()).year
        gantan = datatime.date(nen,1,1)
        print (nen,gantan)

        #1月1日（元日）
        holidayData[gantan] = "元旦"
x = Holiday()
x.HolidayDataBase
