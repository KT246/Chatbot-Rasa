# 🤖 Chatbot Rasa + Flask API (Python 3.10)

Dự án này sử dụng **Rasa 3.6**, chạy trong môi trường ảo **Python 3.10**, tích hợp **API Flask** để kết nối với website và phục vụ mục tiêu chính:

---

# 🎯 Mục tiêu dự án

Xây dựng **chatbot tra cứu từ vựng tiếng Anh**, giúp người dùng:

- Hỏi một từ tiếng Anh → Trả về **nghĩa tiếng Việt**
- Giải thích **nghĩa chi tiết** của từ
- Tra cứu nhanh qua API hoặc giao diện web
- Xử lý câu hỏi tự nhiên bằng Rasa NLU

Ví dụ:

```
User: "beautiful nghĩa là gì?"
Bot: "beautiful nghĩa là đẹp."
```

🎯 Đây là dự án rất phù hợp để đưa vào **CV AI / NLP**, hoặc phục vụ **thực tập**.

---

# 🚀 Hướng dẫn cài đặt & chạy dự án

## ✅ 0. Tạo môi trường ảo bằng Python 3.10

```bash
py -3.10 -m venv rasa_enve
```

---

## ✅ 1. Kích hoạt môi trường ảo

```bash
rasa_enve\Scripts\activate
```

---

## ✅ 2. Cài thư viện

```bash
pip install -r requirements.txt
```

---

## ✅ 3. Train mô hình Rasa

```bash
rasa train
```

---

## ✅ 4. Chạy Action Server (CMD-0)

```bash
rasa run actions
```

---

## ✅ 5. Chạy chatbot để trò chuyện (CMD-1)

```bash
rasa shell
```

---

## ✅ 6. Chạy server API (CMD-2)

```bash
python server.py
```

API nhận nội dung từ client → chuyển vào Rasa → trả về JSON để hiển thị trên website.

---

# ✔️ Hoàn tất

Dự án bao gồm:

- 🎛 **Rasa NLU**: nhận diện ý định & trích xuất dữ liệu  
- 🧠 **Action Server**: xử lý logic tra cứu từ vựng  
- 🌐 **Flask API**: giao tiếp giữa web & chatbot  
- 🖥 **UI Web (index.html)**: giao diện chat đơn giản  

Nếu bạn muốn mình viết thêm:

✨ UI đẹp hơn (React/HTML/CSS)  
✨ Deploy lên Railway  
✨ Thêm API nâng cao  

Cứ nói **"viết thêm cho tôi"** nhé!
