class PrimeNumber:
  def __init__(self, num):
    self.number = num

  def is_prime(self):
    if self.number <= 1:
      return False
    elif self.number <= 3:
      return True
    elif self.number % 2 == 0 or self.number % 3 == 0:
      return False
    i = 5
    while i * i <= self.number:
      if self.number % i == 0 or self.number % (i + 2) == 0:
        return False
      i += 6
    return True