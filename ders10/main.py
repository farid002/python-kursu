"""
FUNKSİYALAR
def açar sözü
"""

a = 5
my_global_variable = 100000

def salam_funksiyasi(firstname="Ali", lastname="Aliyev"):
    print(my_global_variable)
    global a
    print("global_a", a)
    print(f"Hello {firstname} {lastname}!")


"""
Parametrlər
Defolt dəyər
"""
def iki_eded_cemi(a, b):
    """
    :param a: int
    :param b: int
    :return: int Iki ededin (a ve b) cemi
    """
    global my_global_variable
    my_global_variable = 5000
    print(my_global_variable)
    return a + b

def two_numbers_separate_square(a, b):
    return a**2, b**2

# bir ulduz - args - list kimi davranir
def sum_of_numbers(*args):
    return sum(args)

# iki ulduz - kwargs - dict kimi davranir
def return_sum(a, b, **kwargs):
    return a + b, kwargs

def factorial(n):
    my_factorial = 1
    while n > 1:
        my_factorial *= n
        n -= 1
    return my_factorial

"""
return açar sözü
çoxsaylı return dəyəri
"""

"""
main funksiyası
"""

"""
*args - list kimi davranış
**kwargs - dict kimi davranış
"""

mult_function_lambda = lambda x, y: x * y

def square_function_normal(x):
    return x ** 2

"""
lambda funksiyaları (ananonim funksiyalar)
my_func = lambda b,c: b*c
my_func(1, 2)
"""

"""
global dəyişkənlər
"""


if __name__ == '__main__':
    salam_funksiyasi(lastname="Valiyev")
    print(iki_eded_cemi(1, 2))
    print(my_global_variable)