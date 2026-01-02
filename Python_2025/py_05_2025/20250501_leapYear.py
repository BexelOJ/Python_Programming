def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 != 0:
        return False  # Not divisible by 4  : not a leap year
    elif year % 100 != 0:
        return True   # Divisible by 4, not by 100 : leap year
    elif year % 400 == 0:
        return True   # Divisible by 100 and 400 : leap year
    else:
        return False

year = int(input())
print(is_leap(year))


''' DocString/DocComment
Leap Years (Divisible by 4, and follow the rules):
2000 (Divisible by 400, so it's a leap year)

2016 (Divisible by 4, not divisible by 100)

2020 (Divisible by 4, not divisible by 100)

2400 (Divisible by 400, so it's a leap year)

❌ Non-Leap Years (Failing one or more of the leap year conditions):
1900 (Divisible by 100 but not 400)

2100 (Divisible by 100 but not 400)

2023 (Not divisible by 4)

2019 (Not divisible by 4)
'''

# if year Divisible by 4 and not Divisible by 100 -> it is a leap year
# if year is Divisible by 100 then it should also be Divisible by 400 -> it is a leap year
# if year is not Divisible by 4 then it is not a leap year

"""
Divisible by 4 → check for 100

Not divisible by 100 → leap year

Divisible by 100 → check for 400

Divisible by 400 → leap year

Not divisible by 400 → not a leap year

"""
