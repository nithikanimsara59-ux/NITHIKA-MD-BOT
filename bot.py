import os
import io
import requests
from google_images_download import google_images_download
from whatsapp_api import WhatsAppBot

BOT_NAME = "NITHIKA MD"
OWNER_NAME = "Nithika"

def handle_message(message):
    text = message.get('text', '').strip()
    chat_id = message.get('chat_id')
    sender = message.get('sender')
    is_view_once = message.get('is_view_once', False)
    media_type = message.get('media_type')
    media_url = message.get('media_url')

    if is_view_once:
        if media_type == "image":
            return {"action": "send_image", "url": media_url, "caption": f"🔓 *Anti-View Once Image Saved* \nBy {BOT_NAME}"}
        elif media_type == "video":
            return {"action": "send_video", "url": media_url, "caption": f"🔓 *Anti-View Once Video Saved* \nBy {BOT_NAME}"}

    if text == ".menu":
        menu_text = f"🤖 *{BOT_NAME}* 🤖\nOwner: {OWNER_NAME}\n\n*Commands:*\n🔹 `.video [youtube_link]` - Download YT Video\n🔹 `.dp [number]` - Download WhatsApp DP\n🔹 `.alive` - Check Bot Status\n\n*Auto Features:*\n🛡️ `Anti-View Once` - Automatic Save"
        return {"action": "send_message", "reply": menu_text}

    elif text == ".alive":
        return {"action": "send_message", "reply": f"👋 Hi, *{OWNER_NAME}*! I am online 24/7."}

    elif text.startswith(".video"):
        url = text.replace(".video", "").strip()
        if not url:
            return {"action": "send_message", "reply": "❌ Please provide a YouTube video link."}
        
        return {"action": "send_video", "url": url, "caption": f"✅ Downloaded by {BOT_NAME}"}

    elif text.startswith(".dp"):
        target_number = text.replace(".dp", "").strip()
        if not target_number:
            return {"action": "send_message", "reply": "❌ Please provide a number. (e.g. .dp 9477xxxxxxx)"}
        
        return {"action": "send_dp", "number": target_number}

    return None
