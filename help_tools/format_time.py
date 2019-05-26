import time
import datetime

# 计算两个日期相差天数，自定义函数名，和两个日期的变量名。
def Caltime(date1, date2):
    date1 = time.strptime(date1,"%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return (date2 - date1).days
# print(Caltime(date1='2018-11-14',date2='2018-12-10'))
# today_time=datetime.datetime.now().strftime("%Y-%m-%d")
# all_day=Caltime('2015-10-15',today_time)
# print(all_day)