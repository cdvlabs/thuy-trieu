# 🌊 Hệ Thống Theo Dõi & Dự Báo Thủy Triều TP.HCM (2026)

![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-blue?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

Hệ thống tự động hóa hoàn toàn quy trình thu thập, bóc tách và hiển thị dữ liệu thủy văn tại TP.HCM. Dự án được thiết kế để cung cấp thông tin trực quan, nhanh chóng về mực nước tại các trạm trọng điểm: **Nhà Bè**, **Phú An**, và **Thủ Dầu Một**.

---

## ✨ Tính Năng Nổi Bật

- 🤖 **Tự động hóa 100%**: Sử dụng GitHub Actions để tự động tải bản tin PDF từ website chính thức và bóc tách dữ liệu hàng ngày.
- 📊 **Dashboard Hiện Đại**: Giao diện Dashboard chuyên nghiệp với biểu đồ tương tác (Chart.js), hỗ trợ cả **Light Mode** và **Dark Mode**.
- 📅 **Lịch Dự Báo Chi Tiết**: Bảng hiển thị thông tin đỉnh triều/chân triều cho tất cả các ngày có trong dữ liệu bản tin.
- ⚠️ **Cảnh Báo Thông Minh**: Tự động nhận diện và cảnh báo theo các cấp độ **Báo động I (1.4m)**, **Báo động II (1.5m)**, và **Báo động III (1.6m)**.
- 📱 **Tương Thích Mọi Thiết Bị**: Giao diện Responsive hoạt động mượt mà trên cả Điện thoại, Máy tính bảng và PC.

---

## 🛠️ Công Nghệ Sử Dụng

- **Frontend**: HTML5, Tailwind CSS (Styling), JavaScript (Vanilla), Chart.js (Biểu đồ).
- **Backend/Automation**: 
    - **Python**: Sử dụng thư viện `pdfplumber` để bóc tách dữ liệu từ cấu trúc bảng PDF phức tạp.
    - **GitHub Actions**: Lập lịch chạy script tự động hàng ngày (Cron job).
- **Hosting**: GitHub Pages (Miễn phí, băng thông cao, không bao giờ "ngủ").

---

## 🚀 Hướng Dẫn Cài Đặt & Triển Khai

### 1. Khởi tạo Repository
Nếu bạn đã có code trên máy, hãy thực hiện các lệnh sau để đẩy lên GitHub:

```powershell
git remote add origin https://github.com/TEN_USER_CUA_BAN/hcmc-tide-monitor.git
git branch -M main
git push -u origin main
```

### 2. Kích hoạt GitHub Pages
1. Truy cập vào Repository của bạn trên GitHub.
2. Vào mục **Settings** > **Pages**.
3. Tại phần **Build and deployment**, chọn Branch là `main` và thư mục là `/ (root)`.
4. Bấm **Save**. Sau 1-2 phút, trang web của bạn sẽ sẵn sàng tại địa chỉ `https://<ten-user>.github.io/<ten-repo>/`.

---

## 📅 Nguồn Dữ Liệu
Dữ liệu được bóc tách từ các bản tin dự báo thủy văn hàng ngày của **Đài Khí tượng Thủy văn khu vực Nam Bộ**, được công bố chính thức tại website: [phongchonglutbaotphcm.gov.vn](https://www.phongchonglutbaotphcm.gov.vn/).

---

## 📜 Giấy Phép
Dự án này được phát hành dưới giấy phép **MIT License**. Bạn có thể tự do sử dụng, chỉnh sửa và chia sẻ.

---
*Thiết kế và phát triển bởi Gemini CLI - 2026*
