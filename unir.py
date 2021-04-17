import time 
import serial
# python3 -m pip install PySerial

#Leer el primer dato desde arduino y escribo en txt
arduino = serial.Serial('/dev/ttyACM0', 9600)
data = arduino.read()
datad = data.decode('utf-8')
print ('Primer dato...')
print (datad)
datadt = datad+datad

f = open ('datos.txt','w')
f.write(str(datadt))
f.close()

while True:
	# siempre lee los datos seriales
	data1 = datad
	data = arduino.read()
	datad = data.decode('utf-8')	
	print ('mismo datoo.....')
	print (datad)
	
	#cuando lee un dato diferente ingresa al buqle y sobreescribe el archivo	
	if data1 != datad:
		f = open ('datos.txt','w')
		datadt = datad+datad
		f.write(str(datadt))
		f.close()
		print ('cambiando ......')
		print (datadt)

	# time de ejecucion
	time.sleep(1)

arduino.close()
