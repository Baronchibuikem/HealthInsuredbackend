DATE : 5-12-2019
=======================

- Add Enrollees Model 

Date : 12-12-2019
-------------------------

- Resolve issues with .gitignore not picking files
- Modularized Settings files
- Set up celery 
- update requirements file
- add readme update readme

Date: 13-13-2019
----------------------------
- Add models for app_claims

7-03-2020
-----------------

- add reminder_sent field to PlanRegistration Model
- Add custom email functionality to **libs/utils**
- fix & update celery settings and configuration
- write celery task 'send_three_months_reminder' in app_enrollment
- add email templates to **app_enrollment/templates**
- add email config to development settings
- schedule three_months_reminder mail to run every monday by 8:30 am  
- Update requirements file. Installed **python-dateutil and django-celery-beat**
- Add is_expired field to **PlanRegistration** Model
- Add Api routes and viewsets for expired users and users whose policy expires in
  Three months time
- add task to run daily at midnight to check for expired policies and turn
  field **is_expired=True**

8-03-2020
------------

- add endpoint to search(using unique_id and email) for enrollees in the system
- add new field ``is_due_reminder_sent`` to **PlanRegistration model** and renamed
``reminder_sent`` to ``three_month_reminder_sent``
- Add new tasks ``expire_user_plans`` and ``policy_payment_due``  
- Turn the above tasks to crontabs
- Add new email template for policy_payment_due task
- Add new subject for ``policy_payment_due`` in development_settings 

9-03-2020
------------------

- Changed the implementation of ``send_three_months_reminder`` tasks
- Add new serializer in **PlanRegSerilizer**
- added **QueryEnrolleePolicyDate** to query users whose subscription will expire  
  within 14 days of the input date
- Moved all Plan related views to Plan registration viewset
