from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MessageRequest(BaseModel):
    message: str

@app.post("/process")
def process_message(request: MessageRequest):
    message = request.message
    return {"message": message.upper(),
            "length": len(message),
            "reversed": message[::-1]}