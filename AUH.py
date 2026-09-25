class AUH:
    def __init__(self):
        self.BETA = 113.6
        self.Q = 6.8
        self.OMEGA = 3.15068
        self.T = 1466003.456

    def resonanz_ebene(self, anker_hoch: float, anker_tief: float, prozent: float, richtung: str = "abwaerts") -> float:
        spanne = anker_hoch - anker_tief
        if richtung == "abwaerts":
            # Projektion nach unten (z.B. Tiefstwerte-Suche)
            return anker_hoch - (spanne * (prozent / 100.0))
        else:
            # Projektion nach oben
            return anker_tief + (spanne * (prozent / 100.0))

    def trommler_resonanz(self, anker_hoch: float, anker_tief: float, richtung: str = "abwaerts") -> float:
        return self.resonanz_ebene(anker_hoch, anker_tief, self.BETA, richtung)

    def bruchkerze(self, preis: float, kante: float) -> str:
        if preis > kante:
            return "BRUCH NACH OBEN – KABALE FAIL"
        elif preis < kante:
            return "BRUCH NACH UNTEN – CASH IM HAUS"
        else:
            return "RESONANZ HÄLT – Q"
