#THERE MUST NOT BE ANY IMOPRTS OF MODELS IN THE CALL STACK
#WHEN USING POST_MIGRATE

# ********************
# imports python
# ********************

# ********************
# imports django
# ********************

# ********************
# imports vendors
# ********************

# ************************
# imports app
# ************************
from app_claims.setup_seed_tables import seeds_test

def signal_post_migrate(sender,apps, **kwargs):
    """
    run after every migrations
    """

    #create default seeds
    # seeds_test.plant_seeds(apps)