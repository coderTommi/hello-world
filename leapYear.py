#-*-coding:utf-8 -*-
def judgeLeapYear(year):
    if year%400==0:
        return True
    elif year%400!=0 and year%4==0:
        return True
    else:
        return False
