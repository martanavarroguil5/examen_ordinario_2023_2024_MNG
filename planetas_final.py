from EstrellaDeLaMuerte import EstrellaDeLaMuerteClase
from planetas import Planeta

Concordia = Planeta("Concordia", 500, 1)
Ilum = Planeta("Ilum", 1200, 2)
Kamino = Planeta("Kamino", 800, 3)

Estrella_de_la_muerte = EstrellaDeLaMuerteClase(1000)

Estrella_de_la_muerte.destruir_planeta(Concordia)
Estrella_de_la_muerte.destruir_planeta(Ilum)
Estrella_de_la_muerte.destruir_planeta(Kamino)