import sys
import os
import numpy as np


def regresionLinealMultiple(x, y, mostrar_sistema=False):
    """
    Regresión Lineal Múltiple / Multiple Linear Regression

    Parámetros:
        x : arreglo de forma (m, n)  -> m observaciones, n variables independientes
        y : arreglo de forma (m,)    -> variable dependiente

    Se construye el sistema normal lineal (X^T X) a = X^T y, de dimensión (n+1),
    donde X es x con una columna de unos para el término independiente a0.

    Devuelve:
        a  : coeficientes [a0, a1, ..., an]
        r2 : coeficiente de determinación R^2
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float).ravel()
    if x.ndim == 1:
        x = x.reshape(-1, 1)

    m, n = x.shape
    if m <= n:
        raise ValueError(f"Se necesitan más observaciones (m={m}) que variables (n={n}).")

    X = np.column_stack([np.ones(m), x])   # (m, n+1)
    A = X.T @ X                            # sistema normal, (n+1)x(n+1)
    b = X.T @ y

    try:
        a = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        # variables dependientes entre sí (matriz singular): mínimos cuadrados robusto
        a = np.linalg.lstsq(X, y, rcond=None)[0]

    if mostrar_sistema:
        np.set_printoptions(suppress=True, linewidth=120)
        print("Matriz X (con columna de unos):\n", X)
        print("\nX^T X =\n", A)
        print("\nX^T y =\n", b)

    y_est = X @ a
    ss_res = np.sum((y - y_est) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return a, r2


def cargar_csv(ruta):
    """Lee un CSV: columnas = variables x1..xn, ÚLTIMA columna = y. Acepta encabezado."""
    try:
        datos = np.loadtxt(ruta, delimiter=",")
    except ValueError:
        datos = np.loadtxt(ruta, delimiter=",", skiprows=1)
    return datos[:, :-1], datos[:, -1]


def imprimir_resultado(a, r2):
    print("\nModelo: y = " + " + ".join(
        [f"{a[0]:.6g}"] + [f"{c:.6g}*x{i}" for i, c in enumerate(a[1:], start=1)]))
    for i, c in enumerate(a):
        print(f"  a{i} = {c:.6g}")
    print(f"  R^2 = {r2:.6f}")


if __name__ == "__main__":
    carpeta = os.path.dirname(os.path.abspath(__file__))
    archivo = sys.argv[1] if len(sys.argv) > 1 else os.path.join(carpeta, "Casos.csv")
    if True:
        x, y = cargar_csv(archivo)
        print(f"Datos cargados: {x.shape[0]} observaciones, {x.shape[1]} variables.")
    else:
        # Ejemplo: n = 2 variables, m = 8 observaciones
        print("Sin archivo CSV: usando datos de ejemplo (n=2, m=8).")
        x = np.array([[0, 0], [2, 1], [2.5, 2], [1, 3],
                      [4, 6], [7, 2], [3, 4], [5, 5]])
        y = np.array([5, 10, 9, 0, 3, 27, 7, 8])

    a, r2 = regresionLinealMultiple(x, y, mostrar_sistema=True)
    imprimir_resultado(a, r2)