import mraa as m


class adt7410TRZ:

    bus = 1
    address = 0x48
    ambsensor = None

    def __init__(self, bus=1, address=0x48):
        self.bus = bus
        self.address = address
        self.ambsensor = m.I2c(self.bus)
        self.ambsensor.address(self.address)

    def read_temperature(self):
        try:
            msb = self.ambsensor.readReg(0x00)
            lsb = self.ambsensor.readReg(0x01)
            temperature = msb << 8 
            temperature |= lsb & 0x00FF
            temperature = temperature >> 3
            temperature = float(temperature/16.0)
        except:
            temperature = 24.9999
            

        if temperature == 0:
            return 24.9999

        
        return temperature
        
     

if __name__ == "__main__":   
    
   amb = adt7410TRZ(address=0x4b)
        
   temperature = amb.read_temperature()
   print "Temperature is " + str(temperature) + "C"

   