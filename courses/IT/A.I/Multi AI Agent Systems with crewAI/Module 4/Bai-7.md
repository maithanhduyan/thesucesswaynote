Dưới đây là bài giảng chi tiết cho **Bài 7: Ứng dụng AI trong Agent** trong Module 4:

---

### **Bài 7: Ứng dụng AI trong Agent**  
**Thời lượng:** 2 buổi  
**Mục tiêu học tập:**  
- Hiểu cách tích hợp Machine Learning (ML) vào quá trình ra quyết định của Agent.  
- Áp dụng Reinforcement Learning (RL) để Agent tự học và cải thiện hiệu suất.  
- Xây dựng Agent tự học chơi game đơn giản.  

---

### **Nội dung bài giảng**  
#### **1. Giới thiệu (15 phút)**  
- **Ví dụ mở đầu:**  
  > "Một Agent trong game *Pac-Man* cần học cách ăn điểm và tránh ma.  
  → Làm thế nào để Agent **tự học** chiến lược tối ưu mà không cần lập trình cứng?"  
  → Giới thiệu về vai trò của AI trong việc nâng cao khả năng tự chủ của Agent.  

---

#### **2. Machine Learning và Decision Making trong Agent (60 phút)**  
**a. Tích hợp ML vào Agent**  
- **Mục tiêu:** Giúp Agent ra quyết định dựa trên dữ liệu thay vì quy tắc cứng.  
- **Cách thức:**  
  - **Học có giám sát (Supervised Learning):** Dự đoán kết quả dựa trên dữ liệu huấn luyện.  
  - **Học không giám sát (Unsupervised Learning):** Phân cụm hoặc phát hiện mẫu.  
  - **Học tăng cường (Reinforcement Learning):** Học qua thử sai và phần thưởng.  

**b. Ví dụ: Agent dự đoán giá cổ phiếu**  
- **Bài toán:** Dự đoán giá cổ phiếu dựa trên dữ liệu lịch sử.  
- **Giải pháp:** Sử dụng mô hình hồi quy tuyến tính hoặc mạng neural.  
- **Code:**  
  ```python
  from sklearn.linear_model import LinearRegression
  import numpy as np

  # Dữ liệu huấn luyện
  X = np.array([[1], [2], [3], [4], [5]])  # Ngày
  y = np.array([100, 105, 110, 115, 120])  # Giá cổ phiếu

  # Huấn luyện mô hình
  model = LinearRegression()
  model.fit(X, y)

  # Dự đoán
  predicted_price = model.predict([[6]])
  print(f"Predicted price for day 6: {predicted_price[0]}")
  ```

---

#### **3. Reinforcement Learning cho các Agent tự học (60 phút)**  
**a. Khái niệm cơ bản**  
- **Mục tiêu:** Agent học cách tối đa hóa phần thưởng (reward) qua thử sai.  
- **Thành phần chính:**  
  - **State (Trạng thái):** Tình huống hiện tại của Agent.  
  - **Action (Hành động):** Lựa chọn của Agent.  
  - **Reward (Phần thưởng):** Phản hồi từ Environment.  
  - **Policy (Chiến lược):** Quy tắc ra quyết định của Agent.  

**b. Ví dụ: Agent học chơi game *Grid World***  
- **Bài toán:** Agent di chuyển trong lưới để tìm kho báu.  
- **Giải pháp:** Sử dụng Q-Learning.  
- **Code:**  
  ```python
  import numpy as np

  # Khởi tạo Q-table
  q_table = np.zeros((5, 5, 4))  # 5x5 grid, 4 actions (up, down, left, right)

  # Tham số học
  alpha = 0.1  # Learning rate
  gamma = 0.9  # Discount factor
  epsilon = 0.1  # Exploration rate

  # Hàm chọn hành động
  def choose_action(state):
      if np.random.uniform(0, 1) < epsilon:
          return np.random.choice(4)  # Khám phá
      else:
          return np.argmax(q_table[state])  # Khai thác

  # Hàm cập nhật Q-value
  def update_q_table(state, action, reward, next_state):
      q_table[state][action] += alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state][action])
  ```

---

#### **4. Ví dụ: Agent tự học chơi game (60 phút)**  
**a. Thiết kế hệ thống**  
- **Environment:** Game *Flappy Bird* đơn giản.  
- **Agent:** Bird cần học cách bay qua ống.  
- **Phần thưởng:** +1 nếu qua ống, -1 nếu chạm ống.  

**b. Triển khai code**  
```python
import gym
from stable_baselines3 import PPO

# Tạo Environment
env = gym.make("FlappyBird-v0")

# Tạo Agent sử dụng PPO (Proximal Policy Optimization)
model = PPO("MlpPolicy", env, verbose=1)

# Huấn luyện Agent
model.learn(total_timesteps=10000)

# Chạy Agent đã huấn luyện
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    if dones:
        obs = env.reset()
```

---

### **Hoạt động trên lớp**  
1. **Thực hành nhóm (60 phút):**  
   - **Yêu cầu:** Xây dựng Agent tự học chơi game *CartPole*:  
     - Environment: Cây gậy cần giữ thăng bằng.  
     - Agent: Học cách di chuyển để giữ gậy đứng.  
   - **Đầu ra:** Code + Demo mô phỏng.  

---

### **Bài tập về nhà**  
- **Nhiệm vụ:**  
  1. Thiết kế Agent tự học chơi game *Maze*:  
     - Environment: Mê cung 5x5.  
     - Agent: Học cách tìm đường thoát.  
  2. Triển khai bằng Q-Learning hoặc Deep Q-Network (DQN).  
- **Tài liệu:**  
  - [Reinforcement Learning Tutorial](https://www.tensorflow.org/agents/tutorials/0_intro_rl)  
  - [Stable-Baselines3 Documentation](https://stable-baselines3.readthedocs.io/)  

---

### **Tài liệu hỗ trợ**  
- **Slide:** Kiến trúc Reinforcement Learning.  
- **Video:** Demo Agent tự học chơi game *Flappy Bird*.  
- **Mẫu code:**  
  ```python
  # Ví dụ Q-Learning đơn giản
  def train_agent(env, episodes=1000):
      for episode in range(episodes):
          state = env.reset()
          done = False
          while not done:
              action = choose_action(state)
              next_state, reward, done, info = env.step(action)
              update_q_table(state, action, reward, next_state)
              state = next_state
  ```  

--- 

**Chuẩn bị cho Bài 8:** Bài tiếp theo sẽ tập trung vào xử lý ngôn ngữ tự nhiên (NLP) trong MAS.