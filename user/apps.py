from django.apps import AppConfig




class userConfig(AppConfig):
    name = 'user'
    def ready(self):
        import user.signals