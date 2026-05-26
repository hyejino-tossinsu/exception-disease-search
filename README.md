[index.html](https://github.com/user-attachments/files/28259267/index.html)
# exception-disease-search
[tossinsu] 상품팀 예외질환 검색
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>예외질환 검색 사이트</title>
<style>
:root{--p:#4F46E5;--pl:#EEF2FF;--bg:#F5F6FA;--w:#fff;--bd:#E5E7EB;--tx:#111827;--sub:#6B7280;--r:12px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Apple SD Gothic Neo','Malgun Gothic',sans-serif;background:var(--bg);color:var(--tx);font-size:14px}
.top{position:sticky;top:0;z-index:100;background:var(--w);border-bottom:1px solid var(--bd);padding:10px 18px;display:flex;align-items:center;gap:10px;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.logo{font-size:16px;font-weight:700;color:var(--p);white-space:nowrap}
.sw{flex:1;position:relative;max-width:460px}
.sw input{width:100%;padding:8px 14px 8px 36px;border:1.5px solid var(--bd);border-radius:8px;font-size:14px;outline:none;transition:border .2s}
.sw input:focus{border-color:var(--p)}
.sw svg{position:absolute;left:10px;top:50%;transform:translateY(-50%);color:var(--sub);pointer-events:none}
.tr{margin-left:auto;display:flex;align-items:center;gap:8px}
.rc{color:var(--sub);font-size:13px;white-space:nowrap}
.ss{padding:7px 9px;border:1.5px solid var(--bd);border-radius:8px;font-size:13px;background:var(--w);cursor:pointer;outline:none}
.bu{padding:7px 14px;background:var(--p);color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer}.bu:hover{background:#4338CA}
.lay{display:flex;min-height:calc(100vh - 53px)}
.sb{width:210px;flex-shrink:0;background:var(--w);border-right:1px solid var(--bd);padding:14px 12px;overflow-y:auto;position:sticky;top:53px;height:calc(100vh - 53px)}
.sb h3{font-size:11px;font-weight:700;letter-spacing:.06em;color:var(--sub);text-transform:uppercase;margin:14px 0 8px}.sb h3:first-child{margin-top:0}
.fg{display:flex;flex-direction:column;gap:4px}
.fi{display:flex;align-items:center;gap:6px;cursor:pointer}
.fi input{width:14px;height:14px;cursor:pointer;accent-color:var(--p)}
.fi label{cursor:pointer;font-size:13px;flex:1}
.fc{font-size:11px;color:var(--sub);margin-left:auto}
.fdiv{height:1px;background:var(--bd);margin:12px 0}
.breset{width:100%;padding:6px;border:1.5px solid var(--bd);border-radius:7px;font-size:12px;color:var(--sub);background:var(--w);cursor:pointer;margin-top:10px}.breset:hover{border-color:var(--p);color:var(--p)}
.mn{flex:1;padding:18px;overflow-y:auto}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:14px}
.card{background:var(--w);border-radius:var(--r);border:1px solid var(--bd);padding:14px;cursor:pointer;transition:box-shadow .18s,transform .18s;display:flex;flex-direction:column;gap:9px}
.card:hover{box-shadow:0 4px 16px rgba(0,0,0,.13);transform:translateY(-2px)}
.ch{display:flex;align-items:flex-start;justify-content:space-between;gap:8px}
.cn{font-size:15px;font-weight:700}
.db{font-size:11px;font-weight:600;padding:3px 8px;border-radius:20px;white-space:nowrap;flex-shrink:0;background:var(--pl);color:var(--p)}
.cd{font-size:13px;color:var(--sub);line-height:1.55}
.ct{display:flex;flex-wrap:wrap;gap:5px;margin-top:2px}
.tag{font-size:11px;padding:3px 8px;border-radius:20px;font-weight:500}
.tp{background:#F0FDF4;color:#16A34A}.tw{background:#FFF7ED;color:#C2410C}.ti{background:var(--pl);color:var(--p)}.tk{background:#F9FAFB;color:#374151;border:1px solid var(--bd)}
.cf2{display:flex;align-items:center;justify-content:space-between;margin-top:2px}
.vb{font-size:12px;color:var(--p);font-weight:600}
.mhint{font-size:11px;background:#FEF9C3;color:#78350F;padding:3px 8px;border-radius:8px;font-weight:500;border:1px solid #FDE68A}
.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:80px 20px;color:var(--sub);gap:10px}
.mo{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:1000;align-items:center;justify-content:center}.mo.open{display:flex}
.md{background:var(--w);border-radius:16px;width:min(92vw,900px);max-height:93vh;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.3)}
.mh{padding:14px 18px;border-bottom:1px solid var(--bd);display:flex;align-items:flex-start;gap:10px}
.mt{font-size:15px;font-weight:700;flex:1}.mm{display:flex;gap:6px;flex-wrap:wrap;margin-top:4px}
.mc{width:30px;height:30px;border-radius:8px;border:none;background:#F3F4F6;cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;flex-shrink:0}.mc:hover{background:#E5E7EB}
.kw-banner{display:none;padding:10px 18px;background:#FFFBEB;border-bottom:2px solid #FDE68A;gap:8px;align-items:flex-start;flex-wrap:wrap}
.kw-banner.show{display:flex}
.kw-label{font-size:12px;font-weight:700;color:#92400E;white-space:nowrap;margin-top:2px}
.kw-chips{display:flex;flex-wrap:wrap;gap:6px}
.kw-chip{font-size:12px;font-weight:700;background:#FEF08A;color:#713F12;padding:3px 10px;border-radius:20px;border:1.5px solid #FDE047}
.mb{flex:1;overflow-y:auto;padding:14px 18px;text-align:center}
.mb img{max-width:100%;border-radius:8px;cursor:zoom-in;transition:transform .2s}.mb img.zoomed{max-width:none;width:150%;cursor:zoom-out}
.mn2{padding:10px 18px;border-top:1px solid var(--bd);display:flex;align-items:center;justify-content:center;gap:14px}
.nb{padding:7px 18px;border:1.5px solid var(--bd);border-radius:8px;background:var(--w);cursor:pointer;font-size:13px;font-weight:600;transition:all .15s;color:var(--tx)}.nb:hover:not(:disabled){border-color:var(--p);color:var(--p)}.nb:disabled{opacity:.4;cursor:default}
.pi{font-size:14px;font-weight:600;color:var(--sub);min-width:54px;text-align:center}
.uo{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:1001;align-items:center;justify-content:center}.uo.open{display:flex}
.um{background:var(--w);border-radius:16px;width:min(92vw,480px);padding:24px;display:flex;flex-direction:column;gap:16px;box-shadow:0 20px 60px rgba(0,0,0,.3)}
.um h2{font-size:17px;font-weight:700}
.ua{border:2px dashed var(--bd);border-radius:12px;padding:36px 16px;text-align:center;cursor:pointer;transition:all .2s;color:var(--sub)}.ua:hover,.ua.drag{border-color:var(--p);background:var(--pl);color:var(--p)}.ua input{display:none}.ua .ui{font-size:32px;margin-bottom:8px}
.ul2{display:flex;flex-direction:column;gap:5px;max-height:160px;overflow-y:auto}
.uitm{display:flex;align-items:center;gap:8px;padding:7px 10px;background:#F9FAFB;border-radius:8px;font-size:13px}
.un{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ua2{display:flex;gap:8px}
.bcan{flex:1;padding:9px;border:1.5px solid var(--bd);border-radius:8px;font-size:14px;background:var(--w);cursor:pointer}
.bup{flex:2;padding:9px;background:var(--p);color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer}.bup:hover{background:#4338CA}.bup:disabled{background:#9CA3AF;cursor:default}
.umsg{font-size:13px;color:var(--p);text-align:center;font-weight:600}
@media(max-width:680px){.sb{display:none}.cards{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="top">
  <div class="logo">&#x1F3E5; 예외질환 검색</div>
  <div class="sw">
    <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input type="text" id="SI" placeholder="질환명 검색 (예: 용종, 갑상선, 디스크...)" autocomplete="off">
  </div>
  <div class="tr">
    <span class="rc" id="RC"></span>
    <select class="ss" id="SO">
      <option value="date_desc">최신순</option>
      <option value="date_asc">오래된순</option>
      <option value="company">보험사명순</option>
      <option value="count_desc">예외질환 개수순</option>
    </select>
    <button class="bu" onclick="openU()">+ 파일 추가</button>
  </div>
</div>
<div class="lay">
  <aside class="sb">
    <h3>보험사</h3><div class="fg" id="CF"></div>
    <div class="fdiv"></div>
    <h3>상품 유형</h3><div class="fg" id="TF"></div>
    <div class="fdiv"></div>
    <h3>경과 기간</h3><div class="fg" id="WF"></div>
    <button class="breset" onclick="resetF()">&#10005; 필터 초기화</button>
  </aside>
  <main class="mn"><div id="CO"></div></main>
</div>
<div class="mo" id="IM" onclick="closeMob(event)">
  <div class="md">
    <div class="mh">
      <div style="flex:1"><div class="mt" id="MTT"></div><div class="mm" id="MMT"></div></div>
      <button class="mc" onclick="closeM()">&#10005;</button>
    </div>
    <div class="kw-banner" id="KWB">
      <span class="kw-label">&#x1F50D; 이미지 내 검색어:</span>
      <div class="kw-chips" id="KWC"></div>
    </div>
    <div class="mb">
      <img id="MIG" src="" alt="" onclick="toggleZoom(this)" style="display:none">
      <div id="MTBL" style="display:none;width:100%;overflow:auto;text-align:left"></div>
    </div>
    <div class="mn2" id="MNV">
      <button class="nb" id="BP" onclick="chPg(-1)">&#9664; 이전</button>
      <span class="pi" id="PIG"></span>
      <button class="nb" id="BN" onclick="chPg(1)">다음 &#9654;</button>
    </div>
  </div>
</div>
<div class="uo" id="UO" onclick="closeUob(event)">
  <div class="um">
    <h2>&#x1F4E4; 파일 추가 (이번 세션에만 유효)</h2>
    <div class="ua" id="UA" onclick="document.getElementById('FI').click()"
         ondragover="dov(event)" ondragleave="dlv()" ondrop="drp(event)">
      <input type="file" id="FI" accept="image/*,.pdf,.xlsx,.xls,.csv" multiple onchange="selF(event)">
      <div class="ui">&#x1F4C2;</div>
      <p>클릭하거나 파일을 드래그하세요<br><small>JPG, PNG, PDF, Excel, CSV 지원</small></p>
    </div>
    <div class="ul2" id="UL"></div>
    <div class="umsg" id="UMG" style="display:none"></div>
    <div class="ua2">
      <button class="bcan" onclick="closeU()">취소</button>
      <button class="bup" id="BUP" onclick="doU()" disabled>추가하기</button>
    </div>
  </div>
</div>
<script>
let allDocs=[{"filename": "[흥국생명] 26.4.20~ 간편 입원,수술 일수 축소 예외질환.jpg", "company": "흥국생명", "date": "2026.04.20", "sort_date": "20260420", "product_type": "간편보험", "wait_period": "-", "count": null, "description": "26.4.20~ 간편 입원,수술 일수 축소 예외질환", "page": 1, "group_key": "흥국생명||2026.04.20||[흥국생명] 26.4.20~ 간편 입원,수술 일수 축소 예외질환", "pages": [{"page": 1, "filename": "[흥국생명] 26.4.20~ 간편 입원,수술 일수 축소 예외질환.jpg", "src": "%5B%ED%9D%A5%EA%B5%AD%EC%83%9D%EB%AA%85%5D%2026.4.20~%20%EA%B0%84%ED%8E%B8%20%EC%9E%85%EC%9B%90%2C%EC%88%98%EC%88%A0%20%EC%9D%BC%EC%88%98%20%EC%B6%95%EC%86%8C%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98.jpg", "content_type": "image"}], "text": "고혈압 본태성 원발성 당뇨병 고지혈증 어지럼증 갑상선결절 양성유방형성이상 난소양성신생물 장질환 노년백내장 노안 노안수술 결막의기타장애 코비동장애 여성생식관폴립 신장요관결석 추간판장애 디스크 위십이지장기타질환 유방양성신생물 양성지방종 지방종 안면신경마비 패혈증 대상포진 A형간염 호흡곤란 염좌 다발성염좌", "page_count": 1}, {"filename": "[KB라이프생명] 26.3.11~ 간편보험 예외질환경과기간 및 수술횟수 완화.jpg", "company": "KB라이프생명", "date": "2026.03.11", "sort_date": "20260311", "product_type": "간편보험", "wait_period": "-", "count": null, "description": "26.3.11~ 간편보험 예외질환경과기간 및 수술횟수 완화", "page": 1, "group_key": "KB라이프생명||2026.03.11||[KB라이프생명] 26.3.11~ 간편보험 예외질환경과기간 및 수술횟수 완화", "pages": [{"page": 1, "filename": "[KB라이프생명] 26.3.11~ 간편보험 예외질환경과기간 및 수술횟수 완화.jpg", "src": "%5BKB%EB%9D%BC%EC%9D%B4%ED%94%84%EC%83%9D%EB%AA%85%5D%2026.3.11~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%EA%B2%BD%EA%B3%BC%EA%B8%B0%EA%B0%84%20%EB%B0%8F%20%EC%88%98%EC%88%A0%ED%9A%9F%EC%88%98%20%EC%99%84%ED%99%94.jpg", "content_type": "image"}], "text": "피부망성지방증 위염 치핵 치루 피부염 치조골수술 제왕절개 경과기간완화 수술횟수완화", "page_count": 1}, {"filename": "[메리츠화재] 26.3~ 간편보험 예외질환 3대진단(7일 후 즉시인수).jpg", "company": "메리츠화재", "date": "2026.03", "sort_date": "20260300", "product_type": "간편보험", "wait_period": "즉시인수", "count": null, "description": "26.3~ 간편보험 예외질환 3대진단(7일 후 즉시인수)", "page": 1, "group_key": "메리츠화재||2026.03||[메리츠화재] 26.3~ 간편보험 예외질환 3대진단(7일 후 즉시인수)", "pages": [{"page": 1, "filename": "[메리츠화재] 26.3~ 간편보험 예외질환 3대진단(7일 후 즉시인수).jpg", "src": "%5B%EB%A9%94%EB%A6%AC%EC%B8%A0%ED%99%94%EC%9E%AC%5D%2026.3~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%203%EB%8C%80%EC%A7%84%EB%8B%A8%287%EC%9D%BC%20%ED%9B%84%20%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%29.jpg", "content_type": "image"}], "text": "코로나19 근골격계 어깨병변 추간판장애 디스크 척추만곡 무릎질환 골관절염 상기도감염 인후두 급성기관지염 폐렴 인플루엔자 독감 이하선염 볼거리 급성위염 식도위궤양 자극성장증후군 장염 식중독 게실질환 자궁경부 무월경 골반염증 난관염 난소염 갱년기 폐경 각막염 결막염 외이염 이석증 전정신경세포염 메니에르 미로염 코피 봉소염 아토피 지루피부병 두드러기 탈모 백반증 림프절염 수막염 수두 대상포진 단순포진 갑상선염 두통 삼차신경통 성홍열 살모넬라 콜레라 발진타이푸스 쯔쯔가무시 수족구 이질 방아쇠수지 회전근개 족저근막염 요실금 전립선 자궁 난소 대장용종 치과 치주질환 임플란트 암뇌심즉시인수 3대진단", "page_count": 1}, {"filename": "[메리츠화재] 26.3~ 간편보험 예외질환 기본플랜(7일 후 즉시인수).jpg", "company": "메리츠화재", "date": "2026.03", "sort_date": "20260300", "product_type": "간편보험", "wait_period": "즉시인수", "count": null, "description": "26.3~ 간편보험 예외질환 기본플랜(7일 후 즉시인수)", "page": 1, "group_key": "메리츠화재||2026.03||[메리츠화재] 26.3~ 간편보험 예외질환 기본플랜(7일 후 즉시인수)", "pages": [{"page": 1, "filename": "[메리츠화재] 26.3~ 간편보험 예외질환 기본플랜(7일 후 즉시인수).jpg", "src": "%5B%EB%A9%94%EB%A6%AC%EC%B8%A0%ED%99%94%EC%9E%AC%5D%2026.3~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20%EA%B8%B0%EB%B3%B8%ED%94%8C%EB%9E%9C%287%EC%9D%BC%20%ED%9B%84%20%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%29.jpg", "content_type": "image"}], "text": "코로나19 근골격계 어깨병변 추간판장애 디스크 척추만곡 무릎질환 골관절염 상기도감염 인후두 급성기관지염 폐렴 인플루엔자 독감 이하선염 볼거리 급성위염 식도위궤양 자극성장증후군 장염 식중독 게실질환 골반염증 난관염 난소염 갱년기 폐경 각막염 결막염 이석증 전정신경세포염 메니에르 아토피 지루피부병 두드러기 탈모 백반증 림프절염 수막염 수두 대상포진 단순포진 갑상선염 두통 삼차신경통 성홍열 살모넬라 콜레라 발진타이푸스 쯔쯔가무시 수족구 이질 방아쇠수지 회전근개 족저근막염 요실금 전립선 자궁 난소 대장용종 치과", "page_count": 1}, {"filename": "[메리츠화재] 26.3~ 간편보험 예외질환 어무디플랜(7일 후 즉시인수).jpg", "company": "메리츠화재", "date": "2026.03", "sort_date": "20260300", "product_type": "간편보험", "wait_period": "즉시인수", "count": null, "description": "26.3~ 간편보험 예외질환 어무디플랜(7일 후 즉시인수)", "page": 1, "group_key": "메리츠화재||2026.03||[메리츠화재] 26.3~ 간편보험 예외질환 어무디플랜(7일 후 즉시인수)", "pages": [{"page": 1, "filename": "[메리츠화재] 26.3~ 간편보험 예외질환 어무디플랜(7일 후 즉시인수).jpg", "src": "%5B%EB%A9%94%EB%A6%AC%EC%B8%A0%ED%99%94%EC%9E%AC%5D%2026.3~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20%EC%96%B4%EB%AC%B4%EB%94%94%ED%94%8C%EB%9E%9C%287%EC%9D%BC%20%ED%9B%84%20%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%29.jpg", "content_type": "image"}], "text": "코로나19 근골격계 어깨병변 추간판장애 디스크 척추만곡 무릎질환 골관절염 상기도감염 인후두 급성기관지염 폐렴 인플루엔자 독감 이하선염 볼거리 급성위염 식도위궤양 자극성장증후군 장염 식중독 게실질환 골반염증 난관염 난소염 갱년기 폐경 각막염 결막염 이석증 전정신경세포염 메니에르 아토피 지루피부병 두드러기 탈모 백반증 림프절염 수막염 수두 대상포진 단순포진 갑상선염 두통 삼차신경통 성홍열 살모넬라 콜레라 발진타이푸스 쯔쯔가무시 수족구 이질 방아쇠수지 회전근개 족저근막염 요실금 전립선 자궁 난소 대장용종 치과 자궁내막종 난소낭종절제", "page_count": 1}, {"filename": "[메리츠화재] 26.3~ 유병력자실비 예외질환(3개월~).jpg", "company": "메리츠화재", "date": "2026.03", "sort_date": "20260300", "product_type": "유병력자실비", "wait_period": "3개월 경과", "count": null, "description": "26.3~ 유병력자실비 예외질환(3개월~)", "page": 1, "group_key": "메리츠화재||2026.03||[메리츠화재] 26.3~ 유병력자실비 예외질환(3개월~)", "pages": [{"page": 1, "filename": "[메리츠화재] 26.3~ 유병력자실비 예외질환(3개월~).jpg", "src": "%5B%EB%A9%94%EB%A6%AC%EC%B8%A0%ED%99%94%EC%9E%AC%5D%2026.3~%20%EC%9C%A0%EB%B3%91%EB%A0%A5%EC%9E%90%EC%8B%A4%EB%B9%84%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%283%EA%B0%9C%EC%9B%94~%29.jpg", "content_type": "image"}], "text": "코로나19 각막염 결막염 외이염 코피 봉소염 아토피 지루피부병 두드러기 자궁경부 무월경 골반염증 난관염 난소염 갱년기 폐경 상기도감염 인후두 급성기관지염 폐렴 인플루엔자 독감 이하선염 볼거리 림프절염 수막염 수두 콜레라 살모넬라 성홍열 쯔쯔가무시 수족구 대상포진 단순포진 두통 삼차신경통 발진타이푸스 이질 갑상선염 갑상선기능저하 갑상선기능항진 임신출산 백내장 사시 익상편 비염 부비동염 비중격만곡증 이석증 전정신경세포염 메니에르 화상 골절 타박상 표재성손상 요실금 전립선 자궁근종 난소낭종 대장용종 담낭용종 담석증 탈장 탈구 치핵 치질 임플란트 치주질환 치조골수술", "page_count": 1}, {"filename": "[KB라이프생명] 26.2.9~ 간편보험 예외질환 7,402개로 확대(즉시인수 가능).jpg", "company": "KB라이프생명", "date": "2026.02.09", "sort_date": "20260209", "product_type": "간편보험", "wait_period": "즉시인수", "count": 7402, "description": "26.2.9~ 간편보험 예외질환 7,402개로 확대(즉시인수 가능)", "page": 1, "group_key": "KB라이프생명||2026.02.09||[KB라이프생명] 26.2.9~ 간편보험 예외질환 7,402개로 확대(즉시인수 가능)", "pages": [{"page": 1, "filename": "[KB라이프생명] 26.2.9~ 간편보험 예외질환 7,402개로 확대(즉시인수 가능).jpg", "src": "%5BKB%EB%9D%BC%EC%9D%B4%ED%94%84%EC%83%9D%EB%AA%85%5D%2026.2.9~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%207%2C402%EA%B0%9C%EB%A1%9C%20%ED%99%95%EB%8C%80%28%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%20%EA%B0%80%EB%8A%A5%29.jpg", "content_type": "image"}], "text": "대장용종 직장용종 소화기계양성신생물 유방양성신생물 난소신생물 전립선양성신생물 단순낭종 바이러스 수막염 A형간염 헬리코박터 각막염 골절 연조직손상 수두 결막 백내장 녹내장 맥락막장애 시신경염 편도염 폐렴 후두염 천식 급성비염 감기 급성부비동염 급성편도염 인플루엔자 편도비대 위식도역류병 과민대장증후군 두드러기 아토피 자궁근종 난소낭종 지방종 담낭용종 이석증 어지럼증 사시 라식 라섹 다래끼 요로결석 신요관결석 요실금 전립선비대증 치핵 치질 척추측만증 경추관절증 추간판장애 무릎관절증 힘줄파열 유산 임신 제왕절개 산후기", "page_count": 1}, {"filename": "[현대해상] 26.1.17~ 간편보험 즉시인수 추가(총 123개).jpg", "company": "현대해상", "date": "2026.01.17", "sort_date": "20260117", "product_type": "간편보험", "wait_period": "즉시인수", "count": 123, "description": "26.1.17~ 간편보험 즉시인수 추가(총 123개)", "page": 1, "group_key": "현대해상||2026.01.17||[현대해상] 26.1.17~ 간편보험 즉시인수 추가(총 123개)", "pages": [{"page": 1, "filename": "[현대해상] 26.1.17~ 간편보험 즉시인수 추가(총 123개).jpg", "src": "%5B%ED%98%84%EB%8C%80%ED%95%B4%EC%83%81%5D%2026.1.17~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%20%EC%B6%94%EA%B0%80%28%EC%B4%9D%20123%EA%B0%9C%29.jpg", "content_type": "image"}], "text": "백내장 양안수술 디스크 추간판장애 염좌 어깨병변 회전근개증후군 회전근개파열 어깨위팔근육힘줄손상 열린상처 교상 열상 천자 요관결석 신요결석 쇄석술 신장결석 무릎내부장애 반달연골장애 무릎인대자연파열 식도염 위식도역류병 위염 십이지장염 팔골절", "page_count": 1}, {"filename": "[삼성생명] 26.1.14(수)~ 간편보험 대장용종 2년내 예외질환 질병입원수술비류 거절 추가.jpg", "company": "삼성생명", "date": "2026.01.14", "sort_date": "20260114", "product_type": "간편보험", "wait_period": "2년 이내", "count": null, "description": "26.1.14(수)~ 간편보험 대장용종 2년내 예외질환 질병입원수술비류 거절 추가", "page": 1, "group_key": "삼성생명||2026.01.14||[삼성생명] 26.1.14(수)~ 간편보험 대장용종 2년내 예외질환 질병입원수술비류 거절 추가", "pages": [{"page": 1, "filename": "[삼성생명] 26.1.14(수)~ 간편보험 대장용종 2년내 예외질환 질병입원수술비류 거절 추가.jpg", "src": "%5B%EC%82%BC%EC%84%B1%EC%83%9D%EB%AA%85%5D%2026.1.14%28%EC%88%98%29~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EB%8C%80%EC%9E%A5%EC%9A%A9%EC%A2%85%202%EB%85%84%EB%82%B4%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20%EC%A7%88%EB%B3%91%EC%9E%85%EC%9B%90%EC%88%98%EC%88%A0%EB%B9%84%EB%A5%98%20%EA%B1%B0%EC%A0%88%20%EC%B6%94%EA%B0%80.jpg", "content_type": "image"}], "text": "대장용종 대장폴립 2년내 입원수술 기왕력자 가입불가 거절 질병입원수술비 파워수술 질병재해수술 통합양성신생물수술 153대수술", "page_count": 1}, {"filename": "[[삼성화재] 26.1~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고.jpg", "company": "삼성화재", "date": "2026.01", "sort_date": "20260100", "product_type": "간편보험", "wait_period": "-", "count": null, "description": "26.1~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고", "page": 1, "group_key": "삼성화재||2026.01||[[삼성화재] 26.1~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고", "pages": [{"page": 1, "filename": "[[삼성화재] 26.1~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고.jpg", "src": "%5B%5B%EC%82%BC%EC%84%B1%ED%99%94%EC%9E%AC%5D%2026.1~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%205%EB%85%84%20%EC%A7%88%EB%AC%B8%EC%84%9C%20%EC%A4%91%EB%8C%80%EC%A7%88%ED%99%98%20%ED%95%B4%EB%8B%B9%20%EC%A7%88%ED%99%98%20%EC%BD%94%EB%93%9C%20%EC%B0%B8%EA%B3%A0.jpg", "content_type": "image"}], "text": "입술구강인두악성신생물 소화기관악성신생물 호흡기흉곽내기관악성신생물 골관절연골악성신생물 흑색종피부악성신생물 중피성연조직악성신생물 유방악성신생물 여성생식기관악성신생물 남성생식기관악성신생물 요로악성신생물 뇌중추신경계악성신생물 갑상선내분비선악성신생물 림프조혈관련조직악성신생물 협심증 급성심근경색증 심근경색 지주막하출혈 뇌내출혈 뇌경색증 뇌졸중 간섬유증 간경화증 알콜성간경변 심장판막증 승모판장애 대동맥판장애 삼첨판장애 다판막질환 인공심장판막 암 뇌 심장 중대질환 5년질문서", "page_count": 1}, {"filename": "[메리츠화재] 25.9.23~ 간편보험 예외질환 확대(장폐색,혈관종,메니에르,게실염 등).jpg", "company": "메리츠화재", "date": "2025.09.23", "sort_date": "20250923", "product_type": "간편보험", "wait_period": "-", "count": null, "description": "25.9.23~ 간편보험 예외질환 확대(장폐색,혈관종,메니에르,게실염 등)", "page": 1, "group_key": "메리츠화재||2025.09.23||[메리츠화재] 25.9.23~ 간편보험 예외질환 확대(장폐색,혈관종,메니에르,게실염 등)", "pages": [{"page": 1, "filename": "[메리츠화재] 25.9.23~ 간편보험 예외질환 확대(장폐색,혈관종,메니에르,게실염 등).jpg", "src": "%5B%EB%A9%94%EB%A6%AC%EC%B8%A0%ED%99%94%EC%9E%AC%5D%2025.9.23~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20%ED%99%95%EB%8C%80%28%EC%9E%A5%ED%8F%90%EC%83%89%2C%ED%98%88%EA%B4%80%EC%A2%85%2C%EB%A9%94%EB%8B%88%EC%97%90%EB%A5%B4%2C%EA%B2%8C%EC%8B%A4%EC%97%BC%20%EB%93%B1%29.jpg", "content_type": "image"}], "text": "침샘양성종양수술 장기기증자수술 혈관종수술 결핵 헬리코박터 장폐색 백선증 태선 유돌염 고막염 단핵구증 구내염 패혈증 코로나19 메니에르 전정신경세포염 소화기게실질환 게실염 익상편 추간판장애 디스크", "page_count": 1}, {"filename": "[롯데손보] 25.8.20~ 간편보험 3개월내 질병확정진단 완치 예외질환 가능.jpg", "company": "롯데손보", "date": "2025.08.20", "sort_date": "20250820", "product_type": "간편보험", "wait_period": "3개월 경과", "count": null, "description": "25.8.20~ 간편보험 3개월내 질병확정진단 완치 예외질환 가능", "page": 1, "group_key": "롯데손보||2025.08.20||[롯데손보] 25.8.20~ 간편보험 3개월내 질병확정진단 완치 예외질환 가능", "pages": [{"page": 1, "filename": "[롯데손보] 25.8.20~ 간편보험 3개월내 질병확정진단 완치 예외질환 가능.jpg", "src": "%5B%EB%A1%AF%EB%8D%B0%EC%86%90%EB%B3%B4%5D%2025.8.20~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%203%EA%B0%9C%EC%9B%94%EB%82%B4%20%EC%A7%88%EB%B3%91%ED%99%95%EC%A0%95%EC%A7%84%EB%8B%A8%20%EC%99%84%EC%B9%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20%EA%B0%80%EB%8A%A5.jpg", "content_type": "image"}], "text": "어깨병변 완치 3개월내 통원치료 근골격계질환 골절 완치후인수 단기입원완치", "page_count": 1}, {"filename": "[메리츠화재] 25.7.25~ 간편보험 예외질환 즉시인수 시행(암뇌심 관련만) 그 외 기존과 동일하게 7일후.jpg", "company": "메리츠화재", "date": "2025.07.25", "sort_date": "20250725", "product_type": "간편보험", "wait_period": "즉시인수", "count": null, "description": "25.7.25~ 간편보험 예외질환 즉시인수 시행(암뇌심 관련만) 그 외 기존과 동일하게 7일후", "page": 1, "group_key": "메리츠화재||2025.07.25||[메리츠화재] 25.7.25~ 간편보험 예외질환 즉시인수 시행(암뇌심 관련만) 그 외 기존과 동일하게 7일후", "pages": [{"page": 1, "filename": "[메리츠화재] 25.7.25~ 간편보험 예외질환 즉시인수 시행(암뇌심 관련만) 그 외 기존과 동일하게 7일후.jpg", "src": "%5B%EB%A9%94%EB%A6%AC%EC%B8%A0%ED%99%94%EC%9E%AC%5D%2025.7.25~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%20%EC%8B%9C%ED%96%89%28%EC%95%94%EB%87%8C%EC%8B%AC%20%EA%B4%80%EB%A0%A8%EB%A7%8C%29%20%EA%B7%B8%20%EC%99%B8%20%EA%B8%B0%EC%A1%B4%EA%B3%BC%20%EB%8F%99%EC%9D%BC%ED%95%98%EA%B2%8C%207%EC%9D%BC%ED%9B%84.jpg", "content_type": "image"}], "text": "인후두염 폐렴 급성기관지염 독감 이하선염 볼거리 각막염 결막염 이석증 황반변성 백반증 급성위염 식도염 피부다한증 액취증 티눈 지방종 비염 부비동염 중이염 임신출산 임플란트 하지정맥류 치질 자궁내막증 기흉 요로결석 탈장 항문농양 쌍꺼풀 안검하수 백내장 녹내장 사시 어깨병변 추간판장애 디스크 무릎질환 화상 암뇌심즉시인수", "page_count": 1}, {"filename": "[현대해상] 25.7.15~ 간편보험 즉시인수 추가(총 217개).jpg", "company": "현대해상", "date": "2025.07.15", "sort_date": "20250715", "product_type": "간편보험", "wait_period": "즉시인수", "count": 217, "description": "25.7.15~ 간편보험 즉시인수 추가(총 217개)", "page": 1, "group_key": "현대해상||2025.07.15||[현대해상] 25.7.15~ 간편보험 즉시인수 추가(총 217개)", "pages": [{"page": 1, "filename": "[현대해상] 25.7.15~ 간편보험 즉시인수 추가(총 217개).jpg", "src": "%5B%ED%98%84%EB%8C%80%ED%95%B4%EC%83%81%5D%2025.7.15~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%20%EC%B6%94%EA%B0%80%28%EC%B4%9D%20217%EA%B0%9C%29.jpg", "content_type": "image"}], "text": "성홍열 쯔쯔가무시 수막염 수두 피부양성종양 사마귀 피부종기 연조직감염 지루피부병 내향성손발톱 탈모증 다한증 켈로이드 화상 A형간염 위식도역류병 담석증 기흉 각막염 안검내반 눈물관협착 익상편 백내장 사시 라식 라섹 중이염 충치 치주질환 턱관절질환 임플란트 타석증 수족구 돌발성난청 편도염 부비동염 독감 폐렴 비용종 비중격만곡증 성대결절 코뼈골절 안와골절 음낭수종 고환염 자궁근종 난소낭종 질염 자궁탈출 제왕절개 조기양막파수 하지정맥류 외반무지 족저근막염 추간판장애 디스크 대장용종 위용종 치핵 치질 방아쇠수지 결절종 손목터널증후군 회전근개파열 윤활막염 팔골절 팔꿈치인대파열 요실금 방광염 요로결석 전립선비대증 전립선염 골반염증성질환 급성충수염 탈장 장염 식중독 콜레라 과민대장증후군 손가락탈구 발가락탈구 핀제거", "page_count": 1}, {"filename": "[DB손보] 25.7~ 간편 311 예외질환(3개월~).jpg", "company": "DB손보", "date": "2025.07", "sort_date": "20250700", "product_type": "간편보험", "wait_period": "3개월 경과", "count": null, "description": "25.7~ 간편 311 예외질환(3개월~)", "page": 1, "group_key": "DB손보||2025.07||[DB손보] 25.7~ 간편 311 예외질환(3개월~)", "pages": [{"page": 1, "filename": "[DB손보] 25.7~ 간편 311 예외질환(3개월~).jpg", "src": "%5BDB%EC%86%90%EB%B3%B4%5D%2025.7~%20%EA%B0%84%ED%8E%B8%20311%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%283%EA%B0%9C%EC%9B%94~%29.jpg", "content_type": "image"}], "text": "다래끼 대장용종 대장폴립 표재성손상 타박상 목열린상처 바르토린선질환 발목발열린상처 복부골반생식기열린상처 사타구니대퇴탈장 손열상 아래팔열상 어깨위팔열린상처 요실금 유방열린상처 제왕절개 충수염 치아우식증 충치 임플란트 치질 치핵 흉부열린상처 엉덩이대퇴열린상처 총아리무릎열린상처", "page_count": 1}, {"filename": "[KB라이프생명] 25.7~ 간편보험 예외질환 3,167개확대(즉시인수 가능).jpg", "company": "KB라이프생명", "date": "2025.07", "sort_date": "20250700", "product_type": "간편보험", "wait_period": "즉시인수", "count": 3167, "description": "25.7~ 간편보험 예외질환 3,167개확대(즉시인수 가능)", "page": 1, "group_key": "KB라이프생명||2025.07||[KB라이프생명] 25.7~ 간편보험 예외질환 3,167개확대(즉시인수 가능)", "pages": [{"page": 1, "filename": "[KB라이프생명] 25.7~ 간편보험 예외질환 3,167개확대(즉시인수 가능).jpg", "src": "%5BKB%EB%9D%BC%EC%9D%B4%ED%94%84%EC%83%9D%EB%AA%85%5D%2025.7~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%203%2C167%EA%B0%9C%ED%99%95%EB%8C%80%28%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%20%EA%B0%80%EB%8A%A5%29.jpg", "content_type": "image"}], "text": "대장용종 직장용종 위용종 지방종 담낭종 자궁근종 자궁용종 다래끼 눈물샘병 바이러스사마귀 편도염 부비동염 비중격만곡증 코질환 눈물관련질환 시력교정수술 라식 라섹 치질 치핵 치아우식증 충치 임플란트 치조골수술 기흉 요로결석 신요관결석 요실금 다한증 티눈 굳은살 유방양성신생물 난소낭종 갑상선결절 갑상선낭종 양성신생물 급성부비동염 인플루엔자 무지외반증 외반무지 골절 연조직손상 갑상선기능저하 갑상선기능항진 위식도역류 위염 십이지장염 담석증 이석증 어지럼증 백내장 녹내장 사시 각막염 결막염 발진타이푸스 수막염 A형간염 헬리코박터 수두", "page_count": 1}, {"filename": "[현대해상] 25.6.17~ 간편보험 즉시인수 추가.jpg", "company": "현대해상", "date": "2025.06.17", "sort_date": "20250617", "product_type": "간편보험", "wait_period": "즉시인수", "count": null, "description": "25.6.17~ 간편보험 즉시인수 추가", "page": 1, "group_key": "현대해상||2025.06.17||[현대해상] 25.6.17~ 간편보험 즉시인수 추가", "pages": [{"page": 1, "filename": "[현대해상] 25.6.17~ 간편보험 즉시인수 추가.jpg", "src": "%5B%ED%98%84%EB%8C%80%ED%95%B4%EC%83%81%5D%2025.6.17~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%A6%89%EC%8B%9C%EC%9D%B8%EC%88%98%20%EC%B6%94%EA%B0%80.jpg", "content_type": "image"}], "text": "위양성종양 위용종 대장용종 담석증 담낭염 급성충수염 충수염 대상포진 두드러기 아토피피부염 티눈 결절종 늑골흉골흉곽골절 손목손가락골절 발가락발목골절 탈장 치은염 치주질환 임플란트 부비동염 편도염 후두염 다래끼 맥립종 라식 라섹 치핵 치질 결장직장항문양성신생물 항문직장농양궤양탈출 하지정맥류 전립선비대증 자궁근종 자궁양성종양 요실금 유산 제왕절개", "page_count": 1}, {"filename": "[ABL생명] 25.3~  간편보험 예외질환 765개  (1).jpg", "company": "ABL생명", "date": "2025.03", "sort_date": "20250300", "product_type": "간편보험", "wait_period": "-", "count": 765, "description": "25.3~  간편보험 예외질환 765개", "page": 1, "group_key": "ABL생명||2025.03||[ABL생명] 25.3~  간편보험 예외질환 765개", "pages": [{"page": 1, "filename": "[ABL생명] 25.3~  간편보험 예외질환 765개  (1).jpg", "src": "%5BABL%EC%83%9D%EB%AA%85%5D%2025.3~%20%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20765%EA%B0%9C%20%20%281%29.jpg", "content_type": "image"}, {"page": 2, "filename": "[ABL생명] 25.3~  간편보험 예외질환 765개  (2).jpg", "src": "%5BABL%EC%83%9D%EB%AA%85%5D%2025.3~%20%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20765%EA%B0%9C%20%20%282%29.jpg", "content_type": "image"}], "text": "인플루엔자 독감 감염성장염 경추 요추 경추통 요추통 요통 등통증 디스크 추간판장애 추간판탈출증 골반통 골반내염증 관절염 무지외반증 고관절증 척추골절 골절 어깨병변 회전근개 염좌 타박상 석회성건염 테니스엘보 내측상과 대퇴골절 오십견 족저근막염 고관절 무릎 불규칙월경 유방염 자궁내막증식증 자궁내막증 자궁경부비정형 자궁근종 난소낭종 전립선비대 콩팥결석 신장결석 요관결석 신결석 급성방광염 요실금 단핵구증 혈뇨 A형간염 담석증 장폐색 기흉 대장 직장 맹장 충수 자궁 유방 양성신생물 간 갑상선 담관 소화기관 식도 위 십이지장 외음부 난소 고환 구강 편도 대장용종 직장용종 위용종 지방종 각막염 결막염 이석증 황반변성 눈물샘질환 다래끼 사시 녹내장 두드러기 아토피 피부염 티눈 굳은살 사마귀 켈로이드 화상 두통 수면무호흡증 안면신경마비 불면증 뇌진탕 불안증 고혈압 당뇨병 고지혈증 갑상선기능저하증 갑상선기능항진증 천식 기흉 철결핍빈혈 편도염 후두염 비염 부비동염 급성기관지염 폐렴", "page_count": 2}, {"filename": "[[미래에셋생명] 24.10~ 간편보험 심사 대폭완화(예외개수제한X, 제자리암 진단 제외).jpg", "company": "미래에셋생명", "date": "2024.10", "sort_date": "20241000", "product_type": "간편보험", "wait_period": "-", "count": null, "description": "24.10~ 간편보험 심사 대폭완화(예외개수제한X, 제자리암 진단 제외)", "page": 1, "group_key": "미래에셋생명||2024.10||[[미래에셋생명] 24.10~ 간편보험 심사 대폭완화(예외개수제한X, 제자리암 진단 제외)", "pages": [{"page": 1, "filename": "[[미래에셋생명] 24.10~ 간편보험 심사 대폭완화(예외개수제한X, 제자리암 진단 제외).jpg", "src": "%5B%5B%EB%AF%B8%EB%9E%98%EC%97%90%EC%85%8B%EC%83%9D%EB%AA%85%5D%2024.10~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%8B%AC%EC%82%AC%20%EB%8C%80%ED%8F%AD%EC%99%84%ED%99%94%28%EC%98%88%EC%99%B8%EA%B0%9C%EC%88%98%EC%A0%9C%ED%95%9CX%2C%20%EC%A0%9C%EC%9E%90%EB%A6%AC%EC%95%94%20%EC%A7%84%EB%8B%A8%20%EC%A0%9C%EC%99%B8%29.jpg", "content_type": "image"}], "text": "제자리암 상피내암 고혈압 고지혈증 당뇨 예외개수제한없음 경과기간단축 협심증 심근경색 간경화 심장판막증 뇌혈관질환", "page_count": 1}, {"filename": "[DB손보] 24.7~ 유병력자실비 예외질환(3개월~) (1).jpg", "company": "DB손보", "date": "2024.07", "sort_date": "20240700", "product_type": "유병력자실비", "wait_period": "3개월 경과", "count": null, "description": "24.7~ 유병력자실비 예외질환(3개월~)", "page": 1, "group_key": "DB손보||2024.07||[DB손보] 24.7~ 유병력자실비 예외질환(3개월~)", "pages": [{"page": 1, "filename": "[DB손보] 24.7~ 유병력자실비 예외질환(3개월~) (1).jpg", "src": "%5BDB%EC%86%90%EB%B3%B4%5D%2024.7~%20%EC%9C%A0%EB%B3%91%EB%A0%A5%EC%9E%90%EC%8B%A4%EB%B9%84%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%283%EA%B0%9C%EC%9B%94~%29%20%281%29.jpg", "content_type": "image"}, {"page": 2, "filename": "[DB손보] 24.7~ 유병력자실비 예외질환(3개월~) (2).jpg", "src": "%5BDB%EC%86%90%EB%B3%B4%5D%2024.7~%20%EC%9C%A0%EB%B3%91%EB%A0%A5%EC%9E%90%EC%8B%A4%EB%B9%84%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%283%EA%B0%9C%EC%9B%94~%29%20%282%29.jpg", "content_type": "image"}], "text": "A형간염 이석증 BPPV 각막염 결막염 갑상선기능저하증 갑상선기능항진증 갑상선결절 갑상선종 갑상선낭종 갑상샘종 갑상샘낭종 고관절 고환 골반내장증 골반내출혈 골절 갈비뼈 늑골 골반 다발성 두개 무릎 발 발목 손가락 손 척추 팔 손목 급성기관지염 세기관지염 기도이물질 난소낭종 난소질환 눈물샘질환 다래끼 당뇨병 대상포진 대장용종 두드러기 타박상 만성방광염 방광결석 비뇨기질환 요실금 요관결석 신장결석 신우결석 무지외반증 비염 부비동염 편도염 편도비대 사마귀 성홍열 수두 수막염 아토피 안검내반 열린상처 염좌 위식도역류 위염 십이지장염 자궁근종 자궁양성종양 자궁내막증 전립선비대증 전립선염 지방종 치핵 치질 치아우식증 충치 치주질환 콩팥결석 탈장 통풍 티눈 피부양성종양 하지정맥류 회전근개 기흉 임플란트 라식 라섹 근시 난시 발진타이푸스 코로나19 콜레라 타석증 침샘결석 탈구 어깨탈구 무릎탈구 손목탈구 척추탈구 팔꿈치탈구 탈모 표피낭 피부농양 편도주위농양 폐렴 화상 후두염 흉부용종 치조골이식 항문농양 항문질환 헤르페스 회음열상 골절핀제거", "page_count": 2}, {"filename": "[[DB손보] 24.7~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고.jpg", "company": "DB손보", "date": "2024.07", "sort_date": "20240700", "product_type": "간편보험", "wait_period": "-", "count": null, "description": "24.7~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고", "page": 1, "group_key": "DB손보||2024.07||[[DB손보] 24.7~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고", "pages": [{"page": 1, "filename": "[[DB손보] 24.7~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고.jpg", "src": "%5B%5BDB%EC%86%90%EB%B3%B4%5D%2024.7~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%205%EB%85%84%20%EC%A7%88%EB%AC%B8%EC%84%9C%20%EC%A4%91%EB%8C%80%EC%A7%88%ED%99%98%20%ED%95%B4%EB%8B%B9%20%EC%A7%88%ED%99%98%20%EC%BD%94%EB%93%9C%20%EC%B0%B8%EA%B3%A0.jpg", "content_type": "image"}], "text": "입술구강인두악성신생물 소화기관악성신생물 호흡기흉곽내기관악성신생물 골관절연골악성신생물 흑색종피부악성신생물 중피성연조직악성신생물 유방악성신생물 여성생식기관악성신생물 남성생식기관악성신생물 요로악성신생물 뇌중추신경계악성신생물 갑상선내분비선악성신생물 림프조혈관련조직악성신생물 진성적혈구증가증 골수이형성증후군 만성골수증식질환 본태성혈소판혈증 골수섬유증 만성호산구성백혈병 협심증 급성심근경색증 심근경색 지주막하출혈 뇌내출혈 뇌경색증 뇌졸중 간섬유증 간경화증 알콜성간경변 간경변 심장판막증 승모판장애 대동맥판장애 삼첨판장애 류마티스성심장판막 비류마티스성심장판막 다판막질환 인공심장판막 암 뇌 심장 중대질환 5년질문서", "page_count": 1}, {"filename": "[라이나생명] 23.10~  325간편보험 예외질환 710개  (1).jpg", "company": "라이나생명", "date": "2023.10", "sort_date": "20231000", "product_type": "간편보험", "wait_period": "-", "count": 710, "description": "23.10~  325간편보험 예외질환 710개", "page": 1, "group_key": "라이나생명||2023.10||[라이나생명] 23.10~  325간편보험 예외질환 710개", "pages": [{"page": 1, "filename": "[라이나생명] 23.10~  325간편보험 예외질환 710개  (1).jpg", "src": "%5B%EB%9D%BC%EC%9D%B4%EB%82%98%EC%83%9D%EB%AA%85%5D%2023.10~%20%20325%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20710%EA%B0%9C%20%20%281%29.jpg", "content_type": "image"}, {"page": 2, "filename": "[라이나생명] 23.10~  325간편보험 예외질환 710개  (2).jpg", "src": "%5B%EB%9D%BC%EC%9D%B4%EB%82%98%EC%83%9D%EB%AA%85%5D%2023.10~%20%20325%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20710%EA%B0%9C%20%20%282%29.jpg", "content_type": "image"}, {"page": 3, "filename": "[라이나생명] 23.10~  325간편보험 예외질환 710개  (3).jpg", "src": "%5B%EB%9D%BC%EC%9D%B4%EB%82%98%EC%83%9D%EB%AA%85%5D%2023.10~%20%20325%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%20%EC%98%88%EC%99%B8%EC%A7%88%ED%99%98%20710%EA%B0%9C%20%20%283%29.jpg", "content_type": "image"}], "text": "내반족 무지외반증 섬유근육통 화상 타박상 경추 요추 경추통 요추신경통 요추협착증 요통 등통증 골반통 골반내염증 관절염 손가락발가락관절 힘줄인대파열 골절탈구 어깨병변 회전근개 테니스엘보 오십견 족저근막염 대퇴골절 발목 손발관절 발뒤꿈치뼈 방아쇠수지 결절종 손목터널증후군 근막동통증후군 각막 각막염 결막염 녹내장 눈물샘질환 다래끼 티눈굳은살 사시 이석증 전정신경세포염 황반변성 포도막염 내향성손발톱 탈모증 노안 야맹증 색맹 돌발성난청 안검내반 담낭용종 자궁경부이형증 자궁내막증식증 자궁근종 난소낭종 유방양성신생물 갑상선결절 갑상선선종 미만성갑상샘병 신장용종 복막낭종 포경수술 음낭수종 부고환염 고환염 여성요도증후군 과민성방광 전립선비대증 전립선염 요실금 신결석 신장결석 요관결석 방광결석 다낭성신장질환 폐결핵 기흉 비중격만곡증 편도염 부비동염 비후성비염 지방종 다한증 두드러기 아토피피부염 사마귀 탈모 여드름 피부농양 대장용종 대장폴립 직장용종 A형간염 담석증 소화기계양성신생물 비뇨생식기양성신생물 치질 역류식도염 위식도역류병 위염 십이지장염 장폐색 부정맥 심방세동 심방조동 심근병증 심근증 심부전 동맥경화증 고혈압 협심증 두통 편두통 안면신경마비 파킨슨병 ADHD 주의력결핍 발달지연 뇌지주막낭포 당뇨 통풍 고지혈증 비만 갑상선기능저하증 갑상선기능항진증 성홍열 수두 수족구 수막염 쯔쯔가무시 유행성이하선염 편도주위농양 대상포진 콜레라 파상풍 베체트병 간경화 간섬유화 자가면역질환 자궁내막증", "page_count": 3}, {"filename": "[[현대해상] 23.9~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고.jpg", "company": "현대해상", "date": "2023.09", "sort_date": "20230900", "product_type": "간편보험", "wait_period": "-", "count": null, "description": "23.9~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고", "page": 1, "group_key": "현대해상||2023.09||[[현대해상] 23.9~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고", "pages": [{"page": 1, "filename": "[[현대해상] 23.9~ 간편보험 5년 질문서 중대질환 해당 질환 코드 참고.jpg", "src": "%5B%5B%ED%98%84%EB%8C%80%ED%95%B4%EC%83%81%5D%2023.9~%20%EA%B0%84%ED%8E%B8%EB%B3%B4%ED%97%98%205%EB%85%84%20%EC%A7%88%EB%AC%B8%EC%84%9C%20%EC%A4%91%EB%8C%80%EC%A7%88%ED%99%98%20%ED%95%B4%EB%8B%B9%20%EC%A7%88%ED%99%98%20%EC%BD%94%EB%93%9C%20%EC%B0%B8%EA%B3%A0.jpg", "content_type": "image"}], "text": "입술구강인두악성신생물 소화기관악성신생물 호흡기흉곽내기관악성신생물 골관절연골악성신생물 흑색종피부악성신생물 중피성연조직악성신생물 유방악성신생물 여성생식기관악성신생물 남성생식기관악성신생물 요로악성신생물 뇌중추신경계악성신생물 협심증 급성심근경색증 심근경색 지주막하출혈 뇌내출혈 뇌경색증 뇌졸중 간섬유증 간경화증 간경변 승모판장애 대동맥판장애 삼첨판장애 다판막질환 인공심장판막 심장판막증 암 뇌 심장 중대질환 5년질문서 6대질병", "page_count": 1}];
let filtered=[],modal={doc:null,pg:0},currentQuery='';
let sCo=new Set(),sTy=new Set(),sWa=new Set(),pend=[];
function getTerms(q){return q.trim().toLowerCase().split(/\s+/).filter(Boolean);}
function docMatches(d,terms){
  const hay=(d.company+' '+d.description+' '+d.date+' '+d.product_type+' '+d.wait_period+' '+(d.text||'')).toLowerCase();
  return terms.every(t=>hay.includes(t));
}
function getMatchedTermsInText(d,terms){
  if(!d.text)return[];
  const t=d.text.toLowerCase();
  const meta=(d.company+' '+d.description+' '+d.date+' '+d.product_type+' '+d.wait_period).toLowerCase();
  return terms.filter(term=>t.includes(term)&&!meta.includes(term));
}
function renderCB(id,vals,sel,kind){
  document.getElementById(id).innerHTML=vals.map(v=>{
    const n=allDocs.filter(d=>kind==='co'?d.company===v:kind==='ty'?d.product_type===v:d.wait_period===v).length;
    return`<label class="fi"><input type="checkbox" ${sel.has(v)?'checked':''} onchange="togF('${kind}','${v.replace(/'/g,"\\'")}',this.checked)"><label style="flex:1">${v}</label><span class="fc">${n}</span></label>`;
  }).join('');
}
function buildF(){
  renderCB('CF',[...new Set(allDocs.map(d=>d.company))].sort(),sCo,'co');
  renderCB('TF',[...new Set(allDocs.map(d=>d.product_type))].sort(),sTy,'ty');
  renderCB('WF',[...new Set(allDocs.map(d=>d.wait_period))].sort(),sWa,'wa');
}
function togF(kind,v,on){const s=kind==='co'?sCo:kind==='ty'?sTy:sWa;on?s.add(v):s.delete(v);applyF();}
function resetF(){sCo.clear();sTy.clear();sWa.clear();buildF();applyF();}
function applyF(){
  currentQuery=document.getElementById('SI').value;
  const terms=getTerms(currentQuery);
  const so=document.getElementById('SO').value;
  filtered=allDocs.filter(d=>{
    if(sCo.size&&!sCo.has(d.company))return false;
    if(sTy.size&&!sTy.has(d.product_type))return false;
    if(sWa.size&&!sWa.has(d.wait_period))return false;
    return terms.length===0||docMatches(d,terms);
  });
  if(so==='date_asc')filtered.sort((a,b)=>a.sort_date.localeCompare(b.sort_date));
  else if(so==='company')filtered.sort((a,b)=>a.company.localeCompare(b.company));
  else if(so==='count_desc')filtered.sort((a,b)=>(b.count||0)-(a.count||0));
  else filtered.sort((a,b)=>b.sort_date.localeCompare(a.sort_date));
  renderCards();
}
function renderCards(){
  const co=document.getElementById('CO');
  document.getElementById('RC').textContent=filtered.length+'건';
  if(!filtered.length){co.innerHTML='<div class="empty"><div style="font-size:40px">🔍</div><div>검색 결과가 없습니다</div></div>';return;}
  const terms=getTerms(currentQuery);
  co.innerHTML='<div class="cards">'+filtered.map((d,i)=>{
    const wc=d.wait_period==='즉시인수'?'tag ti':'tag tw';
    const hint=terms.length?getMatchedTermsInText(d,terms):[];
    return`<div class="card" onclick="openM(${allDocs.indexOf(d)})">
      <div class="ch"><span class="cn">${d.company}</span><span class="db">${d.date}~</span></div>
      <div class="cd">${d.description}</div>
      <div class="ct"><span class="tag tp">${d.product_type}</span><span class="${wc}">${d.wait_period}</span>${d.count?`<span class="tag tk">예외 ${d.count.toLocaleString()}개</span>`:''}</div>
      <div class="cf2"><span class="vb">🖼 ${d.page_count}페이지 보기</span>${hint.length?`<span class="mhint">🔍 ${hint.slice(0,3).join(', ')} 포함</span>`:''}</div>
    </div>`;
  }).join('')+'</div>';
}
function openM(i){modal.doc=allDocs[i];modal.pg=0;document.getElementById('IM').classList.add('open');renderM();}
function closeM(){document.getElementById('IM').classList.remove('open');}
function closeMob(e){if(e.target===document.getElementById('IM'))closeM();}
function toggleZoom(img){img.classList.toggle('zoomed');}
function renderM(){
  const d=modal.doc,pg=d.pages[modal.pg];
  document.getElementById('MTT').textContent=d.company+'  '+d.date+'~';
  const wc=d.wait_period==='즉시인수'?'tag ti':'tag tw';
  document.getElementById('MMT').innerHTML='<span class="tag tp">'+d.product_type+'</span><span class="'+wc+'">'+d.wait_period+'</span>'+(d.count?'<span class="tag tk">예외 '+d.count.toLocaleString()+'개</span>':'');
  const mig=document.getElementById('MIG');
  const mtbl=document.getElementById('MTBL');
  if(pg.content_type==='table'){
    mig.style.display='none';mtbl.style.display='block';mtbl.innerHTML=pg.src;
  } else {
    mig.style.display='block';mtbl.style.display='none';mig.src=pg.src;mig.classList.remove('zoomed');
  }
  const terms=getTerms(currentQuery);
  const kwb=document.getElementById('KWB');
  const kwc=document.getElementById('KWC');
  const matched=getMatchedTermsInText(d,terms);
  if(matched.length){kwc.innerHTML=matched.map(t=>'<span class="kw-chip">'+t+'</span>').join('');kwb.classList.add('show');}
  else kwb.classList.remove('show');
  const tot=d.pages.length;
  document.getElementById('PIG').textContent=(modal.pg+1)+' / '+tot;
  document.getElementById('BP').disabled=modal.pg===0;
  document.getElementById('BN').disabled=modal.pg===tot-1;
  document.getElementById('MNV').style.display=tot<=1?'none':'flex';
}
function chPg(d){modal.pg=Math.max(0,Math.min(modal.doc.pages.length-1,modal.pg+d));renderM();}
document.addEventListener('keydown',e=>{
  if(!document.getElementById('IM').classList.contains('open'))return;
  if(e.key==='Escape')closeM();
  if(e.key==='ArrowLeft')chPg(-1);
  if(e.key==='ArrowRight')chPg(1);
});
function openU(){pend=[];document.getElementById('UL').innerHTML='';document.getElementById('UMG').style.display='none';document.getElementById('BUP').disabled=true;document.getElementById('UO').classList.add('open');}
function closeU(){document.getElementById('UO').classList.remove('open');}
function closeUob(e){if(e.target===document.getElementById('UO'))closeU();}
function selF(e){addFiles(Array.from(e.target.files));}
function dov(e){e.preventDefault();document.getElementById('UA').classList.add('drag');}
function dlv(){document.getElementById('UA').classList.remove('drag');}
function drp(e){e.preventDefault();dlv();addFiles(Array.from(e.dataTransfer.files));}
function addFiles(fs){
  fs.forEach(f=>{if(!pend.find(p=>p.name===f.name))pend.push(f);});
  document.getElementById('UL').innerHTML=pend.map(f=>`<div class="uitm"><span class="un">${f.name}</span><span style="color:var(--sub);font-size:11px">${(f.size/1024).toFixed(0)}KB</span></div>`).join('');
  document.getElementById('BUP').disabled=pend.length===0;
}
let _pdfJsLoaded=false;
function loadPdfJs(cb){if(_pdfJsLoaded){cb();return;}const s=document.createElement('script');s.src='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js';s.onload=()=>{pdfjsLib.GlobalWorkerOptions.workerSrc='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';_pdfJsLoaded=true;cb();};document.head.appendChild(s);}
let _xlsxLoaded=false;
function loadXlsx(cb){if(_xlsxLoaded){cb();return;}const s=document.createElement('script');s.src='https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js';s.onload=()=>{_xlsxLoaded=true;cb();};document.head.appendChild(s);}
function parseMeta(filename){
  const name=filename.replace(/\.[^.]+$/,'');
  const cm=name.match(/^\[+([^\]]+)\]/);const company=cm?cm[1].trim():'기타';
  const dm=name.match(/(\d{2})\.(\d{1,2})(?:\.(\d{1,2}))?(?:\([^)]*\))?\s*~/);
  let date='날짜 미상',sd='00000000';
  if(dm){const y=2000+parseInt(dm[1]),mo=parseInt(dm[2]),d=dm[3]?parseInt(dm[3]):null;
    date=y+'.'+String(mo).padStart(2,'0')+(d?'.'+String(d).padStart(2,'0'):'');
    sd=y+String(mo).padStart(2,'0')+(d?String(d).padStart(2,'0'):'00');}
  const prod=filename.includes('유병력자실비')?'유병력자실비':'간편보험';
  const wait=filename.includes('즉시인수')?'즉시인수':filename.includes('3개월')?'3개월 경과':'-';
  const desc=name.replace(/^\[+[^\]]+\]\s*/,'').replace(/\s*\(\d+\)\s*$/,'').trim();
  const key='NEW||'+company+'||'+date+'||'+desc;
  return{company,date,sd,prod,wait,desc,key};
}
function addPage(key,meta,pageData,text){
  const ex=allDocs.find(d=>d.id===key);
  if(ex){ex.pages.push({page:ex.pages.length+1,...pageData});ex.page_count=ex.pages.length;if(text)ex.text+=' '+text;}
  else allDocs.unshift({id:key,company:meta.company,date:meta.date,sort_date:meta.sd,product_type:meta.prod,wait_period:meta.wait,count:null,description:meta.desc,text:text||'',pages:[{page:1,...pageData}],page_count:1});
}
function finishUpload(done){buildF();applyF();document.getElementById('UMG').textContent='✅ '+done+'개 추가 완료!';document.getElementById('UMG').style.display='block';setTimeout(closeU,1600);}
function doU(){
  if(!pend.length)return;
  let done=0,total=pend.length;
  const bump=()=>{if(++done===total)finishUpload(done);};
  pend.forEach(f=>{
    const ext=f.name.split('.').pop().toLowerCase();
    const meta=parseMeta(f.name);
    if(ext==='pdf'){
      loadPdfJs(()=>{const reader=new FileReader();reader.onload=async ev=>{try{const pdf=await pdfjsLib.getDocument({data:ev.target.result}).promise;let text='';for(let i=1;i<=pdf.numPages;i++){const page=await pdf.getPage(i);const scale=2.0;const vp=page.getViewport({scale});const canvas=document.createElement('canvas');canvas.width=vp.width;canvas.height=vp.height;await page.render({canvasContext:canvas.getContext('2d'),viewport:vp}).promise;const src=canvas.toDataURL('image/png');try{const tc=await page.getTextContent();text+=' '+tc.items.map(it=>it.str).join(' ');}catch(e){}addPage(meta.key,meta,{src,filename:f.name,content_type:'image'},i===1?text:'');}bump();}catch(err){console.error(err);bump();}};reader.readAsArrayBuffer(f);});
    } else if(['xlsx','xls','csv'].includes(ext)){
      loadXlsx(()=>{const reader=new FileReader();reader.onload=ev=>{try{const wb=XLSX.read(new Uint8Array(ev.target.result),{type:'array'});const ws=wb.Sheets[wb.SheetNames[0]];const html=XLSX.utils.sheet_to_html(ws,{id:'xltbl',editable:false});const tmp=document.createElement('div');tmp.innerHTML=html;const text=tmp.textContent||'';const styledHtml='<style>#xltbl{border-collapse:collapse;font-size:13px;width:100%}#xltbl td,#xltbl th{border:1px solid #ddd;padding:4px 8px;white-space:pre-wrap}</style>'+html;addPage(meta.key,meta,{src:styledHtml,filename:f.name,content_type:'table'},text);bump();}catch(err){console.error(err);bump();}};reader.readAsArrayBuffer(f);});
    } else {
      const reader=new FileReader();reader.onload=ev=>{addPage(meta.key,meta,{src:ev.target.result,filename:f.name,content_type:'image'},'');bump();};reader.readAsDataURL(f);
    }
  });
}
document.getElementById('SI').addEventListener('input',applyF);
document.getElementById('SO').addEventListener('change',applyF);
buildF();applyF();
</script>
</body>
</html>
