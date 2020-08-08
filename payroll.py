#Name:payroll.py
#Author:Julian Miguel Alapan
#Description:Employee Records
#Date:August 7, 2020

fileName = input('Enter the file name: ')

print('\n%-15s | %-15s | %-10s | %-10s | %-10s' % ('Employee Number','Employee Name', 'Hours Worked', 'Hourly Rate', 'Total Pay'))

for line in open(fileName):
    line = line.strip()

    if line != '':
        (enum,lname,fname, hours, hourlyrate) = line.split()


        ename = fname + ' ' + lname
        hours = int(hours)
        hourlyrate = float(hourlyrate)
        totalpay = hourlyrate * hours

        print('%-15s | %-15s | %-10d |  %-10.2f | %-10.2f' % (enum,ename, hours, hourlyrate, totalpay))
