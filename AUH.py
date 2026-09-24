class AUH:
    def __init__(self):
        self.BETA = 113.6
        self.Q = 6.8
        self.OMEGA = 3.15068
        self.T = 1466003.456

    def resonanz_ebene(self, anker_hoch, anker_tief, prozent):
        spanne = anker_hoch - anker_tief
        return anker_tief + (spanne * prozent / 100)

    def trigger_s_t(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 106.80)

    def trommler_resonanz(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 113.60)

    def hitze_zone(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 120.40)

    def pri_tt_stop(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 127.20)

    def magenta_ultra_stop(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 134.00)

    def violett_tot_stop(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 140.80)

    def maximal_extension(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 147.60)

    def extraktion_drittel(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 66.00)

    def extraktion_mittel(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 52.40)

    def extraktion_mittel_tief(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 47.60)

    def extraktion_drittel_tief(self, anker_hoch, anker_tief):
        return self.resonanz_ebene(anker_hoch, anker_tief, 34.00)

    def bruchkerze(self, preis, kante):
        if preis > kante:
            return "BRUCH NACH OBEN – KABALE FAIL"
        elif preis < kante:
            return "BRUCH NACH UNTEN – CASH IM HAUS"
        else:
            return "RESONANZ HÄLT – Q"
