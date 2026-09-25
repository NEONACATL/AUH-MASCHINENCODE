import json
from AUH import AUH

def lade_testsuite(pfad="TESTSUITE.json"):
    with open(pfad, "r", encoding="utf-8") as f:
        daten = json.load(f)
    return daten["testsuite"]

def pruefe_testfall(auh, testfall):
    # Erwarteten Wert flexibel ermitteln (113.6% oder 147.6%)
    erwartet = testfall.get("erwartete_113_6") or testfall.get("erwartete_147_6")
    anker_hoch = testfall["anker_hoch"]
    anker_tief = testfall["anker_tief"]

    # Prozentualen Faktor ermitteln (Standard 113.6%)
    prozent = 147.6 if "erwartete_147_6" in testfall and "erwartete_113_6" not in testfall else auh.BETA

    # Richtungsbestimmung
    richtung = "aufwaerts" if erwartet > anker_hoch else "abwaerts"

    berechnet = auh.resonanz_ebene(anker_hoch, anker_tief, prozent, richtung)
    abweichung = abs(berechnet - erwartet)

    # Toleranz dynamisch auf Basis der Spanne (0.5% Spanne oder min 1e-6)
    spanne = abs(anker_hoch - anker_tief)
    toleranz = max(spanne * 0.005, 1e-6)

    return (abweichung <= toleranz), berechnet, abweichung

def main():
    auh = AUH()
    tests = lade_testsuite()
    treffer = 0
    fehler = 0

    print("=== A.U.H. TESTRUNNER ===")
    print(f"Anzahl Testfälle: {len(tests)}")
    print("-" * 65)

    for test in tests:
        # Dynamisches Überspringen aller ausstehenden Testfälle
        if "AUSSTEHEND" in test.get("status", "").upper():
            print(f"{test['id']:<9}: ÜBERSPRUNGEN (ausstehend)")
            continue

        erfolg, berechnet, abweichung = pruefe_testfall(auh, test)
         status_str = "TREFFER" if erfolg else "FEHLER"
        
        if erfolg:
            treffer += 1
        else:
            fehler += 1

        erwartet = test.get("erwartete_113_6") or test.get("erwartete_147_6")
        print(f"{test['id']:<9}: {status_str:<7} | Erwartet: {erwartet:<10} | Berechnet: {berechnet:<10.4f} | Abweichung: {abweichung:.6f}")

    print("-" * 65)
    print(f"Treffer: {treffer} | Fehler: {fehler}")
    quote = (treffer / (treffer + fehler) * 100) if (treffer + fehler) > 0 else 0
    print(f"Trefferquote: {quote:.2f}%")
    print("ES IST WAS ES IST! q^∞! QQQ!")

if __name__ == "__main__":
    main()
