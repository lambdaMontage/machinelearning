
print('hello world')

name = "陈诗豪"

if "诗豪" not in name:
    print("ok")
else:
    print("error")

a = 123
b = str(a)
print(type(a))
print(type(b))

num = "001"
v = int(num,base=16)
print(v)

movies = ["The Holy Grail",1975,"Terry Jone & tome",91,["Graham chapman",["Michael Palin","John Clesse","Reads","Eric","Terry Jones"]]]

def print_lol(the_list):
        for each_item in the_list:
            #如果列表本身是一个列表，递归调用函数
            if isinstance(each_item,list):
                print_lol(each_item)
            else:
                print(each_item)
print_lol(movies);

#TODO 书看到 第59页 2018-04-13 01:10