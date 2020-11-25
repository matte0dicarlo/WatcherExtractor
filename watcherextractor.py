import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import pandas as pd
import sys

class Watcher:
        DIRECTORY_TO_WATCH =  inputFile = str(sys.argv[1])

        def __init__(self):
            self.observer = Observer()

        def run(self):
            event_handler = Handler()
            self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
            self.observer.start()
            try:
                while True:
                    time.sleep(5)
            except:
                    self.observer.stop()
                    print("Error")

            self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            OUTPUT_DIRECTORY = inputFile = str(sys.argv[2])

            print( "Received %s." % event.src_path)
            fileToHandle = event.src_path
            print(fileToHandle)
            df = pd.read_excel(fileToHandle)
            print(df)
            df = df.drop(
                ['IDCONTRATTO', 'IDHARDWARE', 'DATAEVENTO', 'NOTA', 'STATO', 'ALLARMEREALE', 'CONNECT', 'IDALLARME',
                 'NUMPESONE', 'QUANTDANNO', 'PUNTOIMPATTO', 'SOCCORSOMEDICO', 'INTERLOCUTORE', 'FERITI', 'CONDUCENTE',
                 'VEICOLI', 'GARANZIEACCESSORIE', 'TESTIMONI', 'FORZEORDINE', 'CAI', 'FOTO', 'ANOMALIE', 'PEDONI',
                 'TARGACTP1',
                 'TARGACTP2', 'TIPOLOGIAFO', 'OFFPROPOSTA', 'RESPDICHIARATA', 'VOLONTADENUNCIA'], axis=1)
            print(df)

            filename = fileToHandle.split("/")
            outputFile = filename[1]
            df.to_excel(outputFile)
            shutil.move(outputFile, OUTPUT_DIRECTORY)


if __name__ == '__main__':
    w = Watcher()
    w.run()