# Bisection Method / Método de Bisección
# Finds an approximate root of f(x) = 0 within an interval.
# Encuentra una raíz aproximada de f(x) = 0 dentro de un intervalo.


def biseccion(f, a, b, tol=1e-6, max_iter=100):
    """
    Bisection Method / Método de Bisección

    Parameters / Parámetros:
        f        : Function to evaluate / Función a evaluar
        a, b     : Initial interval endpoints / Extremos del intervalo inicial
        tol      : Error tolerance / Tolerancia del error
        max_iter : Maximum number of iterations / Máximo de iteraciones

    Returns / Retorna:
        Approximate root / Raíz aproximada
    """

    # Check the initial interval has a sign change.
    # Verifica que el intervalo inicial tenga un cambio de signo.
    if f(a) * f(b) >= 0:
        raise ValueError(
            "The interval must satisfy f(a) * f(b) < 0. "
            "El intervalo debe cumplir f(a) * f(b) < 0."
        )

    print(f"{'Iter':<5} {'a':<12} {'b':<12} {'c':<12} "
          f"{'f(a)':<12} {'f(b)':<12} {'f(c)':<12}")

    # Bisection iterations / Iteraciones del método de bisección
    for k in range(1, max_iter + 1):

        # Calculate the midpoint.
        # Calcula el punto medio.
        c = (a + b) / 2

        fa = f(a)
        fb = f(b)
        fc = f(c)

        print(f"{k:<5} {a:<12.10f} {b:<12.10f} "
              f"{c:<12.10f} {fa:<12.10f} "
              f"{fb:<12.10f} {fc:<12.10f}")

        # Stop when the function value or interval size
        # is smaller than the required tolerance.
        # Detiene el método cuando el valor de la función
        # o el tamaño del intervalo es menor que la tolerancia.
        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"\nConvergence reached in {k} iterations.")
            print(f"Convergencia alcanzada en {k} iteraciones.")
            return c

        # Keep the half-interval where the sign changes.
        # Conserva la mitad del intervalo donde existe cambio de signo.
        if fa * fc < 0:
            b = c
        else:
            a = c

    print("\nMaximum number of iterations reached.")
    print("Se alcanzó el número máximo de iteraciones.")

    return c


# ============================================================
# Example / Ejemplo
# f(x) = x^3 - x - 2
# ============================================================

def f(x):
    return x**3 - x - 2


# Initial interval: [1, 2]
# Intervalo inicial: [1, 2]
root = biseccion(f, 1, 2, tol=1e-10)

print(f"\nApproximate root / Raíz aproximada = {root:.8f}")
print(f"f(root) / f(raíz) = {f(root):.8e}")