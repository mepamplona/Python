from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import os

def printMeta():
    pdfFile = PdfFileReader(file('TutorialPython2.pdf','rb'))
    docInfo = pdfFile.getDocumentInfo()

    for metaItem in docInfo:
        print '[+] ' + metaItem + ': ' + docInfo[metaItem]
            

if __name__ == '__main__':
    print "Ejecutado como programa principal"
    try: printMeta()
    except:
        sys.exit()
