# -*- coding: utf-8 -*-


"""
@Lesson Five Loops
@Dec 7th 2020
@Author Lawrie Scott
@1st Assignment for this topic

"""
#variables to dump my list of seperated numbers after working out modulo
failList=[]
fizzList=[]
buzzList=[]
fizzbuzzList=[]

#calculate the list for each Number from 1 to 100
for number in range(1,101):
    if number%3 == 0 and number%5 == 0:
        fizzbuzzList.append(number)
    elif  number%3 == 0:
        fizzList.append(number)
    elif  number%5 == 0:
        buzzList.append(number)
    else:
        failList.append(number)

#Print out all the relative number catergories
print()
print("The Fizz Numbers: ", fizzList)

print()
print("The Buzz Numbers: ", buzzList)

print()
print("The FizzBuzz Numbers: ", fizzbuzzList)

print()        
print("The failed Fizz Buzz Numbers: ", failList)

#calculating prime numbers and no never want to do this again :)
primes = [prime for prime in range(2, number)
          if prime not in
          [notAPrime for i in range(2, int(number**0.5))
           for notAPrime in range(i * 2, number, i)]]

#Print the Primme number list
print()
print("Prime numbers between 2 and", number)
print(primes)