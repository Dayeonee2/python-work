import random

lotto = set();

while len(lotto) != 6:
    n = random.randrange(1, 46);
    lotto.add(n);

print(lotto);