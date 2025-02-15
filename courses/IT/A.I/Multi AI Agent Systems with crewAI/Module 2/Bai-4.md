(Due to technical issues, the search service is temporarily unavailable.)

Dưới đây là bài giảng chi tiết cho **Bài 4: Quản lý nhiều Agent** trong Module 2:

---

### **Bài 4: Quản lý nhiều Agent**  
**Thời lượng:** 2 buổi  
**Mục tiêu học tập:**  
- Hiểu cơ chế điều phối và hợp tác giữa các Agent.  
- Áp dụng cơ chế đàm phán (negotiation) và phân công nhiệm vụ.  
- Xây dựng hệ thống đấu giá đa Agent sử dụng crewAI.  

---

### **Nội dung bài giảng**  
#### **1. Giới thiệu (15 phút)**  
- **Ví dụ mở đầu:**  
  > "Một đội cứu hộ gồm drone (Agent A), robot mặt đất (Agent B), và trung tâm điều khiển (Agent C) phối hợp tìm kiếm người mất tích.  
  → Làm thế nào để chúng **tự động phân công** khu vực tìm kiếm và **thương lượng** khi phát hiện chướng ngại vật?"  

---

#### **2. Điều phối và hợp tác giữa các Agent (60 phút)**  
**a. Điều phối (Coordination)**  
- **Vấn đề:** Tránh xung đột, tối ưu hóa tài nguyên.  
- **Chiến lược:**  
  - **Tập trung:** Agent "quản lý" điều phối (VD: hệ thống đặt xe Grab).  
  - **Phân tán:** Sử dụng giao thức (VD: Contract Net Protocol).  

**b. Hợp tác (Cooperation)**  
- **Cơ chế:**  
  - **Mục tiêu chung:** Các Agent chia sẻ mục tiêu (VD: giảm ùn tắc giao thông).  
  - **Kế hoạch chung:** Lập lịch trình phối hợp (VD: dây chuyền sản xuất).  
- **Ví dụ:** Robot trong kho Amazon hợp tác tránh va chạm.  

**Demo:**  
```python
from crewai import Agent, Environment

# Tạo Agent quản lý và worker
manager = Agent(role="Manager", goal="Phân công task")
worker1 = Agent(role="Worker", goal="Xử lý task A")
worker2 = Agent(role="Worker", goal="Xử lý task B")

# Thiết lập giao thức phân tán
env = Environment(agents=[manager, worker1, worker2])
env.set_protocol("decentralized")  # Agent tự thương lượng
```

---

#### **3. Cơ chế đàm phán (Negotiation) (60 phút)**  
**a. Nguyên tắc cơ bản:**  
- **Bước 1:** Khởi tạo đàm phán (Request).  
- **Bước 2:** Trao đổi đề xuất (Offer/Counteroffer).  
- **Bước 3:** Đạt thỏa thuận (Agreement) hoặc hủy bỏ (Terminate).  

**b. Chiến lược đàm phán:**  
| **Loại**       | **Mô tả**                              | **Ví dụ**               |  
|----------------|----------------------------------------|-------------------------|  
| **Competitive**| Tối đa hóa lợi ích cá nhân             | Đấu giá trên eBay       |  
| **Cooperative**| Cân bằng lợi ích chung                 | Phân bổ ngân sách team  |  

**c. Triển khai trong crewAI:**  
```python
class NegotiationProtocol(Protocol):
    def negotiate(self, task, candidates):
        offers = {}
        for agent in candidates:
            offers[agent.id] = agent.bid(task)
        winner = min(offers, key=offers.get)  # Chọn giá thấp nhất
        return winner

# Agent Worker đưa ra giá
@worker1.register_skill
def bid(task):
    return calculate_cost(task.duration, task.resources)
```

---

#### **4. Phân công nhiệm vụ (Task Allocation) (60 phút)**  
**a. Phương pháp:**  
- **Market-Based:** Đấu giá nhiệm vụ (VD: hệ thống giao hàng).  
- **Contract Net Protocol:**  
  ```mermaid
  graph LR
  A[Manager] -->|Announce Task| B[Worker1]
  A -->|Announce Task| C[Worker2]
  B -->|Bid $10| A
  C -->|Bid $8| A
  A -->|Award Task| C
  ```  

**b. Ví dụ: Hệ thống giao hàng**  
- **Bài toán:** 5 đơn hàng → 3 shipper.  
- **Giải pháp:**  
  - Shipper đấu giá dựa trên khoảng cách và chi phí.  
  - Manager chọn shipper tối ưu.  

**Code demo:**  
```python
# Tạo task và shipper
tasks = [Task("Giao hàng A"), Task("Giao hàng B")]
shippers = [Shipper("Xe máy"), Shipper("Xe tải")]

# Phân công qua Contract Net
for task in tasks:
    winner = manager.allocate_task(task, shippers)
    print(f"Task {task.id} assigned to {winner.id}")
```

---

#### **5. Ví dụ: Xây dựng hệ thống đấu giá (60 phút)**  
**a. Thiết kế hệ thống:**  
- **Agent Đấu giá (Auctioneer):**  
  - Quản lý quy trình đấu giá.  
  - Xác định người thắng.  
- **Agent Người mua (Bidder):**  
  - Đưa ra giá dựa trên chiến lược (VD: tăng dần, giới hạn).  

**b. Triển khai code:**  
```python
from crewai import Agent, Task

class AuctionAgent(Agent):
    def __init__(self, item, reserve_price):
        super().__init__(role="Auctioneer")
        self.item = item
        self.reserve_price = reserve_price
        self.bids = {}

    def receive_bid(self, bidder_id, amount):
        if amount >= self.reserve_price:
            self.bids[bidder_id] = amount

    def close_auction(self):
        if not self.bids:
            return None
        winner = max(self.bids, key=self.bids.get)
        return winner, self.bids[winner]

# Tạo Agent
auctioneer = AuctionAgent(item="Mona Lisa", reserve_price=1000)
bidder1 = Agent(role="Bidder", strategy="incremental_bid")
bidder2 = Agent(role="Bidder", strategy="aggressive_bid")
```

---

### **Hoạt động trên lớp**  
1. **Thực hành nhóm (60 phút):**  
   - **Yêu cầu:** Xây dựng hệ thống đấu giá nghệ thuật với:  
     - 1 Auctioneer kiểm tra giá đặt.  
     - 3 Bidder có chiến lược đặt giá khác nhau.  
   - **Đầu ra:** Code + Demo mô phỏng quá trình đấu giá.  

---

### **Bài tập về nhà**  
- **Nhiệm vụ:**  
  1. Thiết kế hệ thống phân công lái xe tự động:  
     - Task: Đón khách từ điểm A → B.  
     - Driver Agent: Đưa ra giá dựa trên khoảng cách.  
  2. Triển khai bằng Contract Net Protocol.  
- **Tài liệu:**  
  - Paper: [Task Allocation in Multi-Agent Systems](https://arxiv.org/abs/2105.04221)  
  - [crewAI Task Management Guide](https://docs.crewai.com/advanced/task-allocation/)  

---

### **Tài liệu hỗ trợ**  
- **Slide:** So sánh các phương pháp phân công nhiệm vụ.  
- **Video:** Mô phỏng hệ thống đấu giá chứng khoán.  
- **Mẫu code:**  
  ```python
  # Contract Net Protocol Implementation
  def contract_net(task, candidates):
      print(f"Announcing task: {task.description}")
      bids = {agent.id: agent.bid(task) for agent in candidates}
      if not bids:
          return None
      winner_id = min(bids, key=lambda k: bids[k])
      return winner_id
  ```  

--- 

**Chuẩn bị cho Bài 5:** Bài tiếp theo sẽ tập trung vào mô hình hóa môi trường và tương tác Agent-Environment.