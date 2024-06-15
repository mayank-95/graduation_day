def count_ways_and_missed_probability(N):
    # Initialize dynamic programming arrays
    dp = [0] * (N + 1)  # dp[i] represents the number of ways to attend classes on day i
    
    # Base cases
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    dp[3] = 8

    # Calculate the number of ways for each day
    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    # No of ways of missing missing the graduation ceremony for day N

    missed=dp[N-1]-dp[N-5]

    return dp[N],missed

def main():

    # Input N (the last day of the academic year)
    N = int(input("Enter the last day of the academic year (N): "))
    if N<5:
        print("invalid value- number of days should be atleast 5 as per constraints")
        return
    ways, probability = count_ways_and_missed_probability(N)

    print(f"{probability}/{ways}")

main()
