#simple bitfield object
class Adafruit_bitfield(object):
    def __init__(self, _structure):
        self._structure = _structure
        
        for key, value in _structure.iteritems():
            setattr(self, key, 0)
            
    def get(self):
        fullreg = 0
        pos = 0
        for key, value in self._structure.iteritems():
            fullreg = fullreg | ( (getattr(self, key) & (2**value - 1)) << pos )
            pos = pos + value
            
        return fullreg