def arithmetic_operation(operation):
    if (operation == '+'):
        return lambda x, y: x+y
    elif (operation == '-'):
        return lambda x, y: x-y
    elif (operation == '*'):
        return lambda x, y: x*y
    elif (operation == '/'):
        return lambda x, y: x/y
func = arithmetic_operation('/')
print(func(1,4))

def simple_map(transformation, values):
    result = [transformation(value) for value in values]
    return result
values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))

romannumbers = {9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
global one, two, three
one = 5
two = 4
three = 9
def roman(one, two):
    three = one + two
    rone = romannumbers.get(one)
    rtwo = romannumbers.get(two)
    rthree = romannumbers.get(three)
    print(rone, '+', rtwo, '=', rthree)
roman(one, two)
print(one, '+', two, '=', three)

def get_transactions(st):
    global transactions
    if st == 'print_it':
        for transaction in transactions:
            print(transaction[0], transaction[1], transaction[2])
    else:
        phone, action = st.split('-')
        action_type, amount = action.split(':')
        amount = int(amount)

        for transaction in transactions:
            if transaction[1] == action_type:
                transaction[0] += 1
                transaction[2] += amount
                break
        else:
                transactions.append([1, action_type, amount])


transactions = []
get_transactions('880005553535-перевод:100')
get_transactions('111111111-перевод:1000')
get_transactions('880005553535-оплата_жкх:10000')
get_transactions('89065664312-перевод:50000000')
get_transactions('print_it')

def same_by(charecteristic, objects):
    if len(objects) == 0:
        return True
    first_value = charecteristic(objects[0])
    for obj in objects:
        if charecteristic(obj) != first_value:
            return False
    return True

values = [0, 2, 10, 6, 7]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')