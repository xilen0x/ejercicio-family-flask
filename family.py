class Family:
    def __init__(self, last_name):
        self._last_name = last_name
        self._members = []
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        pass
    def delete_member(self, id):
        pass
    def update_member(self, id, member):
        pass
    def get_member(self, id):
        pass
    def get_all_members(self, id):
        return self._members