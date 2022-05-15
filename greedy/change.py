# 복잡도: O(coins)
def change_coin_count(change):
    coins = (500, 100, 50, 10)
    n = 0
    for coin in coins:
        n += change // coin
        change %= coin

    return n


print(change_coin_count(1260))
