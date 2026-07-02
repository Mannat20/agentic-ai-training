# Keyword Arguments -> KeyWord Variable Arguments
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs)) # dictionary


fun(a=10, b=20, c=30, d='john')
fun(name='john', email='john@example.com', phone='+919876543210')


# INTERVIEW QUESTION
def fun(*args, **kwargs):                       
    print(args)
    print(kwargs)

fun(10, 'john', 30, a=10, b=20, c=30)