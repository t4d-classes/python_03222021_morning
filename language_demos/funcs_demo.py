

# dict(first_name="Bob", last_name="Smith")

def do_it(a,b,*args, **kwargs):
    print(a,b,args, kwargs)

do_it(1,2,3,4,5, first="cool", second="awesome", third="nice")
