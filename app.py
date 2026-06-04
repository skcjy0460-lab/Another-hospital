import streamlit as st

# ─── 페이지 설정 ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="타병원 외진 처방 실무 가이드",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS (밝은 테마) ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

* { font-family: 'Noto Sans KR', sans-serif !important; }

/* 전체 배경 – 밝은 회색 */
.stApp { background: #f0f4f8 !important; }

/* 사이드바 – 흰색 계열 */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e3a5f 0%, #1565c0 100%) !important;
    border-right: 1px solid #bbdefb;
}
[data-testid="stSidebar"] * { color: #e3f2fd !important; }
[data-testid="stSidebar"] .stRadio > label { color: #90caf9 !important; font-weight: 600; font-size: 0.85rem; }

.block-container { padding-top: 1rem !important; max-width: 1400px; background: transparent !important; }

/* 메인 컨텐츠 배경 강제 흰색 */
section[data-testid="stMain"] > div { background: transparent !important; }

/* 헤더 */
.main-header {
    background: linear-gradient(135deg, #1565c0 0%, #1976d2 60%, #0288d1 100%);
    border-radius: 16px; padding: 32px 40px; margin-bottom: 24px;
    border: none;
    box-shadow: 0 4px 20px rgba(21,101,192,0.25);
    position: relative; overflow: hidden;
}
.main-header::after {
    content: ''; position: absolute; top: -50%; right: -5%;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.main-header h1 { color: #fff !important; font-size: 1.9rem !important; font-weight: 900 !important; margin: 0 !important; }
.main-header .sub { color: #bbdefb !important; font-size: 0.9rem; margin-top: 8px; }

/* 공통 카드 */
.card {
    background: #ffffff;
    border: 1px solid #e3eaf3;
    border-radius: 12px; padding: 22px 26px; margin: 14px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

/* 알림 박스 – 밝은 배경 + 진한 글씨 */
.box-danger  { background:#fff5f5; border-left:4px solid #e53935; border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; color:#b71c1c; }
.box-warning { background:#fffde7; border-left:4px solid #f9a825; border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; color:#7a5800; }
.box-info    { background:#e3f2fd; border-left:4px solid #1976d2; border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; color:#0d47a1; }
.box-success { background:#f1f8e9; border-left:4px solid #43a047; border-radius:0 8px 8px 0; padding:14px 18px; margin:10px 0; color:#1b5e20; }
.box-purple  { background:#f3e5f5; border:1px solid #ce93d8; border-radius:8px; padding:14px 18px; margin:10px 0; color:#4a148c; font-family:'JetBrains Mono',monospace; font-size:0.87rem; }

/* 표 */
.t { width:100%; border-collapse:collapse; margin:14px 0; font-size:0.88rem; color:#1a2a3a; }
.t th { background:#1565c0; padding:11px 14px; text-align:left; border:1px solid #1976d2; font-weight:700; color:#ffffff; }
.t td { padding:9px 14px; border:1px solid #dee6ef; vertical-align:top; line-height:1.7; background:#ffffff; color:#1a2a3a; }
.t tr:nth-child(even) td { background:#f5f9ff; }
.t tr:hover td { background:#e8f4fd; }

/* 뱃지 */
.b  { display:inline-block; padding:3px 10px; border-radius:20px; font-size:0.78rem; font-weight:700; margin:2px 3px; white-space:nowrap; }
.br { background:#ffebee; color:#c62828; border:1px solid #ef9a9a; }
.bb { background:#e3f2fd; color:#1565c0; border:1px solid #90caf9; }
.bg { background:#e8f5e9; color:#2e7d32; border:1px solid #a5d6a7; }
.bo { background:#fff8e1; color:#e65100; border:1px solid #ffcc02; }
.bp { background:#f3e5f5; color:#6a1b9a; border:1px solid #ce93d8; }

/* 강조 텍스트 */
.red  { color:#c62828; font-weight:700; }
.yel  { color:#e65100; font-weight:700; }
.grn  { color:#2e7d32; font-weight:700; }
.blu  { color:#1565c0; font-weight:700; }

/* 섹션 제목 */
.sec-title { font-size:1.25rem; font-weight:800; color:#1565c0; padding:10px 0 8px; border-bottom:2px solid #bbdefb; margin-bottom:16px; }
.sub-title  { font-size:1.02rem; font-weight:700; color:#1976d2; margin:18px 0 10px; }

/* 흐름도 */
.flow { background:#ffffff; border:1px solid #bbdefb; border-radius:9px; padding:13px 18px; margin:7px 0; color:#1a2a3a; box-shadow:0 1px 4px rgba(0,0,0,0.06); }
.flow-n { display:inline-flex; align-items:center; justify-content:center; background:#1565c0; color:#fff; min-width:26px; width:26px; height:26px; border-radius:50%; text-align:center; font-weight:700; font-size:0.82rem; margin-right:9px; flex-shrink:0; }
.flow-arr { text-align:center; color:#1976d2; font-size:1.3rem; margin:3px 0; }

/* 메트릭 */
[data-testid="stMetricValue"] { color:#1565c0 !important; font-weight:700 !important; }
[data-testid="stMetricLabel"] { color:#37474f !important; }
[data-testid="stMetric"] { background:#ffffff; border:1px solid #e3eaf3; border-radius:10px; padding:12px 16px; box-shadow:0 1px 4px rgba(0,0,0,0.06); }

/* expander */
[data-testid="stExpander"] { background:#ffffff !important; border:1px solid #dce6f0 !important; border-radius:10px !important; box-shadow:0 1px 4px rgba(0,0,0,0.05) !important; }
[data-testid="stExpander"] summary { color:#1565c0 !important; font-weight:600 !important; }

/* 탭 */
.stTabs [data-baseweb="tab-list"] { background:#e8f0f8 !important; border-radius:10px !important; border:1px solid #cfe0f0 !important; }
.stTabs [data-baseweb="tab"] { color:#37474f !important; font-weight:600 !important; }
.stTabs [aria-selected="true"] { color:#1565c0 !important; background:#ffffff !important; border-radius:8px !important; box-shadow:0 1px 4px rgba(0,0,0,0.1) !important; }

/* 체크박스 */
.stCheckbox label { color:#2c3e50 !important; font-size:0.9rem !important; }

/* radio 버튼 */
.stRadio label span { color:#0d47a1 !important; }

/* 하단 */
.footer { margin-top:48px; padding:18px; border-top:1px solid #dce6f0; text-align:center; color:#546e7a; font-size:0.78rem; background:#f8fafc; border-radius:0 0 12px 12px; }
.footer a { color:#1565c0; text-decoration:none; }

/* 인라인 강조 박스 (표 내부) */
div[style*="background:rgba(76,175,80"] { color:#1b5e20 !important; }
div[style*="background:rgba(244,67,54"] { color:#b71c1c !important; }
div[style*="background:rgba(255,152,0"] { color:#7a5800 !important; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:18px 0 22px;">
        <div style="font-size:2.8rem;">🏥</div>
        <div style="font-size:1rem;font-weight:800;color:#1565c0;line-height:1.5;margin-top:6px;">
            타병원 외진 처방<br>실무 가이드
        </div>
        <div style="font-size:0.72rem;color:#455a64;margin-top:6px;">
            원무·심사 실무자용 | 비요양병원
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    menu = st.radio(
        "📂 메뉴",
        [
            "🏠 개요 및 기본원칙",
            "💰 본인부담 100% 적용 상황",
            "💊 원내처방 원칙 & 사유",
            "🚫 원외처방 안 되는 사유",
            "📋 청구 방법 & 수가 산정",
            "🔍 선별집중심사 & 고가검사",
            "📄 진료기록부·서류 발급",
            "⚡ 특수 케이스 Q&A",
            "✅ 빠른 체크리스트",
        ],
        label_visibility="visible"
    )

    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.75rem;color:#37474f;line-height:1.9;padding:4px 0;">
        📌 <b style="color:#455a64;">관련 법령</b><br>
        · 요양급여기준 규칙 별표1<br>
        · 보험급여팀-204호(2008.1.24.)<br>
        · 약사법 제23조 제4항<br>
        · 복지부 보관 65720-295호<br>
        · 국토교통부고시 2023-2호<br>
        <br>
        ⚠️ 법령 개정 시 변경될 수 있음.<br>
        HIRA 포털 교차 확인 필수.
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 헤더
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="main-header">
    <h1>🏥 타병원 외진 처방 실무 가이드</h1>
    <div class="sub">원무·청구심사 실무자를 위한 상세 업무 매뉴얼 &nbsp;|&nbsp; 비요양병원 전용 &nbsp;|&nbsp; 건강보험·의료급여·자동차보험 통합</div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 1: 개요 및 기본원칙
# ══════════════════════════════════════════════════════════════════════════════
if menu == "🏠 개요 및 기본원칙":
    st.markdown('<div class="sec-title">📖 타병원 외진 처방 – 기본 개념과 원칙</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("적용 대상", "병원(요양병원 제외)", "입원환자 외진 시")
    c2.metric("약제 원칙", "원내처방", "원외처방 원칙적 불가")
    c3.metric("청구 주체", "의뢰한 기관", "외진 내역 포함")
    c4.metric("본인부담", "입원 기준 적용", "외래 기준 아님")

    st.markdown("""
    <div class="box-info">
        <b>📌 핵심 개념:</b> "타병원 외진"이란 <b>입원 중인 환자를</b> 해당 기관의 시설·장비·인력으로
        진료가 곤란하여 <b>다른 요양기관에 외래 진료를 의뢰</b>하는 것입니다.
        이 과정에서 발생하는 진료비 청구, 처방, 본인부담 처리 기준을 정확히 숙지해야 합니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">⚖️ 핵심 법적 근거</div>', unsafe_allow_html=True)
    laws = [
        ("요양급여기준에 관한 규칙 별표1 바항",
         "요양기관은 요양급여에 필요한 약제·치료재료를 직접 구입하여 가입자 등에게 지급 → 원내처방 원칙의 근거"),
        ("국민건강보험 요양급여기준 규칙 제2조·제6조",
         "요양급여의뢰서 없이 상급종합병원 이용 시 진료비 100% 본인부담 규정"),
        ("보건복지부 보험급여팀-204호 (2008.1.24.)",
         "타병원 입원환자 진료의뢰 시 약제비 산정방법 행정해석 – 원내처방 원칙 확립"),
        ("약사법 제23조 제4항",
         "원내처방 예외 허용: 조현병·조울증 등 자신/타인 해칠 우려 있는 정신질환자의 경우 원내 직접조제"),
        ("보건복지부 보관 65720-295호 (1996.3.6.)",
         "입원환자 타기관 진료의뢰 청구기준 원칙 수립 – 청구 주체 및 수가 산정 기준"),
        ("국민건강보험법 시행령 별표2 제1호 나목",
         "상급종합병원 진찰료 100% 본인부담 – 단, 차상위 1·2종 및 산정특례 환자 예외"),
    ]
    for title, desc in laws:
        st.markdown(f"""
        <div class="box-purple">
            <b>📜 {title}</b><br>
            <span style="color:#6a1b9a;">{desc}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">🔄 타병원 외진 처리 전체 흐름도</div>', unsafe_allow_html=True)

    steps = [
        ("1", "외진 필요성 판단", "주치의가 시설·장비·인력 부족으로 타기관 진료 필요 판단 → 의뢰 결정"),
        ("2", "진료의뢰서 발급", "의뢰기관: 정식 「요양급여의뢰서」작성 → 환자에게 원본 전달 (유효기간 14일)"),
        ("3", "외진 진료 실시", "환자가 의뢰받은 기관에 방문 → 외래 진료 실시"),
        ("4", "약제 처방 처리", "【원칙】의뢰받은 기관에서 원내처방 / 약제 없으면 처방내역을 의뢰한 기관에 통보"),
        ("5", "진료내역 통보", "의뢰받은 기관 → 의뢰한 기관에 전체 진료내역(처방 포함) 서면 통보"),
        ("6", "청구 (HIRA)", "의뢰한 기관(원 입원기관)이 외진 내역 포함하여 HIRA 청구 / 특정내역 MJ006 기재"),
        ("7", "진료비 정산", "의뢰한 기관 ↔ 의뢰받은 기관 상호 협의하에 진료비 정산"),
    ]
    for i, (num, title, desc) in enumerate(steps):
        st.markdown(f"""
        <div class="flow">
            <span class="flow-n">{num}</span>
            <b style="color:#1565c0;">{title}</b>
            <span style="color:#37474f; margin-left:8px;">→ {desc}</span>
        </div>
        """, unsafe_allow_html=True)
        if i < len(steps)-1:
            st.markdown('<div class="flow-arr">↓</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box-warning" style="margin-top:20px;">
        <b>⚠️ 비요양병원과 요양병원의 차이:</b><br>
        요양병원은 <b>일당정액수가</b>로 약제비가 포함되어 처리 방식이 다릅니다.
        본 가이드는 <span class="red">비요양병원(종합병원·병원·의원)</span> 기준으로 작성되었습니다.
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 2: 본인부담 100%
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "💰 본인부담 100% 적용 상황":
    st.markdown('<div class="sec-title">💰 본인부담 100% 적용 상황 완전 정리</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box-danger">
        <b>🚨 중요:</b> 본인부담 100%란 건강보험 급여 혜택 없이 <b>진료비 전액을 환자가 부담</b>하는 것입니다.
        원무직원은 이 상황을 <u>사전에 환자에게 반드시 고지</u>해야 하며, 청구 시에도 특정내역 기재가 필요합니다.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📌 상황1 - 의뢰서 없이 상급종합병원 이용", expanded=True):
        st.markdown("""
        <table class="t">
            <tr><th>구분</th><th>내용</th><th>본인부담률</th><th>비고</th></tr>
            <tr>
                <td><span class="b bb">상급종합병원 초진</span></td>
                <td>의뢰서 없이 직접 방문</td>
                <td><span class="red">100%</span></td>
                <td>진찰료만 해당 (단, 차상위·산정특례 제외)</td>
            </tr>
            <tr>
                <td><span class="b bb">상급종합→상급종합</span></td>
                <td>상급종합끼리도 의뢰서 필요</td>
                <td><span class="red">100%</span></td>
                <td>의뢰서 없으면 동일 적용</td>
            </tr>
            <tr>
                <td><span class="b bg">의뢰서 제출 후 재방문</span></td>
                <td>의뢰서 제출일부터 보험혜택</td>
                <td><span class="grn">정상 본인부담</span></td>
                <td>소급 불가 – 최초 방문분은 100% 유지</td>
            </tr>
            <tr>
                <td><span class="b bo">차상위 1·2종 환자</span></td>
                <td>의뢰서 없이 상급종합 이용</td>
                <td><span class="grn">정상 본인부담 (예외)</span></td>
                <td>100% 적용 대상 제외</td>
            </tr>
            <tr>
                <td><span class="b bo">산정특례 등록 환자</span></td>
                <td>의뢰서 없이 상급종합 이용</td>
                <td><span class="grn">정상 본인부담 (예외)</span></td>
                <td>100% 적용 대상 제외</td>
            </tr>
        </table>
        <div class="box-warning">
            <b>⚠️ 약제 처방 주의:</b> 의뢰서 없이 100% 본인부담으로 진료받은 경우,
            해당 처방전으로 <b>외부 약국에서도 100% 본인부담</b>으로 조제해야 합니다.
        </div>
        <div class="box-purple">
            📜 <b>근거:</b> 요양급여기준 규칙 제2조·제6조 / 시행령 별표2 제1호 나목
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📌 상황2 - 입원 중 의뢰 없이 임의로 타기관 방문"):
        st.markdown("""
        <div class="box-danger">
            <b>🚫 원칙:</b> 입원환자가 의뢰서 없이 임의로 타기관을 이용하면 <b>진료비 전액 본인부담</b>입니다.
            응급상황은 예외이나 사후 처리 필요.
        </div>
        <table class="t">
            <tr><th>환자 유형</th><th>상황</th><th>본인부담</th><th>소급 여부</th></tr>
            <tr>
                <td>건강보험 입원환자</td>
                <td>의뢰서 없이 타기관 외래</td>
                <td><span class="red">전액 본인부담</span></td>
                <td>소급 적용 불가</td>
            </tr>
            <tr>
                <td>의료급여 입원환자</td>
                <td>의뢰서 없이 타기관 외래</td>
                <td><span class="red">전액 본인부담</span></td>
                <td>소급 적용 불가</td>
            </tr>
            <tr>
                <td>응급 상황 발생</td>
                <td>응급의료 목적 타기관 이용</td>
                <td><span class="grn">급여 적용 가능</span></td>
                <td>응급 인정 시 사후 처리</td>
            </tr>
        </table>
        <div class="box-info">
            <b>📌 원무 실무 포인트:</b><br>
            ① 입원환자 타기관 방문 전 반드시 의뢰서 발급 여부 확인<br>
            ② 의뢰서 없이 이미 진료받고 온 경우 → 소급 급여 적용 불가<br>
            ③ 응급으로 타기관 이용한 경우 → 입원 후 즉시 사후 처리 절차 안내
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📌 상황3 - 의뢰서 원본 미제출·사본·유효기간 초과"):
        st.markdown("""
        <table class="t">
            <tr><th>상황</th><th>처리 방법</th><th>급여 적용</th></tr>
            <tr>
                <td>사본 먼저 제출</td>
                <td>임시 처리 후 원본 제출 필요</td>
                <td><span class="yel">원본 제출 시부터 급여 / 이전 방문분 소급 불가</span></td>
            </tr>
            <tr>
                <td>원본 분실</td>
                <td>발급기관에 재발급 요청</td>
                <td>재발급 후 제출 시부터 급여</td>
            </tr>
            <tr>
                <td>소견서·진단서로 대체</td>
                <td><span class="red">불가</span></td>
                <td>소견서·진단서는 의뢰서 갈음 불가 (100% 유지)</td>
            </tr>
            <tr>
                <td>유효기간 14일 초과</td>
                <td>재발급 후 제출</td>
                <td>초과 기간 진료분은 100% 본인부담</td>
            </tr>
        </table>
        <div class="box-danger">
            <b>🚫 절대 주의:</b> 소견서나 진단서는 「요양급여의뢰서」를 대체할 수 없습니다.
            반드시 정식 서식의 요양급여의뢰서를 수령하세요.
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📌 상황4 - 한방병원 입원 중 양방 외진"):
        st.markdown("""
        <div class="box-warning">
            이 경우 <b>청구 주체가 달라</b> 혼동이 많습니다. 기관 유형에 따라 반드시 구분하세요.
        </div>
        <table class="t">
            <tr><th>상황</th><th>청구 주체</th><th>본인부담률</th></tr>
            <tr>
                <td>한방병원 입원 → 별개 양방기관 외래 의뢰</td>
                <td><span class="yel">의뢰받은 양방기관에서 직접 청구</span></td>
                <td>외래 본인부담률 적용</td>
            </tr>
            <tr>
                <td>양·한방 협진 기관 내 (동일 기관)</td>
                <td><span class="grn">한방 입원기관에서 통합 청구</span></td>
                <td>입원 본인부담률 적용</td>
            </tr>
        </table>
        <div class="box-purple">
            📜 근거: 복지부 보관 65720-295호(1996.3.6.) / 복지부 고시 제2014-126호
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📌 상황5 - 의료급여 수급권자 타기관 이용"):
        st.markdown("""
        <table class="t">
            <tr><th>수급권자 유형</th><th>이용 조건</th><th>본인부담</th></tr>
            <tr>
                <td>1종 수급권자</td>
                <td>선택의료급여기관 거쳐 의뢰 받은 경우</td>
                <td><span class="grn">본인부담 면제 또는 소액</span></td>
            </tr>
            <tr>
                <td>2종 수급권자</td>
                <td>의뢰서 있는 경우</td>
                <td><span class="grn">정상 본인부담</span></td>
            </tr>
            <tr>
                <td>1·2종 공통</td>
                <td>의뢰서 없이 타기관 방문</td>
                <td><span class="red">전액 본인부담</span></td>
            </tr>
            <tr>
                <td>입원 중 외진 (의뢰서 있음)</td>
                <td>적법 의뢰 절차 이행</td>
                <td><span class="grn">급여 적용</span></td>
            </tr>
        </table>
        <div class="box-info">
            <b>📌 의료급여 특이사항:</b><br>
            · 1종 수급권자 입원 시 본인부담 없음 (단, 법정 비급여·전액본인부담 제외)<br>
            · 65세 이상 임플란트: 1종 10%, 2종 20%<br>
            · 정신질환 입원 정액수가 기관에서 타기관 외래 의뢰 시 행위별 수가로 청구 가능
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 3: 원내처방 원칙
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "💊 원내처방 원칙 & 사유":
    st.markdown('<div class="sec-title">💊 원내처방 원칙 및 사유 상세 정리</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box-danger">
        <b>🔴 대원칙:</b> 입원환자를 타기관으로 진료의뢰한 경우, 의뢰받은 기관에서 처방한 약제는
        <b>반드시 원내처방이 원칙</b>입니다. 원외처방전(약국 조제용)은 원칙적으로 발행 불가.
    </div>
    <div class="box-purple">
        📜 <b>근거 1 – 요양급여기준 별표1 바항:</b> "요양기관은 요양급여에 필요한 약제·치료재료를 직접 구입하여 가입자 등에게 지급하여야 한다"<br>
        📜 <b>근거 2 – 보험급여팀-204호 (2008.1.24.):</b> "의뢰받은 병원에서 처방한 약제는 병원에 입원 중인 환자에 대한 처방이므로 의뢰받은 병원에서 원내처방해야 하며, 진료내역은 의뢰한 병원에서 HIRA에 청구"
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="sub-title">✅ 원내처방 원칙 이유 (5가지)</div>', unsafe_allow_html=True)
        items = [
            ("입원 상태 = 약제 직접 지급 의무", "요양기관은 입원환자에게 약제를 직접 구입·지급할 의무가 있음"),
            ("원외처방 = 입원 상태와 불일치", "환자가 약국을 직접 이용하는 것은 입원 중 불가"),
            ("이중청구 방지", "원외처방 + 입원청구 시 이중청구 문제 발생"),
            ("투약 관리 책임", "입원 중 복용 약제는 병원이 관리 책임을 짐"),
            ("건강보험 급여체계 준수", "약제비 급여 체계상 입원환자 약제는 원내처방으로 관리"),
        ]
        for title, desc in items:
            st.markdown(f"""
            <div style="background:#f1f8e9;border-left:3px solid #4caf50;
            padding:10px 14px;margin:6px 0;border-radius:0 7px 7px 0;color:#1b5e20;font-size:0.88rem;">
                <b style="color:#2e7d32;">✅ {title}</b><br>
                <span style="color:#37474f;">{desc}</span>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="sub-title">⚠️ 원내처방 예외 인정 사유 (3가지)</div>', unsafe_allow_html=True)
        exceptions = [
            ("약제 미구비 시 입원기관 원내처방",
             "의뢰받은 기관에 해당 약제 없음 → 처방내역을 의뢰한 기관(원 입원기관)에 통보 → 입원기관에서 원내처방 후 청구",
             "orange"),
            ("정신질환자 위험군 원내 직접조제",
             "조현병·조울증 등으로 자신/타인 해칠 우려 있는 정신질환자 → 원내 직접조제 가능 (약사법 제23조④③)",
             "blue"),
            ("마약류 등 특수 약제",
             "마약류 관리에 관한 법률에 따른 특수 약제는 별도 기준에 따라 처리 (마약류 취급자에서만 취급 가능)",
             "purple"),
        ]
        colors = {"orange": ("#ff9800","#ffe0b2","#fff3e0"), "blue": ("#0288d1","#b3e5fc","#e1f5fe"), "purple": ("#9c27b0","#e1bee7","#f3e5f5")}
        for title, desc, color in exceptions:
            bc, tc, bg = colors[color]
            st.markdown(f"""
            <div style="background:#fffde7;border:1px solid #ffe082;
            padding:12px 16px;margin:8px 0;border-radius:8px;font-size:0.87rem;">
                <b style="color:#e65100;">⚠️ {title}</b><br>
                <span style="color:#37474f;line-height:1.7;">{desc}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">📋 약제 처리 의사결정 흐름도</div>', unsafe_allow_html=True)

    st.markdown("""
    <table class="t">
        <tr>
            <th style="width:100px;text-align:center;">단계</th>
            <th style="width:160px;">주체</th>
            <th>처리 내용</th>
        </tr>
        <tr>
            <td style="text-align:center;vertical-align:middle;">
                <span style="display:inline-block;background:#1565c0;color:#fff;
                padding:4px 10px;border-radius:6px;font-weight:700;font-size:0.82rem;
                white-space:nowrap;">STEP 1</span>
            </td>
            <td>입원기관 A</td>
            <td>진료의뢰서 발급 → 환자를 타기관 B로 외진 의뢰</td>
        </tr>
        <tr>
            <td style="text-align:center;vertical-align:middle;">
                <span style="display:inline-block;background:#1565c0;color:#fff;
                padding:4px 10px;border-radius:6px;font-weight:700;font-size:0.82rem;
                white-space:nowrap;">STEP 2</span>
            </td>
            <td>타기관 B</td>
            <td>외래 진료 실시 → 처방 필요 판단 → <b>B기관 원내 약제 재고 확인</b></td>
        </tr>
        <tr style="background:#f1f8e9;">
            <td style="text-align:center;vertical-align:middle;">
                <span style="display:inline-block;background:#2e7d32;color:#fff;
                padding:4px 10px;border-radius:6px;font-weight:700;font-size:0.82rem;
                white-space:nowrap;">CASE A</span>
            </td>
            <td><span class="grn">약제 있음 (B기관)</span></td>
            <td>① B기관에서 <b>원내처방</b> 및 투약<br>② 처방내역 A기관에 서면 통보<br>③ A기관이 해당 내역 포함하여 HIRA 청구</td>
        </tr>
        <tr style="background:#fff8e1;">
            <td style="text-align:center;vertical-align:middle;">
                <span style="display:inline-block;background:#e65100;color:#fff;
                padding:4px 10px;border-radius:6px;font-weight:700;font-size:0.82rem;
                white-space:nowrap;">CASE B</span>
            </td>
            <td><span class="yel">약제 없음 (B기관)</span></td>
            <td>① B기관에서 <b>처방내역만 A기관에 통보</b> (원외처방전 발행 절대 불가)<br>② A기관에서 해당 약제 <b>원내처방</b> 및 투약<br>③ A기관이 HIRA 청구</td>
        </tr>
        <tr style="background:#f9f0ff;">
            <td style="text-align:center;vertical-align:middle;">
                <span style="display:inline-block;background:#6a1b9a;color:#fff;
                padding:4px 10px;border-radius:6px;font-weight:700;font-size:0.82rem;
                white-space:nowrap;">CASE C</span>
            </td>
            <td><span style="color:#6a1b9a;font-weight:700;">정신질환 위험군</span></td>
            <td>① 조현병·조울증 등 위험 환자 해당 여부 확인<br>② 해당 시 원내 직접조제 가능 (약사법 제23조④③ 적용)<br>③ 원외처방전 발행 불가 원칙 유지</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box-warning">
        <b>⚠️ 실무 핵심 3가지:</b><br>
        ① 어떤 경우든 <span class="red">원외처방전(약국용)은 발행하지 않는 것이 원칙</span><br>
        ② 처방내역 통보는 반드시 <b>서면 또는 공식 통보</b>로 해야 추후 심사 대응 가능<br>
        ③ A기관 HIRA 청구 시 <b>특정내역 MJ006</b>에 의뢰받은 기관정보·의뢰일자 기재 필수
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🧪 원내처방 vs 원외처방 비교 정리"):
        st.markdown("""
        <table class="t">
            <tr><th>항목</th><th>원내처방</th><th>원외처방</th></tr>
            <tr><td>처방 방식</td><td>병원 내 약국에서 직접 조제·투약</td><td>처방전 발급 → 외부 약국 조제</td></tr>
            <tr><td>입원환자 적용</td><td><span class="grn">원칙 적용</span></td><td><span class="red">원칙적 불가</span></td></tr>
            <tr><td>외진 처방</td><td><span class="grn">적용</span></td><td><span class="red">불가</span></td></tr>
            <tr><td>청구 방법</td><td>입원 기관에서 통합 청구</td><td>환자가 약국에서 별도 수납</td></tr>
            <tr><td>처방전 유효기간</td><td>해당 없음</td><td>발급일 포함 3일</td></tr>
        </table>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 4: 원외처방 안 되는 사유
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🚫 원외처방 안 되는 사유":
    st.markdown('<div class="sec-title">🚫 원외처방이 금지되는 사유 완전 정리</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box-danger">
        <b>🔴 원외처방이란?</b> 의원·병원에서 처방전을 발행하여 외부 약국에서 조제받는 방식.
        <b>입원환자</b>의 경우 원외처방이 원칙적으로 금지됩니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">🚫 원외처방 금지 상황 전체 목록</div>', unsafe_allow_html=True)
    st.markdown("""
    <table class="t">
        <tr><th width="250">상황</th><th width="160">원외처방 여부</th><th>근거 / 이유</th></tr>
        <tr>
            <td>입원환자 약제 (모든 경우)</td>
            <td><span class="red">원외처방 금지</span></td>
            <td>요양급여기준 별표1 바항 – 요양기관 직접 구입·지급 의무</td>
        </tr>
        <tr>
            <td>타기관 외진 후 처방 (입원 상태 유지 중)</td>
            <td><span class="red">원외처방 금지</span></td>
            <td>입원 중이므로 원내처방 원칙 적용</td>
        </tr>
        <tr>
            <td>주사제·수액류</td>
            <td><span class="red">원외처방 금지</span></td>
            <td>요양기관 내에서만 투여 가능한 약제</td>
        </tr>
        <tr>
            <td>마약류 (입원환자)</td>
            <td><span class="yel">원외처방 엄격 제한</span></td>
            <td>마약류 관리에 관한 법률 별도 기준 적용</td>
        </tr>
        <tr>
            <td>정신건강의학과 위험 입원환자<br>(조현병·조울증 등 위험군)</td>
            <td><span class="yel">원내 직접조제 원칙</span></td>
            <td>약사법 제23조④③ – 자신/타인 해칠 우려 시</td>
        </tr>
        <tr>
            <td>요양병원 정액수가 입원환자 외진 약제</td>
            <td><span class="yel">원내처방 원칙</span></td>
            <td>정액수가에 약제비 포함 – 별도 원외처방 불가</td>
        </tr>
        <tr>
            <td>외진 기관 약제 미구비로 인한 임의 원외처방</td>
            <td><span class="red">원외처방 금지</span></td>
            <td>약제 없으면 입원기관에 통보 → 입원기관 원내처방 해야 함</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">✅ 원외처방이 허용되는 예외 상황</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="box-success">
        <b>✅ 외래 환자 (비입원)</b><br>
        순수 외래환자는 원외처방이 원칙 (약사법 제23조 기준). 입원 상태가 아닌 경우에 해당.
    </div>
    <div class="box-success">
        <b>✅ 희귀의약품·특수약제</b><br>
        원내 구비 불가한 경우 예외적 원외처방 가능 (개별 고시 확인 필수)
    </div>
    <div class="box-success">
        <b>✅ 일부 항암제 외래 처방</b><br>
        외래 항암화학요법 시 처방전 발급 가능 (급여기준 별도 확인)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box-danger">
        <b>🚫 퇴원 시 처방전 – 원외처방 불가 (주의!):</b><br>
        퇴원 당일 발급하는 처방전도 <b>입원 중 발급이므로 원칙적으로 원외처방 불가</b>입니다.<br><br>
        · 퇴원 후 외래 첫 방문 시 처방전을 발급하는 것이 원칙<br>
        · 단, 퇴원 당일 퇴원처방전은 실무적으로 발급되고 있으나, 
          <b>이는 입원기간이 아닌 퇴원 당일 외래 처방으로 구분</b>되어 처리됨<br>
        · 요양급여기준상 입원 중 원외처방전 발행은 원칙적으로 불가하므로
          <b>퇴원 확정 전 미리 원외처방 처리하는 것은 절대 불가</b><br>
        · 퇴원 당일 처방: 퇴원일자로 외래 처방전 발급 (입원 청구와 구분하여 처리)
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">⛔ 원무직원 현장 실수 사례 TOP 7</div>', unsafe_allow_html=True)
    mistakes = [
        ("외진 처방 원외처방전으로 발행", "약국 조제 → 심사 시 부당청구로 삭감·환수"),
        ("의뢰받은 기관이 원외처방 발행 후 환자 약국 이용", "이중청구 문제 + 입원기관 청구 시 삭감"),
        ("약제 없다는 이유로 임의 원외처방전 발행", "올바른 처리: 입원기관에 통보 → 입원기관 원내처방"),
        ("정신건강의학과 위험 환자에게 원외처방전 발행", "원내 직접조제 원칙 위반 (약사법 위반)"),
        ("퇴원 예정 환자의 외진 처방을 미리 원외처방 처리", "퇴원 확정 전에는 불가"),
        ("의뢰서 없이 진료 후 처방전만 급여로 발행", "의뢰서 없으면 처방전도 100% 본인부담"),
        ("응급이 아닌 상황에서 편의상 원외처방 허용", "응급 예외 사유 해당 안 됨 → 부당청구"),
    ]
    for i, (title, impact) in enumerate(mistakes, 1):
        st.markdown(f"""
        <div style="background:#fff5f5;border-left:3px solid #f44336;
        padding:11px 14px;margin:7px 0;border-radius:0 7px 7px 0;font-size:0.89rem;">
            <b style="color:#c62828;">실수 {i}: {title}</b><br>
            <span style="color:#37474f;">📉 결과: {impact}</span>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 5: 청구 방법 & 수가 산정
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "📋 청구 방법 & 수가 산정":
    st.markdown('<div class="sec-title">📋 외진 청구 방법 및 수가 산정 가이드</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box-info">
        <b>📌 청구 4대 원칙:</b><br>
        ① <b>청구 주체:</b> 진료를 <u>의뢰한 기관</u>(원 입원기관)이 외진 내역 포함하여 HIRA에 청구<br>
        ② <b>수가 단가:</b> 의뢰<u>받은</u> 기관의 유형별 점수당 단가 + 종별 가산율 적용<br>
        ③ <b>본인부담률:</b> 의뢰<u>한</u> 기관 기준 → <b>입원 본인부담률</b> 적용 (외래 아님)<br>
        ④ <b>진료비 정산:</b> 의뢰한 기관 ↔ 의뢰받은 기관 간 상호 협의
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">💡 수가 산정 공식</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#ede7f6;border:1px solid #ce93d8;
    border-radius:12px;padding:22px 26px;margin:14px 0;">
        <div style="font-size:1.05rem;font-weight:700;color:#6a1b9a;margin-bottom:14px;font-family:'JetBrains Mono',monospace;">
            📐 외진 수가 계산 공식
        </div>
        <div style="font-size:0.95rem;line-height:2.4;font-family:'JetBrains Mono',monospace;color:#1a2a3a;">
            <span style="color:#006064;">진료비</span> &nbsp;=&nbsp;
            <span style="color:#2e7d32;">상대가치점수</span> &nbsp;×&nbsp;
            <span style="color:#e65100;">의뢰받은 기관의 유형별 점수당 단가</span> &nbsp;×&nbsp;
            <span style="color:#880e4f;">의뢰받은 기관의 종별 가산율</span>
            <br><br>
            <span style="color:#006064;">본인부담금</span> &nbsp;=&nbsp;
            진료비 &nbsp;×&nbsp; <span style="color:#2e7d32;">의뢰한 기관(입원기관)의 입원 본인부담률</span>
        </div>
        <div style="margin-top:14px;font-size:0.82rem;color:#546e7a;">
            ※ 단가와 종별 가산율은 의뢰받은 기관 기준 / 본인부담률은 의뢰한 기관(원 입원기관) 기준
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="sub-title">📊 종별 가산율</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>기관 종류</th><th>종별 가산율</th><th>점수당 단가</th></tr>
            <tr><td>상급종합병원</td><td><span class="blu">30%</span></td><td>상급종합 기준</td></tr>
            <tr><td>종합병원</td><td><span class="blu">25%</span></td><td>종합병원 기준</td></tr>
            <tr><td>병원</td><td><span class="blu">20%</span></td><td>병원 기준</td></tr>
            <tr><td>의원</td><td><span class="blu">15%</span></td><td>의원 기준</td></tr>
        </table>
        <div style="font-size:0.78rem;color:#455a64;margin-top:4px;">
            ※ <b>의뢰받은 기관</b>의 종별 가산율 적용
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="sub-title">📊 입원 본인부담률 기준</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>환자 유형</th><th>입원 본인부담률</th></tr>
            <tr><td>일반 건강보험 (상급종합 입원)</td><td><span class="yel">20%</span></td></tr>
            <tr><td>일반 건강보험 (종합·병원 입원)</td><td><span class="yel">20%</span></td></tr>
            <tr><td>산정특례 등록 (암·희귀질환 등)</td><td><span class="grn">5%</span></td></tr>
            <tr><td>의료급여 1종</td><td><span class="grn">0% (면제)</span></td></tr>
            <tr><td>의료급여 2종</td><td><span class="yel">10%</span></td></tr>
            <tr><td>차상위 1종</td><td><span class="grn">0~5%</span></td></tr>
        </table>
        <div style="font-size:0.78rem;color:#455a64;margin-top:4px;">
            ※ <b>의뢰한 기관(원 입원기관)</b>의 입원 본인부담률 적용
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sub-title">📝 청구 시 특정내역 기재 방법</div>', unsafe_allow_html=True)
    st.markdown("""
    <table class="t">
        <tr>
            <th style="width:130px;text-align:center;">특정내역 코드</th>
            <th style="width:200px;">항목명</th>
            <th>기재 내용</th>
            <th style="width:150px;">기재 기관</th>
        </tr>
        <tr>
            <td style="text-align:center;">
                <span style="display:inline-block;background:#4a148c;color:#fff;
                padding:4px 12px;border-radius:6px;font-weight:700;font-size:0.85rem;
                white-space:nowrap;">MJ006</span>
            </td>
            <td>의뢰/의뢰받은 기관 정보</td>
            <td>의뢰받은 의료기관기호 / 의뢰일자 기재<br>
                <span style="font-size:0.82rem;color:#455a64;">예: 12345678/20240101</span>
            </td>
            <td>의뢰한 기관 (입원기관)</td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <span style="display:inline-block;background:#4a148c;color:#fff;
                padding:4px 12px;border-radius:6px;font-weight:700;font-size:0.85rem;
                white-space:nowrap;">MT015</span>
            </td>
            <td>진료형태 구분코드</td>
            <td>'69' 기재 – 의뢰받아 시행한 타기관 진료 건임을 표시</td>
            <td>해당 시 기재</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    with st.expander("🚗 자동차보험 입원환자 외진 청구 - 건강보험과 다름"):
        st.markdown("""
        <div class="box-warning">
            <b>⚠️ 자동차보험은 건강보험과 청구 방식이 다릅니다!</b>
        </div>
        <table class="t">
            <tr><th>항목</th><th>건강보험</th><th>자동차보험</th></tr>
            <tr>
                <td>청구 주체</td>
                <td>의뢰한 기관에서 통합 청구</td>
                <td><span class="yel">의뢰한 기관·의뢰받은 기관 각각 별도 청구 가능</span></td>
            </tr>
            <tr>
                <td>의뢰서 종류</td>
                <td>요양급여의뢰서</td>
                <td><span class="yel">교통사고환자 진료의뢰서</span></td>
            </tr>
            <tr>
                <td>의뢰한 기관 기재</td>
                <td>MJ006: 의뢰받은 기관기호/일자</td>
                <td>MJ006: 의뢰받은 기관기호/일자</td>
            </tr>
            <tr>
                <td>의뢰받은 기관 기재</td>
                <td>별도 청구 없음</td>
                <td>MT015: '69' + MJ006: 의뢰한 기관기호/일자</td>
            </tr>
        </table>
        <div class="box-purple">
            📜 근거: 국토교통부고시 제2023-2호 「자동차보험진료수가에 관한 기준」<br>
            📜 국토교통부고시 제2023-3호 「자동차보험진료수가 심사업무처리에 관한 규정」
        </div>
        """, unsafe_allow_html=True)

    with st.expander("💡 실무 계산 예시 - 가상 케이스"):
        st.markdown("""
        <div class="card">
            <b style="color:#1565c0;">📋 케이스 예시</b><br>
            <span style="color:#37474f;">
            A병원(종합병원) 입원 환자 → B의원(의원급)으로 피부과 외진 의뢰<br>
            B의원에서 외래 진찰 실시 (초진 진찰료: 상대가치점수 가정 30점)
            </span>
            <br><br>
            <b style="color:#1976d2;">수가 계산:</b><br>
            <div style="font-family:'JetBrains Mono',monospace;font-size:0.87rem;color:#1a2a3a;margin-top:8px;line-height:2;">
                • 적용 단가: <span class="yel">의원 점수당 단가</span> (B의원 기준)<br>
                • 적용 가산율: <span class="yel">의원 종별 가산율 15%</span> (B의원 기준)<br>
                • 적용 본인부담률: <span class="grn">입원 본인부담률 20%</span> (A병원 입원 기준)<br>
                • 청구 기관: <span class="grn">A병원(의뢰한 기관)</span>이 B의원 외진 내역 포함 청구
            </div>
        </div>
        <div class="box-info">
            <b>💡 핵심 포인트:</b> 단가·가산율은 의뢰받은 기관(B의원) 기준 / 본인부담률은 의뢰한 기관(A병원) 입원 기준
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 6: 선별집중심사 & 고가검사
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "🔍 선별집중심사 & 고가검사":
    st.markdown('<div class="sec-title">🔍 선별집중심사 & 고가검사 대응 가이드</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box-warning">
        <b>⚠️ 선별집중심사란?</b> 건강보험심사평가원이 진료비 증가율이 높거나 적정성이 의심되는 항목을 선정하여
        <b>집중 심사</b>하는 제도. 대상 항목 청구 시 <b>진료기록부 등 참고자료 첨부</b>가 사실상 필수입니다.
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["🧲 MRI 급여기준", "🔬 CT·초음파 기준", "☢️ PET-CT 기준", "📋 2024~2025 심사항목"])

    with tab1:
        st.markdown('<div class="sub-title">🧲 MRI 급여기준 상세 (2022년 강화 후 기준)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="box-danger">
            <b>📈 배경:</b> 뇌·뇌혈관 MRI 진료비 143억(2017) → 1,766억(2021), 1,135% 급증 →
            2022년 급여기준 강화, 2023년 지속 강화 → 지속적 선별집중심사 대상
        </div>
        <table class="t">
            <tr><th>MRI 부위</th><th>급여 인정 주요 조건</th><th>급여여부</th><th>심사 포인트</th></tr>
            <tr>
                <td><span class="b bb">뇌·뇌혈관</span></td>
                <td>뇌질환 확진·의증, 뇌졸중 의증, 뇌종양, 신경학적 이상 동반 두통·어지럼</td>
                <td><span class="grn">급여</span></td>
                <td>신경학적 검진 소견 기재 필수</td>
            </tr>
            <tr>
                <td><span class="b bb">뇌·뇌혈관</span></td>
                <td>단순 두통, 단순 어지럼 (기질적 원인 미확인, 신경학적 이상 없음)</td>
                <td><span class="red">비급여</span></td>
                <td>증상만으로는 급여 불인정 (2022 강화)</td>
            </tr>
            <tr>
                <td><span class="b bb">척추</span></td>
                <td>척추질환 확진·의증, 신경증상(방사통·마비) 동반, 수술 전·후</td>
                <td><span class="grn">급여</span></td>
                <td>신경증상 동반 여부 기재</td>
            </tr>
            <tr>
                <td><span class="b bb">척추</span></td>
                <td>단순 요통 (신경증상 없음)</td>
                <td><span class="red">비급여</span></td>
                <td>단순 통증만은 급여 제한</td>
            </tr>
            <tr>
                <td><span class="b bb">복부·골반</span></td>
                <td>악성종양, 간질환, 췌담도질환, 복강 내 종괴 등</td>
                <td><span class="grn">급여</span></td>
                <td>부위별 세부 기준 확인</td>
            </tr>
            <tr>
                <td><span class="b bb">근골격</span></td>
                <td>외상·골절·인대손상, 수술 전·후, 염증성 관절질환</td>
                <td><span class="yel">급여/비급여 혼재</span></td>
                <td>자동차보험은 별도 기준 적용</td>
            </tr>
        </table>
        <div class="box-info">
            <b>📋 MRI 판독소견서 필수 기재사항 (고시 제2024-159호 기준):</b><br>
            ① 임상정보 (병력, 검사 실시 사유 등)<br>
            ② 획득한 영상기법<br>
            ③ 조영제 사용 여부<br>
            ④ 뇌: 대뇌·소뇌·뇌간·뇌실·뇌실질외 공간 주요 이상소견 여부<br>
            ⑤ 혈관: 협착·폐색·동맥류 등 주요 이상소견 여부 (이상 시 세부 기술)
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="sub-title">🔬 CT 및 초음파 급여기준</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>검사 종류</th><th>급여 인정 기준</th><th>심사 주요 포인트</th><th>선별심사</th></tr>
            <tr>
                <td><span class="b bb">복부 CT</span></td>
                <td>복부질환 의심, 악성종양 확인·추적, 복통 원인 불명</td>
                <td>임상 증상, 선행 초음파 결과</td>
                <td><span class="yel">모니터링</span></td>
            </tr>
            <tr>
                <td><span class="b bb">흉부 CT</span></td>
                <td>폐질환, 폐암 의심, 종격동질환, 흉부X선 이상 소견</td>
                <td>흉부 X선 선행 결과 첨부</td>
                <td>일반 심사</td>
            </tr>
            <tr>
                <td><span class="b bb">두부 CT</span></td>
                <td>외상, 뇌출혈 의심, 응급 신경학적 증상</td>
                <td>응급 여부, 신경학적 증상 기재</td>
                <td>일반 심사</td>
            </tr>
            <tr>
                <td><span class="b bg">간 초음파</span></td>
                <td>만성간염·간경변 연 1회 / 간질환 의심</td>
                <td>연 1회 초과 시 사유 기재</td>
                <td><span class="yel">반복 시 집중심사</span></td>
            </tr>
            <tr>
                <td><span class="b bg">갑상선 초음파</span></td>
                <td>결절 발견, 악성 의심, 갑상선 질환</td>
                <td>촉진 소견 또는 이전 검사 결과</td>
                <td>일반 심사</td>
            </tr>
            <tr>
                <td><span class="b bg">심장 초음파</span></td>
                <td>심질환 확진, 판막질환, 심부전 평가</td>
                <td>심전도·흉부X선 선행 결과</td>
                <td>일반 심사</td>
            </tr>
            <tr>
                <td><span class="b bg">신장·방광 초음파</span></td>
                <td>신장·방광질환 확인 (급여 확대 이후)</td>
                <td>증상·검사 소견 기재</td>
                <td>일반 심사</td>
            </tr>
        </table>
        <div class="box-warning">
            <b>⚠️ 반복 검사 핵심 주의:</b> 동일 부위 단기간 반복 시행은 선별집중심사 대상.
            진료기록부에 <b>반복 시행 사유, 임상 변화, 이전 검사 비교</b>를 반드시 기재하세요.
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="sub-title">☢️ PET-CT 급여기준 상세</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="box-info">
            <b>💡 2022.8.1.부터 산정특례 환자 PET-CT 적용 확대:</b><br>
            암 치료 목적 외래·입원·CT·MRI·PET-CT 급여비용의 <b>5%만 본인부담</b> (산정특례 등록 환자)
        </div>
        <table class="t">
            <tr><th>PET-CT 급여 적응증</th><th>급여 인정 조건</th><th>필수 첨부 서류</th></tr>
            <tr>
                <td>악성종양 병기 결정</td>
                <td>CT·MRI로 병기 결정 불충분 시</td>
                <td>병리조직 확진 결과, 이전 CT·MRI</td>
            </tr>
            <tr>
                <td>암 재발 여부 확인</td>
                <td>종양표지자 상승 등 재발 임상적 의심</td>
                <td>종양표지자 검사 결과, 임상 소견</td>
            </tr>
            <tr>
                <td>치료 효과 판정</td>
                <td>항암·방사선 치료 종료 후</td>
                <td>치료 경과 기록, 이전 영상 결과</td>
            </tr>
            <tr>
                <td>원발소 불명 암</td>
                <td>기타 검사로 원발소 확인 불가</td>
                <td>타 검사 결과 전체</td>
            </tr>
        </table>
        <div class="box-danger">
            <b>🚫 PET-CT 비급여 상황:</b><br>
            · 건강검진 목적<br>
            · 치료방침 없이 경과 관찰 목적<br>
            · 급여 기준 이외 반복 시행<br>
            · 암 진단 전 단순 의심 단계 (병리 확진 전)
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="sub-title">📋 2024~2025 선별집중심사 주요 대상 항목</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>보험 유형</th><th>선별집중심사 항목</th><th>지정 연도</th><th>심사 주요 포인트</th></tr>
            <tr>
                <td><span class="b bo">자동차보험</span></td>
                <td>척추 MRI</td>
                <td>2025</td>
                <td>경상환자 과다 처방, 임상적 필요성</td>
            </tr>
            <tr>
                <td><span class="b bo">자동차보험</span></td>
                <td>복잡추나요법</td>
                <td>2025 신규</td>
                <td>진료비 급증 항목, 적응증 기재</td>
            </tr>
            <tr>
                <td><span class="b bo">자동차보험</span></td>
                <td>첩약</td>
                <td>2024→2025 연속</td>
                <td>처방 적정성, 진료기록 근거</td>
            </tr>
            <tr>
                <td><span class="b bo">자동차보험</span></td>
                <td>경상환자 장기입원</td>
                <td>2024→2025 연속</td>
                <td>입원 필요성, 기간 적정성</td>
            </tr>
            <tr>
                <td><span class="b bo">자동차보험</span></td>
                <td>약침</td>
                <td>2024→2025 연속</td>
                <td>시행 횟수·사유 적정성</td>
            </tr>
            <tr>
                <td><span class="b bb">건강보험</span></td>
                <td>뇌·뇌혈관 MRI</td>
                <td>지속</td>
                <td>신경학적 증상 동반 여부</td>
            </tr>
            <tr>
                <td><span class="b bb">건강보험</span></td>
                <td>근골격계 초음파</td>
                <td>지속 모니터링</td>
                <td>반복 시행 사유, 부위별 기준</td>
            </tr>
            <tr>
                <td><span class="b bb">건강보험</span></td>
                <td>고가 항암제 (허가초과)</td>
                <td>지속</td>
                <td>허가초과 신청·승인 여부</td>
            </tr>
        </table>
        <div class="box-info">
            <b>📌 선별집중심사 대응 전략:</b><br>
            ① 해당 항목 처방·시행 전 <b>급여기준 재확인</b><br>
            ② 진료기록부에 <b>적응증·시행 사유 명확히 기재</b><br>
            ③ 선행 검사 결과 보관 (이전 CT, X선, 혈액검사 등)<br>
            ④ 이의신청 기한: 심사결과 통보 후 <b>90일 이내</b>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 7: 진료기록부·서류 발급
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "📄 진료기록부·서류 발급":
    st.markdown('<div class="sec-title">📄 진료기록부 및 서류 발급 실무 가이드</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📋 심사 참고자료 작성", "📑 의무기록 사본 발급", "✉️ 진료의뢰서 발급"])

    with tab1:
        st.markdown('<div class="sub-title">📋 고가검사·선별심사 시 HIRA 심사 참고자료</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="box-warning">
            <b>⚠️ 핵심:</b> 참고자료 첨부 없이 청구 → 급여→비급여 전환 또는 삭감 위험 높음.
            검사 시행 전부터 진료기록부 기재를 철저히 하는 것이 최선의 대비책입니다.
        </div>
        <table class="t">
            <tr><th width="150">검사·행위</th><th>필수 첨부 서류 및 진료기록 기재 사항</th><th width="170">미비 시 결과</th></tr>
            <tr>
                <td><span class="b bb">MRI (뇌·뇌혈관)</span></td>
                <td>
                    ① 진료기록부: 신경학적 검진 소견 상세 기재<br>
                    ② 증상 발현 시기·경과 및 기질적 원인 감별 필요성 기술<br>
                    ③ 영상판독소견서: 임상정보·영상기법·조영제 여부 포함<br>
                    ④ 선행 CT 결과 (있는 경우 반드시 첨부)
                </td>
                <td><span class="red">급여→비급여 / 전액 삭감</span></td>
            </tr>
            <tr>
                <td><span class="b bb">MRI (척추·기타)</span></td>
                <td>
                    ① 진료기록부: 주소증, 신경증상(방사통·마비 등) 기재<br>
                    ② 영상판독소견서 (임상정보 포함)<br>
                    ③ 이전 X선·CT 결과
                </td>
                <td><span class="red">삭감 가능성 높음</span></td>
            </tr>
            <tr>
                <td><span class="b bg">초음파 (반복)</span></td>
                <td>
                    ① 이전 검사와의 기간 및 반복 시행 사유 명시<br>
                    ② 임상적 변화 소견 기재 (단순 경과 관찰은 불인정)<br>
                    ③ 검사 결과지 전체 보관
                </td>
                <td><span class="yel">반복 시행 불인정</span></td>
            </tr>
            <tr>
                <td><span class="b bp">PET-CT</span></td>
                <td>
                    ① 병리조직 확진 결과 (조직검사 보고서)<br>
                    ② 이전 CT·MRI 결과<br>
                    ③ 검사 목적 명시 (병기결정·재발확인·효과판정 구분)<br>
                    ④ 종양표지자 검사 결과 (재발 의심 시)
                </td>
                <td><span class="red">전액 비급여 전환</span></td>
            </tr>
            <tr>
                <td><span class="b bo">고가 항암제</span></td>
                <td>
                    ① 병리보고서 (암종, 조직형, 바이오마커 결과)<br>
                    ② 급여 기준 해당 여부 확인 근거<br>
                    ③ 이전 치료력 (선행 요법 실패 기록)<br>
                    ④ 허가초과 시 별도 사용승인 신청·결과
                </td>
                <td><span class="red">전액 삭감·환수</span></td>
            </tr>
        </table>
        <div class="box-info">
            <b>📌 진료기록부 기재 황금 원칙:</b><br>
            ❌ 나쁜 예: "두통으로 MRI 시행" (사유 불충분)<br>
            ✅ 좋은 예: "우측 편측성 박동성 두통 2주 지속, 신경학적 이상 소견(우안 시야장애) 동반되어 뇌기질적 원인 감별 위해 뇌 MRI 시행"
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="sub-title">📑 의무기록 사본 발급 절차 및 기준</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>발급 목적</th><th>신청자</th><th>필요 서류</th><th>비용</th><th>처리 기간</th></tr>
            <tr>
                <td>환자 본인 요청</td>
                <td>환자 본인</td>
                <td>신분증</td>
                <td>유료 (기관별 상이)</td>
                <td>즉시~수일</td>
            </tr>
            <tr>
                <td>법정대리인 요청</td>
                <td>법정대리인</td>
                <td>신분증 + 관계증명서</td>
                <td>유료</td>
                <td>즉시~수일</td>
            </tr>
            <tr>
                <td>대리인 (위임) 요청</td>
                <td>위임받은 자</td>
                <td>신분증 + 위임장 + 환자 신분증 사본</td>
                <td>유료</td>
                <td>즉시~수일</td>
            </tr>
            <tr>
                <td>보험사 제출용</td>
                <td>환자 또는 위임인</td>
                <td>신분증 + 위임장 (타인 신청 시)</td>
                <td>유료</td>
                <td>즉시~수일</td>
            </tr>
            <tr>
                <td>HIRA 심사자료</td>
                <td>요양기관 담당자</td>
                <td>심사청구 시 자동 첨부</td>
                <td>무료</td>
                <td>청구 시 동시</td>
            </tr>
            <tr>
                <td>법원·수사기관 제출</td>
                <td>법원·수사기관</td>
                <td>공문서</td>
                <td>무료</td>
                <td>공문 접수 후</td>
            </tr>
        </table>
        <div class="box-warning">
            <b>⚠️ 의무기록 보존 기간 (의료법 제22조):</b><br>
            · 진료기록부: <b>10년</b><br>
            · 처방전: <b>2년</b><br>
            · 수술기록: <b>10년</b><br>
            · 방사선 사진(영상): <b>5년</b><br>
            · 간호기록부: <b>5년</b>
        </div>
        <div class="box-danger">
            <b>🚫 발급 거부 가능 상황:</b><br>
            · 환자 본인·법정대리인·위임자 외 제3자 요청 (개인정보보호법)<br>
            · 위임장 불비 (인감도장 없음, 위임 범위 불명확)<br>
            · 고인의 경우: 유족 관계 증명 필요 (상속인 확인)
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="sub-title">✉️ 진료의뢰서 종류 및 발급 실무</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>서류명</th><th>사용 상황</th><th>유효기간</th><th>주요 기재사항</th><th>주의</th></tr>
            <tr>
                <td><span class="b bb">요양급여의뢰서</span></td>
                <td>건강보험 환자의 타기관 의뢰 (상급기관 포함)</td>
                <td><b>발급일 포함 14일</b></td>
                <td>진료의뢰 목적, 현 진단명, 치료 경과, 의뢰 의사 서명</td>
                <td>원본 제출 원칙</td>
            </tr>
            <tr>
                <td><span class="b bg">의료급여의뢰서</span></td>
                <td>의료급여 수급권자 타기관 의뢰</td>
                <td><b>발급일 포함 14일</b></td>
                <td>의뢰 사유, 진단명, 수급자 정보</td>
                <td>선택의료급여기관에서 발급</td>
            </tr>
            <tr>
                <td><span class="b bo">교통사고 진료의뢰서</span></td>
                <td>자동차보험 환자 타기관 의뢰</td>
                <td>별도 기준</td>
                <td>사고 경위, 진단명, 의뢰 목적</td>
                <td>자동차보험 별도 서식 사용</td>
            </tr>
        </table>
        <div class="box-danger">
            <b>🚫 절대 금지사항:</b><br>
            ① 소견서·진단서로 요양급여의뢰서 대체 → <b>불가</b> (100% 본인부담 유지)<br>
            ② 유효기간(14일) 경과 의뢰서 → 효력 없음 (재발급 필요)<br>
            ③ 사본만 제출 → 원본 제출 전까지 급여 미적용<br>
            ④ 재의뢰 불가 상황: 의뢰받은 기관이 또 타기관으로 재의뢰하는 경우 원칙적 불가 (일부 예외 있음)
        </div>
        <div class="box-info">
            <b>📌 의뢰서 발급 실무 팁:</b><br>
            · 의뢰서 발급일자·유효기간을 환자에게 명확히 안내<br>
            · 원본 1부 환자 전달 / 사본 병원 보관 (향후 분쟁 방지)<br>
            · 외진 후 처리 결과를 진료기록부에 기재 (외진 일자, 기관명, 진료 결과)
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 8: 특수 케이스 Q&A
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "⚡ 특수 케이스 Q&A":
    st.markdown('<div class="sec-title">⚡ 실무 특수 케이스 Q&A</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="box-info">
        <b>📌 이 섹션은</b> 원무·심사 실무에서 자주 발생하는 헷갈리는 케이스를 모아 명쾌하게 답변합니다.
    </div>
    """, unsafe_allow_html=True)

    qas = [
        {
            "q": "Q1. 한방병원 입원 중 내과 진료를 타 내과의원에 의뢰했습니다. 청구는 어디서 해야 하나요?",
            "tag": "🔵 청구",
            "a": """<b>답변:</b><br>
            한방병원(입원) → 별개의 내과의원(외래) 의뢰 시:<br><br>
            · 청구 주체: <span class="yel">의뢰받은 내과의원에서 직접 청구</span> (외래 본인부담률 적용)<br>
            · 단가·가산율: 내과의원 기준<br><br>
            단, 한방병원과 내과가 <b>동일 요양기관번호</b>를 사용하는 양·한방 협진 기관이라면:<br>
            → 한방 입원기관에서 통합 청구 (입원 본인부담률 적용)""",
            "law": "복지부 보관 65720-295호(1996.3.6.) / 복지부 고시 제2014-126호"
        },
        {
            "q": "Q2. 외진 기관에 약제가 없어 처방을 못 했습니다. 원외처방전을 발행해도 되나요?",
            "tag": "🔴 처방",
            "a": """<b>답변: 절대 안 됩니다.</b><br><br>
            올바른 처리 순서:<br>
            ① 외진 기관에서 <span class="yel">처방내역(처방 정보)만 원 입원기관에 통보</span><br>
            ② 원 입원기관에서 해당 약제를 <span class="grn">원내처방</span>으로 처리<br>
            ③ 원 입원기관이 HIRA 청구<br><br>
            <span class="red">원외처방전 발행 → 약국 조제 → 부당청구 → 심사 삭감·환수 위험!</span>""",
            "law": "요양급여기준 별표1 바항 / 보험급여팀-204호(2008.1.24.)"
        },
        {
            "q": "Q3. 입원 중 환자가 응급상황으로 타병원 응급실에서 진료받았습니다. 100% 본인부담인가요?",
            "tag": "🟠 응급",
            "a": """<b>답변: 응급상황은 예외 적용 가능합니다.</b><br><br>
            · 응급의료에 관한 법률에 따른 응급 처치: 의뢰서 없이도 급여 적용<br>
            · 응급실 내역은 해당 응급기관에서 건강보험 급여로 별도 청구<br>
            · 응급 처치 후 안정화 → 원 입원기관으로 귀원 후 사후 처리<br><br>
            <span class="red">단, 응급이 아닌 상황에서 편의상 타병원 이용은 응급 예외 해당 안 됨 → 100% 본인부담</span>""",
            "law": "응급의료에 관한 법률 / 요양급여기준 규칙"
        },
        {
            "q": "Q4. 정신건강의학과 입원 중 내과 질환으로 외진 의뢰 시 청구는 어떻게 하나요?",
            "tag": "🟣 정신건강",
            "a": """<b>답변:</b><br>
            정신질환 입원 중 정신과 의료진으로 진료 불가한 다른 진료과목 질환 발생 시:<br><br>
            ① 해당 기관 시설·인력으로 치료 곤란 판단 → 타기관 외래 의뢰 가능<br>
            ② 내과 진료 내역: <span class="grn">행위별 수가로 청구 가능</span> (정액수가와 별도)<br>
            ③ <span class="yel">의뢰 사유를 진료기록부에 구체적으로 기재 필수</span><br><br>
            단, 정신건강의학과 정액수가 산정 기관에서는 별도 산정 가능 항목 확인 필요""",
            "law": "의료급여수가 기준 Q&A / 요양급여기준 관련 행정해석"
        },
        {
            "q": "Q5. 차상위 1종 환자가 의뢰서 없이 상급종합병원을 이용했습니다. 100% 본인부담인가요?",
            "tag": "🟢 본인부담",
            "a": """<b>답변: 아닙니다. 차상위 1종·2종은 예외입니다.</b><br><br>
            · 일반 건강보험 가입자: 의뢰서 없이 상급종합병원 → 진찰료 <span class="red">100% 본인부담</span><br>
            · <span class="grn">차상위 1종·2종: 100% 적용 대상 제외 → 정상 본인부담률 적용</span><br>
            · 산정특례 등록 환자: 100% 적용 제외<br><br>
            원무에서 수납 시 환자의 건강보험 자격·유형을 반드시 확인하세요.""",
            "law": "국민건강보험법 시행령 별표2 제1호 나목 – 차상위·산정특례 예외 규정"
        },
        {
            "q": "Q6. 선별집중심사 통보를 받았습니다. 무엇을 준비해야 하나요?",
            "tag": "🔴 심사",
            "a": """<b>답변: 즉시 준비할 자료:</b><br><br>
            ① 진료기록부 원본 출력 (검사 시행 전후 기간 전체)<br>
            ② 영상판독소견서 (임상정보·영상기법·조영제 여부 포함된 것)<br>
            ③ 검사 적응증 근거 (신경학적 소견, 증상 기록)<br>
            ④ 선행 검사 결과 (이전 CT, X선 등)<br>
            ⑤ 의사 의견서 (필요 시 담당 의사 작성)<br><br>
            <span class="yel">이의신청 기한: 심사결과 통보 후 <b>90일 이내</b></span><br>
            HIRA 심사결과 조회: 요양기관업무포털 (biz.hira.or.kr)""",
            "law": "국민건강보험법 제87조 – 이의신청 / HIRA 심사결과 통보 절차"
        },
        {
            "q": "Q7. 외진 후 환자에게 어떤 영수증을 발급해야 하나요? 이중수납 우려가 있습니다.",
            "tag": "🔵 수납",
            "a": """<b>답변:</b><br>
            · 의뢰받은 기관이 환자에게 수납한 경우 → 해당 기관명으로 영수증 발급<br>
            · 청구는 의뢰한 기관에서 통합 청구 → 기관 간 정산 필요<br><br>
            <span class="yel">이중수납 방지를 위한 실무 처리:</span><br>
            ① 외진 전 두 기관 간 <b>정산 방법 사전 협의</b> (문서화 권고)<br>
            ② 의뢰받은 기관에서 환자 수납 시 → 입원기관에 해당 금액 통보<br>
            ③ 입원기관 청구 시 환자가 실제 납부한 금액 반영<br>
            ④ 정산 내역 보관 (추후 분쟁 방지)""",
            "law": "건강보험 청구 실무 / 기관 간 협의 사항"
        },
        {
            "q": "Q8. 의뢰서를 가지고 왔으나 유효기간(14일)이 1일 지났습니다. 어떻게 처리하나요?",
            "tag": "🟠 의뢰서",
            "a": """<b>답변:</b><br>
            유효기간 14일을 경과한 의뢰서는 효력이 없습니다.<br><br>
            · 해당 방문분: <span class="red">100% 본인부담</span> (소급 불가)<br>
            · 향후 방문분: 원 의뢰기관에서 <span class="grn">의뢰서 재발급</span> → 재발급 후 제출일부터 급여<br><br>
            <span class="yel">환자 안내:</span> 의뢰서 재발급을 위해 의뢰한 기관(원 입원기관)에 연락 → 재발급 후 본 기관에 재제출<br><br>
            긴급 시: 전화·팩스로 사전 확인 후 당일 원본 지참 가능한지 확인""",
            "law": "요양급여기준 규칙 제2조·제6조 / 의뢰서 유효기간 규정"
        },
    ]

    for qa in qas:
        # tag에서 이모지만 추출 (첫 단어), expander 제목은 순수 텍스트
        tag_emoji = qa['tag'].split()[0]
        expander_label = f"{tag_emoji} {qa['q']}"
        with st.expander(expander_label):
            st.markdown(f"""
            <div style="padding:16px 20px;background:#f5f9ff;border-radius:8px;
            color:#1a2a3a;line-height:1.9;font-size:0.91rem;">
                <span style="display:inline-block;background:#e3f2fd;color:#1565c0;
                font-size:0.75rem;font-weight:700;padding:2px 10px;border-radius:20px;
                margin-bottom:10px;">{qa['tag']}</span><br><br>
                {qa['a']}
            </div>
            <div class="box-purple" style="margin-top:12px;">
                📜 <b>관련 근거:</b> {qa['law']}
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 섹션 9: 빠른 체크리스트
# ══════════════════════════════════════════════════════════════════════════════
elif menu == "✅ 빠른 체크리스트":
    st.markdown('<div class="sec-title">✅ 외진 처리 빠른 체크리스트</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box-info">
        <b>📌 사용 방법:</b> 외진 발생 시 아래 체크리스트를 순서대로 확인하세요.
        체크하며 빠진 항목을 즉시 조치하세요.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="sub-title">📤 외진 의뢰 전 체크 (의뢰기관)</div>', unsafe_allow_html=True)
        pre = [
            "타기관 의뢰 필요성 – 주치의 판단 및 기록",
            "요양급여의뢰서 발급 – 정식 서식 사용",
            "의뢰서 기재 확인: 진단명·의뢰 사유·치료 경과·의사 서명",
            "의뢰서 원본 환자 전달 / 사본 병원 보관",
            "환자 안내: 의뢰서 미제출 시 100% 본인부담 고지",
            "외진 일자·기관·목적 진료기록부 기록",
            "약제 처방 예상 시 원내처방 처리 방침 안내",
            "의뢰서 유효기간 14일 내 사용 안내",
        ]
        for item in pre:
            st.checkbox(item, key=f"p_{item[:15]}")

        st.markdown('<div class="sub-title" style="margin-top:20px;">📥 외진 후 체크 (의뢰기관)</div>', unsafe_allow_html=True)
        post = [
            "의뢰받은 기관으로부터 진료내역 서면 수령",
            "처방내역 수령 – 원내처방 대상 약제 확인",
            "약제 미구비 건 → 원 입원기관에서 원내처방 처리",
            "외진 내역 HIRA 청구 준비 (특정내역 MJ006 기재)",
            "수가: 단가·가산율 의뢰받은 기관 기준 적용 확인",
            "본인부담률: 입원 본인부담률 적용 확인 (외래 아님)",
            "진료비 정산 – 의뢰받은 기관과 협의",
            "외진 결과 진료기록부 기재",
        ]
        for item in post:
            st.checkbox(item, key=f"q_{item[:15]}")

    with col2:
        st.markdown('<div class="sub-title">🔍 고가검사 청구 전 체크</div>', unsafe_allow_html=True)
        exam = [
            "검사 적응증 진료기록부 구체적 기재 확인",
            "영상판독소견서: 임상정보·영상기법·조영제 포함",
            "선행 검사 결과 확인 및 비교 기재 여부",
            "MRI: 신경학적 증상 동반 여부 기재",
            "초음파 반복: 반복 시행 사유 기재",
            "PET-CT: 병리조직 결과·이전 CT·목적 첨부",
            "선별집중심사 대상 항목 해당 여부 사전 확인",
            "허가초과 항암제: 사용승인 여부 확인",
        ]
        for item in exam:
            st.checkbox(item, key=f"e_{item[:15]}")

        st.markdown('<div class="sub-title" style="margin-top:20px;">💰 본인부담 100% 상황 체크</div>', unsafe_allow_html=True)
        burden = [
            "의뢰서 없이 상급종합 이용 여부 확인",
            "의뢰서 원본 제출 여부 확인 (사본 불인정)",
            "의뢰서 유효기간 14일 이내인지 확인",
            "차상위·산정특례 환자 여부 확인 (예외 해당)",
            "환자에게 100% 본인부담 사전 고지 완료",
            "약제 처방 시 약국도 100% 본인부담 안내 완료",
        ]
        for item in burden:
            st.checkbox(item, key=f"b_{item[:15]}")

    st.markdown("---")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="sub-title">📞 주요 문의처</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>기관</th><th>연락처</th><th>주요 업무</th></tr>
            <tr><td>건강보험심사평가원 (HIRA)</td><td><span class="blu">1644-2000</span></td><td>심사기준·청구방법</td></tr>
            <tr><td>국민건강보험공단</td><td><span class="blu">1577-1000</span></td><td>자격·보험료</td></tr>
            <tr><td>보건복지부 보험급여과</td><td><span class="blu">044-202-2637</span></td><td>급여기준 해석</td></tr>
            <tr><td>HIRA 요양기관포털</td><td><span class="blu">biz.hira.or.kr</span></td><td>심사청구·조회</td></tr>
        </table>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="sub-title">🔗 주요 참고 사이트</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="t">
            <tr><th>사이트명</th><th>용도</th></tr>
            <tr><td>HIRA 공식 홈페이지</td><td>급여기준 검색, 심사 조회</td></tr>
            <tr><td>국가법령정보센터 (law.go.kr)</td><td>요양급여기준 등 법령 원문</td></tr>
            <tr><td>보건복지부 홈페이지 (mohw.go.kr)</td><td>고시·행정해석 확인</td></tr>
            <tr><td>HIRA 인정기준 조회시스템</td><td>검사별 급여기준 상세 조회</td></tr>
        </table>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box-warning" style="margin-top:20px;">
        <b>⚠️ 이의신청 기한 알림:</b><br>
        심사결과 통보 후 <b>90일 이내</b> 이의신청 가능 (국민건강보험법 제87조)<br>
        심사 삭감 내역 수령 즉시 진료기록부·참고자료 검토 시작 권장
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 공통 푸터
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    ⚕️ 본 가이드는 실무 참고용입니다. 법령 개정 시 내용이 변경될 수 있으므로
    <a href="https://www.hira.or.kr" target="_blank">HIRA 공식 포털</a> 및 최신 고시 교차 확인 바랍니다.<br>
    건강보험심사평가원 1644-2000 &nbsp;|&nbsp; 국민건강보험공단 1577-1000 &nbsp;|&nbsp; 보건복지부 보험급여과 044-202-2637
</div>
""", unsafe_allow_html=True)
