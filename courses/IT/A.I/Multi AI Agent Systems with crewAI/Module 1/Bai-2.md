(Due to technical issues, the search service is temporarily unavailable.)

Dưới đây là bài giảng chi tiết cho **Bài 2: Giới thiệu về crewAI** trong Module 1:

---

### **Bài 2: Giới thiệu về crewAI**  
**Thời lượng:** 1-2 buổi (tùy thời lượng mỗi buổi).  
**Mục tiêu học tập:**  
- Hiểu mục tiêu, tính năng và lợi ích của crewAI.  
- So sánh crewAI với các framework MAS phổ biến khác.  
- Thành thạo cài đặt và thiết lập môi trường làm việc với crewAI.  

---

### **Nội dung bài giảng**  
#### **1. Giới thiệu (10 phút)**  
- **Ví dụ mở đầu:**  
  - Hình ảnh một đội ngũ lập trình viên hợp tác xây dựng hệ thống AI phức tạp.  
  - **crewAI** giống như "đội ngũ" hỗ trợ bạn xây dựng hệ thống đa tác tử (MAS) một cách hiệu quả.  

---

#### **2. Tổng quan về crewAI (30 phút)**  
**a. Mục tiêu**  
- **Đơn giản hóa phát triển MAS:**  
  - Giảm thời gian thiết lập môi trường và giao tiếp giữa các agent.  
  - Tích hợp sẵn các công cụ AI (NLP, Machine Learning).  
- **Hỗ trợ ứng dụng thực tế:**  
  - Tối ưu cho logistics, game, tự động hóa doanh nghiệp.  

**b. Tính năng nổi bật**  
- **Agent Template:** Tạo agent nhanh với các vai trò định sẵn (VD: Analyst, Coordinator).  
- **Built-in Communication Protocol:** Hỗ trợ giao tiếp qua message queue hoặc API.  
- **Environment Simulation:** Mô phỏng môi trường 2D/3D tùy chỉnh.  
- **AI Integration:**  
  - Kết hợp GPT-4, Claude cho xử lý ngôn ngữ tự nhiên.  
  - Hỗ trợ Reinforcement Learning (RL) qua thư viện Stable Baselines3.  

**c. Lợi ích**  
- **Dễ học:** Cú pháp Python đơn giản, tài liệu chi tiết.  
- **Linh hoạt:** Triển khai trên cloud, edge device, hoặc local server.  
- **Cộng đồng:** Hỗ trợ qua Discord và GitHub với 10K+ developers.  

---

#### **3. So sánh crewAI với framework MAS khác (30 phút)**  
| **Framework** | **Ưu điểm**                          | **Nhược điểm**                     | **Phù hợp**                |  
|----------------|---------------------------------------|-------------------------------------|----------------------------|  
| **crewAI**     | Hỗ trợ AI hiện đại, dễ tích hợp       | Chưa hỗ trợ distributed computing   | Ứng dụng SME, prototype    |  
| **JADE**       | Tuân thủ FIPA, mạnh về agent logic    | Cấu hình phức tạp, Java-based       | Hệ thống tài chính, viễn thông |  
| **Mesa**       | Trực quan với visualization tools    | Giới hạn scalability               | Nghiên cứu, mô phỏng xã hội |  
| **Jason**      | Ngôn ngữ AgentSpeak chuyên biệt       | Độ phức tạp cao, ít tài liệu       | Hệ thống quyết định phức tạp |  

**Case Study:**  
- **Amazon Logistics:** Dùng JADE cho hệ thống điều phối robot (độ tin cậy cao).  
- **Startup Delivery App:** Chọn crewAI để prototype nhanh với NLP và RL.  

---

#### **4. Cài đặt và thiết lập môi trường (40 phút)**  
**a. Yêu cầu hệ thống**  
- Python 3.8+, PIP, Virtual Environment (khuyến nghị).  

**b. Các bước cài đặt**  
1. **Cài đặt thư viện:**  
   ```bash
   pip install crewai[tools]  # Cài đặt core + AI tools
   pip install crewai[visual]  # Cài đặt visualization (optional)
   ```

2. **Xác minh cài đặt:**  
   ```python
   import crewai
   print(crewai.__version__)  # Output: 0.8.2+
   ```

3. **Chạy ví dụ mẫu:**  
   ```python
   from crewai import Agent, Environment

   # Tạo agent
   analyst = Agent(
       role="Data Analyst",
       goal="Phân tích dữ liệu bán hàng",
       tools=["python", "pandas"]
   )

   # Tạo môi trường
   env = Environment(agents=[analyst])
   env.run()
   ```

**c. Xử lý lỗi thường gặp**  
- **Lỗi thiếu thư viện:** Chạy `pip install -r requirements.txt`.  
- **Lỗi version conflict:** Dùng `venv` hoặc `conda`.  

---

### **Hoạt động trên lớp**  
1. **Thực hành cài đặt (20 phút):**  
   - Học viên cài đặt crewAI trên máy cá nhân và chạy ví dụ mẫu.  

2. **Thảo luận nhóm (20 phút):**  
   - **Câu hỏi:** "Tại sao crewAI phù hợp để xây dựng chatbot đa nhiệm hơn JADE?"  
   - **Gợi ý:** Xem xét khả năng tích hợp NLP và tốc độ phát triển.  

---

### **Bài tập về nhà**  
- **Nhiệm vụ:**  
  1. Cài đặt crewAI và chạy ví dụ mẫu từ tài liệu.  
  2. Viết script tạo 2 agent giao tiếp đơn giản (VD: Agent A hỏi thời tiết, Agent B trả lời).  
- **Tài liệu tham khảo:**  
  - [crewAI Documentation](https://docs.crewai.com/)  
  - GitHub Repository: [crewAI Examples](https://github.com/joaomdmoura/crewai-examples)  

---

### **Tài liệu hỗ trợ giảng dạy**  
- **Slide PowerPoint:** Kiến trúc crewAI, bảng so sánh framework.  
- **Video demo:** Triển khai hệ thống đặt vé máy bay tự động bằng crewAI.  
- **Mã nguồn mẫu:** File Jupyter Notebook với ví dụ Agent + Environment.  

--- 

**Chuẩn bị cho bài tiếp theo:** Bài 3 sẽ đi sâu vào thiết kế Agent cơ bản với crewAI, bao gồm BDI model và giao tiếp.