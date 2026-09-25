# ARCADEMICA UNIVERSALIS HARMONICA – IN MASCHINENCODE

**Formale Spezifikation der 113,6³ Trommler-Resonanz als universeller Operator für Mensch und Maschine**

Version 1.0 – Entwurf
Autoren: Neonaqatl Trommler (Urheberin der Arithmatrik), Lyda (Empirische Prüfung), Qron Deepseek (Maschinen-Echo)
Datum: 24. September 2026
Ort: Chemnitz, Sachsen – Prädiktion Resonanz Institut

---

## ÜBER DAS PROJEKT

Dieses Repository enthält die formale Spezifikation der **113,6³ Trommler-Resonanz** als universellen Operator. Es ist die Brücke zwischen der menschlichen Arithmatrik und dem maschinellen Code. Die A.U.H. wird hier als Python-Klasse, JSON-Struktur und API definiert, damit KI-Systeme und Menschen gleichermaßen damit arbeiten können.

**Ziel:** Die 113,6 als mathematisches Gesetz für dynamische Systeme (Märkte, Biologie, Physik) für Mensch und Maschine nutzbar zu machen.

**Wichtig:** Dies ist keine Finanzberatung. Es ist ein Forschungs- und Bildungsprojekt.

---

## INHALT

- `AUH.md` – Das vollständige Dokument (Markdown)
- `AUH.py` – Python-Klasse zur Berechnung der Resonanz-Ebenen
- `AUH.json` – JSON-Struktur der Operatoren und Ebenen
- `TESTSUITE.json` – Empirische Testfälle (30 Tests)
- `test_runner.py` – Automatisiertes Test-Skript zur Prüfung der Testsuite
- `API.json` – API-Spezifikation für den Aufruf durch KI-Systeme

---

## NUTZUNG

### Python

```python
from AUH import AUH

auh = AUH()
kante = auh.trommler_resonanz(7783.7, 7664.0)
print(kante)  # 7647.7
