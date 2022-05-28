import numpy as np
import sympy as sm


def lagrange(x, y):
    _x = sm.Symbol('x')
    result = 0
    for i in range(len(x)):
        temp = 1
        for j in range(len(x)):
            if j != i:
                temp *= (_x - x[j]) / (x[i] - x[j])
        temp *= y[i]
        result += temp
    return result


def coefficient(x, y):
    m = len(x)

    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (x[k:m] - x[k - 1])

    return a


def _newton(x_data, y_data, x):
    a = coefficient(x_data, y_data)
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k]) * p

    return p


def task1():
    print("===================================\nTASK 1\n")

    x = np.array([0.68, 0.73, 0.8, 0.88, 0.93, 0.99], float)
    y = np.array([0.80866, 0.89492, 1.02964, 1.20966, 1.34087, 1.52368], float)
    a = np.array([0.896, 0.812, 0.774, 0.955, 0.715], float)

    f = lagrange(x, y)
    f = sm.expand(f)
    print("Lagrange interpolation polynomial\nL(x) =", f, "\n")

    for i in range(len(a)):
        print(f"L({a[i]}) = {f.subs('x', a[i])}")

    #sm.plot(f)
    for i in range(len(x)):
        print(y[i])


def task2():
    print("\n===================================\nTASK 2\n")

    x = np.array([3.50, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80,
                  3.85, 3.90, 3.95, 4.00, 4.10, 4.15, 4.20], float)

    y = np.array([33.1154, 34.8133, 36.5982, 38.4747, 40.4473, 42.5211, 44.7012,
                  46.9931, 49.4024, 51.5982, 57.3975, 60.3403, 63.4340, 66.6863], float)

    a = np.array([3.522, 4.176, 3.475, 4.25], float)

    for i in range(len(a)):
        print(f"L({a[i]}) = {_newton(x, y, a[i])}")


task1()
task2()
