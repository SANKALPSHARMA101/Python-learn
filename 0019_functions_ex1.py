def interest(principal, time = 2, rate = 0.02):
    return (principal*time*rate)/100

pri = int(input("Enter the amount of money for the interest:"))
print("The interest on the given amount is:",interest(pri))
roi = float(input("Enter the desired value of rate of interest:"))
time = int(input("Enter the desired time for the interest:"))
print("The interest on the amount , rate of interest and time chosen by user is:",interest(pri, roi, time))

