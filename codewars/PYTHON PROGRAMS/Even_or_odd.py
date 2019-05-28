#define a function which takes an integer and return whether the number is even of odd



def even_or_odd(number):
    if(number%2==0):
        return ("Even")
    else:
        return ("Odd")


number=int(input())
print(even_or_odd(number))
