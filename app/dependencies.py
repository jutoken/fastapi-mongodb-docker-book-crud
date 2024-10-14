from bson import ObjectId
from fastapi import HTTPException, status

async def verify_object_id(id:str):
    try :
        objectid = ObjectId(id)
    except:
        raise HTTPException(detail="Check firstly that you passed a correct object id",status_code=status.HTTP_400_BAD_REQUEST)
    
    return objectid