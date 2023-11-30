"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    limit = 2
    if number_of_primes < 1:
        raise ValueError('Argument was less than 1')
    else:
        while len(list) < number_of_primes:
            
            
                    prime  = True
                    for j in range(2, limit):
                        if (limit % j == 0):
                            prime = False
                            break
                    if prime:
                        list.append(limit)
                    limit += 1
                
                    



        return list
