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
        cur = supabase.cursor()
        cur.execute(
            """
            INSERT INTO Emails (subject, sender, content, classification, response)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
            """,
            (email.subject, email.sender, email.content, classification, response)
        )
        email_id = cur.fetchone()[0]
        supabase.commit()
        return {"id": email_id, "classification": classification, "response": response}
    except Exception as e:
        supabase.rollback()
        raise HTTPException(status_code=500, detail=str(e))