value1 = 30000.146713
value2 = -26785.6756337
value3 = 4.567


#print(f"{value1:.2f}") .2f signifies it update our value till 2 floating points
#print(f"{value2:.1f}") .1f means till 1 floating point

#print(f"{value1:13}")  will print total 13 spaces (space +digits)
#print(f"{value1:013}")  will print 0's before number till total spaces becomes 13

#print(f"{value1:<12}")  will left adjust 
#print(f"{value2:<12}")
#print(f"{value3:<12}")

#print(f"{value1:>12}")  will right adjust
#print(f"{value2:>12}")
#print(f"{value3:>12}")



#print(f"{value1:^12}") will centre adust

#print(f"{value1:+}") will add +before value if it is positive or - if negative

#print(f"{value1: }") will put space before value of if it is positive

#print(f"{value1:,}") will use comma in numbers like 3,000,000

print(f"{value1:+,.2f}")
print(f"{value2:+,.2f}")
print(f"{value3:+,.2f}")
