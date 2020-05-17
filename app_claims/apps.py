from django.apps import AppConfig


class AppClaimsConfig(AppConfig):
    name = 'app_claims'
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
from app_claims import signals

class AppClaimsConfig(AppConfig):
    name = 'app_claims'

    def ready(self):
        post_migrate.connect(signals.signal_post_migrate, sender=self)
