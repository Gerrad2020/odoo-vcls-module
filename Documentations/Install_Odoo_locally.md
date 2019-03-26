# Installing the Odoo Development Environment (Windows 10)
#### Please ensure you have admin's rights on your laptop before following these steps.
#### Ask the administrator for GitHub repository access before following these steps.
#### Ctrl click the links as Github does not support open in new tab.

## Installing The Dependencies (1)

- Install the latest version of [Python](https://www.python.org/downloads/)

![Screenshot Python webpage](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen_python.png)

- Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)
    - Scroll the page until you find "Tools for Visual Studio 2017" & select "Build Tools for Visual Studio 2017"
    - Select all Windows build tools and Web & cloud build tools (except Office/Sharepoint build tools)
    - A restart will be required to finalize the installation

![Screenshot Visual Studio webpage](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen%20vs.png)

- Install the latest version of [PostGreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) (EnterpriseDB installer) (Windows x86-64 version)

For the installation details, follow the step bellow:
![Screenshot postGreSQL installer](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen_pginstall.png)

- For the database superuser please type the following (you'll be asked to enter your password later) :
    - password: KalpaPG
- You don't need to change the default port

- After installation, follow the steps below to finalize the program configuration :
    - Open pgAdmin4 (it will be opened in your default browser)
    - On the "Connect to server" prompt, type your postgres password and check "Save Password" box
    - Create a new user
        - login: odoo
        - password: odoo

![Screenshot pgadmin4](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/PostgreSQL_install2.JPG)
![Screenshot pgadmin4](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/PostgreSQL_install3.JPG)
![Screenshot pgadmin4](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/PostgreSQL_install4.JPG)



- Install the latest version of [NodeJS](https://nodejs.org/en/) (LTS for Windows x64 version)
    - Accept all the default settings

- Install Git and GitHub desktop
    - [Git](https://git-scm.com/download)
    - [GitHub desktop](https://desktop.github.com/)
    - Accept all the default settings for both

## Copy Odoo source files and VCLS source files
- Create a new directory (it will store your Odoo files)

![screenshot folder](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen_folder.png)

- Open your git client (I will use GIT BASH) and go to your folder:

![Screenshot Git Bash](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen_git.png)

- Clone the [Odoo Community repository](https://github.com/odoo/odoo.git):
```
git clone https://github.com/odoo/odoo.git
```

- (If possible) Clone the [Odoo Enterprise repository](https://github.com/odoo/enterprise.git):
```
git clone https://github.com/odoo/enterprise.git
```

- Clone the [VCLS repository](https://github.com/VCLS-org/odoo-vcls-module.git):
```
git clone https://github.com/VCLS-org/odoo-vcls-module.git
```

## Install dependencies (2)
- Open a CMD
- Go to your Odoo path:
```
cd YourOdooPath
```

- Install Less using NodeJS:
```
npm install –g less
```

- Install psycopg2
```
pip install psycopg2
```

- Install psutil
```
pip install psutil
```

- Open requirements.txt at YourOdooPath/odoo/requirements.txt
- Edit the file:
    - remove psycopg2 & psutil as you already have it
    - remove the optional Pillow, python-ldap and gevent because they require compilation
    - add pypiwin32 because it's needed under windows
```
pypiwin32 ; sys_platform == ‘win32’
```

- Go again to your CMD and naviguate to your Odoo path
- Install everything in requirements.txt
```
pip install –r requirements.txt
```

## Running Odoo for the first time
- Open a CMD and go to YourOdooPath/odoo
- Run Odoo in a local instance:
```
python ./odoo-bin -w odoo -r odoo --addons-path=addons,../enterprise,../odoo-vcls-module
```

![Screenshot cmd](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen_cmd.png)

- Open any web browser and type the address of your HTTP server:
    - You will be asked to create a new database:

![Screenshot database](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen_db.png)

- Go to Apps and install all VCLS modules (error may occur because of module’s dependencies):

![Screenshot apps](https://github.com/VCLS-org/odoo-vcls-module/blob/12.0-Documentations/Documentations/img/screen_apps.png)



