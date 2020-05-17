# ********************
# imports python
# ********************

# ********************
# imports django
# ********************
from django.apps import AppConfig
from django.db.models.signals import post_migrate

# ********************
# imports vendors
# ********************

# ************************
# imports libs
# ************************
from app_enrollment import signals

class AppEnrollmentConfig(AppConfig):
    name = 'app_enrollment'

    def ready(self):
        post_migrate.connect(signals.signal_post_migrate, sender=self)
