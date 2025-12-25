---
title: "What we learned building an affordable Zero Trust Network with Tailscale & Headscale"
category: 
  - zero-trust-networking
tag: 
  - tailscale
  - headscale
  - zero-trust-networking
date: 2025-12-25
---

# What we learned building an affordable Zero Trust Network with Tailscale & Headscale

### [Link](https://www.youtube.com/watch?v=1XMkEmnjQ-Q)

Chúng tôi sẽ trình bày về những bài học kinh nghiệm khi xây dựng một mạng lưới Zero Trust với chi phí hợp lý bằng cách sử dụng Tailscale và Headscale. Chương trình hôm nay bao gồm phần giới thiệu về doanh nghiệp, tổng quan về giải pháp công nghệ, các trường hợp sử dụng thực tế tại Service Integrators và phần demo trực tiếp. ASP là nhà cung cấp dịch vụ quản lý có trụ sở tại Brussels, tập trung vào thị trường tầm trung với đội ngũ khoảng 60 nhân sự và doanh thu 7 triệu euro. Nhiệm vụ của chúng tôi là hỗ trợ các doanh nghiệp tập trung vào chuyển đổi số, trong khi chúng tôi chịu trách nhiệm quản lý và đảm bảo sự ổn định cho cơ sở hạ tầng công nghệ thông tin của họ.

Service Integrators được thành lập năm 1993, là công ty chuyên về giám sát hệ thống và cung cấp sản phẩm Monitor Now dựa trên nền tảng Checkmk. Vào tháng 3 năm 2024, ASP đã mua lại công ty này nhờ sự tương đồng về công nghệ và nhu cầu tích hợp công cụ giám sát vào dịch vụ quản lý. Chúng tôi cùng sử dụng một hệ thống công nghệ chung, tạo ra sự kết hợp hiệu quả để phục vụ khách hàng.

Tailscale và Headscale là các giải pháp bảo mật Zero Trust mã nguồn mở, giúp thay thế mô hình bảo mật truyền thống dựa trên tường lửa. Triết lý Zero Trust hoạt động theo nguyên tắc không bao giờ tin tưởng mặc định, mà chỉ cấp quyền dựa trên danh tính đã được xác thực và ủy quyền rõ ràng. Việc quản lý truy cập dựa trên danh tính cho phép kiểm soát chặt chẽ quyền hạn của người dùng và giới hạn thời gian truy cập, điều mà các tường lửa truyền thống khó thực hiện được.

Trong bối cảnh mạng lưới hiện đại với nhu cầu làm việc từ xa và sử dụng thiết bị cá nhân (BYOD) ngày càng tăng, các VPN truyền thống thường trở thành nút thắt cổ chai. Tailscale giải quyết vấn đề này bằng cách tạo ra một mạng lưới mesh được mã hóa an toàn giữa các thiết bị, cho phép kết nối trực tiếp mà không cần đi qua cổng tập trung. Headscale đóng vai trò là máy chủ điều khiển mã nguồn mở, cho phép doanh nghiệp tự quản lý hệ thống mạng của mình mà không phụ thuộc vào máy chủ của bên thứ ba.

Quy trình triển khai bao gồm việc thiết lập máy chủ Headscale có địa chỉ IP công cộng và cài đặt agent Tailscale trên các thiết bị cần quản lý. Chúng tôi có thể định nghĩa các chính sách truy cập (ACL) dựa trên người dùng để kiểm soát cụ thể ai được phép truy cập vào tài nguyên nào. Giải pháp này giúp giảm bề mặt tấn công, đơn giản hóa việc quản lý và cải thiện đáng kể trải nghiệm người dùng so với VPN truyền thống.

Đối với trường hợp sử dụng tại Service Integrators, chúng tôi cần truy cập vào máy chủ của khách hàng để quản lý mà không muốn thiết lập các kết nối VPN phức tạp hay cấp thiết bị riêng. Bằng cách sử dụng Headscale, chúng tôi có thể kiểm soát quyền truy cập chi tiết và đảm bảo an toàn thông qua xác thực đa yếu tố. Hệ thống cho phép chúng tôi dễ dàng thêm hoặc loại bỏ quyền truy cập của nhân viên và bên thứ ba một cách linh hoạt.

Trong phần demo, chúng tôi sẽ hiển thị quy trình đăng nhập và xác thực thiết bị vào mạng lưới mesh thông qua Entra ID. Các bạn có thể thấy cách thiết lập các thẻ (tag) và danh sách kiểm soát truy cập (ACL) để ngăn chặn hoặc cho phép kết nối giữa các máy chủ và thiết bị cá nhân. Hệ thống phản hồi rất nhanh với các thay đổi cấu hình, đảm bảo tính bảo mật và tuân thủ quy trình ngay lập tức khi quyền truy cập bị thu hồi.