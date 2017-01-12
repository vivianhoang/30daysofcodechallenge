#Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.

n = int(raw_input().strip())
   
count = 1

while count <= 10:
    print "{0} x {1} = {2}".format(n, count, n*count)
    count += 1