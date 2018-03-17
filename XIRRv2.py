import scipy.optimize
import datetime
from datetime import date
import xlrd

file_location = "C:/Users/saurabh/Desktop/xirr_example2.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
def xnpv(rate, values, dates):
    '''Equivalent of Excel's XNPV function.'''
    #print(rate)
    if rate <= -1.0:
        return float('inf')
    d0 = min(dates)
    return sum([ vi / (1.0 + rate)**((di - d0).days / 365.0) for vi, di in zip(values, dates)])

def xirr(values, dates):
    '''Equivalent of Excel's XIRR function.'''
    try:
        return scipy.optimize.newton(lambda r: xnpv(r, values, dates), 0.0)
    except RuntimeError:    # Failed to converge?
        return scipy.optimize.brentq(lambda r: xnpv(r, values, dates), -1.0, 1e10)


values =[]
for col in range(sheet.nrows):
    values.append(sheet.cell_value(col,0))

dates =[]
for col in range(sheet.nrows):
    excel_time = sheet.cell_value(col,1)
    time_tuple = xlrd.xldate_as_tuple(excel_time, 0)
    onlyd = datetime.datetime(*time_tuple)
    dates.append(onlyd.date())

#dates = [date(2007, 1, 1), date(2007, 1, 10), date(2007, 6, 1),date(2007, 10, 25),date(2007, 12, 31),date(2008, 3, 1),date(2008, 6, 15)]
#values = [-50000, 500, 500, 500, 500, 500, 51000 ]
print(xirr(values, dates),"%")
#print(dates)

