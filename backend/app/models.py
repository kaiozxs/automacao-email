from pydantic import BaseModel

class EmailCreate(BaseModel):
    subject: str
    sender: str
    content: str        