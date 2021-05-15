# UTILIZZO DEL TELECOMANDO
# PER ACCENDERE E SPEGNERE UN LED

import pyb
from pyb import Pin, Timer
import machine
import sys

class IrRemote:
    # Limiti per il BIT START
    _strbit1 = 8000
    _strbit2 = 10000
    _strbit3 = 4000
    _strbit4 = 5000
    
    def __init__(self,irpin):
        self._irpin = irpin

    def decode_ir(self):
        # il segnale del telecomando IR viene
        # inviato al PIN_X10     
        ingresso = Pin(self._irpin, Pin.IN, Pin.PULL_UP)
        lettura_tot = []
        copia_lettura_tot = []
        #for i in range(50):
        while True:
            read1 = machine.time_pulse_us(ingresso,0)
            read2 = machine.time_pulse_us(ingresso,1)
            #print(len(lettura_tot))
            if read1 > 0 :
                lettura_tot.append(read1)
            if read2 > 0 :
                lettura_tot.append(read2)
            if len(lettura_tot) > 70 :
                copia_lettura_tot = lettura_tot
                lettura_tot = []
                return copia_lettura_tot

        
        
    def trovaflag(self,lista,start,end,start1,end1):
        for count in range(len(lista)-1):
            b1 = lista[count]
            b2 = lista[count+1]
            if (start < b1 < end) and (start1 < b2 < end1) :
                return count+1
            


    # Converte un numero da binario a decimale
    def bin2dec(self,binario):
        lung = len(binario)
        dec = 0
        for i in range(lung):
            indice = lung - i - 1
            cifra = int(binario[indice]) * pow(2, i)
            dec = dec + cifra
        return dec



    def prot_nec(self,lista):
        contabit = 0
        allbit = []
        endbit = False

        first = self.trovaflag(lista,  IrRemote._strbit1,
                                       IrRemote._strbit2,
                                       IrRemote._strbit3,
                                       IrRemote._strbit4) - 1  
        last = first + 64
        lista = lista[first:last]

        # versione protocollo in bit
        bitcode = int(((last - first) - 3) / 2)
        for count in range(0, len(lista), 2):
            b1 = lista[count]
            b2 = lista[count + 1]
            if (IrRemote._strbit1 < b1 < IrRemote._strbit2) and (IrRemote._strbit3 < b2 < IrRemote._strbit4):
                pass
            elif (b1 < 700) and (b2 < 700):  # BIT 0
                allbit.append('0')
                contabit += 1
            elif (b1 < 700) and (1500 < b2 < 1700):  # BIT 1
                allbit.append('1')
                contabit += 1
            elif (b1 < 700) and (30000 < b2):  # END BIT
                endbit = True
    
        c = allbit[16:24]
        c.reverse()
        c1 = "".join(c) 
        return(self.bin2dec(c1))

    # Controlla che il telecomando associato sia quello
    # ELEGOO con protocollo NEC. In presenza di altri
    # raggi IR non reagisce
    def identify_prot(self,lista):
        tmp1 = (self.trovaflag(lista, 8000, 10000, 4300, 4700))
        print("Pos. StartBit",tmp1)
        if tmp1 is not None:
            if tmp1 > 0:
                code = self.prot_nec(lista)
                return code
               

# creo un oggetto irremote
# e gli passo il pin a cui è
# collegato il sensore
irremote = IrRemote("X5")

led = Pin("X1",Pin.OUT)
led.off()

while True:
    # prelevo la lista generata dal telecomando
    rawcode = irremote.decode_ir()
    print(rawcode)
    print("N° letture",len(rawcode))
    # passo la lista alla funzione di decodifica
    # code = è il codice del tasto digitato
    code = irremote.identify_prot(rawcode)
    print("Codice",code)
    if code == 94:   # tasto 3 accende il led
        led.on()
        print("Led acceso\n")
    elif code == 12: # tasto 1 spegne il led
        led.off()
        print("Led spento\n")
    elif code == 22: # tasto 0 esce dal ciclo
        led.off()
        print("Esco dal controllo\n")
        sys.exit()

