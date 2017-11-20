import nmap #Necesario instalar python-nmap
import sys
import traceback

class NmapScanner:
    def __init__(self):
        self.nms = nmap.PortScanner()
        print 'Inicializando clase'

    def scan(self,host, port):
        print 'Chequeando puertos... ' + port
        try:
            self.nms.scan(host,port)
            print 'Comando ejecutado: ' + self.nms.command_line()
            print '[*]... ' + host + ', state=' + self.nms[host]['tcp'][int(port)]['state']
        except Exception:
            print 'Excepcion a la hora de conectar al puerto' + traceback.format_exc()

#Opcion Directa
# n = NmapScanner()
#n.scan()

if __name__ == '__main__':
    try:
        print 'Ejecutando programa principal'
        NmapScanner().scan('127.0.0.1','80')
        print 'Saliendo'
    except:
        sys.exit()
