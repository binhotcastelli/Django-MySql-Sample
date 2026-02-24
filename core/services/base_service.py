class BaseService:

    def __init__(self, repository):
        self.repository = repository

    def list(self):
        return self.repository.all()

    def get(self, id):
        return self.repository.get_by_id(id)

    def delete(self, id):
        return self.repository.delete(id)