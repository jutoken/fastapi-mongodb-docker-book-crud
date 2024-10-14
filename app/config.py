import motor.motor_asyncio 

client = motor.motor_asyncio.AsyncIOMotorClient("db",27017)
db = client.library
collection = db.get_collection("books")