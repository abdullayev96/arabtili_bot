from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


Api_Key="5844741219:AAE_aG8mUqRSHfSG-YOS2saRIAhISMC_3Nk"   #### Api address

# ma_buttons=ReplyKeyboardMarkup([
#         [KeyboardButton(text="🔤 Tajvid darslari "), KeyboardButton(text="🕋 Arab tili harflari")],
#         [KeyboardButton(text="👳 Madina  kitobi ", callback_data="ib2"), KeyboardButton(text="🗣 Arab tili nahv")],
#         [KeyboardButton(text="🤲Duolar", ), KeyboardButton(text="📞 Biz bilan bog'lanish", callback_data="ibn4")],
#     ])

main_buttons=[
        [InlineKeyboardButton(text="🔤 Tajvid darslari ", callback_data="ib1"), InlineKeyboardButton(text="🕋 Arab tili harflari", callback_data="ibn5")],
        [InlineKeyboardButton(text="👳 Madina  kitobi ", callback_data="ib2"), InlineKeyboardButton(text="🗣 Arab tili nahv", callback_data="ibn6")],
        [InlineKeyboardButton(text="🤲Duolar", callback_data="ib3"), InlineKeyboardButton(text="📞 Biz bilan bog'lanish", callback_data="ibn4")],
    ]
ortbutton = [
           [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ar_back"),InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]
tabutton = [
           [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ta_back"),InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]
mabutton = [
           [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ma_back"),InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]
taj_menu = [
            [InlineKeyboardButton(text="1-2 dars", callback_data="ta1"), InlineKeyboardButton(text="3-4 dars", callback_data="ta2")],
            [InlineKeyboardButton(text="5-6 dars", callback_data="ta3"), InlineKeyboardButton(text="7-8 dars", callback_data="ta4")],
            [InlineKeyboardButton(text="9-10 dars", callback_data="ta5"), InlineKeyboardButton(text="11-12 dars", callback_data="ta6")],
            [InlineKeyboardButton(text="13-14 dars", callback_data="ta7"),InlineKeyboardButton(text="15 dars", callback_data="ta8")],
            [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ib3.6"), InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]


def start_command(update, context):
    user=update.message.from_user
    # user1=update.message.from_user.id
    # update.message.reply_html('Szning chat_id raqamingz <b> {} !!! </b>'
    #                           .format(user1))

    update.message.reply_html('😊😊 Botimzga Hush kelibsz bu bot orqali ilmizni oshirishingz mumkin!!! \n <b> {} !!! </b>'
                              .format(user.first_name),reply_markup=InlineKeyboardMarkup(main_buttons)
    )

def inline_messages(update, context):
    query=update.callback_query
    if query.data == "ib1":
        buttons = [
            [InlineKeyboardButton(text="1-2 dars", callback_data="ta1"), InlineKeyboardButton(text="3-4 dars", callback_data="ta2")],
            [InlineKeyboardButton(text="5-6 dars", callback_data="ta3"), InlineKeyboardButton(text="7-8 dars", callback_data="ta4")],
            [InlineKeyboardButton(text="9-10 dars", callback_data="ta5"), InlineKeyboardButton(text="11-12 dars", callback_data="ta6")],
            [InlineKeyboardButton(text="13-14 dars", callback_data="ta7"),InlineKeyboardButton(text="15 dars", callback_data="ta8")],
            [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ib3.6"), InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]
        query.message.reply_text("Choose please", reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))

    elif query.data == "ta_back":
        query.message.reply_text("go_back", reply_markup=InlineKeyboardMarkup(taj_menu))

    elif query.data == "ta1":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>1-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/IRNm8zCI0kY",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>2-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/bLobgqBzH3Q",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton)
                                  )

    elif query.data == "ta2":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>3-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/IRNm8zCI0kY",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>4-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/V0xUtx7ybuc",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton)
                                  )

    elif query.data == "ta3":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>5-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/xswBue3xzTc",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>6-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/D2Pmp1gIM20",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton)
                                  )

    elif query.data == "ta4":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>7-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/AxHcWA6llyI",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>8-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/pGeoHYOu2P0",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton)
                                  )
    elif query.data == "ta5":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>9-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/XxAusFiHXFs",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>10-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/3qa5k0XlDjU",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton))

    elif query.data == "ta6":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>11-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/Ds9xrLdk9A0",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>12-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/6u58pBdAlfI",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton)
                                  )

    elif query.data == "ta7":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>13-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/nvmflnNuEvE",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>14-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/mSju92uusVA",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton)
                                  )

    elif query.data == "ta8":
        query.message.reply_text(text="👤 <b>Ustoz  </>: Musa Saidov  <b>13-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/W1VdfGNDTJY",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=tabutton)
                                  )

    elif query.data == "ib2":
        buttons = [
            [InlineKeyboardButton(text="1-2 dars", callback_data="ma1"),InlineKeyboardButton(text="3-4 dars", callback_data="ma2")],
            [InlineKeyboardButton(text="5-6 dars", callback_data="ma3"),InlineKeyboardButton(text="7-8 dars", callback_data="ar4")],
            [InlineKeyboardButton(text="9-10 dars", callback_data="ma5"),InlineKeyboardButton(text="11-12 dars", callback_data="ma6")],
            [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ib3.6"),InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]

        query.message.reply_text("choose", reply_markup=InlineKeyboardMarkup(buttons))
    elif query.data == "ma1":
        query.message.reply_text(text="👤 <b>Ustoz </>: Musa Saidov  <b>1-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/lJ-wpDsAzqA",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <code>Ustoz </>: Musa Saidov <b>2-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/XAeOVpOZTaY",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=mabutton)
                                  )


    elif query.data == "ma2":
        query.message.reply_text(text="👤 <code>Ustoz </>: Musa Saidov  <b>3-dars </> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/u5v0t7bhcqE",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=mabutton)
                                  )

    elif query.data == "ibn4":
        query.message.reply_text(text="☎ <i>Teacher Tel</>:<b> +998 99 749 10 11 </> \n "
                                      "📝 <code>Teacher </>: @ArabtiliMusa \n "
                                      " 📚 <i>Telegram kanal </>: https://t.me/musa1110",
                                 parse_mode="HTML")
        query.message.reply_text(text="👤 <code> Muso Saidov </> \n "
                                          " <code> Youtobe kanal </> : https://youtube.com/playlist?list=PLqdU8LXTFyA57vxx2KdzhmZqm6BlX-Y8-",
                                  parse_mode="HTML"
                                  )

    elif query.data == "ar_back":
        buttons = [
            [InlineKeyboardButton(text="1-2 dars", callback_data="ar1"),InlineKeyboardButton(text="3-4 dars", callback_data="ar2")],
            [InlineKeyboardButton(text="5-6 dars", callback_data="ar3"),InlineKeyboardButton(text="7-8 dars", callback_data="ar4")],
            [InlineKeyboardButton(text="9-10 dars", callback_data="ar5"),InlineKeyboardButton(text="11-12 dars", callback_data="ar6")],
            [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ib3.6"),InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    elif query.data == "ib3":
        query.message.reply_text(text=" 🤲 Duolar va Zikrlar \n "
                                      "https://youtube.com/playlist?list=PLqdU8LXTFyA4ypT1PYHIdhizkKK8ROEAD")

    elif query.data == "ibn5":
        buttons = [
            [InlineKeyboardButton(text="1-2 dars", callback_data="ar1"), InlineKeyboardButton(text="3-4 dars", callback_data="ar2")],
            [InlineKeyboardButton(text="5-6 dars", callback_data="ar3"), InlineKeyboardButton(text="7-8 dars", callback_data="ar4")],
            [InlineKeyboardButton(text="9-10 dars", callback_data="ar5"), InlineKeyboardButton(text="11-12 dars", callback_data="ar6")],
            [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ib3.6"), InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib3.6")],

        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == "ar1":
        query.message.reply_text(text="👤 <b>Ustoz </>: Musa Saidov  <b>1-dars</> \n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/fUkOuF_anxM \n ",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz </>: Musa Saidov <b> 2-dars </>\n "
                                          "<i> Telegram kanal </>: https://t.me/musa1110 \n "
                                          "https://youtu.be/lUIo4u0e0pM",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=ortbutton)
                                  )

    elif query.data == "ar2":
        query.message.reply_text(text="👤 <b>Ustoz </>: Musa Saidov <b> 3-dars </>\n "
                        
                                          "https://youtu.be/6eEOYorEGKY",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz </>: Musa Saidov <b> 4-dars </>\n "
                        
                                          "https://youtu.be/XbeFgPyX_d8",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=ortbutton)
                                  )
    elif query.data == "ar3":
        query.message.reply_text(text="👤 <b>Ustoz </>: Musa Saidov <b> 5-dars </>\n\n "
                                          "https://youtu.be/6eEOYorEGKY",
                                  parse_mode="HTMl"
                                  )
        query.message.reply_text(text="👤 <b>Ustoz </>: Musa Saidov <b> 6-dars </>\n "
                                          "https://youtu.be/XbeFgPyX_d8"
                                      "<i> Telegram kanal </>: https://t.me/musa1110 \n ",
                                  parse_mode="HTMl",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=ortbutton)
                                  )


    elif query.data =="ib3.6":
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(main_buttons))


def main():
    updater = Updater(Api_Key, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CallbackQueryHandler(inline_messages))


    updater.start_polling()
    updater.idle()

if __name__== '__main__':
    main()



