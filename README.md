# Flask-api-with-models
### migration.py
    create structure of your model
    structure is array of python dict (ie: [{...},{...},{...}]) and each dict contains the fields information like "name" of field , "type"(ie: INT ,CHAR ,DATE etc all sqlite data types) , and constrains of fields like (primary key , auto increment , unique etc) 
    ### constrains of fields:
        constrains = {"not null":"NOT NULL",
                      "unique":"UNIQUE",
                      "primary key":"PRIMARY KEY",
                      "check":"", # value will be a condition
                      "default":"", #  enter default values
                      "auto":"AUTOINCREMENT"}
        create object of Model class and pass name of the model or tabel to create in database (ie : users = Model("user"))
        users.migrate() # to make changes in data base
        by default sqlite database file name is  "api_Database.db" but you can change the name , by change value of __Database_ variable (model.py)
      
### Modal class methods
    get_all(self) : returns JSON serialize data of all the row present in a model. (ie: [{...}, {....}, .... ,{...}])
                    usage : users.get_all()
    insert(self,data)  : to insert data into database. it's take dict type data with key_names are the fields of tabel and their values (ie: {"name":"abc","class":"MCA"})
                         usage : users.insert({"name":"abc","class":"MCA"})
    describe(self) : it return structure of tabel/model
    serialize(self) : it return JSON serialize Data of given query.
    filter(self,filter) : to get the rows that passes filter example : to get row have id = 2 , ===> users.filter({id:2});
    update(self,data,id) : to update the data in a row, it takes data to update & id of row. example : ===> users.update({"name":"ABC","class":"BCA"},2)
    delete(self,id) : to delete the row in a table having the following id pass to the method.
    
    
        
