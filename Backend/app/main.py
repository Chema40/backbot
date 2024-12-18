from fastapi import FastAPI, HTTPException
from app.models import AssistanceRequest, deparments
from app.services import contact_method

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: AssistanceRequest):

    if request.topic.lower() in deparments:
        status, response = contact_method()
        if status == 200:
            data = [item for item in response if item["department"] == request.topic]

        if status != 200:
            raise HTTPException(status_code=500, detail=f"Contact Error: {response}")
        return {"message": data[0]}
    
    else:
        raise HTTPException(status_code=400, detail="Unsupported department")
