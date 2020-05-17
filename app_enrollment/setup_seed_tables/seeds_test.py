# # ********************
# # imports python
# # ********************
#
# # ********************
# # imports django
# # ********************
# from django.utils import timezone
#
# # ********************
# # imports vendors
# # ********************
#
# # ************************
# # imports app
# # ************************
#
# # ************************
# # imports libs
# # ************************
#
# def plant_seeds(param_django_apps):
#     """
#     create seed data for models
#     """
#     #===========================================
#     #SEED FOR MODEL-DEPARTMENT
#     #===========================================
#     seed_department_dataentry=param_django_apps.get_app_config('app_enrollment').get_model("Department")(
#         name="data_entry"
#     )
#     seed_department_claimsvetting=param_django_apps.get_app_config('app_enrollment').get_model("Department")(
#         name="claims_vetting"
#     )
#
#     #===========================================
#     #SEED FOR MODEL-PLANS
#     #===========================================
#     seed_plan_premium=param_django_apps.get_app_config('app_enrollment').get_model("GenericPlan")(
#         plan_name="Premium",
#         price=50000,
#         date_created=timezone.now(),
#         json="json object"
#     )
#     seed_plan_gold=param_django_apps.get_app_config('app_enrollment').get_model("GenericPlan")(
#         plan_name="Gold",
#         price=10000,
#         date_created=timezone.now(),
#         json="json object"
#     )
#     seed_plan_silver=param_django_apps.get_app_config('app_enrollment').get_model("GenericPlan")(
#         plan_name="Silver",
#         price=30000,
#         date_created=timezone.now(),
#         json="json object"
#     )
#
#     #===========================================
#     #RUN SAVE HERE DUE TO LAZY-LOADING
#     #===========================================
#     seed_department_dataentry.save()
#     seed_department_claimsvetting.save()
#
#     seed_plan_premium.save()
#     seed_plan_gold.save()
#     seed_plan_silver.save()