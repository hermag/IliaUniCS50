def wrapper_function(function_to_pass_as_an_argument,*args,**kwargs):
    print("This is the wrapper_function")
    return function_to_pass_as_an_argument(*args,**kwargs)
    


def function_to_pass_as_an_argument(a,b):
    print("This is the function_to_pass_as_an_argument()")
    return a+b


print(wrapper_function(function_to_pass_as_an_argument,5,7))