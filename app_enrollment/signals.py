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
from setup_group_perms import run_setup_groups_perms
from app_enrollment.setup_seed_tables import seeds_test

def signal_post_migrate(sender,apps, **kwargs):
    """
    run after every migrations
    """
    #setup default groups
    run_setup_groups_perms.run_setup(apps)

    # #create default seeds
    # seeds_test.plant_seeds(apps)