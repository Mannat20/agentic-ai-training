# Variable Arguments in Python
def fun(*args):
    print('args:', args)
    print('args type:', type(args)) #tuple
    print('sum of args:', sum(args))

fun(10, 20, 30, 40, 50)
fun(10, 20, 30)
fun(10,20,20)
fun(-10,-20)