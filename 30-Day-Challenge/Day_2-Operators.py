# Enter your code here. Read input from STDIN. Print output to STDOUT

mealCost = float(raw_input())
tipPercent = float(raw_input())/100
taxPercent = float(raw_input())/100

totalCost= mealCost + tipPercent*mealCost + taxPercent*mealCost

new_total = int(round(totalCost))

print "The total meal cost is %s dollars." % (new_total)