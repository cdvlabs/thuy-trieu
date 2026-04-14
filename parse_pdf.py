import pdfplumber
import json
import glob
import re
import os

def parse_tide_pdf(pdf_path):
    data = {}
    try:
        with pdfplumber.open(pdf_path) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()
            lines = text.split('\n')
            
            current_station = None
            for line in lines:
                if "Phú An" in line: current_station = "Phú An"
                elif "Nhà Bè" in line: current_station = "Nhà Bè"
                elif "Thủ Dầu Một" in line: current_station = "Thủ Dầu Một"
                
                match = re.search(r'^(\d{2}/\d{2})\s+(.*)', line)
                if match and current_station:
                    day = match.group(1)
                    parts = re.findall(r'(-?\d+\.\d+)', match.group(2))
                    if len(parts) >= 4:
                        if current_station not in data: data[current_station] = {}
                        heights, times = [], []
                        for i in range(0, len(parts)-1, 2):
                            try:
                                h = float(parts[i])
                                t = parts[i+1].replace('.', ':')
                                if len(t.split(':')[0]) == 1: t = "0" + t
                                heights.append(h)
                                times.append(t)
                            except: continue
                        data[current_station][day] = {"h": heights, "t": times}
    except Exception as e: print(f"Lỗi {pdf_path}: {e}")
    return data

def main():
    all_data = {}
    # Lấy danh sách file PDF và SẮP XẾP theo tên (ngày tăng dần)
    # File HCMC_TVHN_20260414.pdf sẽ đứng sau 20260413.pdf
    pdf_files = sorted(glob.glob("HCMC_TVHN_*.pdf"))
    
    print(f"Tìm thấy {len(pdf_files)} file PDF. Bắt đầu xử lý...")
    
    for pdf in pdf_files:
        print(f"Đang bóc tách: {pdf}")
        pdf_data = parse_tide_pdf(pdf)
        for station, dates in pdf_data.items():
            if station not in all_data: all_data[station] = {}
            # Khi update, dữ liệu từ file mới (đứng sau) sẽ ghi đè lên dữ liệu cũ
            all_data[station].update(dates)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    print("Hoàn tất! Dữ liệu mới nhất đã được ưu tiên.")

if __name__ == "__main__":
    main()
