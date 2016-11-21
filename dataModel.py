class DataModel():
    def __init__(self, ident, data):
        self.ident = ident
        self.data = data

    def transaction(self):
        self.data = self.data + 1

    def updateData(self, updated):
        self.data = updated
        self.ident = self.ident + 1

    def updateId(self, ident):
        self.ident = ident

    def updateDataAndId(self, data, ident):
        self.ident = ident
        self.data = data