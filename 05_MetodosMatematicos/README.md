# Numerical Methods

Implementations of numerical methods in Python for solving mathematical problems and finding roots of equations.

## Methods

### 1. Bisection Method

The Bisection Method finds an approximate root of a function by repeatedly dividing an interval into two halves.

**Main concepts:**
- Sign change
- Midpoint calculation
- Error tolerance
- Iterative approximation

File: [`01_biseccion.py`](./01_biseccion.py)

---

### 2. Secant Method

The Secant Method finds an approximate root using two initial approximations and the secant line between them.

**Main concepts:**
- Two initial approximations
- Iterative approximation
- Secant formula
- Error tolerance

File: [`02_secante.py`](./02_secante.py)

---

### 3. Multiple Linear Regression

Multiple Linear Regression fits a linear model with several independent variables to a set of observations using the least squares method, by building and solving the normal equations.

**Main concepts:**
- Design matrix `X` (with a column of ones for the intercept)
- Normal equations: `(XᵀX)a = Xᵀy`
- Least squares solution
- Coefficient of determination (R²)

**Input:** a CSV file (`Casos.csv`) in the same folder as the script. Each row is an observation, the first columns are the independent variables (`x1, x2, ..., xn`) and the **last column is `y`**. A header row is optional and values must be separated by commas.

```csv
x1,x2,y
2,1,23
3,2,30
4,2,34
5,3,42
6,4,51
7,4,55
8,5,64
9,6,72
```

**Output:** the coefficients `a0, a1, ..., an`, the fitted model and R². For the data above:

```text
y = 9.6667 + 3.9333·x1 + 4.4667·x2
R² = 0.998959
```

**Usage:**

```bash
python 03_regresion_lineal_multiple.py
```

File: [`03_regresion_lineal_multiple.py`](./03_regresion_lineal_multiple.py)

---

## Example Function

Methods 1 and 2 use:

```text
f(x) = x³ - x - 2
```