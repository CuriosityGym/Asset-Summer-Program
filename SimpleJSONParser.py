import json

myJSONDetails='{"first_name":"Rupin","last_name":"Chheda"}'
myJSON=json.loads(myJSONDetails)
print(myJSON["first_name"])
print(myJSON["last_name"])

