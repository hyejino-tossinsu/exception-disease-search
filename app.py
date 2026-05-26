"""
예외질환 검색 사이트 - 로컬 Flask 서버
실행: python app.py  (또는 실행.bat 더블클릭)
주소: http://localhost:5000
"""
import os, re, threading, time, webbrowser
from pathlib import Path
from flask import Flask, send_file, jsonify, request

app = Flask(__name__)
BASE_DIR = Path(__file__).parent.resolve()
ALLOWED = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}

def parse_filename(filename):
    name = Path(filename).stem
    company_match = re.match(r'^\[+([^\]]+)\]', name)
    company = company_match.group(1).strip() if company_match else "기타"

    date_match = re.search(r'(\d{2})\.(\d{1,2})(?:\.(\d{1,2}))?(?:\([^)]*\))?\s*~', name)
    if date_match:
        year  = 2000 + int(date_match.group(1))
        month = int(date_match.group(2))
        day   = int(date_match.group(3)) if date_match.group(3) else None
        date_str  = f"{year}.{month:02d}" + (f".{day:02d}" if day else "")
        sort_date = f"{year}{month:02d}" + (f"{day:02d}" if day else "00")
    else:
        date_str = "날짜 미상"
        sort_date = "00000000"

    count_match = re.search(r'([\d,]+)\s*개(?!월)', name)
    count = int(count_match.group(1).replace(',', '')) if count_match else None

    if '유병력자실비' in name:
        product_type = '유병력자실비'
    elif '간편보험' in name or re.search(r'간편\s', name):
        product_type = '간편보험'
    else:
        product_type = '기타'

    if '즉시인수' in name:
        wait_period = '즉시인수'
    elif '7일' in name:
        wait_period = '7일 경과'
    elif '3개월' in name:
        wait_period = '3개월 경과'
    elif '1개월' in name:
        wait_period = '1개월 경과'
    elif '2년' in name:
        wait_period = '2년 이내'
    else:
        wait_period = '-'

    page_match = re.search(r'\((\d+)\)\s*$', name)
    page_num = int(page_match.group(1)) if page_match else 1

    desc = re.sub(r'^\[+[^\]]+\]\s*', '', name)
    desc = re.sub(r'\s*\(\d+\)\s*$', '', desc).strip()

    base = re.sub(r'\s*\(\d+\)\s*$', '', name).strip()
    group_key = f"{company}||{date_str}||{base}"

    return {
        'filename': filename, 'company': company, 'date': date_str,
        'sort_date': sort_date, 'product_type': product_type,
        'wait_period': wait_period, 'count': count,
        'description': desc, 'page': page_num, 'group_key': group_key,
    }

def get_all_documents():
    files = []
    for ext in ALLOWED:
        files += list(BASE_DIR.glob(f'*{ext}'))
        files += list(BASE_DIR.glob(f'*{ext.upper()}'))
    files.sort(key=lambda x: x.name)

    groups = {}
    for f in files:
        doc = parse_filename(f.name)
        key = doc['group_key']
        if key not in groups:
            groups[key] = {
                'id': key, 'company': doc['company'], 'date': doc['date'],
                'sort_date': doc['sort_date'], 'product_type': doc['product_type'],
                'wait_period': doc['wait_period'], 'count': doc['count'],
                'description': doc['description'], 'pages': [],
            }
        groups[key]['pages'].append({'page': doc['page'], 'filename': doc['filename']})

    for g in groups.values():
        g['pages'].sort(key=lambda x: x['page'])
        g['page_count'] = len(g['pages'])

    result = list(groups.values())
    result.sort(key=lambda x: x['sort_date'], reverse=True)
    return result

@app.route('/')
def index():
    return send_file(BASE_DIR / 'index.html')

@app.route('/api/documents')
def api_documents():
    return jsonify(get_all_documents())

@app.route('/images/<path:filename>')
def serve_image(filename):
    path = BASE_DIR / filename
    if path.exists() and path.suffix.lower() in ALLOWED:
        return send_file(path)
    return jsonify({'error': 'not found'}), 404

@app.route('/api/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return jsonify({'error': '파일이 없습니다'}), 400
    uploaded, errors = [], []
    for file in request.files.getlist('files'):
        if not file.filename:
            continue
        ext = Path(file.filename).suffix.lower()
        if ext not in ALLOWED:
            errors.append(f'{file.filename}: 지원하지 않는 형식')
            continue
        file.save(BASE_DIR / file.filename)
        meta = parse_filename(file.filename)
        uploaded.append({'filename': file.filename, 'company': meta['company'], 'date': meta['date']})
    return jsonify({'uploaded': uploaded, 'errors': errors, 'total': len(uploaded)})

def open_browser():
    time.sleep(1.2)
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    print("=" * 50)
    print("  예외질환 검색 사이트 시작!")
    print("  http://localhost:5000")
    print("  종료: Ctrl+C 또는 창 닫기")
    print("=" * 50)
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=False)
