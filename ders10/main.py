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
def iki_eded_cemi(a:int, b=5):
    """
    :param a: int
    :param b: int
    :return: int Iki ededin (a ve b) cemi
    """
    # global my_global_variable
    # my_global_variable = 5000
    # print(my_global_variable)
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
*args - tuple kimi davranış
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

def kwargslu_func(a, b=5, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

def argsli_func(*args):
    print(args)

kwargslu_func(5, 7, 8, 9, 3, c=7, f=6)
argsli_func(5, 3, 7, 6)


my_sq_function = lambda x, y: (x ** 2, y ** 2)
print(my_sq_function(30, 15))


if __name__ == '__main__':
    print(iki_eded_cemi(2))
    print(iki_eded_cemi(5, 2))
    print(iki_eded_cemi(4, 2))
    print(iki_eded_cemi(1, 5))