
import math

def q_solve(a, b, c):
    D = b**2 - 4*a*c

    if D < 0:
        print("The equation has no real solutions.")

    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"The solutions are: x1 = {x1}, x2 = {x2}")


print("Quadratic Equation Solver")
print("-------------------------")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

q_solve(a, b, c)


