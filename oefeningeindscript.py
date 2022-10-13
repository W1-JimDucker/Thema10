import pymssql 
import time
from gpiozero import LightSensor

conn = pymssql.connect(host='jimduckerserver.database.windows.net', port=1433, database='Thema10', user='jimducker', password='Kw1cDucker')

varSensor = LightSensor(18)

while True:
    print("Nieuwe update")
    
    sensorValue = varSensor.value

    sensorValue *= 100

    print(sensorValue)
    
    cursor = conn.cursor()
    cursor.execute("UPDATE Oefening21 SET SensorsValue = " + str(sensorValue) + " WHERE SensorDevice = 'LDR';")
    
    conn.commit()
    
    time.sleep(10)
    
conn.close()
