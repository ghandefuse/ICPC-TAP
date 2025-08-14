PosVic=[
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[6,4,2]
]


def ganador(tablero):
    for comb in PosVic:
        if all(tablero[pos] == 1 for pos in comb):
            return 1
        if all(tablero[pos] == 2 for pos in comb):
            return -1
    if all(val != 0 for val in tablero):
        return 0
    return None


def posvalida(b,tablero,restricciones):
    if tablero[b] != 0:
        return False
    for a in restricciones[b]:
        if tablero[a] == 0:
            return False
    return True


memo = {}


def DFSGOAT(tablero, restricciones, turno):
    clave = (
        tuple(tablero),
        turno,
        tuple(frozenset(r) for r in restricciones)
    )
    if clave in memo:
        return memo[clave]

    estado = ganador(tablero)
    if estado is not None:
        memo[clave] = estado
        return estado

    mejor_valor = -999 if turno == 0 else 999
    jugada_posible = False

    for i in range(9):
        if posvalida(i, tablero, restricciones):
            jugada_posible = True
            Resguardo_Resc = [set(r) for r in restricciones]
            tablero[i] = 1 if turno == 0 else 2
            eliminarres(i, restricciones)
            valor = DFSGOAT(tablero, restricciones, 1 - turno)
            tablero[i] = 0
            for j in range(9):
                restricciones[j] = set(Resguardo_Resc[j])

            if turno == 0:
                mejor_valor = max(mejor_valor, valor)
            else:
                mejor_valor = min(mejor_valor, valor)

    if not jugada_posible:
        memo[clave] = 0
        return 0

    memo[clave] = mejor_valor
    return mejor_valor


def eliminarres(b,restricciones):
    for i in range(9):
        if b in restricciones[i]:
            restricciones[i].remove(b)

turno=0
tablero=[0]*9
restricciones =[set() for i in range(9)]
n=int(input())
for i in range(n):
    a, b = map(int, input().split())
    restricciones[b-1].add(a-1)

resultado_final = DFSGOAT(tablero, restricciones, turno)

if resultado_final == 1:
    print("X")
elif resultado_final == -1:
    print("O")
else:
    print("E")
