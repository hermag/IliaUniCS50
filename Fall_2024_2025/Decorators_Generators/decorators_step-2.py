def decorator(func):                    # [step-2]
    def inner_func(*args, **kwargs):    # [step-3] [step-6]
        print("Inside decorator")       # [step-7]
        output = func(*args, **kwargs)  # [step-8]
        print("Function is executed")   # [step-12]
        return output                   # [step-13]
    return inner_func                   # [step-4]   

def used_func(a, b):                    # [step-9]
    print("Function is executing")      # [step-10]
    return a + b                        # [step-11]


used_func = decorator(used_func)        # [step-1]

used_func(1, 2)                         # [step-5] [step-14]

@decorator
def used_func(a, b):
    print("Function is executing")
    return a + b 

used_func(1, 2)   