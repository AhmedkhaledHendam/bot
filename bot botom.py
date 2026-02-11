 
import telebot
from telebot import types
import sqlite3
import json

TOKEN = "8573382461:AAHsJj-p4DxzZlfaISP3aMTRRrGkOykwUgM"
bot = telebot.TeleBot(TOKEN)

# ================= DATABASE =================
conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    chat_id INTEGER PRIMARY KEY,
    state TEXT,
    category TEXT,
    answers TEXT,
    product TEXT,
    history TEXT
)
""")
conn.commit()


def get_user(chat_id):
    cursor.execute("SELECT * FROM users WHERE chat_id = ?", (chat_id,))
    row = cursor.fetchone()

    if row:
        return {
            "state": row[1],
            "category": row[2],
            "answers": json.loads(row[3]) if row[3] else {},
            "product": row[4],
            "history": json.loads(row[5]) if row[5] else []
        }
    else:
        user = {
            "state": "WELCOME",
            "category": None,
            "answers": {},
            "product": None,
            "history": []
        }

        cursor.execute("""
            INSERT INTO users (chat_id, state, category, answers, product, history)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (chat_id, "WELCOME", None, json.dumps({}), None, json.dumps([])))

        conn.commit()
        return user


def save_user(chat_id, user):
    cursor.execute("""
        UPDATE users
        SET state = ?, category = ?, answers = ?, product = ?, history = ?
        WHERE chat_id = ?
    """, (
        user["state"],
        user["category"],
        json.dumps(user["answers"]),
        user["product"],
        json.dumps(user["history"]),
        chat_id
    ))
    conn.commit()


def set_state(chat_id, user, new_state):
    if user["state"] != new_state:
        user["history"].append(user["state"])
        user["state"] = new_state
        save_user(chat_id, user)


def go_back(chat_id, user):
    if user["history"]:
        user["state"] = user["history"].pop()
    else:
        user["state"] = "MAIN"

    save_user(chat_id, user)

    if user["state"] == "MAIN":
        bot.send_message(chat_id, "اختار القسم 👇", reply_markup=main_menu())
    elif user["state"] == "QUESTIONS":
        ask_questions(chat_id, user)
    elif user["state"] == "PRODUCT":
        product_menu(chat_id, user["category"])


# ================= PRODUCTS =================
PRODUCTS = {
    "face": ["غسولات", "تونر", "مقشرات", "مزيل ميكاب",
             "سيرمات", "مرطبات", "ماسكات", "كريم نهار وليل"],
    "hair": ["شامبو", "بلسم", "كريم شعر",
             "سيرم شعر", "زيوت شعر", "ماسكات شعر"],
    "body": ["اسكراب جسم", "لوشن للجسم",
             "واقي شمس", "بادي سبلاش"],
    "eyes": ["ماسكات وسائد عين", "سيرم تحت العين", "كريم الهالات"],
    "lips": ["ماسكات شفايف", "اسكراب شفايف", "مرطب شفايف"],
    "personal": ["يدين وقدمين (ترطيب)",
                 "يدين وقدمين (تفتيح)", "مزيل عرق"]
}

CATEGORY_NAMES = {
    "face": "🧖‍♀️ الوجه",
    "hair": "💆‍♀️ الشعر",
    "body": "🧴 الجسم",
    "eyes": "👁 العين",
    "lips": "💋 الشفايف",
    "personal": "🪥 العناية الشخصية"
}

QUESTIONS = {
    "face": "نوع بشرتك ايه؟",
    "hair": "مشكلة شعرك الأساسية ايه؟",
    "body": "محتاج ايه أكتر؟",
    "eyes": "مشكلة العين ايه؟",
    "lips": "شفايفك محتاجة ايه؟",
    "personal": "اختار نوع العناية 👇"
}

OPTIONS = {
    "face": ["دهنية", "جافة", "مختلطة", "حساسة"],
    "hair": ["تساقط", "هيشان", "قشرة", "جفاف"],
    "body": ["ترطيب", "تفتيح", "حماية من الشمس"],
    "eyes": ["هالات", "انتفاخ", "ترطيب"],
    "lips": ["ترطيب", "تفتيح", "تشقق"],
    "personal": ["يدين وقدمين", "مزيل عرق"]
}


# ================= MENUS =================
def start_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("▶️ ابدأ")
    return kb


def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🧖‍♀️ الوجه", "💆‍♀️ الشعر")
    kb.add("🧴 الجسم", "👁 العين")
    kb.add("💋 الشفايف", "🪥 العناية الشخصية")
    return kb


def question_menu(options):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for op in options:
        kb.add(op)
    kb.add("🔙 رجوع")
    return kb


def ask_questions(chat_id, user):
    cat = user["category"]
    bot.send_message(
        chat_id,
        QUESTIONS[cat],
        reply_markup=question_menu(OPTIONS[cat])
    )


def product_menu(chat_id, category):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in PRODUCTS[category]:
        kb.add(item)
    kb.add("🔙 رجوع")
    bot.send_message(chat_id, "اختار المنتج المناسب 👇", reply_markup=kb)


# ================= START =================
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user = get_user(chat_id)

    user["state"] = "WELCOME"
    user["history"].clear()
    save_user(chat_id, user)

    bot.send_message(
        chat_id,
        "أهلاً بيك 👋\n"
        "هساعدك تختار أنسب منتج ليك 💙\n\n"
        "اضغط ابدأ 👇",
        reply_markup=start_menu()
    )


# ================= HANDLER =================
@bot.message_handler(func=lambda m: True)
def handle(message):
    chat_id = message.chat.id
    text = message.text
    user = get_user(chat_id)

    if text == "🔙 رجوع":
        go_back(chat_id, user)
        return

    if user["state"] == "WELCOME":
        if text == "▶️ ابدأ":
            set_state(chat_id, user, "MAIN")
            bot.send_message(chat_id, "اختار القسم 👇", reply_markup=main_menu())
        return

    if user["state"] == "MAIN":
        categories = {
            "🧖‍♀️ الوجه": "face",
            "💆‍♀️ الشعر": "hair",
            "🧴 الجسم": "body",
            "👁 العين": "eyes",
            "💋 الشفايف": "lips",
            "🪥 العناية الشخصية": "personal"
        }

        if text in categories:
            user["category"] = categories[text]
            user["answers"].clear()
            save_user(chat_id, user)
            set_state(chat_id, user, "QUESTIONS")
            ask_questions(chat_id, user)
        return

    if user["state"] == "QUESTIONS":
        user["answers"]["need"] = text
        save_user(chat_id, user)
        set_state(chat_id, user, "PRODUCT")
        product_menu(chat_id, user["category"])
        return

    if user["state"] == "PRODUCT":
        if text in PRODUCTS[user["category"]]:
            user["product"] = text
            save_user(chat_id, user)
            set_state(chat_id, user, "DONE")

            bot.send_message(
                chat_id,
                f"✅ الترشيح المناسب ليك:\n\n"
                f"📂 {CATEGORY_NAMES[user['category']]}\n"
                f"❓ احتياجك: {user['answers']['need']}\n"
                f"🧴 المنتج: {text}",
                reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("🔙 رجوع")
            )
        return

    if user["state"] == "DONE":
        bot.send_message(chat_id, "تقدر ترجع خطوة وتغيّر اختيارك 🔙")


# ================= RUN =================
bot.infinity_polling(skip_pending=True)