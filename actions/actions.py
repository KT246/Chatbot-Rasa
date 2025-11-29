# --- VÁ LỖI WINDOWS ---
import platform
import asyncio
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# ----------------------

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import os
import random

GLOBAL_DICTIONARY = {}

def init_dictionary():
    global GLOBAL_DICTIONARY
    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "dictionary.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                GLOBAL_DICTIONARY = json.load(f)
            print(f"✅ [INIT] Đã nạp {len(GLOBAL_DICTIONARY)} từ vào RAM.")
        else:
            print(f"⚠️ Không tìm thấy file dictionary.json")
            GLOBAL_DICTIONARY = {}
    except Exception as e:
        print(f"❌ Lỗi nạp từ điển: {e}")
        GLOBAL_DICTIONARY = {}

init_dictionary()

# ======================================================
# 1️⃣ ACTION TRẢ NGHĨA ĐƠN GIẢN (Ngắn gọn, đa dạng)
# ======================================================
class ActionTraNghiaDonGian(Action):
    def name(self) -> Text:
        return "action_tra_nghia_don_gian"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = next(tracker.get_latest_entity_values("word"), None)
        
        # Mẫu câu hỏi lại khi không bắt được từ
        if not word:
            prompts = [
                "Bạn muốn tra từ nào nhỉ? 🤔",
                "Mình chưa nghe rõ, bạn muốn hỏi từ gì?",
                "Nhập từ bạn cần tra nghĩa đi nào! 👇"
            ]
            dispatcher.utter_message(text=random.choice(prompts))
            return []
        
        info = GLOBAL_DICTIONARY.get(word.lower())
        
        if info:
            vi = info.get("vi", "Chưa có định nghĩa.")
            
            # 🎨 10 MẪU TRẢ LỜI NGẮN GỌN ĐA DẠNG
            templates = [
                f"✅ **{word}** có nghĩa là: {vi}",
                f"📖 Theo từ điển thì **{word}** = {vi}",
                f"🔍 Kết quả nè: **{word}** là {vi}",
                f"💡 **{word}** dịch sang tiếng Việt là {vi} nha!",
                f"🤓 Từ **{word}** mang nghĩa là {vi}",
                f"📝 Ghi nhớ nhé: **{word}** -> {vi}",
                f"✨ **{word}** có nghĩa đơn giản là {vi}",
                f"🎯 Nghĩa của **{word}** là: {vi}",
                f"💬 Người ta thường dùng **{word}** với nghĩa là {vi}",
                f"👉 **{word}** là {vi} đó bạn!"
            ]
            dispatcher.utter_message(text=random.choice(templates))
        else:
            not_found = [
                f"😅 Xin lỗi nha, mình chưa tìm thấy từ '{word}'.",
                f"🤔 Hmmm, từ '{word}' này lạ quá, mình chưa cập nhật kịp.",
                f"📚 Từ điển của mình chưa có từ '{word}', bạn thử từ khác nhé?",
                f"🙈 Rất tiếc, dữ liệu về '{word}' đang bị thiếu.",
                f"🔍 Mình tìm đỏ mắt mà không thấy từ '{word}' đâu cả!"
            ]
            dispatcher.utter_message(text=random.choice(not_found))
            
        return []

# ======================================================
# 2️⃣ ACTION TRẢ NGHĨA CHI TIẾT (Giải thích + Ví dụ)
# ======================================================
class ActionTraNghiaChiTiet(Action):
    def name(self) -> Text:
        return "action_tra_nghia_chi_tiet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = next(tracker.get_latest_entity_values("word"), None)
        
        if not word:
            dispatcher.utter_message(text="Bạn muốn hỏi chi tiết từ nào? 👇")
            return []

        info = GLOBAL_DICTIONARY.get(word.lower())
        
        if info:
            vi = info.get("vi", "...")
            exp = info.get("exp", "Chưa có ví dụ cụ thể.")
            
            # 🎨 10 MẪU TRẢ LỜI CHI TIẾT SINH ĐỘNG
            templates = [
                f"📘 **{word}**: {vi}\n👉 *Ví dụ:* {exp}",
                f"✨ **{word}** nghĩa là **{vi}**.\n📝 *Ngữ cảnh:* {exp}",
                f"💡 Giải thích: **{word}** là **{vi}**.\n🧠 {exp}",
                f"🧐 Chi tiết về **{word}**:\n- Nghĩa: {vi}\n- Ví dụ: {exp}",
                f"📚 Theo từ điển: **{word}** = **{vi}**.\n🗣️ *Câu mẫu:* {exp}",
                f"🌸 **{word}** (nghĩa: {vi}).\n💬 *Cách dùng:* {exp}",
                f"🎓 Học từ mới nè: **{word}** là **{vi}**.\n✍️ *Example:* {exp}",
                f"🔎 Mình tìm thấy rồi! **{word}** là **{vi}**.\n📌 *Lưu ý:* {exp}",
                f"📖 **{word}** dịch là **{vi}**.\n🗣️ *Ví dụ thực tế:* {exp}",
                f"🚀 **{word}** -> **{vi}**.\n🌟 *Mở rộng:* {exp}"
            ]
            dispatcher.utter_message(text=random.choice(templates))
        else:
            not_found_templates = [
                f"😅 Tiếc quá, mình chưa có thông tin chi tiết về '{word}'.",
                f"📚 Từ '{word}' này mới quá, để mình cập nhật sau nhé!",
                f"🔍 Mình tìm đỏ mắt mà chưa thấy giải thích cho '{word}'. Sorry nha!",
                f"🤔 Hmm, '{word}' lạ quá, mình chưa biết nghĩa.",
                f"🙈 Dữ liệu về '{word}' đang bị thiếu, bạn thử từ khác xem?"
            ]
            dispatcher.utter_message(text=random.choice(not_found_templates))
            
        return []
    





