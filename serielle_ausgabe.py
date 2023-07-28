import serial
import time
import os





# Verbinde dich mit der seriellen Schnittstelle (angepasste Einstellungen verwenden)
ser = serial.Serial("COM13", baudrate=115200, timeout=1)


# Die aktuelle Zeit im Format "Stunde:Minute:Sekunde" ausgeben


try:
    while True:
        # Lies die Daten aus der seriellen Schnittstelle
        data = ser.readline().decode().strip()

        # Gib die empfangenen Daten auf der Konsole aus

        if data == "1":
            # Play a audio file when someone is detected
            # play a audio file when someone is detected
            
            os.system ("Person_alarm.mp3")
            

           

            
            
            aktuelle_zeit = time.time()
            print(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(aktuelle_zeit)),
                "|",
                "Person Gesichtet",
            )


except KeyboardInterrupt:
    # Schließe die serielle Verbindung, wenn das Programm beendet wird
    ser.close()
