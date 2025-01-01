
Die Darstellung, wie es die Teilnehmer sehen werden, finden Sie unter diesem Link: [https://riddle.hackingescaperoom.tech](https://riddle.hackingescaperoom.tech)

# Einführung

„Hallo zusammen! Wir sind TechBrainAI, ein Unternehmen, das sich auf Künstliche Intelligenz spezialisiert hat. Leider haben wir ein ernstes Problem: Wir wurden offenbar von einem Hacker oder einer Hackergruppe angegriffen. Zumindest ist unser IT-Team davon überzeugt, nachdem es verdächtige Aktivitäten im Netzwerk entdeckt hat.

Wir brauchen dringend eure Hilfe, um diesen Angriff zu untersuchen und herauszufinden, was die Hacker geplant haben. Ich werde euch durch die Untersuchung leiten. Ach ja, ich habe natürlich auch einen speziellen Namen – ihr könnt mich ‚Shadowman‘ nennen. Ich bin ein ‚White-Hat-Hacker‘, also einer der ‚Guten‘. Während wir White-Hats helfen, Systeme zu sichern, nutzen ‚Black-Hats‘ ihre Fähigkeiten, um Schaden anzurichten. Und genau so einen Black-Hat haben wir hier aufgespürt. Seid ihr bereit, ihn zu jagen? Seid ihr bereit, in die Welt der Cyber-Ermittlungen einzutauchen?“

(Teilnehmer antworten „Ja“)

# Posten 1

„Die erste verdächtige Spur hat unser IT-Team in einem der Verzeichnisse auf einem unserer Rechner gefunden. Es scheint, dass der Hacker eine Datei tief im System versteckt hat – und was dort drin ist, könnte uns einen wichtigen Hinweis geben, wie wir weiter vorgehen können.

Normalerweise wird so etwas als ‘versteckte Datei’ abgelegt, damit sie im ersten Moment nicht auffällt. Aber ein erfahrener White-Hat-Hacker weiß, wie man solche Dateien aufspürt. Schaut genau hin und denkt daran, manchmal sind Dinge nicht so sichtbar, wie sie scheinen. Wenn ihr etwas entdeckt, lasst bitte das Fenster offen. Wir brauchen es später noch. Geht nun bitte zum 2. Posten.“

# Posten 2

„Gut gemacht, ihr habt die versteckte Datei gefunden! Doch der Hacker scheint noch eine weitere Falle hinterlassen zu haben. Diesmal geht es um einen der ältesten Tricks im Buch, n USB-Falle. Fremde USB-Sticks in das System einzustecken, kann gefährlich sein, besonders wenn man nicht weiss, woher sie kommen oder was darauf versteckt ist.

Auf einem der USB-Sticks hier ist ein entscheidender Hinweis für uns. Aber seid vorsichtig! Der Hacker hat mindestens einen der Sticks so präpariert, dass er euch in die Irre führen könnte. Wenn ihr den falschen Stick auswählt, wird eine Nachricht ausgelöst, die euch vom richtigen Weg abbringen soll und euch wertvolle Zeit kostet.

Schaut euch die Sticks genau an und überlegt, welchem ihr vertrauen könnt. Wichtig! Habt ihr den richtigen Stick gefunden, solltet ihr die versteckte Datei vom ersten Posten sowie alle weiteren wichtigen Informationen darauf speichern (kopieren).“

# Posten 3

„Merkt euch! Vertraut niemals einem fremden USB-Stick. Selbst harmlose Sticks können mit bösartigem Code infiziert sein. Hier ein Beispiel: Ein sogenannter ‚Rubber Ducky‘ kann sich als Tastatur ausgeben und selbstständig gefährliche Befehle ausführen. Unbedachte Nutzung könnte ein System gefährden oder sogar sensible Daten stehlen. So etwas dürfen wir dem Hacker natürlich nicht ermöglichen!

Ihr seid wirklich gut! Dank eurer bisherigen Arbeit haben wir jetzt die versteckte Datei und den Hinweis auf die Steganografie-Methode, die der Hacker benutzt hat. Die meisten Menschen denken bei einem Bild an nichts weiter als das, was sie sehen. Aber erfahrene Hacker wissen, dass man oft viel mehr darin verstecken kann, als auf den ersten Blick sichtbar ist. So eine versteckte Nachricht im Bild nennt man Steganografie.

Der Hacker hat uns offenbar eine Nachricht hinterlassen, die in einem Bild auf unserem System versteckt ist. Wenn wir diese Nachricht finden und entschlüsseln können, erfahren wir vielleicht mehr über den Angreifer. Öffnet Terminal, aber passt auf: der Steganografie-Befehl, den ihr im ersten Posten gefunden habt, muss erst noch richtig sortiert werden, um das versteckte Bild zu entschlüsseln. Zusätzlich dazu, müssen wir nach dem Befehl das Password eingeben.

Zum Glück konnte unser IT-Team bereits eine Liste mit möglichen Passwörtern des Hackers erstellen. Es gibt etwa 25 Kombinationen, die infrage kommen könnten. Ihr könnt euch die Passwortliste bei unserem IT-Team holen.

Ich habe unsem IT-Team darauf hingewiesen, dass man solche Passwörter in der Regel auch automatisiert knacken kann, aber hier brauchen wir eure Hilfe und Kreativität! Versucht, die Passwörter nacheinander durchzugehen, um die Nachricht im Bild zu entschlüsseln.“

# Posten 4

„Ihr habt grossartige Arbeit geleistet und euch durch die verschlüsselte Nachricht gekämpft! Wir haben jetzt einige wertvolle Informationen, aber eine letzte Hürde müssen wir noch nehmen, bevor wir die eigentliche Nachricht des Hackers knacken können. Der Hacker hat seinen Hash gut geschützt und verschlüsselt. Wir müssen genau herausfinden, welcher Typ Hash das ist, bevor wir ihn weiter entschlüsseln können.

Im nächsten Schritt verwenden wir spezialisierte Tools, die uns bei der Identifizierung des Hashtyps unterstützen. Es gibt viele verschiedene Hasharten. Jeder hat eine andere Struktur und Methode zur Verschlüsselung. Ihr müsst jetzt zuerst den Hashtyp bestimmen und dann den passenden „Hashcat“-Wert herausfinden, den wir später brauchen, um den Hash zu knacken. Öffnet dafür bitte ein neues Terminalfenster.“

Anleitung zur Tool-Nutzung:

„Als Erstes schliesst bitte das bisherige Terminalfenster von Posten 3. Dann startet ein neues Terminalfenster und gebt den folgenden Befehl für das erste Tool hash-identifier ein. So können wir herausfinden, welcher Hash in unserem Fall vorliegt. Gebt dazu Folgendes ein:

hash-identifier

und drückt Enter. Anschliessend fügt ihr den Hash aus Posten 2 ein, um den Typ zu ermitteln.

Nun brauchen wir ein weiteres Tool, um herauszufinden, wie wir diesen Hash in „Hashcat“ knacken können. Öffnet dafür ein zweites Terminalfenster und gebt den folgenden Befehl für das Tool hashid ein:

hashid (hier euren Hash einsetzen) -m

Dies zeigt euch die spezifische Nummer, die in „Hashcat“ für diesen Hashtyp verwendet wird. Merkt euch diesen „-m“ Wert gut. Er ist entscheidend, um im nächsten Posten den Hash endgültig zu entschlüsseln.“

Zusammenfassung für Posten 4:

Schritt 1: Schliesst das bisherige Terminal und öffnet ein neues. Gebt hash-identifier ein, fügt den Hash ein und identifiziert den Hashtyp.

Schritt 2: Öffnet ein zweites Terminalfenster, gebt hashid (Hash) -m ein, um den spezifischen Hashcat-Wert zu erhalten.

Notiert den Wert: Dieser Wert („-m“) wird benötigt, um den Hash im nächsten Posten zu knacken.

# Posten 5

„Fast geschafft! Ihr habt es bereits weit gebracht. Nun steht ihr vor dem letzten Schritt, um die Botschaft des Hackers zu knacken. Der Hash, den ihr habt, ist der Schlüssel,aber ohne das passende Passwort bleibt er verschlossen. Dank eurer Analyse in Posten 4 habt ihr den richtigen Hashcat-Wert ermittelt. Jetzt ist es an der Zeit, diesen anzuwenden, um das Passwort herauszufinden.

Um den Hash zu knacken, müsst ihr zunächst den Hashcat-Befehl im Terminal eingeben und den Hash aus Posten 3 einsetzen. Kopiert den Hash, den ihr dort gefunden habt und fügt ihn direkt in den Befehl ein. Hier ist die Anleitung:

1.Öffnet ein weiteres Terminalfenster und gebt folgenden Befehl ein:

hashcat -m (Wert von Posten 4) -a 0 (Hash aus Posten 3) "/usr/share/wordlists/rockyou.txt"

Drückt Enter, um den Vorgang zu starten.

2.Nun müsst ihr denselben Befehl noch einmal eingeben, allerdings mit einem kleinen Zusatz, um das Ergebnis anzuzeigen. Gebt dazu diesen Befehl ein:

hashcat -m (Wert aus Posten 4) -a 0 (Hash aus Posten 3) "/usr/share/wordlists/rockyou.txt" --show

Wenn alles geklappt hat, solltet ihr jetzt das Passwort entschlüsselt sehen! Dies ist das letzte Puzzlestück, das wir brauchen, um die Pläne des Hackers zu durchschauen. Ein super Job! Mit diesem Passwort habt ihr den Hacker enttarnt!“