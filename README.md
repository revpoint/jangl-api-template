= Jangl API Template for Django 1.8

To create a project with template, make sure you have Django 1.8 installed and type the following command:
```
django-admin.py startproject --template https://github.com/revpoint/jangl-api-template/archive/master.zip --extension=py,ini --name=Dockerfile <project_name> <destination>
```

Or you can add this to your ~/.bash_profile:
```
alias start-api-project='django-admin.py startproject --template https://github.com/revpoint/jangl-api-template/archive/master.zip --extension=py,ini --name=Dockerfile'
```

Then you can simply type:
```
start-api-project <project_name> <destination>
```
