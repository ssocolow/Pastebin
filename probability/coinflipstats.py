import random

#return number of heads in x flips
def coinflip(x):
  heads = 0
  for i in range(x):
    if random.random() > 0.5:
      heads += 1
    else:
      pass
  return heads

for i in range(100):
  heads = coinflip(100)
  z = (heads - 50)/5
  print("heads: " + str(heads) + " z score: " + str(z))
