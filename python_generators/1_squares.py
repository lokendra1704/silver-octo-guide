def gen_squares(max_root):
    for i in range(1,max_root+1):
        yield i**2

squares = gen_squares(10)   #Returns a Generator Object
type(squares)
