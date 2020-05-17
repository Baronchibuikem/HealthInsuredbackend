#********************
#imports python
#********************

#********************
#imports django
#********************
from django.shortcuts import redirect, render
from django.contrib import messages


#********************
#imports vendors
#********************

#************************
#imports libs
#************************

#************************
#imports packages
#************************
from libs.app_pages_redirector import base_pages_redirector

def redirect_with_message(param_request,param_route,param_message,param_message_type="INFO"):

    base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:"+param_route)

def redirect_django_admin(param_request):
    return redirect("/admin")

def redirect_page_landing(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:page_landing")

def redirect_page_signup(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:signup_page")

def redirect_page_login(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:login")

def redirect_page_care_providers_search(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:care_provider_search")

def redirect_page_individual_signup(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:individual_signup")

def redirect_page_organization_signup(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:organization_signup")

def redirect_page_individual_profile(
    param_request,
    param_id,
    param_message_type="INFO",
    param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:organization_page",id=param_id)

def redirect_page_organization_profile(
    param_request,
    param_id,
    param_message_type="INFO",
    param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:organization_page",id=param_id)

def redirect_page_individual_dashboard(
    param_request,
    param_id,
    param_message_type="INFO",
    param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:individual_dashboard",id=param_id)

def redirect_page_organization_dashboard(
    param_request,
    param_id,
    param_message_type="INFO",
    param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_enrollment:organization_dashboard",id=param_id)