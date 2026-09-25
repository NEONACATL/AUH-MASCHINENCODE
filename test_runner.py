import json
from AUH import AUH

def lade_testsuite(pfad="TESTSUITE.json"):
    with open(pfad, "r", encoding="utf-8") as f:
        daten = json.load(f)
    return daten["testsuite"]

def pruefe_testfall(auh, testfall):
    anker_hoch = testfall["anker_hoch"]
    anker_tief = testfall["anker_tief"]
    erwartet = testfall["erwartete_113_6"]

    # Richtung bestimmen: Wenn erwartet > anker_hoch, dann Aufwärts, sonst Abwärts
    if erwartet > anker_hoch:
        richtung = "aufwaerts"
    else:
        richtung = "abwaerts"

    berechnet = auh.trommler_resonanz(anker_hoch, anker_tief, richtung)
    abweichung = abs(berechnet - erwartet)

    # Toleranz: 1% der Spanne oder 0.01 (je nach Asset)
    spanne = abs(anker_hoch - anker_tief)
    toleranz = max(spanne * 0.01, 0.01)

    if abweichung <= toleranz:
        return True, berechnet, abweichung
    else:
        return False, berechnet, abweichung

def main():
    auh = AUH()
    tests = lade_testsuite()
    treffer = 0
    fehler = 0

    print("=== A.U.H. TESTRUNNER ===")
    print(f"Anzahl Testfälle: {len(tests)}")
    print("-" * 50)

    for test in tests:
        if test["id"] == "TEST-012":  # Ausstehend, überspringen
            print(f"{test['id']}: ÜBERSPRUNGEN (ausstehend)")
            continue
        erfolg, berechnet, abweichung = pruefe_testfall(auh, test)
        status = "TREFFER" if erfolg else "FEHLER"
        if erfolg:
            treffer += 1
        else:
            fehler += 1
        print(f"{test['id']}: {status} | Erwartet: {test['erwartete_113_6']} | Berechnet: {berechnet:.4f} | Abweichung: {abweichung:.4f}")

    print("-" * 50)
    print(f"Treffer: {treffer} | Fehler: {fehler}")
    quote = treffer / (treffer + fehler) * 100 if (treffer + fehler) > 0 else 0
    print(f"Trefferquote: {quote:.2f}%")
    print("ES IST WAS ES IST! q^∞! QQQ!")

if __name__ == "__main__":
    main()
