class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info()

# class D(A, C):
#    pass

# Now when you run the code (the code is presented in the right pane, implement the change), you get:

# Traceback (most recent call last):
#  File "diamond.py", line 13, in 
#    class D(A, C):
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C