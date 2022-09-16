import math
checker = "yes"
def prime_checker(number):
    if number == 1 or number == 2:
        return True
    if number % 2 == 0:
        return False
    if number <= 0:
        return False

    halfOfNumber = math.floor(number / 2)

    prime = True
    while prime:
            for digits in range(2, halfOfNumber):

                modulo = number % digits
                if modulo == 0:
                     if digits == 1:
                        digits - 1
                        print("1")
                     else:
                        prime = False
                        return False

            return True

if __name__ == "__main__":
    while checker == "yes":
        n = int(input("Check this number: "))
        if (prime_checker(number=n)):
            print("It's prime")
        else:
            print("It's not prime.")
        checker = input("Do you want to check another number? Yes or No:\n").lower()
    print("Sadge cya later alligator!")



