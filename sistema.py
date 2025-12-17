from typing import List, Dict, Callable, Tuple, Optional, Any
from dataclasses import dataclass

# Base para las reglas del sistema
@dataclass
class Regla:
    nom: str
    cond: Callable[[Dict[str, object]], bool]
    res: str

# Reglas individuales del sistema
def regla_caminar() -> Regla:
    return Regla(
        nom = "R1) Si la distancia es corta y el clima es bueno -> caminar",
        cond = lambda h: (h.get("distancia") == "corta" and h.get("clima") == "bueno"),
        res = "caminar",
    )
def regla_autobus() -> Regla:
    return Regla(
        nom="R2) Si la distancia es media y hay transporte publico -> autobus",
        cond = lambda h: (h.get("distancia") == "media" and h.get("transporte_pub") is True),
        res = "autobus",
    )
def regla_automovil() -> Regla:
    return Regla(
        nom="R3) Si la distancia es larga -> automovil",
        cond = lambda h: (h.get("distancia") == "larga"),
        res = "automovil",
    )

# Motor de inferencia
class MotorInferencia:
    def __init__(self, reglas: List[Regla]):
        self.reglas = reglas

    # Inferir dinamicamente las reglas
    def inferir(self, hechos: Dict[str, object]) -> Tuple[Optional[Regla], Optional[str]]:
        for regla in self.reglas:
            if regla.cond(hechos):
                return regla, regla.res
        return None, None

# Para mostrar la inferencia de los casos de prueba
def mostrar_inf(num: int, hechos: Dict[str, object], motor: MotorInferencia):
    print(f"--- Caso de prueba #{num} ---")
    print("Hechos:")
    for k, v in hechos.items():
        print(f"  > {k}: {v}")

    regla, rec = motor.inferir(hechos)
    if regla is None:
        print(f"Regla: Ninguna")
        print(f"Recomendacion: No se pudo inferir una recomendacion")
    else:
        print(f"Regla: {regla.nom}")
        print(f"Recomendacion: {rec}\n")


def main():
    # Juntar los pedazos de info dentro del main
    reglas = [regla_caminar(), regla_autobus(), regla_automovil()]  # En orden
    motor = MotorInferencia(reglas)

    # Casos de prueba
    casos = [
        {
            "distancia": "corta",
            "clima": "bueno",
            "transporte_pub": False,
        },
        {
            "distancia": "media",
            "clima": "malo",
            "transporte_pub": True,
        },
        {
            "distancia": "larga",
            "clima": Any,
            "transporte_pub": Any,
        },
    ]

    for i, hechos in enumerate(casos, start=1):
        mostrar_inf(i, hechos, motor)

if __name__ == "__main__":
    main()
