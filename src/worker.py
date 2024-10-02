class Worker:
    roles = ["builder", "architect"]
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def create(cls, name, role):
        if role not in cls.roles:
            return None
        
        return cls(name, role)
    



