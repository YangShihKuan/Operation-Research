print"#1"
print'divisible by 11'
for x in range(1,51):
    if x % 11 ==0:
        print x
print        
print"#2"
print'divisible by 5 or 7'
for y in range(1,31):
    if y % 5 == 0 or y % 7 == 0:
        print y
print
print"#3"
print'divisible by 2 and 7'
for z in range(1,31):
    if z % 2 == 0 and z % 7 == 0:
        print z
print
print"#4"
print'not divisible by 2 nor 7'
a = 1
while a <= 20:
    if a % 2.0 != 0 and a % 7.0 != 0 :
        print a
    a =a + 1
print
print"#5"
print'odd integers'
n = 20
odd = 1
while odd <= n:
    print odd
    odd = odd +2