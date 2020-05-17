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

DEFAULT_GROUP_DATA_ENTRY_CLERK="data_entry_clerk"
DEFAULT_GROUP_OFFICER_IN_CHARGE="officer_in_charge"
DEFAULT_GROUP_DIRECTOR_1="director_1"
DEFAULT_GROUP_DIRECTOR_2="director_2"

class Exception_Can_Not_Recreate_Group(Exception):
    def __init__(self, param_group_name="Unknown  file"):
        self.message="can not recreate existing group ("+param_group_name+")"

class Exception_Can_Not_Update_Group_Perms(Exception):
    def __init__(self, param_group_name="Unknown  file"):
        self.message="can not update permissions of a non-existing group ("+param_group_name+")"


def helper_check_group_exists(param_apps,param_group_name):
    """
    check setup of a default group

    Args:
        :param_group_name: the name of the group to check

    Returns:
        :rtype bool:
    """

    return param_apps.get_app_config('auth').get_model("Group").objects.filter(name=param_group_name).exists()

def helper_give_group_model_permissions(
    param_apps,
    param_model,
    param_give_perm_view=False,
    param_give_perm_add=False,
    param_give_perm_change=False,
    param_give_perm_delete=False):
    """
    get the permission objects of a model and add to it

    Returns:
        :rtype list:
    """
    perms=[]

    #get the model type
    data_model_contenttype = param_apps.get_app_config('contenttypes').get_model("ContentType").objects.get_for_model(param_model)

    #give this permission
    if param_give_perm_view:
        perms.append(
            param_apps.get_app_config('auth').get_model("Permission").objects.filter(
                content_type=data_model_contenttype,
                codename__startswith='view_'
            )[0]
        )

    #give this permission
    if param_give_perm_add:
        perms.append(
            param_apps.get_app_config('auth').get_model("Permission").objects.filter(
                content_type=data_model_contenttype,
                codename__startswith='add_'
            )[0]
        )

    #give this permission
    if param_give_perm_change:
        perms.append(
            param_apps.get_app_config('auth').get_model("Permission").objects.filter(
                content_type=data_model_contenttype,
                codename__startswith='change_'
            )[0]
        )

    #give this permission
    if param_give_perm_delete:
        perms.append(
            param_apps.get_app_config('auth').get_model("Permission").objects.filter(
                content_type=data_model_contenttype,
                codename__startswith='delete_'
            )[0]
        )

    return perms