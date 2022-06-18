import time
import random
import os

answers = ["Absolutely","yes","no","not at all","never","Yes!","maybe"]

print("Type your question")
user = input("-> ")

os.system('clear')
print("Thinking.")
time.sleep(0.5)
os.system('clear')
print("Thinking..")
time.sleep(0.5) 
os.system('clear')
print("Thinking...")
time.sleep(0.5)

os.system('clear')
if "?" not in user:
   print(user + "?")
   print(random.choice(answers))
else:
   print(user)
   print(random.choice(answers))
