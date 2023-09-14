# University Attendance README

This README file provides an overview of the problem statement and instructions for solving it.

## Problem Statement

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not allowed to miss classes for four or more consecutive days. Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

## Solution

### 1. Number of Ways to Attend Classes

To calculate the number of ways to attend classes over N days, we need to find the total number of valid attendance patterns. We can solve this problem using dynamic programming.

### 2. Probability of Missing Graduation Ceremony

To calculate the probability of missing your graduation ceremony, we need to find the number of invalid attendance patterns (patterns where you miss the graduation ceremony) and then calculate the probability as the ratio of invalid patterns to the total number of patterns.

### String Format for the Solution

The solution should be represented in the string format as "Answer of (2) / Answer of (1)", where:
- "Answer of (1)" is the number of ways to attend classes over N days.
- "Answer of (2)" is the probability that you will miss your graduation ceremony.

## How to Use

You can use the provided solution to calculate the answers for different values of N by providing the input value of N to the solution algorithm. The algorithm will return the answers in the specified string format.

## Test Cases

Here are some test cases along with their expected results:

- For 5 days: "Answer of (2) / Answer of (1)" = "14/29"
- For 10 days: "Answer of (2) / Answer of (1)" = "372/773"

You can use these test cases to verify the correctness of the solution.

## Implementation

You can find the implementation of the solution in the code files provided with this repository.

## Author

This README and the solution were created by [Your Name].

---

Feel free to replace "[Your Name]" with the actual author's name or any other additional information you want to include in the README file.