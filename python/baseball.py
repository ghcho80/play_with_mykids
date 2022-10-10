import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(numbers)

three_numbers = numbers[:3]
hidden_numbers = "".join(three_numbers)
#print(hidden_number)
answer = input()
#print(answer, hidden_numbers)

count = 0
while answer != hidden_numbers:
    count = count + 1
    strike = 0
    ball = 0
    if answer[0] in hidden_numbers:
        if answer[0] == hidden_numbers[0]:
            strike = strike + 1
        else:
            ball = ball + 1
    if answer[1] in hidden_numbers:
        if answer[1] == hidden_numbers[1]:
            strike = strike + 1
        else:
            ball = ball + 1
    if answer[2] in hidden_numbers:           
        if answer[2] == hidden_numbers[2]:
            strike = strike + 1
        else:
            ball = ball + 1
    print("Strike: %d, Ball: %d" % (strike, ball))
    if strike == 3: break
    answer = input()
        
print("%d 번만에 맞추셨습니다. 축하합니다!" % (count))

