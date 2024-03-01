def StockPicker(arr):
  n=len(arr)
  profit = 0
  for i in range(n-1):
    for j in range(i+1,n):
      curr_profit = arr[j] - arr[i]
      profit = max (profit, curr_profit)
    
  # code goes here
  return profit-1 if profit == 0 else profit

# keep this function call here 
print(StockPicker(input()))
