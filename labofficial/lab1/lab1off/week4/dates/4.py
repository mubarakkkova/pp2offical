import datetime 



def date_diff(dt2:datetime.date,dt1:datetime.date) -> (int or float):
    
    diff = dt2 - dt1 
    return abs(diff.days*24*3600 + diff.seconds) 




DateA = datetime.date(2020,12,2)
DateB = datetime.date(2023,12,2)


print(f"There is {date_diff(DateA,DateB)} seconds between {DateA} and {DateB}" )