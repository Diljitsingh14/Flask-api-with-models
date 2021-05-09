from models import constrains,Model
structs = [
    {"name":"id","type":"INTEGER","constrains":[constrains["primary key"],constrains["auto"]]},
    {"name":"name","type":"varchar(20)","constrains":[constrains['not null'],constrains["default"]]},
    {"name":"class","type":"varchar(20)","constrains":[constrains['not null']]},

]
users = Model("user")
try:
    users.migrate(structs)
except:
    pass