# Funktion zum Einfügen von Daten in eine Datenbank
def einfuegen(time, cpu, ram, cursor, datenbank, tabelle):
    sql = "INSERT INTO "+tabelle+" (Timestamp, CPU, RAM) VALUES (%s, %s, %s)"
    val = (time, cpu, ram)
    cursor.execute(sql, val)
    datenbank.commit()

# Funktion zum Ermitteln der maximalen CPU-AUslastung der letzten 2 Stunden
def statMaxCPU(cursor, tabelle):
    sql = "SELECT MAX(CPU) FROM "+tabelle+" WHERE Timestamp >= DATE_SUB(NOW(), INTERVAL 2 HOUR)"
    cursor.execute(sql)
    return cursor.fetchone()

# Funktion zum Ermitteln der maximalen RAM-AUslastung der letzten 2 Stunden
def statMaxRAM(cursor, tabelle):
    sql = "SELECT MAX(RAM) FROM "+ tabelle +" WHERE Timestamp >= DATE_SUB(NOW(), INTERVAL 2 HOUR)"
    cursor.execute(sql)
    return cursor.fetchone()

# Funktion zum Ermitteln der durchschnittlichen CPU-AUslastung der letzten 2 Stunden
def statAvgCPU(cursor, tabelle):
    sql = "SELECT AVG(CPU) FROM " + tabelle +" WHERE Timestamp >= DATE_SUB(NOW(), INTERVAL 2 HOUR)"
    cursor.execute(sql)
    return cursor.fetchone()

# Funktion zum Ermitteln der durchschnittlichen RAM-AUslastung der letzten 2 Stunden
def statAvgRAM(cursor, tabelle):
    sql = "SELECT AVG(RAM) FROM "+ tabelle +" WHERE Timestamp >= DATE_SUB(NOW(), INTERVAL 2 HOUR)"
    cursor.execute(sql)
    return cursor.fetchone()

# Funktion zum Ermitteln der minimalen CPU-AUslastung der letzten 2 Stunden
def statMinCPU(cursor, tabelle):
    sql = "SELECT MIN(CPU) FROM " + tabelle +" WHERE Timestamp >= DATE_SUB(NOW(), INTERVAL 2 HOUR)"
    cursor.execute(sql)
    return cursor.fetchone()

# Funktion zum Ermitteln der minimalen RAM-AUslastung der letzten 2 Stunden
def statMinRAM(cursor, tabelle):
    sql = "SELECT Min(RAM) FROM "+ tabelle +" WHERE Timestamp >= DATE_SUB(NOW(), INTERVAL 2 HOUR)"
    cursor.execute(sql)
    return cursor.fetchone()