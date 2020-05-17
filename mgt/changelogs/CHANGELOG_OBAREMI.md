DATE : 4-12-2019
=======================

add a new function to get all staffs count in repository_staff_get_all

DATE : 5-12-2019
=======================

-add model Department

-made all imports absolute to their modules

DATE : 6-12-2019
=======================

-created repositories for the models of app_enrollment

-resturctured the project to be more inline with django defaults

-added the template and static structure

-created simple UIs, for landing-page,signin-modal to test the template,static and views workflow

DATE : 9-12-2019
=======================

added RBAC for staff to the model structure
--------------------------------------------

-added a **StaffRole Model**,**StaffRolePermissions Model**

-updated the **Staff Model** with a **ForeignKey** to **StaffRole Model**

DATE : 10-12-2019
=======================

updated the model
-----------------------

-removed the **Policy Model** after consulting with PM(project manager) on the use of it

-refactored **Policy Model** ForeignKey out of **Clients Models(ClientIndividual and ClientOrganization)** 
and relaced it with **Plan**

-add **ForeignKey** from Clients(ClientIndividual and ClientOrganization) to Enrollees

DATE : 11-12-2019
=======================

-created a **migration post_migrate signal** run after every migrations that checks if default groups are present 
and updates their permissions if not the group is created and permissions are given

DATE : 17-12-2019
=======================
-created a **seed function** that runs after every migration to add default data
-improved the default creation of groups and permissions

DATE : 18-12-2019
=======================
-implemented login