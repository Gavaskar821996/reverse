from datetime import datetime
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return (d1.year - d2.year)*12 + d1.month - d2.month
print days_between('2012-10-20','2012-05-25')
