from fastapi import  FastAPI
from app.config import collection
from app.books import Book,Book_ID
from typing import  List
from bson import ObjectId
from app.dependencies import *


app = FastAPI(title="Tersea Demo",version="1.0.0",summary="This is a demo for tersea group",description="Books CRUD")

@app.get("/books/",tags=["Books"])
async def list_books()->List[Book_ID]:
    """
    List all DB Books
    """
    return await collection.find().to_list()

@app.get("/books/{id}",tags=["Books"])
async def get_book(id:str)->Book_ID:
    """
    Get specific Book by ID
    """
    id = await verify_object_id(id)    
    book =  await collection.find_one( {"_id" : ObjectId(id) } )

    if book :
        return book
    else :
        raise HTTPException(detail="id does not exist in db",status_code=status.HTTP_404_NOT_FOUND)
    

@app.post("/books/",tags=["Books"])
async def add_book(item:Book)->Book_ID:
    """
    Add new Book
    """
    book = item.model_dump()
    new_book = await collection.insert_one(book)
    
    return await collection.find_one({"_id":new_book.inserted_id})

@app.put("/books/{id}",tags=["Books"])
async def update_book(id:str,item:Book)->Book_ID:
    """
    Update Book based on ID
    """
    objectid = await verify_object_id(id)
    
    new_book = item.model_dump()
    update = await collection.update_one({"_id":objectid},{"$set":new_book})
    
    if update.modified_count == 1 :
        return await collection.find_one({"_id":objectid})
    else :
        raise HTTPException(detail="It does not updated, verify you ID !!!!",status_code=status.HTTP_400_BAD_REQUEST)
    
@app.delete("/books/{id}",tags=["Books"])
async def delete_book(id:str)->dict:
    """
    Delete Book based on id
    """
    objectid = await verify_object_id(id)    
    deleted = await collection.delete_one({"_id":objectid})    
    if deleted.deleted_count:
        return {"message": "deleted successfully"}
    else:
        raise HTTPException(detail="It does not deleted, Verify your ID !!!!",status_code=status.HTTP_400_BAD_REQUEST)