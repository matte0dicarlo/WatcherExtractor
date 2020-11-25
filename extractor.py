import shutil
import pandas as pd
import sys
import xlwt

inputFile = str(sys.argv[1])
print(inputFile)

df = pd.read_excel(inputFile)

print(df)

df = df.drop(['IDCONTRATTO', 'IDHARDWARE', 'DATAEVENTO', 'NOTA', 'STATO', 'ALLARMEREALE', 'CONNECT', 'IDALLARME',
         'NUMPESONE', 'QUANTDANNO', 'PUNTOIMPATTO','SOCCORSOMEDICO', 'INTERLOCUTORE', 'FERITI', 'CONDUCENTE',
         'VEICOLI','GARANZIEACCESSORIE', 'TESTIMONI', 'FORZEORDINE', 'CAI', 'FOTO', 'ANOMALIE', 'PEDONI', 'TARGACTP1',
         'TARGACTP2', 'TIPOLOGIAFO', 'OFFPROPOSTA','RESPDICHIARATA', 'VOLONTADENUNCIA'], axis=1)

print(df)

filename = inputFile.split("/")
outputFile = filename[1]
df.to_excel(outputFile)

shutil.move(outputFile,"OutputIMA")             #todo sostituire con il nome della dir.