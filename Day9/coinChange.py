def coinChange(coins, amount):
    # Initializing an array to store the minimum number of coins needed for each amount from 0 to 'amount'.
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Zero coins are needed to make amount 0.

    # Calculating the minimum number of coins for each amount from 1 to 'amount'.
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Receiving the inputs
coins_input = input("Enter the coins  (comma-separated): ")
coins = [int(coin) for coin in coins_input.split(",")]

amount = int(input("Enter the amount: "))
print(coinChange(coins, amount))  

