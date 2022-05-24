class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context