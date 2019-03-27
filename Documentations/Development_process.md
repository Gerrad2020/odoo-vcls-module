# Our development process

## Developing and adding a new functionality
- Create a new branch from 12.0-vcls_master
- Edit the new branch (make sure to commit and push several times in order to avoid losses and share your work)
- When 12.0-vcls_master is updated, pull the changes within your branch to ensure full-compatibility
- When completed, verify the feasibility of your changes by using Odoo test cases or adding your own test cases before submitting a “pull request” in order to be reviewed by an admin (or merge directly if you’re an admin)
- (Admin) merge changes from 12.0-vcls_master to 12.0-vcls-module to update our Odoo instance

## Applying a fix
**Bugs and problems may occurs in https://vcls.odoo.com. In order to fix these bugs as quick as possible, please follow this process:**
- Create a new branch from 12.0-vcls-module
- Edit the new branch (make sure to commit and push several times in order to avoid losses and share your work)
- When completed, verify the feasibility of your changes by using Odoo test cases or adding your own test cases before submitting a “pull request” in order to be reviewed by an admin (or merge directly if you’re an admin)
- (Admin) merge changes with 12.0-vcls-module and 12.0-vcls-master to update our Odoo instance
- In every other branches, pull the changes from 12.0-vcls-master in order to avoid conflicts

## Add a new user (employee or external resources)
- Create a new GitHub user (if not already exists)
- Add the new user to the VCLS repository
- (If VCLS employee) ask someone from Odoo to add the user to the enterprise repository (limited to 3)
- Select matching rights in the VCLS repository

## Revert back to an old version (of vcls modules only)
Not recommended, do it only when a major bug occur. Reverting back to an older version do NOT revert back any data from our Odoo instance. Only codes is modified.
- Always use Git revert function in order to NOT lose your commit
