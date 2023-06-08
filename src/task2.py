
#Question Two
def oddNumbers(start,stop):
    oddsList= [i for i in range(start,stop) if i%2==1]
    return oddsList

print(oddNumbers(1,47))