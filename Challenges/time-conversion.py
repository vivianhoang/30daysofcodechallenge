time = raw_input().strip()
(h, m, AmPm) = time.split(':')

m = int(m)
h = int(h)

"""Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Sample Input

07:05:45PM

Sample Output

19:05:45
"""

# if there is a 'PM' at the end of the seconds, add 12
if AmPm.find('PM') != -1:
    timeFormat = "PM"
    if h >= 1 and h <= 11:
        h += 12
# if not, don't add anything
else:
    timeFormat = "AM"
    if h == 12:
        h = 0

s = AmPm.replace(timeFormat, '')
#format two places
h = '{:02}'.format(h)
m = '{:02}'.format(m)

time_convesion = str(h) + ":" + str(m) + ":" + s
print(time_convesion)