Dưới đây là bài giảng chi tiết cho **Bài 5: Mô hình hóa môi trường** trong Module 3:

---

### **Bài 5: Mô hình hóa môi trường**  
**Thời lượng:** 2 buổi  
**Mục tiêu học tập:**  
- Hiểu khái niệm và vai trò của Environment trong hệ thống đa tác tử (MAS).  
- Tạo môi trường ảo sử dụng crewAI.  
- Mô phỏng tương tác giữa Agent và Environment.  

---

### **Nội dung bài giảng**  
#### **1. Giới thiệu (15 phút)**  
- **Ví dụ mở đầu:**  
  > "Một thành phố thông minh (Smart City) là một Environment, nơi các Agent (xe tự lái, đèn giao thông, cảm biến) tương tác để tối ưu hóa giao thông và tiết kiệm năng lượng."  
  → Giới thiệu về tầm quan trọng của Environment trong MAS.  

---

#### **2. Khái niệm về Environment trong MAS (45 phút)**  
**a. Định nghĩa Environment**  
- **Environment:** Không gian vật lý hoặc ảo nơi các Agent hoạt động và tương tác.  
- **Đặc điểm:**  
  - **Động (Dynamic):** Thay đổi theo thời gian.  
  - **Không chắc chắn (Uncertain):** Thông tin không đầy đủ.  
  - **Tương tác (Interactive):** Agent có thể thay đổi Environment.  

**b. Phân loại Environment**  
| **Loại**            | **Mô tả**                              | **Ví dụ**               |  
|----------------------|----------------------------------------|-------------------------|  
| **Discrete**         | Không gian rời rạc (VD: bàn cờ)        | Game cờ vua             |  
| **Continuous**       | Không gian liên tục (VD: bản đồ)       | Mô phỏng giao thông     |  
| **Static**           | Không thay đổi theo thời gian          | Môi trường phòng thí nghiệm |  
| **Dynamic**          | Thay đổi theo thời gian                | Thị trường chứng khoán  |  

**c. Vai trò của Environment**  
- **Cung cấp thông tin:** Agent nhận dữ liệu từ Environment.  
- **Giới hạn hành động:** Quy định các hành động khả thi.  
- **Phản hồi:** Đánh giá kết quả hành động của Agent.  

---

#### **3. Tạo môi trường ảo với crewAI (60 phút)**  
**a. Cấu trúc Environment trong crewAI**  
```python
from crewai import Environment

# Tạo môi trường 2D đơn giản
class GridEnvironment(Environment):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def add_agent(self, agent, x, y):
        self.grid[y][x] = agent

    def move_agent(self, agent, new_x, new_y):
        old_x, old_y = self.find_agent(agent)
        self.grid[old_y][old_x] = None
        self.grid[new_y][new_x] = agent

    def find_agent(self, agent):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == agent:
                    return x, y
        return None
```

**b. Ví dụ: Môi trường kho hàng**  
- **Yêu cầu:**  
  - Agent di chuyển trong kho để tìm kiếm sản phẩm.  
  - Environment cập nhật vị trí và trạng thái sản phẩm.  
- **Code:**  
  ```python
  warehouse = GridEnvironment(width=10, height=10)
  robot = Agent(role="Picker", goal="Find product A")
  warehouse.add_agent(robot, x=0, y=0)
  warehouse.move_agent(robot, new_x=5, new_y=5)
  ```

---

#### **4. Mô phỏng tương tác giữa Agent và Environment (60 phút)**  
**a. Cơ chế tương tác**  
1. **Agent nhận thông tin:**  
   ```python
   class RobotAgent(Agent):
       def perceive(self, environment):
           self.position = environment.find_agent(self)
           self.surroundings = environment.get_surroundings(self.position)
   ```  

2. **Agent hành động:**  
   ```python
   def act(self, environment):
       if self.goal == "Find product A":
           if "product_A" in self.surroundings:
               self.pick_product()
           else:
               self.move_toward_goal()
   ```  

3. **Environment cập nhật:**  
   ```python
   def update(self):
       for agent in self.agents:
           agent.perceive(self)
           agent.act(self)
   ```  

**b. Demo: Mô phỏng giao thông**  
- **Environment:** Bản đồ thành phố với đèn giao thông và xe cộ.  
- **Agent:** Xe tự lái di chuyển theo tín hiệu đèn.  
- **Code:**  
  ```python
  class TrafficEnvironment(Environment):
      def __init__(self):
          super().__init__()
          self.traffic_lights = {"A": "red", "B": "green"}
          self.cars = []

      def add_car(self, car):
          self.cars.append(car)

      def update_lights(self):
          for light in self.traffic_lights:
              self.traffic_lights[light] = "green" if self.traffic_lights[light] == "red" else "red"
  ```

---

### **Hoạt động trên lớp**  
1. **Thực hành nhóm (60 phút):**  
   - **Yêu cầu:** Xây dựng môi trường đơn giản (VD: bản đồ 5x5) với:  
     - 1 Agent di chuyển tìm kiếm "kho báu".  
     - Environment cập nhật vị trí và trạng thái.  
   - **Đầu ra:** Code + Demo mô phỏng.  

---

### **Bài tập về nhà**  
- **Nhiệm vụ:**  
  1. Thiết kế môi trường mô phỏng hệ thống đặt xe tự động:  
     - Environment: Bản đồ thành phố với điểm đón/trả khách.  
     - Agent: Xe tự lái di chuyển theo yêu cầu.  
  2. Triển khai tương tác Agent-Environment.  
- **Tài liệu:**  
  - [Environment Design in MAS](https://www.sciencedirect.com/topics/computer-science/multi-agent-environment)  
  - [crewAI Environment Docs](https://docs.crewai.com/core-concepts/environment/)  

---

### **Tài liệu hỗ trợ**  
- **Slide:** Kiến trúc Environment trong MAS.  
- **Video:** Mô phỏng hệ thống giao thông thông minh.  
- **Mẫu code:**  
  ```python
  # Ví dụ Environment đơn giản
  class SimpleEnvironment(Environment):
      def __init__(self):
          super().__init__()
          self.agents = []
          self.state = {}

      def add_agent(self, agent):
          self.agents.append(agent)
          self.state[agent.id] = "active"
  ```  

--- 

**Chuẩn bị cho Bài 6:** Bài tiếp theo sẽ tập trung vào tương tác giữa các Agent trong môi trường phức tạp.