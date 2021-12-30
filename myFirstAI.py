import math
a = 0
b = 1000
tries = 0
lower_bound = a
upper_bound = b
guess = math.ceil((lower_bound+upper_bound)/2)
messeage = '''
If your answer is more than my guess, press '>' and then Enter.
If your answer is less than my guess, press '<' and then Enter.
If your answer is what I printed, press '=' and then Enter.
Have fun. Good luck. You can't beat me ;)
'''
print(messeage)    
ans = input(f'Choose a number between {a} and {b}\n\nIs it {guess}?')
lives = math.ceil(math.log2(b-a))
while tries <= lives:
    tries+=1
    if ans == '=':
        break
    elif ans == '<':
        # lower_bound = lower_bound
        upper_bound = guess
        guess = math.floor((lower_bound+upper_bound)/2)
        ans = input(f'Is it {guess}?')
    elif ans == '>':
        lower_bound = guess
        # upper_bound = upper_bound
        guess = math.ceil((lower_bound+upper_bound)/2)
        ans = input(f'Is it {guess}?')
    else:
        tries-=1
        ans = input(f'you can only enter >,< or =')
if ans == '=':
    print(f'I found the answer in {tries} tries. I am a genius :D Good luck!')
else:
    print(f"I did't find the answer in {tries+1} tries!!! It's weird\nI'm probably sure it's {guess} Sorry, but I think you cheated ;(")
