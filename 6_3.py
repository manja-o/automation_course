# task_3 - Two functions to work with datatype

def receive_value():
    value = input("Please, enter some value: ")
    return value


def return_data_type(data):
    try:
        data_type = type(eval(data))
        print(f'User is going to work with {data_type}')
    except Exception:
        print('Sorry, something went wrong')


user_data = receive_value()
return_data_type(user_data)
