def count_calls():
    global calls
    calls += 1


def is_contains(string, list_to_search):
    count_calls()
    for str in list_to_search:
        if string.lower() == str.lower():
            return True #  , f'{string} ~ {str}'
    return False

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Ecclesiastes'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('aBcD', ['bAbcd', 'abcd ', 'AbCd']))
print(calls)