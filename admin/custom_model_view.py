from flask_admin.contrib.sqla import ModelView

class CustomModelView(ModelView):
    def get_pk_tuple(self, model):
        pk = self.get_pk_value(model)
        if not isinstance(pk, tuple):
            return (pk,)
        return pk