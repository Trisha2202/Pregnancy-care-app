
# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Pregnancy AI Companion - Expanded")

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class ChatRequest(BaseModel):
    message: str
    user_name: str = "Guest"
    pregnancy_month: int = None
    postpartum_weeks: int = None
    baby_age_months: int = None

# Home endpoint
@app.get("/")
async def home():
    return {"message": "Expanded Pregnancy AI Companion Backend is alive!"}

# Chat endpoint
@app.post("/chat")
async def chat_endpoint(data: ChatRequest):
    message = data.message.lower()
    user_name = data.user_name or "Guest"
    reply = ""

    # ===== Stress & Mental Health =====
    if any(word in message for word in ["stress", "anxiety", "anxious", "worry"]):
        reply = (
            f"Hi {user_name}, I understand pregnancy can be stressful.\n"
            "- Practice deep breathing exercises 5-10 minutes daily.\n"
            "- Try gentle prenatal yoga.\n"
            "- Keep a journal to express your thoughts.\n"
            "- Talk to a partner, friend, or counselor.\n"
            "- Avoid overexertion and ensure proper sleep."
        )

    elif any(word in message for word in ["sleep", "insomnia", "tired"]):
        reply = (
            f"{user_name}, for better sleep during pregnancy:\n"
            "- Sleep on your left side with pillows for support.\n"
            "- Keep a consistent bedtime routine.\n"
            "- Avoid caffeine or heavy meals 3 hours before bed.\n"
            "- Take short naps during the day if needed."
        )

    # ===== Nutrition =====
    elif any(word in message for word in ["nutrition", "diet", "food", "meal"]):
        reply = (
            f"{user_name}, here’s some nutrition advice:\n"
            "- Include leafy greens, colorful vegetables, and fruits.\n"
            "- Eat protein-rich foods: eggs, chicken, fish low in mercury, beans.\n"
            "- Whole grains for energy and fiber.\n"
            "- Dairy for calcium (milk, yogurt, cheese).\n"
            "- Stay hydrated: 8-10 glasses of water daily.\n"
            "- Avoid alcohol, raw meat, unpasteurized cheese, and excessive caffeine."
        )

    elif any(word in message for word in ["craving", "foods to avoid"]):
        reply = (
            f"{user_name}, during pregnancy:\n"
            "- Moderation is key. Occasional cravings are fine.\n"
            "- Avoid excessive junk food, highly processed foods, and sugary drinks.\n"
            "- Reduce consumption of high-mercury fish (shark, swordfish, king mackerel).\n"
            "- Limit caffeine to 1-2 cups of coffee per day."
        )

    # ===== Exercise & Yoga =====
    elif any(word in message for word in ["exercise", "yoga", "stretching", "walk"]):
        reply = (
            f"{user_name}, prenatal exercise tips:\n"
            "- Daily walking for 20-30 mins is safe and effective.\n"
            "- Prenatal yoga helps flexibility, reduces stress, and strengthens muscles.\n"
            "- Avoid high-impact or contact sports.\n"
            "- Do Kegel exercises to strengthen pelvic floor muscles.\n"
            "- Stop any activity if you feel dizziness, pain, or bleeding."
        )

    # ===== Postpartum =====
    elif any(word in message for word in ["postpartum", "after delivery", "recovery"]):
        reply = (
            f"{user_name}, postpartum recovery tips:\n"
            "- Rest whenever you can and accept help from family.\n"
            "- Gentle stretches and light walking improve recovery.\n"
            "- Eat nutritious meals and stay hydrated.\n"
            "- Breastfeeding requires patience and support.\n"
            "- Watch for mood changes; postpartum depression is common and normal. Seek help if needed."
        )

    elif any(word in message for word in ["breastfeeding", "milk supply", "lactation"]):
        reply = (
            f"{user_name}, breastfeeding guidance:\n"
            "- Nurse on demand, typically every 2-3 hours.\n"
            "- Ensure proper latch to prevent pain.\n"
            "- Stay hydrated and maintain a balanced diet.\n"
            "- Rest as much as possible.\n"
            "- Track feeding times and baby’s weight gain for guidance."
        )

    # ===== Baby / Childcare =====
    elif any(word in message for word in ["baby", "newborn", "infant", "childcare"]):
        reply = (
            f"{user_name}, newborn care tips:\n"
            "- Feed on demand; monitor baby’s hunger cues.\n"
            "- Burp the baby after every feed.\n"
            "- Keep skin clean; change diapers frequently.\n"
            "- Safe sleep: baby on back, firm mattress, no loose bedding.\n"
            "- Monitor for rashes and use gentle, baby-safe skincare products."
        )

    elif any(word in message for word in ["baby food", "food for baby", "infant nutrition"]):
        age = data.baby_age_months or 6
        if age <= 6:
            reply = (
                f"{user_name}, babies 0-6 months should be exclusively breastfed or formula-fed. "
                "Avoid solid foods until about 6 months."
            )
        elif 6 < age <= 8:
            reply = (
                f"{user_name}, babies {age} months can start pureed fruits, vegetables, and cereals. "
                "Introduce one new food at a time and watch for allergies."
            )
        elif 8 < age <= 12:
            reply = (
                f"{user_name}, babies {age} months can eat soft finger foods like mashed fruits, cooked vegetables, and small pieces of soft proteins. "
                "Avoid honey, whole nuts, and processed sugar."
            )
        else:
            reply = f"{user_name}, continue age-appropriate meals with balanced nutrition and avoid processed foods."

    elif any(word in message for word in ["baby skincare", "baby lotion", "baby oil"]):
        reply = (
            f"{user_name}, baby skincare tips:\n"
            "- Use gentle, fragrance-free lotions.\n"
            "- Natural oils like coconut oil are safe in small amounts.\n"
            "- Avoid adult skincare products.\n"
            "- Patch test any new product.\n"
            "- Keep skin clean and dry to prevent rashes."
        )

    # ===== General fallback =====
    else:
        reply = (
            f"Hi {user_name}! I am your AI Pregnancy & Childcare Companion.\n"
            "I can help with:\n"
            "- Stress, sleep, nutrition, and exercise during pregnancy\n"
            "- Postpartum recovery, breastfeeding, mental health\n"
            "- Baby feeding, nutrition, and skincare\n"
            "- Ask me questions like 'How can I reduce stress?', 'What foods are safe?', or 'Postpartum exercises'."
        )

    return {"reply": reply}