# 43696

a, b, n = map(int, input().split())

# Handle integer part
a %= b

# Current digit
i = 0

# Process long division with batch to reduce loop times
batch_d = 10000
batch_pow = pow(10, batch_d)
while i + batch_d < n:
    a = (a * batch_pow) % b
    i += batch_d

# Step long division to reach `i = n - 1`
while i + 1 < n:
    a = (a * 10) % b
    i += 1

# Get the digit from `n` to `n + 2`
last_3 = a * 1000 // b
print(f"{last_3:03}")
