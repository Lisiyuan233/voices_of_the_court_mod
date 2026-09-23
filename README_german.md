# Häufig gestellte Fragen

## 1. Es erscheint kein Dialogfeld
Diese Mod erfordert ein zusätzliches Backend-Programm. Laden Sie das lokalisierte Backend-Programm hier herunter: [https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest). Die heruntergeladene .exe-Datei installiert sich beim Öffnen automatisch.

## 2. Probleme bei der API-Konfiguration
Es wird empfohlen, die offizielle DeepSeek-API zu verwenden. Wählen Sie im Dropdown-Menü für die Verbindung zum Dialogmodell die Seite `custom(openai-compatible)` aus, um Folgendes zu konfigurieren:
- Server-URL: `https://api.deepseek.com/beta`
- API-Schlüssel: Geben Sie Ihren eigenen API-Schlüssel ein, den Sie unter [https://platform.deepseek.com](https://platform.deepseek.com) beantragen können.

OpenAI und OpenRouter sollten ebenfalls kompatibel sein.

## 3. Es erscheint kein Dialogfeld, obwohl das Backend-Programm nach der Installation läuft
**Lösung**: Sie müssen die Lokalisierungs-Mod verwenden.

Installationsmethoden (wählen Sie eine):
1. Nachdem Sie die heruntergeladenen Dateien der Lokalisierungs-Mod extrahiert haben, überschreiben Sie die ursprünglichen Mod-Dateien direkt im Steam Workshop-Verzeichnis.
2. Legen Sie den extrahierten Mod-Ordner `voices_of_the_court_mod-1.2.1-beta` in den Mod-Ordner des Spiels. Erstellen Sie dann mit Notepad eine neue Datei namens `voices_of_the_court_mod-1.2.1-beta.mod` im Ordner `Documents\Paradox Interactive\Crusader Kings III\mod` mit folgendem Inhalt:
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ [Ihr PC-Benutzername hier] / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

Wenn das Dialogfeld nach der Installation und Aktivierung der Lokalisierungs-Mod immer noch nicht erscheint, ist möglicherweise der Pfad des CK3-Benutzerordners falsch eingestellt oder das Spiel befindet sich im Ironman-Modus. Diese Mod funktioniert nicht im Ironman-Modus.

## 4. Fehler "TypeError: Cannot read properties of undefined (reading 'playerID')" mit rotem Text beim Öffnen des Chat-Fensters
**Lösung**: Erstellen Sie einen Ordner namens `run` in `Documents\Paradox Interactive\Crusader Kings III`. Gehen Sie in diesen Ordner und erstellen Sie eine Textdatei namens `votc.txt`.

## 5. Kürzliche Erinnerungen werden beim Sprechen mit Charakteren nicht gelesen
**Lösung**:
1. Dies ist ein kleiner Fehler im Backend-Programm des ursprünglichen Autors; das Herunterladen des lokalisierten Backends löst dies.
2. Es kann auch an den Token-Limits für den Speicher liegen. Passen Sie die Größe der `max memory tokens` auf der Einstellungsseite des Backend-Programms an. Nach dem Anpassen der Speicher-Token sollten Sie auch die `max new tokens` erhöhen; es ist am besten, wenn `max new tokens` größer als `max memory tokens` ist.

## 6. Das Prompt-Generierungsskript wird nach dem Neustart des Backend-Programms zurückgesetzt
**Lösung**:
Speichern Sie es als separate Datei im Ordner `custom`.

## Lizenz und Zuschreibung

### Mod-Informationen
- **Mod-Name**: Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **Lizenz**: GNU General Public License v3.0 (GPLv3)
- **Unterstützte CK3-Version**: 1.18 "Crane"

### Credits & Attribution
This project, Voices of the Court 2.0 - Community Edition, is a derivative work of Voices of the Court (VOTC) / AliChat.

**Original Work**: Voices of the Court and Voices of the Court 2.0 Mod

**Original Authors**: The VOTC Team, Durond, MrAndroPC, and community contributors.

**Source**: [https://github.com/Voices-of-the-Court/votc_mod](https://github.com/Voices-of-the-Court/votc_mod)

**Original License**: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU GPLv3.

**Modifications**:

* integration with Voices of the Court 2.0 - Community Edition
* Added features
* Added bug fixes

Relicensed derivative works under GNU GPLv3 as a compatible ShareAlike license.

### GPLv3 Hinweis
Dieses Programm ist freie Software: Sie können es unter den Bedingungen der GNU General Public License, wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Wahl) jeder späteren Version.

Dieses Programm wird in der Hoffnung verteilt, dass es nützlich sein wird, aber OHNE JEGLICHE GARANTIE; sogar ohne die implizite Garantie der MARKTGÄNGIGKEIT oder der EIGNUNG FÜR EINEN BESTIMMTEN ZWECK. Weitere Details finden Sie in der GNU General Public License.

Sie sollten eine Kopie der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <https://www.gnu.org/licenses/>.
