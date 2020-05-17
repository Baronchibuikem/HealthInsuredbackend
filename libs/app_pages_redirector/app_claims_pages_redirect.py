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

    return redirect("app_claims:"+param_route)

def redirect_page_claims_vetting(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:claims_vetting")

def redirect_page_upload_claims(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:upload_claims")

def redirect_page_approve_claims(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:approve_claims")

def redirect_page_claims_payment(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:claims_payment")

def redirect_page_claims_wrapper(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:claims_wrapper")

def redirect_page_view_claims(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:view_claims")

def redirect_page_approve_payment(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:approve_payment")

def redirect_page_batch_claims(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:batch_claims")

def redirect_page_claim_batch_list(param_request,param_message_type="INFO",param_message=None):
    if param_message!=None:
        base_pages_redirector.flash_message(param_request,param_message,param_message_type)

    return redirect("app_claims:claim_batch_list")