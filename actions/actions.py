# --- DÁN ĐOẠN MÃ NÀY VÀO ĐẦU TIÊN ---
# Đoạn mã này vá lỗi "Event loop is closed" trên Windows
import platform
import asyncio

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# -----------------------------------

# (Các dòng import gốc của bạn bắt đầu từ đây)
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import os
import random


class ActionGiaiThichTu(Action):
    def name(self):
        return "action_giai_thich_tu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        word = next(tracker.get_latest_entity_values("word"), None)
        if not word:
            dispatcher.utter_message(text="🤔 Bạn muốn hỏi nghĩa của từ nào vậy nè?")
            return []

        # Đường dẫn đến file dictionary.json
        path = os.path.join(os.path.dirname(__file__), "dictionary.json")
        print(f"Action triggered for word: {word}")


        try:
            with open(path, "r", encoding="utf-8") as f:
                dictionary = json.load(f)
        except Exception as e:
            dispatcher.utter_message(text=f"⚠️ Có lỗi khi đọc dữ liệu: {e}")
            return []

        info = dictionary.get(word.lower())

        if info:
            vi = info.get("vi", "Chưa có nghĩa tiếng Việt.")
            exp = info.get("exp", "")

            # 🎨 10 mẫu phản hồi sinh động và tự nhiên hơn
            replies = [
                f"📘 *{word}* có nghĩa là *{vi}* đó nha. {exp} 😄",
                f"💡 Nếu dịch *{word}* sang tiếng Việt thì là *{vi}* á. {exp} 🌼",
                f"✨ *{word}* mang ý nghĩa *{vi}* trong tiếng Việt nha! {exp} 🌸",
                f"🧠 Theo từ điển, *{word}* = *{vi}*. {exp} 👍",
                f"🎯 Nghĩa của *{word}* là *{vi}*. {exp} 🚀",
                f"💬 Khi người ta nói *{word}*, ý là *{vi}* đó bạn! {exp} 😍",
                f"📖 *{word}* dịch ra tiếng Việt là *{vi}* nha~ {exp} 💖",
                f"🌿 *{word}* có thể hiểu là *{vi}*. {exp} 🌼",
                f"😎 Dễ lắm, *{word}* chỉ đơn giản là *{vi}* thôi. {exp}",
                f"🪄 *{word}* mang nghĩa *{vi}* nha! {exp} ✨"
            ]

            dispatcher.utter_message(text=random.choice(replies))

        else:
            # Khi không có dữ liệu
            no_data_replies = [
                f"😅 Oops, mình chưa có thông tin về *{word}* luôn á.",
                f"🤔 Mình chưa biết nghĩa của *{word}* bạn ơi.",
                f"🙈 Hình như *{word}* chưa có trong từ điển của mình.",
                f"🧐 Mình không tìm thấy *{word}* trong dữ liệu.",
                f"📭 *{word}* vẫn đang được cập nhật, chờ chút nha!",
                f"🔍 Từ *{word}* chưa nằm trong danh sách, nhưng mình sẽ nhớ nó! 😉",
                f"😇 Mình chưa học tới *{word}* đâu, bạn chỉ mình thêm được không?",
                f"🤓 Từ *{word}* nghe hay đó, tiếc là mình chưa có nghĩa của nó 😅",
                f"📚 *{word}* chưa có trong bộ dữ liệu, nhưng mình sẽ ghi chú lại nhé! 📝",
                f"👀 Chưa thấy *{word}* trong dữ liệu, để mình tìm hiểu thêm nha~"
            ]

            dispatcher.utter_message(text=random.choice(no_data_replies))

        return []