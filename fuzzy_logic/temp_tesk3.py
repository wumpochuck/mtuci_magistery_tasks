import numpy as np
import matplotlib.pyplot as plt


def F(A, U=None, m=None):
    """Возвращает дополнение дискретного или непрерывного нечеткого множества."""
    if m is not None:
        return lambda x: 1 - m(x)

    if U is None:
        raise ValueError("Для дискретного множества необходимо указать универсум U")

    return {x: 1 - A.get(x, 0) for x in U}


# Дискретный случай
U = {1, 2, 3, 4, 5}
A = {1: 0.1, 2: 0.4, 3: 0.7, 4: 1.0}
A_complement = F(A, U)

print(f"Универсум U: {U}")
print(f"Нечеткое множество A: {A}")
print(f"Дополнение A: {A_complement}")


# Непрерывный случай: гауссова функция принадлежности
x = np.linspace(-5, 5, 500)
mu_A = lambda x: np.exp(-(x - 1) ** 2 / 2)
mu_not_A = F(None, m=mu_A)

plt.figure(figsize=(8, 4))
plt.plot(x, mu_A(x), label="A: μA(x)")
plt.plot(x, mu_not_A(x), label="Дополнение: 1 - μA(x)")
plt.xlabel("x")
plt.ylabel("Степень принадлежности")
plt.title("Дополнение непрерывного нечеткого множества")
plt.ylim(0, 1.1)
plt.grid(True)
plt.legend()
plt.show()