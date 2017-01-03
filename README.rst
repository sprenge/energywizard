energywizard
============
Register meter readings (electricity, gaz, water, ...) and share in groups.  The application makes use of the django and angular 1 frameworks.  This web application has been created in the context of a project to save energy in housholds.  Household members and supervisors can enter and consult meter readings respecting privacy.  Supervisors can enter and read for assigned groups while household member are restricted to their own measurements.  Also support for degree days is foreseen (only implemented for Belgium at this moment).

Entering and consulting meter readings is possible via a user friendly GUI (with mobile support).  Managing the configuration (groups, users, defining meters, assigning meters to household, assigning users to groups) has to be done via the django admin interface.  The configuration management will also be implemented at the GUI level if there is enough interest.

Graphical representation of meter readings (including degree days awareness) is currently under development.

Feel free to contact sprengee54@gmail.com if you need help or more information on this webapplication.

You can find an example of the energy wizard on http://energywizard.strangled.net, use the credentials energywizard/test123!@# as a h
ousehold test account.  You can contact me if you want a demo for the admin part.

The energywizard application is free software (see license) but you can always buy professional services (e.g. installation/commissioning, training, features ...).  I can provide you with a reliable contact if you desire.

Configuration Steps (via admin interface)
-----------------------------------------
- Create a group and assign model rights --> AUTHENTICATION AND AUTHORIZATION
- Create a household and assign to a group --> HOUSEHOLD
- Create a user --> AUTHENTICATION AND AUTHORIZATION
   - assign to one or more groups (one group in case of household user)
   - assign staff user rights to supervisors (never to household users)
- Create energy types (is rather a commissioning step) --> METER
- Create meter types --> METER
- Assign user to a household (this is the initial household for the supervisor) --> HOUSEHOLD
- Assign meter types to the household --> METER

Screenshot for the admin interface : https://github.com/sprenge/energywizard/blob/master/admin_interface.png
