DATE : 5-12-2019
=======================
1. add .gitignore file to project root
2. modify Staff model fields in app_enrollment
3. modify default names for app_enrollment models instances

DATE : 10-12-2019
=======================
1. add csv validator and serializer function to util functions

DATE : 13-12-2019
=======================
1. write test for csv validator function
2. add test for csv serialization function

DATE : 16-12-2019
=======================
1. write test for batch csv registration celery task


DATE: 20-12-2019
=======================
1. Modify test for csv registration (model changed)
2. Hook Up batch CSV Registration task into views template
3. Add async AJAX POST request for csv registration
4. Modify table listing for registered users(enrollee) in an organization 


DATE: 06-01-2020
=======================
1. Add restframework support for project


DATE: 07-01-2020
=======================
1. Add custom backend support for client models


DATE: 08-01-2020
=======================
1. Refractor/Encapsulate api in individual app
2. Generate token for users on post request api auth-token