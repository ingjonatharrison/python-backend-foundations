"""
Secant Method / Método de la Secante

Finds an approximate root of f(x) = 0 using two initial points.
Encuentra una raíz aproximada de f(x) = 0 usando dos puntos iniciales.

Example / Ejemplo:
    f(x) = x^3 - x - 2
"""


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Secant Method / Método de la Secante

    Parameters / Parámetros:
        f        : Function to evaluate / Función a evaluar
        x0, x1   : Initial approximations / Aproximaciones iniciales
        tol      : Error tolerance / Tolerancia del error
        max_iter : Maximum number of iterations / Máximo de iteraciones

    Returns / Retorna:
        Approximate root and number of iterations.
        Raíz aproximada y número de iteraciones.
    """

    f0 = f(x0)
    f1 = f(x1)

    print(
        f"{'k':>2} {'x_(k-1)':>14} {'x_k':>14} "
        f"{'f(x_(k-1))':>14} {'f(x_k)':>14} "
        f"{'x_(k+1)':>14} {'|dx|':>14}"
    )

    # Secant iterations / Iteraciones del método de la secante
    for k in range(max_iter):

        # Avoid division by a value too close to zero.
        # Evita dividir entre un valor demasiado cercano a cero.
        if abs(f1 - f0) < 1e-15:
            raise ZeroDivisionError(
                "Division by zero or very small difference. "
                "División por cero o diferencia demasiado pequeña."
            )

        # Secant formula / Fórmula de la secante
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        print(
            f"{k:2d} {x0:14.9f} {x1:14.9f} "
            f"{f0:14.9e} {f1:14.9e} "
            f"{x2:14.9f} {abs(x2 - x1):14.9e}"
        )

        # Stop when the change between approximations is below the tolerance.
        # Detiene el método cuando el cambio entre aproximaciones
        # es menor que la tolerancia.
        if abs(x2 - x1) < tol:
            return x2, k + 1

        # Update the previous and current approximations.
        # Actualiza las aproximaciones anterior y actual.
        x0, x1 = x1, x2
        f0, f1 = f1, f(x1)

    return x1, max_iter


# ============================================================
# Example / Ejemplo
# f(x) = x^3 - x - 2
# ============================================================

def f(x):
    return x**3 - x - 2


if __name__ == "__main__":
    root, iterations = secante(
        f,
        1.0,
        2.0,
        tol=1e-6
    )

    print("\nResults / Resultados")
    print("-" * 40)
    print(f"Approximate root / Raíz aproximada : {root:.12f}")
    print(f"Iterations / Iteraciones            : {iterations}")
    print(f"f(root) / f(raíz)                    : {f(root):.12e}")