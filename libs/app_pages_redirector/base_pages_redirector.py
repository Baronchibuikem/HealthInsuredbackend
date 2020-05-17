#********************
#django imports
#********************
from django.shortcuts import redirect
from django.contrib import messages

MESSAGE_TYPE_ERROR="ERROR"
MESSAGE_TYPE_WARNING="WARNING"
MESSAGE_TYPE_INFO="INFO"
MESSAGE_TYPE_SUCCESS="SUCCESS"
MESSAGE_TYPE_DEBUG="DEBUG"

def flash_message(param_request,param_message,param_message_type="INFO"):
    if param_message_type==MESSAGE_TYPE_INFO:
        messages.info(
            param_request,
            param_message
        )
    elif param_message_type==MESSAGE_TYPE_WARNING:
        messages.warning(
            param_request,
            param_message
        )
    elif param_message_type==MESSAGE_TYPE_ERROR:
        messages.error(
            param_request,
            param_message
        )
    elif param_message_type==MESSAGE_TYPE_SUCCESS:
        messages.success(
            param_request,
            param_message
        )
    elif param_message_type==MESSAGE_TYPE_DEBUG:
        messages.debug(
            param_request,
            param_message
        )
    else:
        messages.info(
            param_request,
            param_message
        )