x1 = 2
xn = 5
dx = 0.1
a = 4
b = 7
x = x1
while x <= xn:
    f = a * x + b
    print(f"x = {x:.1f}, f(x) = {f:.3f}")
    x += dx
