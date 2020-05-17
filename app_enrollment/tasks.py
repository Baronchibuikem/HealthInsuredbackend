from __future__ import absolute_import
from openhisa_sec8.celery import app
from celery import shared_task, Celery
from app_enrollment.models import PlanRegistration, CustomUser
from datetime import datetime, date, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import datetime
#from dateutil.relativedelta import relativedelta

from libs.utils.request_mail import send_custom_mail


@app.task
def deactivate_account(username):
    """
    Deactivates a user account. The ``Scripts.DESTROY`` does the destruction of all user instances
    :param username: Username of account to be deactivated
    :type username: string
    """
    user = PlanRegistration.objects.get(username=username).first()
    print(user)
    current_date = datetime.now()
    if current_date > user.expired:
        CustomUser.deactivate()
        # send_mail("Your Account Has Been Deactivated!",
        #           "You Will Need To Renew Your Plan",
        #           "support@gmail.com",)
        print("it works")



# 3 months expiration reminders
@app.task
def send_three_months_reminder():
    #three_months = datetime.today() + relativedelta(months=+3)
    # Since django uses aware datetimes we have to convert 3 months to aware datetime
    #three_months = timezone.make_aware(three_months, timezone.utc)

    users = PlanRegistration.objects.all()
    template_name = "emails/three_months_reminder.html"
    subject = settings.THREE_MONTHS_REMINDER_SUBJECT
    
    for user in users:
        start_date = user.expired
        end_date = timezone.now()
        num_months = abs((end_date.year - start_date.year) * 12\
            + (end_date.month - start_date.month))
        if num_months <= 3 and user.three_month_reminder_sent == False:
            from_user = [settings.ADMIN_EMAIL]
            receipiant = [user.email] 
            context = {
                'subject': subject,
                'name': f'{user.first_name} {user.last_name}'
            }
            send_custom_mail(
                subject, template_name, from_user, receipiant, context=context
                )
            user.three_month_reminder_sent = True
            user.save()
            return {'status': True}
        else:
            print('no expired policys yet')
            return {'status': False}

@app.task
def expire_user_plans():
    """
    checks PlanRegistration model for accounts whose expiry date is less
    than the current date and then turns is_expired to True
    """
    users = PlanRegistration.objects.all()
    current_date = timezone.now()
    for user in users:
        if user.expired < current_date:
            user.is_expired = True
            user.save()
            return {'status': True}
        return {'status': False}

@app.task
def policy_payment_due():
    """
    checks for Policies that have expired and sends a reminder to the respective 
    people telling them about it
    """

    users = PlanRegistration.objects.all()
    current_date = timezone.now()

    template_name = "emails/policy_payment_due.html"
    subject = settings.POLICY_PAYMENT_DUE_SUBJECT

    for user in users:
        # checking against two conditions first incase
        # @task expire_user_plans has not run

        if (user.is_expired==True or user.expired < current_date) and \
            user.is_due_reminder_sent == False:

            from_user = [settings.ADMIN_EMAIL]
            receipiant = [user.email]
            context = {
                'subject': subject,
                'name': f'{user.first_name} {user.last_name}'
            }
            send_custom_mail(
                subject, template_name, from_user, receipiant, context=context
                )
            user.is_due_reminder_sent = True
            user.save()
            return {'status':True}
        return {'status':False}

