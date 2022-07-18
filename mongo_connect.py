import pymongo
import urllib.parse
# I need to install some component, pls refer to mongodb official documentation


#As i am mentioned @, I am parsing the user id and password
username = urllib.parse.quote_plus('aisaptarshi')
password = urllib.parse.quote_plus("Peter@123")
conn_str = "mongodb+srv://{}:{}@cluster0.aean8.mongodb.net/?retryWrites=true&w=majority".format(username,password)

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
    print(client)
    dict1 = {

        "name" : "samriddhi sanyal",
        "school":"Assembly of God Church, Asansol"

    }
    db1 = client['mongotest']
    coll = db1['test']
    coll.insert_one(dict1)

except Exception:
    print("Unable to connect to the server.")