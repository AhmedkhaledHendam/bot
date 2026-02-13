
import telebot
from telebot import types
import os

# ================= TOKEN =================
TOKEN = os.getenv("8573382461:AAHsJj-p4DxzZlfaISP3aMTRRrGkOykwUgM")
bot = telebot.TeleBot(TOKEN)

 
#
user_data = {}
 
 #hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
product_map_skin = {
    "بهتان": {
        "حساسة": {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
            },
        "دهنية":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "مختلطة":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "جافة":   
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
       } }
      ,
    "حبوب": {
        "حساسة": {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }},
            
        "دهنية":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "مختلطة":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "جافة":   
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
       } }
      ,
    "تصبغات": {
        "حساسة": {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
            },
        "دهنية":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "مختلطة":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "جافة":   
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
        }
     },
    "جفاف": {
        "حساسة": {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
            },
        "دهنية":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "مختلطة":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
        "جافة":   
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
    }   } },
      
    "دهون زيادة": {
        "حساسة": {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
            
        "دهنية":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
             },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "مختلطة":  
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } },
        "جافة":   
            {
            "غسولات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "تونر": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مقشرات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرمات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "مرطبات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسكات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
               "مزيل ميكاب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم نهار وليل" : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
           } }
     }}
      
       
  
 ########################################################

product_map_hair = {
    "تساقط": {
       
            "شامبو": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "بلسم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
            }
            
       
        ,
      
    "هيشان": {
       
            "شامبو": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "بلسم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
            }
        
           
        ,
      
    "قشرة" : {
        "شامبو": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "بلسم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
            },
        
     
    "جفاف": {
        "شامبو": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "بلسم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سيرم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "كريم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
            },
        
     
    "تقصف": {
        "شامبو": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "بلسم": {     
                "name": "Glow Gentle Cleanser",  
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"  },
             "سيرم": {
               "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",     
                "price": "250 جنيه"  },
             "كريم": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
            }
            }

 #####################################################################       
 

product_map_lip = {
    "تشققات": {
       
                  "مرطب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سكراب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
            }
            
       
        ,
      
    "جفاف": {
       
                    "مرطب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سكراب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
            }
        
           
        ,
      
    "اسمرار" : {
        "مرطب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
            "ماسك": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
             "سكراب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }
            }
            }
           
product_map_personal = {
    
       
      
        "بادي اسبلاش"  : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
      ,
        "مزيل عرق": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }   
            }
              
product_map_eye = {
    
       
       "كريم هالات": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
        "باتش للعين"  : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
      ,
        "سيروم تحت العين": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }   
            }
                           
product_map_body = {
     "يدين وقدمين": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
       
       "لوشن": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            },
        "سكراب"  : {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } 
      ,
        "كريم تفتيح": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            } ,
        "كريم ترطيب": {
                "name": "Glow Gentle Cleanser",
                "desc": "ينضف بلطف ويدي إشراقة للبشرة الحساسة",
                "price": "250 جنيه"
            }  
            }   
###########################################

def welcome ():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("start ❤️")
    return kb

def back_only():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("رجوع")
    return kb
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,  "  اهلا بك في shiny store 💖 \n\nهسالك كام سؤال عشان اختارلك المنتج المناسب ✨", reply_markup=welcome())
@bot.message_handler(func=lambda m: m.text == "start ❤️")
def section_one_step1(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🧖‍♀️ الوجه", "💆‍♀️ الشعر")
    kb.add("🧴 الجسم", "👁 العين")
    kb.add("💋 الشفايف", "🪥 العناية الشخصية")
    kb.add("رجوع")
    bot.send_message(message.chat.id,"اختار القسم المطلوب ☺️" , reply_markup=kb)
    
#############################################################################

@bot.message_handler(func=lambda m: m.text == "🧖‍♀️ الوجه")
def choose_problem_skin(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id] = {}
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("حبوب","تصبغات")
    kb.add("جفاف","دهون زيادة")
    kb.add("بهتان")
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المشكلة 😌", reply_markup=kb)
    bot.register_next_step_handler(message, choose_skin)

def choose_skin(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["problem_skin"] = message.text
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("دهنية", "جافة")
    kb.add("مختلطة", "حساسة")
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع بشرتك 💆‍♀️", reply_markup=kb)
    bot.register_next_step_handler(message, choose_product_skin)

def choose_product_skin(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["skin"] = message.text
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("غسولات","تونر")
    kb.add("مقشرات","سيرمات")
    kb.add("مرطبات","ماسكات" )
    kb.add("كريم نهار وليل")
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المنتج 🧴", reply_markup=kb)
    bot.register_next_step_handler(message, skin_result)

def skin_result(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
  
    user_data[message.chat.id]["product_skin"] = message.text
    problem = user_data[message.chat.id]["problem_skin"]
    skin = user_data[message.chat.id]["skin"]
    product_type = user_data[message.chat.id]["product_skin"]
    try:
        product = product_map_skin[problem][skin][product_type]
        bot.send_message(
            message.chat.id,
            "✅ الترشيح المناسب ليكي:\n\n"
            "✨ " + product["name"] + "\n"
            "📝 " + product["desc"] + "\n"
            "💰 السعر: " + product["price"]+ "\n"
            "اطلب الان:" "https://cml47050e0rvd01lh238b165q.wuiltstore.com/ar",
            reply_markup=back_only()
            )
    except KeyError:
        bot.send_message(message.chat.id, "الاختيار ده مش متوفر 🤍")

##############################################################################

@bot.message_handler(func=lambda m: m.text == "💆‍♀️ الشعر")
def choose_problem_hair(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id] = {}
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("تساقط","هيشان")
    kb.add("قشرة","تقصف")
    kb.add("جفاف")
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المشكلة 😌", reply_markup=kb)
    bot.register_next_step_handler(message,choose_product_hair )

def choose_product_hair (message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["problem_hair"] = message.text
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("بلسم","شامبو")
    kb.add("كريم" ,"سيرم")
    kb.add("ماسك")
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المنتج 🧴", reply_markup=kb)
    bot.register_next_step_handler(message, hair_result)


def hair_result(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["product_hair"] = message.text
    problem = user_data[message.chat.id]["problem_hair"]
    product_type = user_data[message.chat.id]["product_hair"]
    try:
        product = product_map_hair[problem][product_type]
        bot.send_message(
            message.chat.id,
            "✅ الترشيح المناسب ليكي:\n\n"
            "✨ " + product["name"] + "\n"
            "📝 " + product["desc"] + "\n"
            "💰 السعر: " + product["price"]+ "\n"
            "اطلب الان:" "https://cml47050e0rvd01lh238b165q.wuiltstore.com/ar",
            reply_markup=back_only()
        )

    except KeyError:
        bot.send_message(message.chat.id, "الاختيار ده مش متوفر 🤍")

###############################################################

@bot.message_handler(func=lambda m: m.text == "💋 الشفايف")
def choose_problem_lip(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id] = {}
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("جفاف",  "تشققات")
    kb.add( "اسمرار")
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المشكلة 😌", reply_markup=kb)
    bot.register_next_step_handler(message,choose_product_lip )

def choose_product_lip (message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["problem_lip"] = message.text
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("ماسك","مرطب")
    kb.add("سكراب" )
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المنتج 🧴", reply_markup=kb)
    bot.register_next_step_handler(message, lip_result)


def lip_result(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["product_lip"] = message.text
    problem = user_data[message.chat.id]["problem_lip"]
    product_type = user_data[message.chat.id]["product_lip"]
    try:
        product = product_map_lip[problem][product_type]
        bot.send_message(
            message.chat.id,
            "✅ الترشيح المناسب ليكي:\n\n"
            "✨ " + product["name"] + "\n"
            "📝 " + product["desc"] + "\n"
            "💰 السعر: " + product["price"]+ "\n"
            "اطلب الان:" "https://cml47050e0rvd01lh238b165q.wuiltstore.com/ar",
            reply_markup=back_only()
        )

    except KeyError:
        bot.send_message(message.chat.id, "الاختيار ده مش متوفر 🤍")


#########################################################################

@bot.message_handler(func=lambda m: m.text == "🪥 العناية الشخصية")
def choose_product_personal (message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]= {}
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("بادي اسبلاش"  ,"مزيل عرق" )
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المنتج 🧴", reply_markup=kb)
    bot.register_next_step_handler(message, personal_result)


def personal_result(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["product_personal"] = message.text
    product_type = user_data[message.chat.id]["product_personal"]
    try:
        product = product_map_personal[product_type]
        bot.send_message(
            message.chat.id,
            "✅ الترشيح المناسب ليكي:\n\n"
            "✨ " + product["name"] + "\n"
            "📝 " + product["desc"] + "\n"
            "💰 السعر: " + product["price"]+ "\n"
            "اطلب الان:" "https://cml47050e0rvd01lh238b165q.wuiltstore.com/ar",
            reply_markup=back_only()
        )

    except KeyError:
        bot.send_message(message.chat.id, "الاختيار ده مش متوفر 🤍")

##############################################################

@bot.message_handler(func=lambda m: m.text == "👁 العين")
def choose_product_eye (message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]= {}
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add( "كريم هالات", "باتش للعين" )
    kb.add(  "سيروم تحت العين" )
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المنتج 🧴", reply_markup=kb)
    bot.register_next_step_handler(message, eye_result)


def eye_result(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["product_eye"] = message.text
    product_type = user_data[message.chat.id]["product_eye"]
    try:
        product = product_map_eye[product_type]
        bot.send_message(
            message.chat.id,
            "✅ الترشيح المناسب ليكي:\n\n"
            "✨ " + product["name"] + "\n"
            "📝 " + product["desc"] + "\n"
            "💰 السعر: " + product["price"]+ "\n"
            "اطلب الان:" "https://cml47050e0rvd01lh238b165q.wuiltstore.com/ar",
            reply_markup=back_only()
        )

    except KeyError:
        bot.send_message(message.chat.id, "الاختيار ده مش متوفر 🤍")

###########################################################################


@bot.message_handler(func=lambda m: m.text == "🧴 الجسم")
def choose_product_body(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id] = {}
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(  "لوشن", "يدين وقدمين" )
    kb.add(  "كريم ترطيب",   "كريم تفتيح")
    kb.add("سكراب" )
    kb.add("رجوع")
    bot.send_message(message.chat.id, "اختاري نوع المنتج 🧴", reply_markup=kb)
    bot.register_next_step_handler(message, body_result)


def body_result(message):
    if message.text == "رجوع":
        bot.send_message(message.chat.id, "رجعنا للبداية ✨", reply_markup=welcome())
        return
    user_data[message.chat.id]["product_body"] = message.text
    product_type = user_data[message.chat.id]["product_body"]
    try:
        product = product_map_body[product_type]
        bot.send_message(
            message.chat.id,
            "✅ الترشيح المناسب ليكي:\n\n"
            "✨ " + product["name"] + "\n"
            "📝 " + product["desc"] + "\n"
            "💰 السعر: " + product["price"]+ "\n"
            "اطلب الان:" "https://cml47050e0rvd01lh238b165q.wuiltstore.com/ar",
            reply_markup=back_only()
        )

    except KeyError:
        bot.send_message(message.chat.id, "الاختيار ده مش متوفر 🤍")





#####################################################
@bot.message_handler(func=lambda m: m.text == "رجوع")
def go_home(message):
    bot.send_message(
        message.chat.id,
        "رجعنا للبداية ✨",
        reply_markup=welcome()
    )
bot.infinity_polling(timeout=30, long_polling_timeout=20, skip_pending=True)
