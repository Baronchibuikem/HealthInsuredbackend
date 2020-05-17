# DATE : 5-12-2019

Created policy, plan and client models

# DATE : 6-12-2019

Created ClientIndividual and ClientOrganization forms

# DATE : 10-12-2019

Refactored forms for ClientIndividual and ClientOrganization because fields in our database kept changing.

Created queries and logic for clientIndividual to get it to work and be saved to our database

Created queries and logic for clientOrganization to get it to work and be saved to our database

Implemented a test mockup(template) to be able to visualize the forms and form is being saved to our database when a user enters data in the fields

Connected the models to the admin interface so the superuser can be able to perform CRUD operations from the admin interface

# DATE : 11-12-2019

As a result of changing requirement, i restructured the staff, staffrole and staffpermission models which we were initially using and embedded all of them to a new model class called Staff which has a foreignKey relationship to django user model.

Implemented login functionality for the new created staff models which will allow them login to the platform

Created html templates to visualize the login interface and confirmed the login functionality was working

Implemented queries that maps a perculiar and customized page to a clientIndividual upon registration

Implemented queries that maps a perculiar and customized page to a clientOrganization upon registration

# DATE : 17-12-2019

Implemented template for Landing page, login page, Registration page for both Organization and Individuals, Individual profile page and organization profile page

Changed the Organization and Individual forms to use form.Form against the initial modelform it was using and wrote the logic to save them in the database.

Added image field to ClientIndividual model and added it to both IndividualForm and individual_signup_view

Added Pillow to render images and updated Requirements.txt

Updated common.py in settings and added static root and paths

# DATE : 18-12-2019

Created a form to handle claims upload in app_claims

Implemented logic to process the claims form and ensured it's saved to the database

Created template files to display the form to the user

Created dashboard template for Organization and Individuals

# DATE : 19-12-2019

Created templates for vetting Claims and claims payment

Implemented logic to connect the views i wrote for claims vetting, claims payment, batch claims and view all claims

Refactored the design implementation of Upload_claims templates

# DATE : 20-12-2019

Connected all the app_claims views and logic to their urls, and templates

# DATE : 23-12-2019

Redesigned the claims upload form to match the mockup provided by the design team

Refactored the Claims model fields to match what was asked of us from the design provided

Refactored the claim_upload template to match the mockup provided by the design team

# DATE : 24-12-2019

Implemented an edit functionality to allow approved users to be able to edit a claims form that has been save on the database

Implemented the template design for the edit form

Added the url that connects the edit functionality to it's respective template

# DATE : 25-12-2019

Customized the app_claim and App_enrollment tables in the admin interface to show more
helpful details for the super Admin user to easily relate with

Deleted views for view_claims_within_batches and complete_or_incomplete_claims along with their respective urls, views_implementation and templates as they were only redunctant and weren't doing much.

# DATE : 27-12-2019

Implemeted a delete functionality for claims uploded into the database.(This means claims can now be both edited and deleted by the approved staff)

# DATE : 7-1-2020

Created api_views folder in app_claims and added batch_upload, careprovider, claims_view, payment_view and their logic

Created serializer folder in app_claims and added batch_serializer, careprovider_serializer, claims_serializer, payment_serializer and their logic

Created URL's for the different app_claims endpoint

# DATE : 7-1-2020

Implemented accept payment and reject payment functionality to app claim and created their endpoint

# DATE : 8-1-2020

Restructured the whole codebase and started adding docstring

# DATE : 13-1-2020

Added functionality to generate a unique ID for a user upon registration

Added activation functionality to allow dependents to be activated or deactivated

Changed the fields in the Dependent model instance

# DATE : 14-1-2020

Added functionality that allows you make query to get the profile of a particular user base on their unique ID's

# DATE : 17-1-2020

Fixed a bug that was occuring when you try to log into the admin interface (removed the custom hashing we added to the CustomUser model

# DATE : 20-1-2020

Refactored the payment schedule endpoint to be able to fetch the total sum of approved claims

Added functionality to ensure user login with their email address and not username

# DATE : 27-1-2020

Created models for FamilyPlanning, OutPatientConsultantion and Management

Created serializers for FamilyPlanning, OutPatientConsultantion and Management

implemented logic to handle CRUD operation on FamilyPlanning, OutPatientConsultantion and Management viewsets

Connect the viewsets to their respective url's

# DATE : 31-1-2020

Created API endpoint to query users and their details

# DATE : 3-2-2020

Refactored the claim serializer to allow claim_batch field to display batch name

Added django test to test the various API endpoints in app_claims

# DATE : 5-2-2020

Removed password hashing functionality from the customUser

Modified the serializers in app_claim and renameed their corresponding endpoints

# DATE : 6-2-2020

Fixed a bug in the PlanRegistration model that wasn't allowing the data to be saved in the database

# DATE : 7-2-2020

Removed permissions from app_claims

Added created_by field in app_claims Batch model

Add id to PlanRegistrationSerializer and made it a read_only
