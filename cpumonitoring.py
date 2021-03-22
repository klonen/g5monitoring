"""
    Ausgangsbeschreibung:   "Programm zum Auslesen der CPU- und RAM-
                            Auslastung und Export in das CSV-Datenformat."

    Autor:                  K. Faengmer
    Datum:                  09.12.2020

    Aktuelle Beschreibung:  "Programm zum Auslesen der CPU- und RAM-
                            Auslastung und senden dieser an eine
                            Datenbank, sowie zuum Abrufen einer Statistik
                            der minimalen, maximalen und durschnittlichen
                            Auslastung der letzten zwei Stunden. 

    Überarbeitet durch:     Kyra Werner, Richard Voth, Mia Möbes
    Letzte Bearbeitung:     06.03.2021
"""


# Importieren der benötigten Module
import mysql.connector
import psutil
import sq
from datetime import datetime

while True:

    # Benutzermenü mit Übersicht über die Funktionen des Programms
    print("-------------------------------")
    print("|            Menü             |")
    print("-------------------------------")
    print("  Daten aufzeichnen: Rasp1 (1) ")
    print("  Daten aufzeichnen: Rasp2 (2) ")
    print("  Statistik abrufen: Rasp1 (3) ")
    print("  Statistik abrufen: Rasp2 (4) ")
    print("  Programm beenden:        (0) ")
    print("-------------------------------")
    antwort = input("Was möchten Sie tun?(1/2/3/4/0) ")

    # Programm beenden
    if( antwort == "0"):
        print("Das Programm wird nun beendet...")
        break

    # Datenbankverbindung aufbauen
    if( antwort == "1" or antwort == "2" or antwort == "3" or antwort == "4"):
        pidaten = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pidaten")

        mycursor = pidaten.cursor()

    if(antwort == "1" or antwort == "2"):
        try:
            while True:            
                # Zeit und Auslastung ermitteln
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cpu = psutil.cpu_percent(1)
                ram = psutil.virtual_memory().percent

                # Bildschirmausgabe und übermitteln der Auslastung an die Datenbank
                print(time,"\t",cpu,"\t\t",ram)
                if(antwort == "1"):
                    table = "raspi1"
                    sq.einfuegen(time, cpu, ram, mycursor, pidaten, table)
                else:
                    table = "raspi2"
                    sq.einfuegen(time, cpu, ram, mycursor, pidaten, table)

        # Beenden des Vorgangs und Abbau der Datenbankverbindung
        except KeyboardInterrupt:
            print("... Abbruch!")
            pidaten.close()

    elif(antwort == "3" or antwort == "4"):

        if(antwort == "3"):
            table = "raspi1"
            print("Die Daten werden für die letzten zwei Stunden angegeben.")
            print("Statistik für Raspberry Pi 1:")
        elif(antwort == "4"):
            print("Die Daten werden für die letzten zwei Stunden angegeben.")
            table = "raspi2"
            print("Statistik für Raspberry Pi 2:")
    
        # Daten für die Statistik abrufen
        maxCpu = sq.statMaxCPU(mycursor, table)
        avgCpu = sq.statAvgCPU(mycursor, table)
        minCpu = sq.statMinCPU(mycursor, table)
        maxRam = sq.statMaxRAM(mycursor, table)
        avgRam = sq.statAvgRAM(mycursor, table)
        minRam = sq.statMinRAM(mycursor, table)

        # Ausgabe der Statistik
        print("Maximale CPU Auslastung: " + str(maxCpu[0]))
        print("Durschnittliche CPU Auslastung: " + str(avgCpu[0]))
        print("Minimale CPU Auslastung: " + str(minCpu[0]))
        print("Maximale RAM Auslastung: " + str(maxRam[0]))
        print("Durchschnittliche RAM Auslastung: " + str(avgRam[0]))
        print("Minimale RAM Auslastung: " + str(minRam[0]))

        # Beenden der Datenbankverbindung
        pidaten.close()

    else:
        print("Eingabe nicht erkannt, bitte wählen Sie erneut aus.")