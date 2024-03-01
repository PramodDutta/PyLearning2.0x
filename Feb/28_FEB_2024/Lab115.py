# Single - 80%
# Multiple
# Multi level
# Hybrid
# Heri

# API, Web Automation - 80% -> Single

# Multilevel Inheritance

class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    def child_method(self):
        return "Child's method"


child = Child()

# parent ref = parent Object()
parent = Parent()
parent.parent_method()
parent.grandparent_method()


#
grandparent_ref = Grandparent()
grandparent_ref.grandparent_method()



print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())