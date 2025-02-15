# Cấu trúc Dự án như sau:

```
../
├── .github
│   └── workflows
│       └── deploy.yml
├── blog
│   ├── .vuepress
│   │   ├── client.js
│   │   ├── components
│   │   │   └── ArticleList.vue
│   │   ├── config.js
│   │   ├── layouts
│   │   │   ├── Article.vue
│   │   │   ├── Category.vue
│   │   │   ├── Tag.vue
│   │   │   └── Timeline.vue
│   │   └── styles
│   │       └── index.scss
│   ├── get-started.md
│   └── posts
│       ├── archive1.md
│       ├── archive2.md
│       ├── article1.md
│       ├── article10.md
│       ├── article11.md
│       ├── article12.md
│       ├── article2.md
│       ├── article3.md
│       ├── article4.md
│       ├── article5.md
│       ├── article6.md
│       ├── article7.md
│       ├── article8.md
│       ├── article9.md
│       ├── ke-manh-tu-minh-tinh-thuc.md
│       ├── sticky.md
│       └── sticky2.md
├── case-study
│   └── Shophouse của bạn Hương tại dự án Aqua City Đồng Nai (Novaland).md
├── courses
│   ├── Chinese
│   │   ├── 500-words.html
│   │   └── vocabulary.html
│   ├── IT
│   │   └── A.I
│   │       └── Multi AI Agent Systems with crewAI
│   │           ├── Module 1
│   │           │   ├── Bai-1.md
│   │           │   └── Bai-2.md
│   │           ├── Module 2
│   │           │   ├── Bai-3.md
│   │           │   └── Bai-4.md
│   │           ├── Module 3
│   │           │   ├── Bai-5.md
│   │           │   └── Bai-6.md
│   │           ├── Module 4
│   │           │   ├── Bai-7.md
│   │           │   └── Bai-8.md
│   │           ├── Module 5
│   │           └── Module 6
│   ├── Learn_How_to_Learn
│   │   ├── 71-cach-hoc.md
│   │   ├── 71_learning_methods.md
│   │   └── Personalised+Learning+Plan+(Click+on+File+_+Make+a+copy).xlsx
│   ├── ProjectManager
│   │   ├── SkillShare.md
│   │   ├── Top_10_Terms_Project_Managers_Use.md
│   │   └── farmstay.md
│   ├── lean_six_sigma
│   │   ├── 5 Whys
│   │   ├── 5S
│   │   ├── DMAIC Model
│   │   ├── Histogram
│   │   ├── Hoshin Kanri
│   │   ├── Ishikawa
│   │   ├── Kaizen
│   │   ├── Kanban
│   │   ├── OGSM
│   │   ├── Poka-Yoke
│   │   ├── REAME.md
│   │   ├── SIPOC
│   │   └── World Class Manufacturing.md
│   └── mba
│       ├── human_resource
│       ├── lean_six_sigma
│       │   └── images
│       │       ├── 6_big_loss.jpeg
│       │       ├── Road-map_to_world_class_manufacturing.jpg
│       │       ├── Screenshot 2023-12-01 204515.png
│       │       ├── Screenshot 2023-12-01 210358.png
│       │       └── world_class_manufacturing.png
│       └── operational_excillent_OE
├── images
│   ├── cryptocurrency
│   │   ├── Công Thức Đầu Tư Tiền Mã Hóa.drawio
│   │   └── Công Thức Đầu Tư Tiền Mã Hóa.drawio.png
│   └── wallet
│       └── DOGE-DDYnGiWgpSm1cmi8imksqHY8aLX7RtzVEa.png
├── note
│   ├── Cổ Học Tinh Hoa
│   │   ├── 7 Kiểu Người Hủy Hoại Cuộc Sống Bạn.md
│   │   ├── Bài học kiểm soát cảm xúc từ cổ nhân.md
│   │   ├── Bạn nghĩ chúng ta phải trả giá bao nhiêu lần cho một sai lầm.md
│   │   ├── Khi con người bắt đầu thích khoe khoang.md
│   │   ├── Kẻ mạnh tự thức tỉnh.md
│   │   ├── Ngộ Không từng nói một câu sâu sắc như thế này.md
│   │   ├── Nếu bạn để ý kỹ những người thành đạt và có địa vị cao xung quanh.md
│   │   ├── TÍNH KHÍ SẼ QUYẾT ĐỊNH ĐẾN SỐ PHẬN CỦA MỘT NGƯỜI.md
│   │   ├── Tại sao có những người có thể ở nhà cả ngày mà không cần bước chân ra ngoài.md
│   │   └── tu-kiem-hoa-tinh-con-duong-den-su-an-nien-tuyet-doi.md
│   ├── blogs
│   │   ├── 2025
│   │   │   ├── Chien-Tranh-Kinh_te_Mi-Trung.md
│   │   │   └── Nghe-Thuat-Dam-Phan-Donald-Trump.md
│   │   ├── Hieu.TV
│   │   │   └── Xây Dựng Sự Tự Tin.md
│   │   ├── Sadhguru
│   │   │   └── Duc-Phat-da-giac-ngo-nhu-the-nao.md
│   │   ├── TamQuoc
│   │   │   ├── Goc-nhin-tam-quoc-qua-do-tuoi.md
│   │   │   ├── Ky-Muu-Ty-Ngọ-Coc-cua-Nguy-Dien.md
│   │   │   └── Tam-Su-Tao-Thao.md
│   │   ├── ThinksmartBrother.md
│   │   └── ThuanCapital
│   │       ├── Bitcoin có phải là một zero-sum game không.md
│   │       └── Chung_Khoan_Howey_Test.md
│   ├── books
│   │   ├── 48_Nguyen_Tac_Chu_Chot_cua_Quyen_Luc.md
│   │   ├── Atomic_Habits_James_Clear
│   │   │   ├── Atomic_Habits_James_Clear.md
│   │   │   ├── Sức Mạnh Của Lợi Thế Tích Lũy.md
│   │   │   └── images
│   │   │       ├── Mathew_Effect.png
│   │   │       ├── vilfredo-pareto-1870s.png
│   │   │       └── winner_takes_all.png
│   │   ├── BiMatTuDuyTrieuPhu_SecretsOfTheMillionaireMind.md
│   │   ├── Chìa khóa để trở thành người giàu. Tận dụng Tư duy Đòn bẩy.md
│   │   ├── Làm chủ tư duy phản biện. Biến đổi tư duy để phát triển cá nhân toàn diện.md
│   │   ├── Miyamoto Musashi.md
│   │   ├── TheOneMinuteManager.md
│   │   └── WAY OF THE TURTLE.md
│   ├── chat
│   │   └── Phát triển trí não.md
│   ├── maithanhduyan
│   │   ├── Dau-tu-theo-xu-huong.md
│   │   ├── Phuoc-duc-cua-mot-nguoi-rot-cuoc-la-gi.md
│   │   ├── Xuan-At-Ty-2025.md
│   │   ├── binhluanchientranh1979.md
│   │   └── thu-gui-me-dau-tien.md
│   ├── markdown-cheat-sheet.md
│   ├── mindset
│   │   ├── 10NguyenTacDauTu.md
│   │   ├── 21NguyenTacTuDoTaiChinh.md
│   │   ├── 3-bi-mat-nguoi-giau-khong-noi.md
│   │   ├── 4MoVangThanhCong.md
│   │   ├── 5DieuCanLamDeTuDoTaiChinh.md
│   │   ├── 6 CHIẾN THUẬT KIẾM TIỀN.md
│   │   ├── 7TinHieuThanhCong.md
│   │   ├── 8BaiHocLamGiauHieuQuaCuaRobertKiosaky.md
│   │   ├── 8ThieuSotLonNhatCuaDoiNguoi.md
│   │   ├── Binh-Phap-Ton-Tu-Trong-Dau-Tu.md
│   │   ├── Cach-nguoi-giau-bien-tien-thanh-nhieu-tien-hon.md
│   │   ├── CachKiemTienHieuQua2022HieuTV.md
│   │   ├── LichSuTienTe.md
│   │   ├── TamThaiTotSucManhGap100LanTriTue.md
│   │   ├── ThoiQuenTotCuaThanhCong.md
│   │   ├── ThuThach5Dola.md
│   │   ├── Toi-uu-hoa-thoi-gian-de-gia-tang-gia-tri-tai-san.md
│   │   ├── Vit-con-boi-thanh-hanh-sau-me.md
│   │   ├── amazon-nam-2001.md
│   │   ├── co-the-lam-giau-bang-dau-tu-hay-khong-cau-chuyen-cua-warren-buffett.md
│   │   ├── cot-loi-cua-viec-thu-hut-tai-van-la-khong-can-lam-gi-qua-nhieu.md
│   │   └── tai-sao-ban-mai-ngheo-be-gay-tu-duy-cu-de-lam-giau-ngay-hom-nay.md
│   ├── process-steps
│   │   └── How_to_Get_Rich_by_Felix_Dennis.md
│   ├── q&a
│   │   └── Mua Bất Động Sản ở Mỹ.md
│   ├── quotes
│   │   ├── Albert Einstein.md
│   │   ├── Benjamin Franklin.md
│   │   ├── Benjamin Graham.md
│   │   ├── Carl Icahn.md
│   │   ├── Carl Jung.md
│   │   ├── George Soros.md
│   │   ├── Jesse Livermore.md
│   │   ├── Jim Rohn.md
│   │   ├── John Neff.md
│   │   ├── Li Ka-shing Lý Gia Thành.md
│   │   ├── Peter Lynch.md
│   │   ├── Ray Dalio.md
│   │   ├── Ray_Dalio
│   │   │   ├── Ray_Dalio_2024_04_10.jpg
│   │   │   └── Để làm việc hiệu quả.md
│   │   ├── Robert Kiyosaki.md
│   │   ├── Sir John Templeton.md
│   │   ├── Warren Buffett.md
│   │   └── Wiliam O’Neil.md
│   ├── stories
│   │   ├── JohnTempleton.md
│   │   └── RonaldRead.md
│   └── training
│       ├── GaryVee
│       ├── RobinSharma
│       ├── TIỀN THÂN Podcast Series
│       ├── TaiChinhCaNhan
│       │   ├── 23-cach-kiem-tien.md
│       │   └── Lam-gi-voi-muc-luong-15-trieu.md
│       └── TaiZen
│           ├── 10_Mindset_About_Money_by_TaiFu.md
│           ├── 4_Phuong_Phap_Quan_Ly_Cam_Xuc.md
│           ├── Ben_Ngoai_Cua_Em_Giong_Nhu_Nguoi_Thanh_Cong_Khong.md
│           ├── Phuong_Phap_Mua_Dat_Cat_Nha.md
│           ├── Phuong_Phap_Tim_Kiem_Tien_Ma_Hoa_Co_Kha_Nang_Lam_Loi.md
│           ├── Phuong_Phap_VC_MAN.md
│           └── Quotes.md
├── novel
│   └── Đặc Công Xuyên Không Về Thời Nguyên Thuỷ
│       ├── Phần 1.md
│       ├── Phần 10.md
│       ├── Phần 11.md
│       ├── Phần 12.md
│       ├── Phần 13.md
│       ├── Phần 14.md
│       ├── Phần 15.md
│       ├── Phần 16.md
│       ├── Phần 17.md
│       ├── Phần 18.md
│       ├── Phần 19.md
│       ├── Phần 2.md
│       ├── Phần 20.md
│       ├── Phần 21.md
│       ├── Phần 22.md
│       ├── Phần 23.md
│       ├── Phần 24.md
│       ├── Phần 25.md
│       ├── Phần 26.md
│       ├── Phần 27.md
│       ├── Phần 28.md
│       ├── Phần 29.md
│       ├── Phần 3.md
│       ├── Phần 30.md
│       ├── Phần 4.md
│       ├── Phần 5.md
│       ├── Phần 6.md
│       ├── Phần 7.md
│       ├── Phần 8.md
│       └── Phần 9.md
├── package-lock.json
├── package.json
└── templates
    ├── Business Model Canvas Template.pdf
    └── Value_Proposition_Canvas_Template.pdf
```

# Danh sách chi tiết các file:

