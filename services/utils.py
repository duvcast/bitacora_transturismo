import datetime


def next_weekday(date_target, weekday):
    days_ahead = weekday - date_target.weekday()
    if days_ahead == 0:
        return date_target + datetime.timedelta(days_ahead)  # If the date is equal today then return today
    if days_ahead < 0:  # Target day already happened this week
        days_ahead += 7
    return date_target + datetime.timedelta(days_ahead)

# date_target = datetime.date(2022, 3, 31) next_monday = next_weekday(date_target, 1)  # 0 = Monday, 1=Tuesday,
# 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday
