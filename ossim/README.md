# OS-SIM Django Web app

## Structure
.  
├── disk  
├── job  
├── memory  
├── ossim  
├── process  
├── synchro  
├── db.sqlite3  
├── manage.py  
└── README.md


Each web app has similar structure within. Example, the 'process' app/folder:

.  
├── templates  
│   └── process  
│       ├── detail.html  
│       ├── index.html  
│       └── process.html  
├── admin.py  
├── apps.py  
├── __init__.py  
├── models.py  
├── tests.py  
├── urls.py  
├── utils.py  
└── views.py  


### All functions pertaining to each section should be added to the utils.py file in respective app

## Static Files

All static files are to be added to the static folder inside the ossim folder in the current directory.

It looks like this

.  
├── static  
│   ├── css  
│   │   └── demo.css  
│   └── js  
│       ├── display.js  
│       └── input.js  
├── templates  
│   └── ossim  
│       └── index.html  
├── __init__.py  
├── settings.py  
├── urls.py  
├── views.py  
└── wsgi.py  
