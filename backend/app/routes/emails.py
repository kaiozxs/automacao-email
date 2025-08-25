from fastapi import APIRouter, HTTPException
from app.models import EmailCreate
from app.database import supabase
from app.services.classifier import classify_email, generate_response

router = APIRouter()

@router.post("/emails")
def create_email(email: EmailCreate):
    classification = classify_email(email.content)
    response = generate_response(classification)

    try:
        # Inserir registro no Supabase
        result = supabase.table("Emails").insert({
            "subject": email.subject,
            "sender": email.sender,
            "content": email.content,
            "classification": classification,
            "response": response
        }).execute()

        if not result.data:
            raise HTTPException(status_code=500, detail="Falha ao salvar no Supabase")

        new_email = result.data[0]  # pega o registro inserido
        return {
            "id": new_email["id"],
            "classification": classification,
            "response": response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
