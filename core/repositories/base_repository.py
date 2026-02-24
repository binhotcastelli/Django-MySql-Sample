class BaseRepository:

    def __init__(self, model):
        self.model = model

    def all(self):
        return self.model.objects.filter(active=True)

    def get_by_id(self, id):
        return self.model.objects.filter(id=id, active=True).first()

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def delete(self, id):
        obj = self.get_by_id(id)
        if obj:
            obj.active = False
            obj.save()
        return obj