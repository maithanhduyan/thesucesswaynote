(Due to technical issues, the search service is temporarily unavailable.)

Dưới đây là bài giảng chi tiết cho **Bài 3: Thiết kế Agent cơ bản** trong Module 2:

---

### **Bài 3: Thiết kế Agent cơ bản**  
**Thời lượng:** 1-2 buổi  
**Mục tiêu học tập:**  
- Hiểu mô hình BDI (Beliefs, Desires, Intentions) trong thiết kế Agent.  
- Tạo Agent đơn giản bằng crewAI với đầy đủ thuộc tính.  
- Lập trình giao tiếp cơ bản giữa các Agent qua message passing.  

---

### **Nội dung bài giảng**  
#### **1. Giới thiệu (10 phút)**  
- **Ví dụ mở đầu:**  
  > "Một Agent giao hàng tự động cần:  
  > - **Tin tưởng (Belief):** Biết vị trí hiện tại và giao thông.  
  > - **Mong muốn (Desire):** Giao hàng đúng hạn.  
  > - **Ý định (Intention):** Chọn tuyến đường tối ưu."  
  → Giới thiệu về tầm quan trọng của BDI trong thiết kế Agent.  

---

#### **2. Thuộc tính của Agent: Mô hình BDI (40 phút)**  
**a. Beliefs (Niềm tin)**  
- **Định nghĩa:** Thông tin Agent "tin" là đúng về môi trường.  
- **Ví dụ:**  
  ```python
  weather_agent.beliefs = {
      "current_temperature": 25,
      "rain_probability": 30%
  }
  ```  

**b. Desires (Mong muốn)**  
- **Định nghĩa:** Mục tiêu dài hạn của Agent.  
- **Ví dụ:**  
  ```python
  delivery_agent.desires = ["Minimize delivery time", "Avoid toll roads"]
  ```  

**c. Intentions (Ý định)**  
- **Định nghĩa:** Kế hoạch hành động để đạt Desire.  
- **Ví dụ workflow:**  
  ```
  1. Nhận đơn hàng → 2. Tính toán route → 3. Di chuyển → 4. Cập nhật trạng thái
  ```  

**d. Triển khai BDI trong crewAI**  
```python
from crewai import Agent

# Tạo Agent phân tích thời tiết
weather_analyst = Agent(
    role="Weather Analyst",
    beliefs={"location": "Hanoi", "data_source": "API"},
    desires=["Predict rain accurately", "Update hourly"],
    intentions=[
        "Fetch data from API",
        "Run prediction model",
        "Send alert if rain > 50%"
    ]
)
```

---

#### **3. Tạo Agent đơn giản với crewAI (40 phút)**  
**a. Cấu trúc Agent cơ bản**  
```python
from crewai import Agent, Tool

# Định nghĩa công cụ (Tool)
search_tool = Tool(
    name="Google Search",
    func=lambda query: f"Kết quả tìm kiếm cho '{query}'"
)

# Tạo Agent
research_agent = Agent(
    role="Researcher",
    goal="Tìm thông tin về AI",
    tools=[search_tool],
    verbose=True
)
```  

**b. Agent lifecycle**  
1. Khởi tạo → 2. Nhận nhiệm vụ → 3. Đánh giá Beliefs → 4. Lập kế hoạch (Intentions) → 5. Hành động → 6. Cập nhật trạng thái  

**Demo trực tiếp:**  
- Tạo Agent đặt lịch họp tự động với:  
  - Beliefs: Lịch làm việc của team  
  - Desires: Tránh xung đột lịch  
  - Intentions: Gợi ý khung giờ trống  

---

#### **4. Giao tiếp giữa các Agent (40 phút)**  
**a. Message Passing**  
- **Cơ chế:** Agent gửi/thu nhận message qua ID duy nhất.  
- **Ví dụ:**  
  ```python
  # Agent A gửi message
  coordinator.send_message(
      to=analyst_agent.id,
      content={"type": "request", "data": "sales_report_2023"}
  )

  # Agent B nhận message
  messages = analyst_agent.get_messages()
  ```  

**b. Communication Protocols**  
- **FIPA-ACL:** Chuẩn ngôn ngữ giao tiếp Agent  
  ```json
  {
    "performative": "request",
    "sender": "agent1@platform",
    "receiver": "agent2@platform",
    "content": "need_weather_data"
  }
  ```  
- **Custom Protocol trong crewAI:**  
  ```python
  class WeatherProtocol(Protocol):
      def handle_request(self, message):
          if message['type'] == 'weather_update':
              return self.fetch_weather(message['location'])
  ```  

**c. Demo: Hệ thống hỏi đáp**  
- **Agent hỏi (QA_Agent):** Gửi câu hỏi về thời tiết  
- **Agent trả lời (Weather_Agent):** Phân tích và phản hồi  

---

### **Hoạt động trên lớp**  
1. **Thực hành coding (30 phút):**  
   - Tạo 2 Agent: 1 Agent thu thập dữ liệu, 1 Agent phân tích.  
   - Thiết lập giao tiếp để Agent phân tích yêu cầu dữ liệu mới nhất.  

2. **Thảo luận nhóm (20 phút):**  
   - **Tình huống:** Thiết kế Agent phục vụ nhà hàng với:  
     - Beliefs: Thực đơn, số bàn trống  
     - Desires: Tối đa doanh thu  
     - Intentions: Gợi ý món ăn theo nhóm khách  

---

### **Bài tập về nhà**  
- **Nhiệm vụ:**  
  1. Tạo hệ thống 3 Agent mô phỏng thư viện:  
     - Agent Quản lý (Theo dõi sách)  
     - Agent Mượn/Trả (Xử lý giao dịch)  
     - Agent Thông báo (Nhắc nhở hạn trả)  
  2. Triển khai giao tiếp qua FIPA-ACL.  
- **Tài liệu:**  
  - [FIPA ACL Specifications](http://www.fipa.org/repository/aclspecs.html)  
  - [crewAI Communication Docs](https://docs.crewai.com/core-concepts/communication/)  

---

### **Tài liệu hỗ trợ**  
- **Video:** Demo hệ thống đặt món ăn tự động dùng BDI.  
- **Mẫu code:**  
  ```python
  # Ví dụ Agent giao tiếp
  class ChatAgent(Agent):
      def __init__(self):
          super().__init__()
          self.protocol = SimpleChatProtocol()
          
      def respond(self, message):
          return self.protocol.process(message)
  ```  

--- 

**Chuẩn bị cho Bài 4:** Bài tiếp theo sẽ tập trung vào quản lý nhiều Agent, cơ chế đấu giá và phân công nhiệm vụ phức tạp.