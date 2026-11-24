nombre = "Itau"
clientes = 1500
tasa = 0.035
activo = True
sin_dato = None            # equivale a NULL

print(type(tasa))
print(f"{nombre} tiene {clientes} clientes")
monto = int("2500")

mora_dias = 45
if mora_dias == 0:
    tramo = "al día"
elif mora_dias <= 30:
    tramo = "1-30"
elif mora_dias <= 90:
    tramo = "31-90"
else:
    tramo = "90+"
print(tramo)

for i in range(3):
    print(i)

n = 0
while n < 3:
    n += 1
    print(n)


    # Lista: ordenada y modificable
montos = [100, 250, 80]
montos.append(300)
print(montos[0], montos[-1], len(montos), sum(montos))

# Diccionario: clave -> valor (como una fila)
cliente = {"rut": "12345678-9", "saldo": 500000, "mora": 0}
print(cliente["saldo"])
cliente["segmento"] = "personas"

# Lista de diccionarios = una tabla
tabla = [
    {"rut": "1-9", "saldo": 100},
    {"rut": "2-7", "saldo": 900},
]

# Set: valores únicos (como DISTINCT)
unicos = set(["A", "B", "A"])   # {'A', 'B'}

# Tupla: lista que no se modifica
coordenada = (-33.53, -70.66)

altos = [t["rut"] for t in tabla if t["saldo"] > 500]

altos = []
for t in tabla:
    if t["saldo"] > 500:
        altos.append(t["rut"])

def calcular_tramo(dias: int) -> str:
    """Devuelve el tramo de mora según los días de atraso."""
    if dias <= 0:
        return "al día"
    if dias <= 30:
        return "1-30"
    if dias <= 90:
        return "31-90"
    return "90+"

print(calcular_tramo(0))

def es_par(numero: int) -> bool:
    return numero % 2 ==0

print(es_par(5))