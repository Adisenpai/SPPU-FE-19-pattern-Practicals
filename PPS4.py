""" To accept student’s five courses marks and compute his/her result. Student is passing if
he/she scores marks equal to and above 40 in each course. If student scores aggregate
greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the
grade if first division. If aggregate is 50>= and <60, then the grade is second division. If
aggregate is 40>= and <50, then the grade is third division. """

per = int(input("enter your per : "))

if(per >= 75) :

    print("distinction")

elif(per >= 60 and per <= 74) :

    print('first division')

elif(per >= 50 and per <= 59) :

    print("second division")

elif(per >= 40 and per <= 49) :

    print("third division")

else:

    print("fail")