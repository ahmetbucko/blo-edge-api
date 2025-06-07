from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from articleModel import Article, ArticleList
import uvicorn

app = FastAPI(
    title="Bloconnect edge API",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex = "http.*",
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

article_list = ArticleList(
    articles=[
        Article(
            id=1,
            user="John Doe",
            title="First Article",
            content="Content of the first article."
        ),
        Article(
            id=2,
            user="Jane Smith",
            title="Second Article",
            content="Content of the second article."
        )
    ]
)

@app.get("/items")
def get_all_items():
    """
    Get all items from the list.
    """
    return article_list

@app.post("/items")
def add_item(item: Article):
    """
    Add a new item to the list.
    """
    if not hasattr(item, "id") or item.id is None:
        raise HTTPException(status_code=400, detail="Item must have 'id'")
    
    # Check if id already exists
    for article in article_list.articles:
        if article.id == item.id:
            raise HTTPException(status_code=400, detail=f"Item with this '{item.id}' already exists")
    
    article_list.articles.append(item)
    return {"message": "Item added successfully", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Delete an item from the list by ID.
    """
    for article in article_list.articles:
        if article.id == item_id:
            article_list.articles.remove(article)
            return {"message": "Item deleted successfully", "article": article}
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)

__all__ = ['app']