import math

class QuadraticEquationSolver:
    
    def findRoots(self, a, b, c):

        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return "No Real Roots"
        
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
        return root1, root2

solver = QuadraticEquationSolver()
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = solver.findRoots(a, b, c)
print("The roots of the equation are:", roots)
