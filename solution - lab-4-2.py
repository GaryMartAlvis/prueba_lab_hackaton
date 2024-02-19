from typing import Tuple


db = set()
db.add(("Cliente B", "Hamburguesa", "Papas Fritas"))
db.add(("Cliente A", "Hamburguesa", "Refresco"))

def almacenar_orden(orden: Tuple[str, ...]) -> bool:
    if orden in db:
        return False
    else:
        db.add(orden)
        return True
