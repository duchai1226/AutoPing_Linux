import subprocess
import time

# Địa chỉ IP cần ping
ip_address = "115.78.231.95"

# Số lượng cửa sổ cmd cần mở
number_of_cmds = 100

# Hàm mở cửa sổ cmd và thực hiện lệnh ping
def open_cmd_and_ping(ip):
    try:
        # Lệnh ping sẽ chạy vô hạn. Nếu muốn giới hạn số lần ping, thêm tùy chọn -n <số_lần_ping> (với Windows)
        subprocess.Popen(["cmd", "/c", f"start cmd /k ping {ip}"])
    except Exception as e:
        print(f"Đã xảy ra lỗi khi mở cmd và ping: {e}")

# Mở 100 cửa sổ cmd và thực hiện lệnh ping
for i in range(number_of_cmds):
    open_cmd_and_ping(ip_address)
    time.sleep(0.1)  # Thời gian chờ ngắn giữa các lần mở để tránh quá tải hệ thống
