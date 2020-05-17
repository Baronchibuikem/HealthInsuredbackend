# ********************
# imports python
# ********************

# ********************
# imports django
# ********************
from django.utils import timezone

# ********************
# imports vendors
# ********************

# ************************
# imports app
# ************************

# ************************
# imports libs
# ************************

def plant_seeds(param_django_apps):
    """
    create seed data for models
    """
    #===========================================
    #SEED FOR MODEL-DEPARTMENT
    #===========================================
    seed_1=param_django_apps.get_app_config('app_claims').get_model("CareProvider")(
        name="hospital 1",
        lga="lga 1"
    )
    seed_2=param_django_apps.get_app_config('app_claims').get_model("CareProvider")(
        name="hospital 2",
        lga="lga 2"
    )

    #===========================================
    #RUN SAVE HERE DUE TO LAZY-LOADING
    #===========================================
    seed_1.save()
    seed_2.save()