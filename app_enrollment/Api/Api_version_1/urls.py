from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from app_enrollment.Api.Api_version_1.viewsets.department_viewset import DepartmentView
from app_enrollment.Api.Api_version_1.viewsets.dependent_viewset import DependentView
from app_enrollment.Api.Api_version_1.viewsets.staff_viewset import StaffViewSet as StaffView
from app_enrollment.Api.Api_version_1.viewsets.generic_plan_viewset import GenericPlanViewSet
from app_enrollment.Api.Api_version_1.viewsets.plan_registration_viewset import PlanRegistrationViewSet
from app_enrollment.Api.Api_version_1.viewsets.user_query_viewset import (
    QueryAllUsersView, CustomUserViewSet
    )
    
from app_enrollment.Api.Api_version_1.viewsets.plan_registration_viewset import (
    QueryExpiredUsersViews, QueryUsersExpiringInThreeMonths,
    EnrolleeListView, QueryEnrolleePolicyDate
)

router = routers.DefaultRouter()


# This endpoint is used to perform CRUD operation on Department database
router.register('departments', DepartmentView)


# This endpoint is used to perform CRUD operation on Dependent database
router.register('dependents', DependentView)


# This endpoint is used to perform CRUD operation on Staff database
router.register('staff', StaffView)


# This endpoint is used to perform CRUD operation on GenericPlan database
router.register('plan', GenericPlanViewSet)


# This endpoint is used to register users into a new plan
router.register('register', PlanRegistrationViewSet)


# This endpoint is responsible for querying all registered in the database
router.register('get-user', QueryAllUsersView)

# This endpoint is responsive for querying all registered user in the customerUser
router.register("get-adminUser", CustomUserViewSet)


router.register('expired-users', QueryExpiredUsersViews)

router.register('expiring-in-three-months', QueryUsersExpiringInThreeMonths)
#endpoint responsible for querying query with dates, all policies expiring within 14 days
router.register('enrollees-policy-dates/', QueryEnrolleePolicyDate, basename='get-with-date'),


urlpatterns = [
    # default api auth for restframework

    # This endpoint is used to log in a user
    path('Login/', jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),


    path('Login/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    
    # endpoint responsible for querying enrollees
    path('enrollees-list/', EnrolleeListView.as_view()),

]

urlpatterns += router.urls

