from collections import Counter


inventory = Counter()
loot = {"xp": 1000, "gold": 500, "potion": 3}
inventory.update(loot)
print(inventory)
print(inventory["xp"])
inventory.update({"gold": -1000, "potion": 2, "magic_scroll": 1})
print(inventory)
