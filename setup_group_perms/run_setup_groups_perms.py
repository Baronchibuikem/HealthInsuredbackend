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
# imports libs
# ************************
from setup_group_perms import base_setup_group_perms
from setup_group_perms import group_perms_data_entry_clerk
from setup_group_perms import group_perms_officer_in_charge
from setup_group_perms import group_perms_director_1
from setup_group_perms import group_perms_director_2

def run_setup(param_django_apps):
    """
    this runs after every migration 
    checks if groups and permissions exists
    and add new or updates
    """
    #===================================
    #SETUP THIS GROUP
    #===================================
    
    if base_setup_group_perms.helper_check_group_exists(
            param_django_apps,
            base_setup_group_perms.DEFAULT_GROUP_DATA_ENTRY_CLERK
        ):
        #update
        group_perms_data_entry_clerk.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )
    else:
        #create
        group_perms_data_entry_clerk.run_group_permissions(
            param_django_apps,
            param_create_new=True
        )
        #update
        group_perms_data_entry_clerk.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )

    #===================================
    #SETUP THIS GROUP
    #===================================
    
    if base_setup_group_perms.helper_check_group_exists(
            param_django_apps,
            base_setup_group_perms.DEFAULT_GROUP_OFFICER_IN_CHARGE
        ):
        #update
        group_perms_officer_in_charge.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )
    else:
        #create
        group_perms_officer_in_charge.run_group_permissions(
            param_django_apps,
            param_create_new=True
        )
        #update
        group_perms_officer_in_charge.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )

    #===================================
    #SETUP THIS GROUP
    #===================================
    
    if base_setup_group_perms.helper_check_group_exists(
            param_django_apps,
            base_setup_group_perms.DEFAULT_GROUP_DIRECTOR_1
        ):
        #update
        group_perms_director_1.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )
    else:
        #create
        group_perms_director_1.run_group_permissions(
            param_django_apps,
            param_create_new=True
        )
        #update
        group_perms_director_1.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )

    #===================================
    #SETUP THIS GROUP
    #===================================
    
    if base_setup_group_perms.helper_check_group_exists(
            param_django_apps,
            base_setup_group_perms.DEFAULT_GROUP_DIRECTOR_2
        ):
        #update
        group_perms_director_2.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )
    else:
        #create
        group_perms_director_2.run_group_permissions(
            param_django_apps,
            param_create_new=True
        )
        #update
        group_perms_director_2.run_group_permissions(
            param_django_apps,
            param_create_new=False
        )

    print("|")
    print("==================================================================")
    print("APP-ENROLLMENT RUN-SETUP DEFAULT GROUPS-PERMISSIONS COMPLETED")
    print("==================================================================")
    print("|")