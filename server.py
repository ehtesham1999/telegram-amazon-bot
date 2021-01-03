from bot import telegram_chatbot
import products
import time

bot = telegram_chatbot("config.cfg")


def make_reply(msg,from_):

        if msg is not None:
            bot.send_message('Results for '+msg, from_)
            prods = products.main(msg)
            count = 0
            for item in prods:
                count += 1
                time.sleep(2)
                if count > 5:
                    break
                reply = ''
                reply = str(item[0]) + '\n' + str(item[1]) + '  ' + item[4]
                time.sleep(2)
                bot.send_message(reply, from_)
                print(reply)
                print()




update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            first_term = message.split(' ')[0]
            search_term = ' '.join(message.split(' ')[1:])
            if first_term == '/find':
                bot.send_message('Finding', from_)
                make_reply(search_term,from_)
