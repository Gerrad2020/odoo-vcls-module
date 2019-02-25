# Branches
## Branch logic
### 12.0-vcls-module
This is our principal branch which is synchronized with our Odoo instance at https://vcls.odoo.com.
Every changes in this branch will directly impact everyone in the company.
For these reasons, only GitHub admin can do changes to this branch. It is strongly advised to not edit directly this branch but modify 12.0-vcls-master and then merge 12.0-vcls_master into 12.0-vcls-module.

#### Applied protection rules :
- Restrict who can push to matching branches

### 12.0-vcls_master
This is our main development branch. When a new functionality is being developed, every stable version must be committed on this branch until the everything is done. Once this branch is stable enough then Git admins can push the changes to 12.0-vcls-module to release the new version to the entire organization.
This branch can be used in order to perform some tests with some key users but it is not intended to be shared within the whole company and is not supposed to be a replacement for 12.0-vcls-module.

This branch is managed by Git admins, it is not possible for a normal developer to makes changes to this branch directly. Normal developer must do a “pull request” and be approved by a Git admin in order to modify this branch.

Every new branch must be created from this branch in order to ensure full compatibility when merged.

#### Applied protection rules :
- Require “pull request” reviews before merging

### Every other branches
Every other branches must be created from 12.0-vcls_master and be deleted when it is not used anymore. For every new committed version of 12.0-vcls_master, changes must be pulled as soon as possible to ensure again a full compatibility when merged within the main development branch.
Every Git collaborator has the right to create, edit and delete new branch, Git admins are not supposed to manage all branches. This task is entrusted to the creator of the branch.

#### Applied protection rules :
- None

## Naming convention
Aside from the main branch and the main development branch, every branch must follow this naming convention :
```
[Odoo version]-[functionality developed within this branch]
```
#### Example:
- 12.0-vcls_leave_module
- 12.0-fix_bug_ticket

The name of the branch must be as clear as possible.
