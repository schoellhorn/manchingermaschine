# manchingermaschine
## A bot to automatically vote for Manching's Realschule

# Schnelle Installationsanleitung
## Hinweis
Dieser Bot wurde nicht ausgiebig getestet, ich habe versucht ihn so stabil wie möglich zu machen, ich hatte aber nicht allzu viel Zeit, weswegen ich das ganze Projekt innerhalb von wenigen Stunden programmiert habe.
Einige Teile des Programmes sind in C++ (wodurch es aufgrund fehlender Kontrolle zu Memory Leaks kommen könnte).

Der Installer wird neben der Manchinger Maschine noch einige andere Programme installieren!

### Ganz wichtig: Ihr nutzt dieses Programm auf euer eigenes Risiko, ich bin nicht für Schäden verantwortlich!
Dieses Projekt ist nicht in Zusammenarbeit mit Antenne Bayern entstanden und deswegen weiß ich auch noch nicht, wie diese zu dem Bot stehen.
Der Bot wird wenn er läuft euren Computer "bedienen", weswegen man ihn währenddessen nicht benutzen kann (Auch nicht mit einem zweiten Bildschirm).
Und hier kommt auch einer der größten Probleme, obwohl ich einige Maßnahmen ergriffen habe (Der Bot sollte sich neustarten wenn er nicht auf genau der richtigen Seite ist), könnte es zum Beispiel passieren dass der Bot ein anderes Programm startet oder sich frei im Netz herumklickt <- ihr benutzt das Programm auf euer eigenes Risiko

## Den Bot installieren
Die [Installer.exe](https://github.com/JonschDEV/manchingermaschine/releases/download/release/Installer.exe) aus den Releases herunterladen und starten

Nach einer Zeit sollte falls ihr Python nicht bereits installiert habt, sich ein Fenster öffnen wie auf dem Bild gezeigt

![alt text](https://github.com/JonschDEV/manchingermaschine/blob/main/exact0.png?raw=true)

Haken sie wie auf dem Bild gezeigt den Text "Add Python 3.1 to PATH" ab

Klicken sie jetzt auf "Install now" und warten sie bis die Installation abgeschlossen hat

Drücken sie nun auf "Close"

![alt text](https://github.com/JonschDEV/manchingermaschine/blob/main/exact1.png?raw=true)

Sollten sie Firefox nicht bereits installiert haben sollte Firefox' Installer in Kürze erscheinen

Drücken sie auf Installieren und warten sie bis die Installation abgeschlossen ist

![alt text](https://github.com/JonschDEV/manchingermaschine/blob/main/exact2.png?raw=true)

Firefox' Installer sollte sich nun geschlossen haben und mit ihm der ManchingerMaschine Installer

Starten sie nun noch einmal den Installer um die Abhängigkeiten zu installieren

Lassen sie sich hierbei nicht von den Fehlermeldungen irritieren, diese sind meistens völlig normal

Warten sie geduldig bis die Installation fertig ist

## Den Bot benutzen

Als erstes sollten sie Firefox öffnen und sollten sie eine Meldung bekommen ob sie Firefox als Hauptbrowser festlegen wollen, haken sie "Diese Nachricht nichtmehr anzeigen" an und klicken sie auf "Nicht Jetzt"

![alt text](https://github.com/JonschDEV/manchingermaschine/blob/main/exact3.png?raw=true)

Sie können Firefox jetzt schließen und sollten auch jedes geöffnete Firefox Fenster schließen

Auf ihrem Desktop sollten 4 Neue Dateien sein: manchingermaschine.py, StartBot.exe, vote.png, second.png und third.png

Bitte löschen oder verschieben sie keine dieser Dateien da sie essentiell für die Funktionalität des Bots sind.

Starten sie den Bot nun mit dem Program StartBot.exe und nehmen sie die Hände von der Maus/Tastatur, denn ab jetzt "übernimmt" der Bot.

Sollten sie immer noch Probleme haben könnte es helfen den Installer immer wieder zu starten, falls bestimmte Abhängigkeiten nicht ordnungsgemäß installiert wurden

## Wichtige Sachen
Der Bot ist auf eine bestimmte Geschwindigkeit ausgelegt, sollte ihr Computer oder ihr Internet zu langsam sein
könnte der Bot nicht funktionieren
Es könnte auch sein das der Bot manche Anläufe nicht auf Anhieb schafft, bei den meisten Fehlern startet sich
der Bot jedoch automatisch neu wodurch keine Interaktion mit dem Nutzer nötig ist
Der Bot wurde innerhalb von wenigen Stunde programmiert weil Antenne Bayern's Aktion nurnoch wenige Tage läuft, ich habe probiert den Bot so stabil und sicher wie möglich zu machen kann aber wegen dem Zeitdruck nicht garantieren, dass der Bot fehlerfrei läuft -> Sie können davon ausgehen das der Bot manchmal mehrere Anläufe braucht oder es bei ihnen garnicht funktioniert! Es könnte z.B. auch dazu kommen das der Bot frei im Internet surft oder ihren PC anderweitig ungewollt bedient, wobei ich einige Sicherheitssysteme eingebaut haben welche das verhinden sollten könnte dieser Fall trotzdem eintreten und ich möchte nocheinmal darauf hinweisen dass sie den Bot auf eigenem Risiko benutzen

## Mehr oder weniger wichtige Kleinigkeiten
- Sie können den Bot schließen in dem sie "187" in die Zwischenablage kopieren (kein Scherz)
- Treten sie auch gerne dem Subreddit [r/manching](https://www.reddit.com/r/manching)
- Im Code des Bots (manchingermaschine.py) ist eine Variable namens "reboot", wenn sie diese auf 0 stellen, wird sich der Bot anstatt neuzustarten, abschalten
- Wenn sie in die erste Zeile des Programmes (manchingermaschine.py) die Phrase "#haxor" hinzufügen (wie auf dem Bild gezeigt), so wird das Programm in einem anderen Modus starten, dies empfehlt sich jedoch nur falls sie Startschwierigkeiten haben, der Modus funktioniert jedoch selbst bei mir nicht deswegen ist er eher unnötig

![alt text](https://github.com/JonschDEV/manchingermaschine/blob/main/haxor.png?raw=true)
