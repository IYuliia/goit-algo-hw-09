import time

def find_coins_greedy(amount, coins):
   
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result


def find_min_coins(amount, coins):

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  
    
    backtrack = [-1] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                backtrack[x] = coin

    if dp[amount] == float('inf'):
        return None  
  
    result = {}
    while amount > 0:
        coin = backtrack[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 113


start_time = time.time()
greedy_result = find_coins_greedy(amount, coins)
greedy_time = time.time() - start_time


start_time = time.time()
dp_result = find_min_coins(amount, coins)
dp_time = time.time() - start_time


print("Жадібний алгоритм:")
print("Результат:", greedy_result)
print("Час виконання:", greedy_time, "секунд")

print("\nДинамічне програмування:")
print("Результат:", dp_result)
print("Час виконання:", dp_time, "секунд")


large_amount = 10000

start_time = time.time()
find_coins_greedy(large_amount, coins)
greedy_time_large = time.time() - start_time

start_time = time.time()
find_min_coins(large_amount, coins)
dp_time_large = time.time() - start_time

print("\nПорівняння на великій сумі (", large_amount, "):")
print("Жадібний алгоритм:", greedy_time_large, "секунд")
print("Динамічне програмування:", dp_time_large, "секунд")
