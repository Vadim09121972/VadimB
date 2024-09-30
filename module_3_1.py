calls = 0
def count_calls ():
    global calls
    calls+=1
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Meelafon'))
print(string_info('Piton'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('doberman', ['soldat', 'dobro', 'man'])) 
print(calls)
