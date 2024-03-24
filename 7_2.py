# task_2 - using lambda for raising number to a power

def func(x: int):
    return lambda y: pow(y, x)


power_of_3 = func(3)
print(power_of_3(2))  # 2^3 = 8

