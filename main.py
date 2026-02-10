from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title="Pregnancy Care AI Chatbot")

# Allow frontend connection
app.mount("/static",
         StaticFiles(directory = "static", html = True),
          name = "static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    language: str | None = "en"   # en / hi / hinglish



# ---------------- AI LOGIC ---------------- #

def pregnancy_answers(lang):
    responses = {
        "en": [
            "Pregnancy is a beautiful journey 🤍 Make sure you eat nutritious food, stay hydrated, and get enough rest.",
            "During pregnancy, regular checkups, iron-rich foods, and gentle exercise are very important.",
            "Avoid alcohol, smoking, and raw foods during pregnancy."
        ],
        "hi": [
            "गर्भावस्था एक सुंदर यात्रा है 🤍 संतुलित आहार और आराम बहुत ज़रूरी है।",
            "प्रेगनेंसी में नियमित जांच और पोषक तत्व लेना जरूरी होता है।",
            "शराब और धूम्रपान से दूर रहें।"
        ],
        "hinglish": [
            "Pregnancy ek beautiful journey hai 🤍 healthy khana, rest aur hydration zaroori hai.",
            "Pragnancy mein doctor checkups aur iron-rich food bahut important hai."
        ]
    }
    return random.choice(responses.get(lang, responses["en"]))


def nutrition_answers(lang):
    responses = {
        "en": [
            "Eat fruits, vegetables, whole grains, milk, nuts, and pulses during pregnancy.",
            "Avoid junk food, excess sugar, and street food during pregnancy.",
            "Iron, calcium, folic acid, and protein are essential nutrients."
        ],
        "hi": [
            "फल, सब्ज़ियां, दूध और दालें गर्भावस्था में बहुत फायदेमंद होती हैं।",
            "जंक फूड और ज्यादा मीठा खाने से बचें।"
        ],
        "hinglish": [
            "Fruits, veggies, milk aur protein pregnancy mein must hote hain.",
            "Junk food avoid karna better hota hai."
        ]
    }
    return random.choice(responses.get(lang, responses["en"]))


def exercise_answers(lang):
    responses = {
        "en": [
            "Walking, prenatal yoga, and breathing exercises are safe during pregnancy.",
            "Avoid heavy workouts and high-impact exercises.",
            "Always consult your doctor before starting exercise."
        ],
        "hi": [
            "प्रेगनेंसी में हल्की वॉक और योग फायदेमंद होते हैं।",
            "भारी व्यायाम से बचें।"
        ],
        "hinglish": [
            "Light walking aur prenatal yoga safe hote hain.",
            "Heavy workout avoid karo."
        ]
    }
    return random.choice(responses.get(lang, responses["en"]))


def postpartum_answers(lang):
    responses = {
        "en": [
            "Postpartum recovery takes time. Rest, good nutrition, and emotional support are important.",
            "Mild exercises and pelvic floor workouts help after delivery.",
            "Postpartum mood swings are normal, but seek help if sadness persists."
        ],
        "hi": [
            "डिलीवरी के बाद शरीर को ठीक होने में समय लगता है।",
            "भावनात्मक सहयोग बहुत जरूरी होता है।"
        ],
        "hinglish": [
            "Delivery ke baad rest aur nutrition bahut zaroori hai.",
            "Mood swings common hote hain."
        ]
    }
    return random.choice(responses.get(lang, responses["en"]))


def childcare_answers(lang):
    responses = {
        "en": [
            "For babies under 6 months, only breast milk or formula is recommended.",
            "Introduce solid foods slowly after 6 months.",
            "Always check food allergies before feeding new food."
        ],
        "hi": [
            "6 महीने तक केवल मां का दूध या फॉर्मूला दूध दें।",
            "धीरे-धीरे ठोस आहार शुरू करें।"
        ],
        "hinglish": [
            "6 months tak sirf breast milk best hota hai.",
            "Solid food slowly introduce karo."
        ]
    }
    return random.choice(responses.get(lang, responses["en"]))


def mental_health_answers(lang):
    responses = {
        "en": [
            "It’s okay to feel overwhelmed. You are doing your best 🤍",
            "Talking to someone you trust can help reduce stress.",
            "Meditation and deep breathing can calm your mind."
        ],
        "hi": [
            "तनाव महसूस करना सामान्य है। आप अच्छा कर रही हैं 🤍",
            "किसी अपने से बात करना मददगार होता है।"
        ],
        "hinglish": [
            "Overwhelmed feel karna normal hai 🤍",
            "Deep breathing try karo."
        ]
    }
    return random.choice(responses.get(lang, responses["en"]))


# ---------------- MAIN CHAT ROUTE ---------------- #
@app.get("/", response_class = HTMLResponse)
async def home():
    with open("static/index.html") as f:
        return f.read()


@app.post("/chat")
def chat(req: ChatRequest):
    msg = req.message.lower()
    lang = req.language or "en"

    if any(word in msg for word in ["hi", "hello", "hey", "namaste"]):
        return {"reply": random.choice([
            "Hello 🤍 How can I help you today?",
            "Hi there 🌸 Ask me anything about pregnancy or childcare.",
            "Namaste 🙏 Main aapki madad ke liye hoon."
        ])}

    if "pregnan" in msg:
        return {"reply": pregnancy_answers(lang)}

    if any(word in msg for word in ["food", "eat", "nutrition", "diet"]):
        return {"reply": nutrition_answers(lang)}

    if any(word in msg for word in ["exercise", "yoga", "workout"]):
        return {"reply": exercise_answers(lang)}

    if any(word in msg for word in ["postpartum", "after delivery"]):
        return {"reply": postpartum_answers(lang)}

    if any(word in msg for word in ["baby", "child", "infant"]):
        return {"reply": childcare_answers(lang)}

    if any(word in msg for word in ["sad", "stress", "anxiety", "depressed"]):
        return {"reply": mental_health_answers(lang)}

    return {
        "reply": random.choice([
            "I’m here to support you 🤍 Please tell me more.",
            "Could you explain your concern a bit more?",
            "I can help with pregnancy, baby care, nutrition, or mental health 🌸"
        ])
    }
