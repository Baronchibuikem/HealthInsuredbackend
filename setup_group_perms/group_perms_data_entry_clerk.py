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

def run_group_permissions(param_apps,param_create_new=False):
    """
    update or create permissions for this group
    =============================================

    Args:
        :param param_create_new: if **False** will update if **True** will create new
    """

    GROUP_NAME = base_setup_group_perms.DEFAULT_GROUP_DATA_ENTRY_CLERK

    if param_create_new:
        #==================================================
        #CREATE GROUP
        #==================================================

        data_exists_group=param_apps.get_app_config('auth').get_model("Group").objects.filter(name=GROUP_NAME).exists()

        if data_exists_group:
            raise base_setup_group_perms.Exception_Can_Not_Recreate_Group(GROUP_NAME)

        param_apps.get_app_config('auth').get_model("Group").objects.create(name=GROUP_NAME)
    else:
        all_perms=[]

        #==================================================
        #GET GROUP
        #==================================================

        try:
            data_group=param_apps.get_app_config('auth').get_model("Group").objects.get(name=GROUP_NAME)
        except param_apps.get_app_config('auth').get_model("Group").DoesNotExist:
            raise base_setup_group_perms.Exception_Can_Not_Update_Group_Perms(GROUP_NAME)

        #==================================================
        #GIVE GROUP-PERMISSIONS FOR THIS MODEL
        #==================================================

        all_perms.extend(
            base_setup_group_perms.helper_give_group_model_permissions(
                param_apps,
                param_apps.get_app_config('app_enrollment').get_model("GenericPlan"),
                param_give_perm_view=True,
                param_give_perm_add=False,
                param_give_perm_change=False,
                param_give_perm_delete=False
            )
        )

        all_perms.extend(
            base_setup_group_perms.helper_give_group_model_permissions(
                param_apps,
                param_apps.get_app_config('app_enrollment').get_model("Staff"),
                param_give_perm_view=False,
                param_give_perm_add=False,
                param_give_perm_change=False,
                param_give_perm_delete=False
            )
        )

        all_perms.extend(
            base_setup_group_perms.helper_give_group_model_permissions(
                param_apps,
                param_apps.get_app_config('app_enrollment').get_model("Department"),
                param_give_perm_view=False,
                param_give_perm_add=False,
                param_give_perm_change=False,
                param_give_perm_delete=False
            )
        )

        all_perms.extend(
            base_setup_group_perms.helper_give_group_model_permissions(
                param_apps,
                param_apps.get_app_config('app_enrollment').get_model("Dependent"),
                param_give_perm_view=False,
                param_give_perm_add=False,
                param_give_perm_change=False,
                param_give_perm_delete=False
            )
        )

        #==================================================
        #ADD PERMISSIONS TO GROUP
        #==================================================

        data_group.permissions.set(all_perms)