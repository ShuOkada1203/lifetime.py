# import datetime
# bf=datetime.date(1999,12,3)
# today=datetime.date.today()
# before=today-bf
# # print(int(10000-before))
# print(before.days)

import tkinter as tk
import datetime

root = tk.Tk()
root.minsize(350,400)
root.title("あなたが何日生きているのか知れるアプリ")


ltk = tk.Label(text="あなたは何日生きているでしょうか？調べてみましょう")
ltk.pack()


def count_year():
    got_year = geting_years.get()
    got_month = geting_months.get()
    got_day = geting_days.get()
    
    life=datetime.date(got_year,got_month,got_day)
    today=datetime.date.today()
    lifedays=today-life

    weekdays=life.weekday()
    dayweek=["月","火","水","木","金","土","日"]
    print(f"あなたは{dayweek[weekdays]}曜日生まれです")

    if lifedays.days >= 20000:
        limit_2=30000-lifedays.days
        one_year=limit_2//365
        rest=limit_2-one_year*365
        future=today+datetime.timedelta(limit_2)
        print(f"おめでとうございます。あなたは20000日以上、{lifedays.days}日生きています。30000日まで残り{limit_2}日、{one_year}年と{rest}日で、30000日目は{future}です。")


    elif lifedays.days >= 10000:
        limit_2=20000-lifedays.days
        one_year=limit_2//365
        rest=limit_2-one_year*365
        future=today+datetime.timedelta(limit_2)
        print(f"おめでとうございます。あなたは10000日以上、{lifedays.days}日生きています。20000日まで残り{limit_2}日、{one_year}年と{rest}日で、20000日目は{future}です。")

    else:
        limit=10000-lifedays.days
        one_year=limit//365
        rest=limit-one_year*365
        future=today+datetime.timedelta(limit)
        print(f"あなたは{lifedays.days}日生きています。10000日まで残り{limit}日、{one_year}年と{rest}日後で、10000日目は{future}です。")
        


years_ask = tk.Label(text="西暦を教えてください")
years_ask.pack()
geting_years = tk.Entry()
geting_years.pack()

months_ask = tk.Label(text="生まれた月を教えてください")
months_ask.pack()
geting_months = tk.Entry()
geting_months.pack()

days_ask = tk.Label(text="生まれた日付を教えてください")
days_ask.pack()
geting_days = tk.Entry()
geting_days.pack()




# years=int(input("西暦を教えて下さい"))
# months=int(input("生まれた月を教えて下さい"))
# date=int(input("生まれた日付を教えて下さい"))

# life=datetime.date(years,months,date)
# today=datetime.date.today()
# lifedays=today-life

# weekdays=life.weekday()
# dayweek=["月","火","水","木","金","土","日"]
# print(f"あなたは{dayweek[weekdays]}曜日生まれです")

# if lifedays.days >= 20000:
#     limit_2=30000-lifedays.days
#     one_year=limit_2//365
#     rest=limit_2-one_year*365
#     future=today+datetime.timedelta(limit_2)
#     print(f"おめでとうございます。あなたは20000日以上、{lifedays.days}日生きています。30000日まで残り{limit_2}日、{one_year}年と{rest}日で、30000日目は{future}です。")


# elif lifedays.days >= 10000:
#     limit_2=20000-lifedays.days
#     one_year=limit_2//365
#     rest=limit_2-one_year*365
#     future=today+datetime.timedelta(limit_2)
#     print(f"おめでとうございます。あなたは10000日以上、{lifedays.days}日生きています。20000日まで残り{limit_2}日、{one_year}年と{rest}日で、20000日目は{future}です。")

# else:
#     limit=10000-lifedays.days
#     one_year=limit//365
#     rest=limit-one_year*365
#     future=today+datetime.timedelta(limit)
#     print(f"あなたは{lifedays.days}日生きています。10000日まで残り{limit}日、{one_year}年と{rest}日後で、10000日目は{future}です。")




root.mainloop()

# ('sqlite_zenkoku/zenkoku.sqlite3', 'sqlite_zenkoku'),
#     ('data/tip.json', 'data')