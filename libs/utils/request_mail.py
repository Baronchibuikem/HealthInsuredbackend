from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


def send_custom_mail(
    subject, template_name,
    _from, _to, html=True, context=dict()
    ):
    """
    Function to send emails

    :param template: template name or string message to be rendered
    :type template: string
    :param _from, as the name implies are the normal mail fields
    :param context: context variables to be passed and rendered in the message
    :type context: dict

    :param html: If email should also be sent as html message
    :type html: bool
    :returns: a tuple of rendered message, html_message
    :rtype: tuple

    """
    html_msg = ""
    context['render_html'] = html
    html_msg = render_to_string(template_name, context)
    msg = EmailMultiAlternatives(
        subject=subject, from_email=_from, to=_to
        )
    msg.attach_alternative(html_msg, 'text/html')
    return msg.send()