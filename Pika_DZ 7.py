# Ex_1
from datetime import datetime
def working_hours_only(func):
    def wrapper():
        f = datetime.strptime('9:00', '%H:%M').time()
        d = datetime.strptime('18:00','%H:%M').time()
        now = datetime.now().time()
        if f <= now <= d:
            func()
        else:
            print('Работать нельзя!!!!!!')
    return wrapper


@working_hours_only
def work():
    print('Работаем')
work()

# Ex_2

def type_check(correct_type):
    def f(func):
        def wrapper(arg1):
            if type(arg1) is correct_type:
                return func(arg1)
            return 'Bad type'
        return wrapper
    return f

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2(True))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(1.5))
