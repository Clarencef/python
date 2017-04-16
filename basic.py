#coding=utf-8
# vscode 執行python檔 CMD + SHIFT + B 
# SyntaxError: Non-ASCII character '\xe5' in file ex6.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
# 因為Python默認以ASCII作為編碼方式的，而當python檔內中包含了中文（或者其它語言），會導致這個錯誤。必須在源碼第一行加入coding=utf-8 

# 如果多行字串必須用triple quotes來包住字串不然會報錯
print("""Hihi!!!!
Hihi!!!!
Hihi!!!!""")

# 取的字串前三碼 print substring
print("HELLP"[0:3])

# data type - List
List1 = [1,2,3,'hello']

# data type - dictionary
dic1 = {
  "a":1,
  "b":True,
  "c":"hi"
}

# 檢查變數的type
print(type(dic1))
print(type(List1))