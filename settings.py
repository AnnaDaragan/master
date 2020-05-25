MONGO_URI="mongodb+srv://nameUser:@dateapi-fbdwm.mongodb.net/ApiDBName"
#J5mJRhwn1j2RwLx1
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

X_DOMAINS = '*'
ALLOW_UNKNOWN=True

CollectionApi= {
    "_items":{
        "shema":{
            "id": {"type":"string"},
            "userName": {"type":"string"},
            "post": {
                "title": {"type":"string"},
                "content": {"type":"string"}
                }
         }
    }
}

DOMAIN = {
    "CollectionApi": CollectionApi
    }
