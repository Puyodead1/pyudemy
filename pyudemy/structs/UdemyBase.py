class UdemyBase:
    def __init__(self, data):
        self.cclass = data.get("_class")
        self._id = data.get("id")

    @property
    def _class(self):
        return self.cclass
    
    @_class.setter
    def _class(self, value):
        self.cclass = value
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value