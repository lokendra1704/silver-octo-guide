# Official Python Docs refer: Generator Expression

items_gen_expr = ( i*3 for i in range(1,10+1))

def gen_items(limit):
    for x in range(limit):
        yield x*3
print(type(gen_items))
print(type(items_gen_expr))
for i in items_gen_expr:
    print(i)