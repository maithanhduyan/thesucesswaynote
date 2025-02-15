Dưới đây là bài giảng chi tiết cho **Bài 6: Tương tác giữa các Agent** trong Module 3:

---

### **Bài 6: Tương tác giữa các Agent**  
**Thời lượng:** 2 buổi  
**Mục tiêu học tập:**  
- Hiểu các mô hình giao tiếp đồng bộ và bất đồng bộ giữa các Agent.  
- Áp dụng cơ chế xử lý xung đột và cạnh tranh trong hệ thống đa tác tử.  
- Xây dựng hệ thống giao thông thông minh với nhiều Agent tương tác.  

---

### **Nội dung bài giảng**  
#### **1. Giới thiệu (15 phút)**  
- **Ví dụ mở đầu:**  
  > "Một hệ thống giao thông thông minh gồm các Agent: xe tự lái, đèn giao thông, và trung tâm điều khiển.  
  → Làm thế nào để chúng **giao tiếp hiệu quả**, **tránh xung đột**, và **tối ưu hóa lưu lượng**?"  

---

#### **2. Các mô hình giao tiếp (60 phút)**  
**a. Giao tiếp đồng bộ (Synchronous Communication)**  
- **Định nghĩa:** Các Agent phải đồng bộ thời gian để giao tiếp.  
- **Ưu điểm:** Đơn giản, dễ kiểm soát.  
- **Nhược điểm:** Chậm, không phù hợp hệ thống lớn.  
- **Ví dụ:**  
  ```python
  # Agent A gửi yêu cầu và chờ phản hồi
  response = agent_b.send_request("get_traffic_data", wait=True)
  ```  

**b. Giao tiếp bất đồng bộ (Asynchronous Communication)**  
- **Định nghĩa:** Các Agent giao tiếp không cần đồng bộ thời gian.  
- **Ưu điểm:** Linh hoạt, phù hợp hệ thống phân tán.  
- **Nhược điểm:** Phức tạp, khó kiểm soát.  
- **Ví dụ:**  
  ```python
  # Agent A gửi yêu cầu và tiếp tục công việc
  agent_b.send_request("get_traffic_data", callback=handle_response)
  ```  

**c. Triển khai trong crewAI**  
```python
from crewai import Agent, MessageQueue

# Tạo hàng đợi tin nhắn
message_queue = MessageQueue()

# Agent gửi tin nhắn bất đồng bộ
agent_a.send_message(
    to=agent_b.id,
    content={"type": "request", "data": "traffic_update"},
    queue=message_queue
)

# Agent nhận tin nhắn
messages = agent_b.receive_messages(queue=message_queue)
```

---

#### **3. Xử lý xung đột và cạnh tranh (60 phút)**  
**a. Nguyên nhân xung đột**  
- **Tài nguyên giới hạn:** VD: Đường giao thông, năng lượng.  
- **Mục tiêu mâu thuẫn:** VD: Xe tự lái muốn đi nhanh, đèn giao thông muốn giảm ùn tắc.  

**b. Cơ chế giải quyết xung đột**  
| **Phương pháp**       | **Mô tả**                              | **Ví dụ**               |  
|------------------------|----------------------------------------|-------------------------|  
| **Đàm phán (Negotiation)** | Các Agent thỏa thuận để đạt giải pháp chung | Phân làn đường giao thông |  
| **Bỏ phiếu (Voting)**  | Agent bỏ phiếu để quyết định           | Chọn tuyến đường tối ưu |  
| **Luật ưu tiên (Priority Rules)** | Quy tắc cứng để phân xử              | Xe ưu tiên (cứu thương) |  

**c. Triển khai trong crewAI**  
```python
class ConflictResolver:
    def resolve(self, agents, conflict):
        if conflict.type == "resource":
            return self.negotiate(agents, conflict)
        elif conflict.type == "goal":
            return self.vote(agents, conflict)

    def negotiate(self, agents, conflict):
        offers = {}
        for agent in agents:
            offers[agent.id] = agent.propose_solution(conflict)
        return min(offers, key=offers.get)  # Chọn giải pháp tối ưu

    def vote(self, agents, conflict):
        votes = {}
        for agent in agents:
            votes[agent.id] = agent.vote(conflict.options)
        return max(votes, key=votes.get)  # Chọn option nhiều phiếu nhất
```

---

#### **4. Ví dụ: Xây dựng hệ thống giao thông thông minh (60 phút)**  
**a. Thiết kế hệ thống**  
- **Agent Xe tự lái:**  
  - Mục tiêu: Đến đích nhanh nhất.  
  - Hành động: Điều chỉnh tốc độ, chọn tuyến đường.  
- **Agent Đèn giao thông:**  
  - Mục tiêu: Giảm ùn tắc.  
  - Hành động: Điều chỉnh thời gian đèn.  
- **Agent Trung tâm điều khiển:**  
  - Mục tiêu: Tối ưu hóa lưu lượng.  
  - Hành động: Phân tích dữ liệu, đưa ra quyết định.  

**b. Triển khai code**  
```python
from crewai import Agent, Environment

# Tạo Agent
car_agent = Agent(role="Car", goal="Reach destination quickly")
traffic_light_agent = Agent(role="TrafficLight", goal="Reduce congestion")
control_center_agent = Agent(role="ControlCenter", goal="Optimize traffic flow")

# Tạo Environment
traffic_env = Environment(agents=[car_agent, traffic_light_agent, control_center_agent])

# Mô phỏng tương tác
def simulate_traffic(env):
    for _ in range(10):  # 10 bước mô phỏng
        env.update()
        print(f"Step {_}: Traffic status updated")

simulate_traffic(traffic_env)
```

---

### **Hoạt động trên lớp**  
1. **Thực hành nhóm (60 phút):**  
   - **Yêu cầu:** Xây dựng hệ thống giao thông đơn giản với:  
     - 2 Xe tự lái cạnh tranh để đi qua ngã tư.  
     - 1 Đèn giao thông điều phối.  
   - **Đầu ra:** Code + Demo mô phỏng.  

---

### **Bài tập về nhà**  
- **Nhiệm vụ:**  
  1. Thiết kế hệ thống đặt chỗ nhà hàng:  
     - Agent Khách hàng: Đặt bàn, yêu cầu dịch vụ.  
     - Agent Nhà hàng: Quản lý bàn, xử lý yêu cầu.  
  2. Triển khai cơ chế giải quyết xung đột khi bàn đã kín.  
- **Tài liệu:**  
  - [Multi-Agent Communication Protocols](https://arxiv.org/abs/2003.03423)  
  - [crewAI Conflict Resolution Guide](https://docs.crewai.com/advanced/conflict-resolution/)  

---

### **Tài liệu hỗ trợ**  
- **Slide:** So sánh các mô hình giao tiếp.  
- **Video:** Mô phỏng hệ thống giao thông thông minh.  
- **Mẫu code:**  
  ```python
  # Ví dụ đàm phán giữa các Agent
  class TrafficNegotiation:
      def __init__(self, agents):
          self.agents = agents

      def negotiate(self, conflict):
          solutions = {}
          for agent in self.agents:
              solutions[agent.id] = agent.propose(conflict)
          return min(solutions, key=lambda k: solutions[k]["cost"])
  ```  

--- 

**Chuẩn bị cho Bài 7:** Bài tiếp theo sẽ tập trung vào ứng dụng AI trong Agent, bao gồm Machine Learning và Reinforcement Learning.