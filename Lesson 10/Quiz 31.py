# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def nextDay(year, month, day):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        days_in_months[1] = 29

    if day < days_in_months[month - 1]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")


#test()

#print (daysBetweenDates(1993, 3, 24, 2018, 8, 14))

# when will I be 1000 days old?

def anniversaryDate(year, month, day, days):
    i = 0
    while i < days:
        year, month, day = nextDay(year, month, day)
        i += 1
    return year, month, day

#print (anniversaryDate(1993, 3, 24, 10000))

def printYourInfo(name, bday_year, bday_month, bday_day, today_year, today_month, today_day):
    print('')
    days_old = daysBetweenDates(bday_year, bday_month, bday_day, today_year, today_month, today_day)
    print ('Hi ' + name + ', You are currently ' + str(days_old) + ' days old.')
    ann_year, ann_month, ann_day = anniversaryDate(bday_year, bday_month, bday_day, 10000)
    print ('You will be 10000 days old on the ' + str(ann_day) + '/' + str(ann_month) + '/' + str(ann_year) + '.')
    days_until_ann = daysBetweenDates(today_year, today_month, today_day, ann_year, ann_month, ann_day)
    print ('That is in ' + str(days_until_ann) + ' days time.')


printYourInfo('Colin', 1997, 2, 9, 2018, 8, 14)