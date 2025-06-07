from pydantic import BaseModel, Field

class ArticleList(BaseModel):
    articles: list['Article'] = []

class Article(BaseModel):
    id: int = Field(..., description="The unique identifier for the article")
    user: str = Field(..., description="The URL of the article")
    title: str = Field(..., description="The title of the article")
    content: str = Field(..., description="The content of the article")