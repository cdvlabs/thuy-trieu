import pdfplumber
import json
import glob
import re
import requests
import os
from datetime import datetime, timedelta

def download_pdf(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            with open(filename, 'wb') as f: f.write(response.content)
            return True
        return False
    except: return False

def parse_tide_pdf(pdf_path):
    data = {}
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = pdf.pages[0].extract_text()
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
    except: pass
    return data

def main():
    all_data = {}
    now = datetime.now()
    
    print("--- BẮT ĐẦU QUY TRÌNH TỰ ĐỘNG ---")
    
    # 1. Tự động tải dữ liệu mới nhất (3 ngày gần đây)
    for i in range(3):
        target = now - timedelta(days=i)
        y, m, d = target.strftime("%Y"), target.strftime("%m"), target.strftime("%d")
        url = f"https://www.phongchonglutbaotphcm.gov.vn/phocadownload/{y}/{m}-{y}/HCMC_TVHN_{y}{m}{d}.pdf"
        filename = f"HCMC_TVHN_{y}{m}{d}.pdf"
        if download_pdf(url, filename):
            print(f"Tải thành công: {filename}")
        else:
            print(f"Bỏ qua (không tìm thấy): {url}")

    # 2. Quét tất cả file PDF và sắp xếp theo thứ tự thời gian (ngày tăng dần)
    pdf_files = sorted(glob.glob("HCMC_TVHN_*.pdf"))
    
    for pdf in pdf_files:
        print(f"Đang bóc tách dữ liệu: {pdf}")
        pdf_data = parse_tide_pdf(pdf)
        for station, dates in pdf_data.items():
            if station not in all_data: all_data[station] = {}
            # Dữ liệu từ file mới nhất (vòng lặp sau) sẽ ghi đè lên dữ liệu cũ
            all_data[station].update(dates)

    # 3. Ghi vào file JSON
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    
    print(f"HOÀN TẤT! Đã cập nhật {len(all_data)} trạm thủy văn vào data.json.")

if __name__ == "__main__":
    main()
