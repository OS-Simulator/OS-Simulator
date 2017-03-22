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

## Module Structure and I/O

process/utils.py
```python
def roundrobin(data):
  at0 = data[0]["at"] # at of first process in list
  bt0 = data[0]["bt"] # bt of first process in list
  no0 = data[0]["no"] # Pno of first process in list
  ...
  ...
  return result
```

### Input: data - a list of dictionaries
```pyton
element = {"at":1,
           "bt":2,
           "no":1}
data = [list of elements]
```
 `
 [{"at":1,"bt":2,"no":1},{"at":0,"bt":3,"no":2},{"at":2,"bt":5,"no":3}]
 `
 
### Output - result - contains two lists "gantt" and "table"
```python
tableElement = {'tat': 8,     
                'no': 1,
                'wt': 8, 
                'bt': 0, 
                'at': 1, 
                'ct': 9}
          
ganttElement = {'stop': 3, 
                'no': 1, 
                'start': 1}
                
result ={ 'table': [list of tableElements],
          'gantt': [list of ganttElements] }
```
 `
 {'table': [{'tat': 8, 'no': 1, 'wt': 8, 'bt': 0, 'at': 1, 'ct': 9}, {'tat': 12, 'no': 2, 'wt': 12, 'bt': 0, 'at': 2, 'ct': 14}, {'tat': 13, 'no': 3, 'wt': 13, 'bt': 0, 'at': 3, 'ct': 16}], 'gantt': [{'stop': 3, 'no': 1, 'start': 1}, {'stop': 5, 'no': 2, 'start': 3}, {'stop': 7, 'no': 3, 'start': 5}, {'stop': 9, 'no': 1, 'start': 7}, {'stop': 11, 'no': 2, 'start': 9}, {'stop': 13, 'no': 3, 'start': 11}, {'stop': 14, 'no': 2, 'start': 13}, {'stop': 16, 'no': 3, 'start': 14}]}
`
