# use of _init_

class cake:

    #class attribute:
    info = 'This is cake class!'

    #instantiate attribute:
    def __init__(self, type_):
        self.type_ = type_

#instantiate the class:
obj = cake(type_ = 'veggie')

# Accessing the attribute:
print(f"\n I want a {obj.type_} cake")
