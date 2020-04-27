import pandas as pd
import numpy as np

import time

df = pd.read_excel(open('Deutsch_table.xlsx', 'rb'),sheet_name='der Verben - Konjugation der Ve')

table = df.to_numpy()
print(" ---------------------------")
print("|Enter exit to stop training|")
print(" ---------------------------")
while(True):
  row = np.random.randint(2,table.shape[0])
  col = np.random.randint(table.shape[1])
  if col == 0 and (row == 0 or row == 1):
    continue
  print("Enter the correct combination: {} {}({})".format((table[row][0]),(table[0][col]),table[1][col]))
  guess = input()
  if guess == "exit":
    break
  if guess == table[row][0]+" "+ table[row][col]:
    print(f"\u2714:{table[row][0]} {table[row][col]}")
  else:
    print("\u274c:The correct answer is \n{} {}".format((table[row][0]),(table[row][col])))
  print("____________________________________________")
  #time.sleep(1)
