def count_of_no_of_divisors(num):
    count = 0
    for i in range(1, num+1):
         if(num % i == 0):
              count = count + 1
    return count

def check_9_factors(n):
    c = 0
    for i in range(1, n+1):
        if(count_of_no_of_divisors(i) == 9):
            print(i, end= " ")
            c = c + 1
    print("Total :" , end = ' ')
    print(c)

n = int(input("Enter a number : " ))
print('The number which has exactly 9 divisors are ')
check_9_factors(n)
