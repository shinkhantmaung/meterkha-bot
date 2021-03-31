from telegram import *
from telegram.ext import *
import wikipedia

bot = Bot("1767761618:AAGXnLlnrcrJ6N5bg6emGbtaNKduOFRIlNE")

print(bot.get_me()) 

updater = Updater("1767761618:AAGXnLlnrcrJ6N5bg6emGbtaNKduOFRIlNE",use_context=True)

dispatcher : Dispatcher =  updater.dispatcher

keyword = ""
chat_id = ""

def start(update,context):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    # Welcome message
    msg = ("ဟယ်လို!\n")
    msg += ("ကျွန်တော်က {0} ဖြစ်ပြီး လူကြီးမင်း၏ မီတာခ စုစုပေါင်းကျသင့်ငွေကို တွက်ချက်ပေးမည့် chatbot လေးတစ်ခုဖြစ်ပါတယ်ဗျ\n\n").format(me.first_name)
    msg += ("ကျွန်တော်မှ မီတာခ တွက်ချက်ပေးရန်အတွက် လူကြီးမင်း၏ သုံးစွဲမီတာ ယူနစ်အား ရိုက်ထည့်ပေးပါခင်ဗျ။ \n\n")

    # Commands menu
    main_menu_keyboard = [[KeyboardButton('/Get_Started')],
                            [KeyboardButton('/Meter_Calculator')]]
    reply_kb_markup = ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup) 

def ask(update,context):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text = "လူကြီးမင်း၏ သုံးစွဲမီတာယူနစ်အား ရိုက်ထည့်ပေးပါ။",
        parse_mode =  ParseMode.HTML
    )

def showkeyboard(update,context):
    global keyword , chat_id

    keyword =update.message.text
    chat_id = update.message.chat_id

    keyboard = [[
        InlineKeyboardButton('အိမ်သုံးမီတာ အမျိုးအစား',callback_data="1")],
        [InlineKeyboardButton('လုပ်ငန်းသုံးမီတာ အမျိုးအစား',callback_data="2")
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("လူကြီးမင်း တွက်ချက်လိုသော မီတာအမျိုးအစားအား ရွေးချယ်ပေးပါ။ ",reply_markup=reply_markup)

def buttonclick(update,context):
    global keyword , chat_id

    query : CallbackContext = update.callback_query
    data_type = type(keyword)
    if query.data == "1":
        amount = 0 
        total = 0
        units = int(keyword)
        surcharge = 500   

        if(units < 30):
            amount = units * 35 
            content = [amount] 
        elif(units <= 50):
            amount = ((units - 30) * 50)+ 1050
            content = [1050,amount]
        elif(units <= 75):
            amount = ((units - 50) * 70)+ 2050
            content = [1050,1000,amount] 
        elif(units <= 100):
            amount = ((units - 75) * 90)+ 3800
            content = [1050,1000,1750,amount] 
        elif(units <= 150):
            amount = ((units - 100) * 110)+ 6050
            content = [1050,1000,1750,2250,amount]
        elif(units <= 200):
            amount = ((units - 150) * 120)+ 11550
            content = [1050,1000,1750,2250,5500,amount]
        else:
            amount = ((units - 200) * 125)+ 17550
            content = [1050,1000,1750,2250,5500,6000,amount] 
        total = amount + surcharge

        #keyboard
        keyboard = [[
            InlineKeyboardButton('ဘောင်ချာအား ကြည့်မည်။',url = "http://shinkhantmaung.pythonanywhere.com/opt1/{}".format(units))
        ]]

        reply_markup = InlineKeyboardMarkup(keyboard)        

        bot.send_message(
            chat_id = update.effective_chat.id,
            text = "အိမ်သုံးမီတာအတွက် စုစုပေါင်းကျသင့်ငွေမှာ {} ကျပ်  ဖြစ်ပါတယ်ဗျ".format(total),
            parse_mode =  ParseMode.HTML,
            reply_markup=reply_markup
        )

    if query.data == "2":
        amount = 0 
        total = 0
        units = int(keyword)
        surcharge = 0   

        if(units < 500):
            amount = units * 125
            content = [amount] 
        elif(units <= 5000):
            amount = ((units - 500) * 135)+ 62500
            content = [62500,amount]
        elif(units <= 10000):
            amount = ((units - 5000) * 145)+ 607500
            content = [62500,607500,amount] 
        elif(units <= 100):
            amount = ((units - 10000) * 155)+ 725000
            content = [62500,607500,725000,amount] 
        elif(units <= 150):
            amount = ((units - 20000) * 165)+ 1550000
            content = [62500,607500,725000,1550000,amount]
        elif(units <= 200):
            amount = ((units - 50000) * 175)+ 4950000
            content = [62500,607500,725000,1550000,4950000,amount]
        else:
            amount = ((units - 200) * 180)+ 8750000
            content = [62500,607500,725000,1550000,4950000,8750000,amount] 
        total = amount + surcharge

        #keyboard
        keyboard = [[
            InlineKeyboardButton('ဘောင်ချာအား ကြည့်မည်။',url = "http://shinkhantmaung.pythonanywhere.com/opt2/{}".format(units))
        ]]

        reply_markup = InlineKeyboardMarkup(keyboard) 
        
        bot.send_message(
            chat_id = update.effective_chat.id,
            text = "လုပ်ငန်းသုံးမီတာအတွက် စုစုပေါင်းကျသင့်ငွေမှာ {} ကျပ်  ဖြစ်ပါတယ်ဗျ".format(total),
            parse_mode =  ParseMode.HTML ,
            reply_markup = reply_markup
        )



dispatcher.add_handler(CommandHandler("Get_Started", start))
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("Meter_Calculator", ask))

dispatcher.add_handler(MessageHandler(Filters.text,showkeyboard))
dispatcher.add_handler(CallbackQueryHandler(buttonclick))
updater.start_polling()