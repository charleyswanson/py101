# Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

def century(year):
    if (year / 100) > (year // 100):
        answer = str((year // 100) + 1)
    else:
        answer = str(year // 100)
        
    if any(answer[-2:] == item for item in ["11", "12", "13"]):
        answer = answer + 'th'
    elif answer[-1] == '1':
        answer = answer + 'st'
    elif answer[-1] == '2':
        answer = answer + 'nd'
    elif answer[-1] == '3':
        answer = answer + 'rd'
    else:
        answer = answer + 'th'
    
    return answer

# century(2000)
# century(2001)
# century(1965)
# century(256)
# century(5)
# century(10103)
# century(1052)
# century(1127)
# century(11201)

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True