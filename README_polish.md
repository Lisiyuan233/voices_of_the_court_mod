# Często zadawane pytania

## 1. Nie pojawia się okno dialogowe
Ten mod wymaga dodatkowego programu backendowego do działania. Pobierz zlokalizowany program backendowy tutaj: [https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest). Pobrany plik .exe zainstaluje się automatycznie po otwarciu.

## 2. Problemy z konfiguracją API
Zaleca się korzystanie z oficjalnego API DeepSeek. W menu rozwijanym połączenia modelu dialogowego wybierz stronę `custom(openai-compatible)`, aby skonfigurować:
- Adres URL serwera: `https://api.deepseek.com/beta`
- Klucz API: Wprowadź własny klucz API, o który można ubiegać się na stronie [https://platform.deepseek.com](https://platform.deepseek.com).

OpenAI i OpenRouter również powinny być kompatybilne.

## 3. Okno dialogowe nie pojawia się nawet wtedy, gdy program backendowy działa po instalacji
**Rozwiązanie**: Musisz użyć moda lokalizacyjnego.

Metody instalacji (wybierz jedną):
1. Po wypakowaniu pobranych plików moda lokalizacyjnego, nadpisz oryginalne pliki moda bezpośrednio w katalogu Steam Workshop.
2. Umieść wypakowany folder moda `voices_of_the_court_mod-1.2.1-beta` w folderze modów gry. Następnie użyj Notatnika, aby utworzyć nowy plik o nazwie `voices_of_the_court_mod-1.2.1-beta.mod` w folderze `Documents\Paradox Interactive\Crusader Kings III\mod` o następującej treści:
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ [Twoja nazwa użytkownika PC] / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

Jeśli okno dialogowe nadal nie pojawia się po zainstalowaniu i włączeniu moda lokalizacyjnego, ścieżka folderu użytkownika CK3 może być ustawiona nieprawidłowo lub gra może być w trybie Ironman. Ten mod nie działa w trybie Ironman.

## 4. Błąd "TypeError: Cannot read properties of undefined (reading 'playerID')" z czerwonym tekstem podczas otwierania okna czatu
**Rozwiązanie**: Utwórz folder o nazwie `run` w `Documents\Paradox Interactive\Crusader Kings III`. Wejdź do tego folderu i utwórz plik tekstowy o nazwie `votc.txt`.

## 5. Ostatnie wspomnienia nie są odczytywane podczas rozmowy z postaciami
**Rozwiązanie**:
1. Jest to mały błąd w programie backendowym oryginalnego autora; pobranie zlokalizowanego backendu rozwiązuje ten problem.
2. Może to być również spowodowane limitami tokenów pamięci. Dostosuj rozmiar `max memory tokens` na stronie ustawień programu backendowego. Po dostosowaniu tokenów pamięci należy również zwiększyć `max new tokens`; najlepiej, jeśli `max new tokens` jest większe niż `max memory tokens`.

## 6. Skrypt generowania promptów powraca do stanu pierwotnego po zrestartowaniu programu backendowego
**Rozwiązanie**:
Zapisz go jako oddzielny plik w folderze `custom`.

## Licencja i Atrybucja

### Informacje o Modzie
- **Nazwa Moda**: Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **Licencja**: GNU General Public License v3.0 (GPLv3)
- **Obsługiwana wersja CK3**: 1.18 "Crane"

### Credits & Attribution
This project, Voices of the Court 2.0 - Community Edition, is a derivative work of Voices of the Court (VOTC) / AliChat.

**Original Work**: Voices of the Court and Voices of the Court 2.0 Mod

**Original Authors**: The VOTC Team, Durond, MrAndroPC, and community contributors.

**Source**: [https://github.com/Voices-of-the-Court/votc_mod](https://github.com/Voices-of-the-Court/votc_mod)

**Original License**: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU GPLv3.

**Modifications**:

* Integration with Voices of the Court 2.0 - Community Edition
* Added features
* Added bug fixes

Relicensed derivative works under GNU GPLv3 as a compatible ShareAlike license.

### Uwaga GPLv3
Ten program jest wolnym oprogramowaniem: możesz go rozpowszechniać i/lub modyfikować zgodnie z warunkami GNU General Public License opublikowanej przez Free Software Foundation, w wersji 3 Licencji lub (według twojego wyboru) dowolnej późniejszej wersji.

Ten program jest rozpowszechniany w nadziei, że będzie użyteczny, ale BEZ ŻADNEJ GWARANCJI; nawet bez domyślnej gwarancji PRZYDATNOŚCI HANDLOWEJ lub PRZYDATNOŚCI DO OKREŚLONEGO CELU. Więcej szczegółów znajdziesz w GNU General Public License.

Powinieneś otrzymać kopię GNU General Public License wraz z tym programem. Jeśli nie, zobacz <https://www.gnu.org/licenses/>.
