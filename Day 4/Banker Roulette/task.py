import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1st way
random_index = random.randint(0, len(friends) - 1)
print(friends[random_index])
# 2nd way
print(random.choice(friends))
