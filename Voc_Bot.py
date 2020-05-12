import pandas as pd
import numpy as np
import requests
import  json


import time

df = pd.read_excel(open('Deutsch_table.xlsx', 'rb'),sheet_name='der Verben - Konjugation der Ve')

table = df.to_numpy()
print(" ---------------------------")
print("|Enter exit to stop training|")
print(" ---------------------------")
limit = 0
wrong = []
while(True):
  row = np.random.randint(2,table.shape[0])
  col = np.random.randint(1,table.shape[1])
  if col == 0 and (row == 0 or row == 1):
    continue
  extra = ""
  if row == 4:
    extra = "(she)"
  if row == 8:
    extra = "(they)"
  print("Enter the correct combination: {}{} {}({})".format((table[row][0]),(extra),(table[1][col]),(table[0][col])))
  guess = input()
  if guess == "exit":
    print(" ---------------")
    print("|Nice job, Miga!|")
    print(" ---------------")
    print("Have a look at these wrong answers appeared the training:")
    for ele in wrong:
      print(ele)
    input()
    break
  if guess == table[row][0]+" "+ table[row][col]:
    print(f"\u2714:{table[row][0]} {table[row][col]}")
    limit += 1
  else:
    print("\u274c:The correct answer is \n{} {}".format((table[row][0]),(table[row][col])))
    wrong.append(table[row][0]+" "+ table[1][col] +"("+table[0][col]+")")
  print("____________________________________________")
  #time.sleep(1)

print("Do you want to chat with 二号？Enter Yes or No.")
msg = input()
if msg == "Yes" or msg == "yes":
  print(" ------------------------------------------------------------------------")
  print(f"|Miga got {limit} correct answers, you can chat with 二号 for at most {limit} rounds.|")
  print(" ------------------------------------------------------------------------")
  seq = 0
  print("二号已经上线, 竭诚为Miga答疑解惑, 知无不言. 输入 exit 就可以停止对话喔.")
  if limit == 0:
    print("\n二号：聊天次数到了，亲爱的主人~ Miga多背一个单词，二号就能在地球上多待一会儿呢！")
    time.sleep(6)
  while(seq<limit):
    your_chat =input('Miga：')  # 假定为  ： 你是谁？
    if msg == "exit" or msg == "Exit":
      break
    #url: 机器人接口地址
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    # data_param: post请求的参数，向服务器提交的数据。类型为字典(dict)
    # inputeText ----> text:你的聊天信息（一句话）
    data_param = {
                "reqType":0,
                "perception": {
                    "inputText": {
                        "text": your_chat
                                  },
                    "inputImage":{
                        "url": "imageUrl"
                                  },
                    "selfInfo":  {
                        "location":  {
                            "city": "张家港",
                            "province": "江苏",
                            "street": "中联皇冠"
                                      }
                                  }
                              },
                "userInfo":  {
                    "apiKey": "b1dc399d502a438dbabae9315bfc8e68",
                    "userId": "Bot"
                             }
                  }
    response = requests.post(url=url,json=data_param)
    py_json = response.text

    py_dict = json.loads(py_json)
    results_list = py_dict['results']
    results_0_dict = results_list[0]
    values_dict = results_0_dict['values']
    text_str = values_dict['text']
    print('二号：' + text_str)
    seq += 1
    if seq == limit:
      print("\n二号：聊天次数到了，亲爱的主人~ Miga多背一个单词，二号就能在地球上多待一会儿呢！")
      time.sleep(6)
      break
else:
  print("二号 Will Miss You, Have a Good Day!")
  time.sleep(6)