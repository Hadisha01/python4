def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

print(sum_series(3))
print(sum_series(17))