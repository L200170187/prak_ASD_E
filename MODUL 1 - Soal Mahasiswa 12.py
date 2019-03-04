import random

numberofGuesses = 0
number = random.randint(1,100)

print (number)
print("Permainan Tebak Angka !!!")
print("Saya Menyimpan sebuah angka bulat antara 1 sampai 100. coba tebak.")

while numberofGuesses < 100:
  guess = input("Apa Tebakanmu? ")
  guess = int(guess)

  numberofGuesses = numberofGuesses + 1;
  guessesLeft = 0 + numberofGuesses;

  if guess < number:
    guessesLeft=str(guessesLeft)
    print("Angka Itu terlalu kecil. ini tebakan mu ke-" + guessesLeft + " Ayo Coba Lagi!!!")

  if guess > number:
    guessesLeft=str(guessesLeft)
    print("Angka Itu terlalu Besar. ini tebakan mu ke- " + guessesLeft + " Ayo Coba Lagi!!!")

  if guess==number:
    break

if guess==number:
  numberofGuesses=str(numberofGuesses)
  print("Ya, Tebakan anda Benar!!! " + numberofGuesses + " Selamat :)")

if guess!=number:
  number=str(number)
  print("Sorry. The number I was thinking of was " + number + " :)")
