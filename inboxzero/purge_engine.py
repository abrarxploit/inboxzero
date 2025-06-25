from inboxzero.auth import get_gmail_token
from inboxzero.ai_engine import analyze_sentiment
from googleapiclient.discovery import build
from base64 import urlsafe_b64decode
from email import message_from_bytes

def purge_inbox():
    token_hash, creds = get_gmail_token()
    service = build("gmail", "v1", credentials=creds)

    results = {"kept": [], "deleted": []}
    
    print("[INFO] Fetching recent emails...")
    messages = service.users().messages().list(userId="me", maxResults=20).execute().get("messages", [])
    print(f"[DEBUG] Total emails retrieved: {len(messages)}")

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        payload = msg_data.get("payload", {})
        headers = payload.get("headers", [])
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        snippet = msg_data.get("snippet", "")

        label, confidence = analyze_sentiment(snippet)
        print(f"[ANALYSIS] '{subject}' => {label} ({confidence * 100:.2f}%)")

        if label == "NEGATIVE":
            service.users().messages().delete(userId="me", id=msg["id"]).execute()
            results["deleted"].append({"id": msg["id"], "subject": subject, "confidence": confidence})
            print(f"🗑️ Deleted: {subject}")
        else:
            results["kept"].append({"id": msg["id"], "subject": subject, "confidence": confidence})
            print(f"✅ Kept: {subject}")

    return results
if __name__ == "__main__":
    purge_inbox()

