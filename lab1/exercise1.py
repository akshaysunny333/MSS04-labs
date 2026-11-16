
import math

def q_solve(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"The solutions are: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x1 = -b / (2 * a)
        print(f"One real solution: x = {x1}")
    else:
        real_part = -b / (2 * a)
        imag_part = ((-D)**0.5) / (2 * a)
        x1 = real_part + imag_part * 1j
        x2 = real_part - imag_part * 1j
        print(f"Two complex solutions: x1 = {x1}, x2 = {x2}")



print("Quadratic Equation Solver")
print("-------------------------")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

q_solve(a, b, c)


