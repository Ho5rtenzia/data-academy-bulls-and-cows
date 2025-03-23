# Bulls & Cows – Hra na hádání čtyřciferného čísla

Tento projekt je vypracováním úkolu pro **Engeto Academy**, ve kterém vytvářím hru **Bulls and Cows**.

---

## Popis programu

Program simuluje klasickou logickou hru, ve které hráč hádá tajné čtyřciferné číslo. Každý pokus je vyhodnocen pomocí tzv. **bulls** (správná číslice na správném místě) a **cows** (správná číslice na špatném místě).

---

## Co program umí

1. **Zobrazí úvodní hlášku a přivítání uživatele**

2. **Vygeneruje tajné 4místné číslo**
   - Číslice jsou **unikátní**
   - Číslo **nezačíná nulou**

3. **Hráč hádá číslo**
   - Program kontroluje, zda:
     - vstup má **přesně 4 číslice**
     - nezačíná **nulou**
     - obsahuje **jen čísla**
     - číslice jsou **unikátní**
   - Neplatné vstupy jsou oznámeny, ale stále se **počítají jako pokusy**

4. **Vyhodnocení každého pokusu**
   - Po každém vstupu program vypíše počet:
     - `bull(s)` – správná číslice na správném místě
     - `cow(s)` – správná číslice, ale na jiném místě
   - Program správně používá **jednotné a množné číslo**

5. **Konec hry**
   - Jakmile hráč uhodne správné číslo:
     - Program vypíše počet pokusů
     - Zobrazí, kolik času bylo potřeba
     - Na základě výkonu ukáže **zpětnou vazbu**:
       - `Excellent!`, `Good job!`, `Not bad!`, `Keep practicing!`

---

## Struktura projektu

Projekt obsahuje následující soubory:

```
data-academy-bulls-and-cows/
├── projekt_2_bulls_and_cows.py              # Hlavní skript programu

```
## Autor

**Eva Vallusová**

