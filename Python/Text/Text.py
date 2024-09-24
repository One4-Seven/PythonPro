from function import make_name
from function import collect_info

print("Press [Quit] to end the program!")
while True:
    first = input("Please give me the first name: ")
    if first.lower() == 'quit':
        break
    middle = input("Please give me the middle name: ")
    if middle.lower() == 'quit':
        break
    last = input("Please give me the last name: ")
    if last.lower() == 'quit':
        break
    really_name = make_name(first,last,middle)    
    print(f"The really name for you is {really_name}")

collections = collect_info()    # 创建实例 #
print("Press [Quit] to end the collect")
while True:
    answer = input("Please tell me the first language you learn: ")
    if answer.lower() != 'quit':
        collections.collect(answer)
    else:
        break

collections.show()
