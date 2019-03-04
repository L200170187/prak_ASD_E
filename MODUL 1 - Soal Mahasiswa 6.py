for BilanganPrima in range(2, 1000):
    
    isPrime = True
    for num in range(2, int(BilanganPrima ** 0.5) + 1):
        if BilanganPrima % num == 0:
            isPrime = False
            break
      
    if isPrime:
        print(BilanganPrima)
