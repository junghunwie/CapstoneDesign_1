import streamlit as st

# 배경을 흰색으로 설정하는 스타일 적용
def set_background():
    page_bg_style = """
    <style>
    body {
        background-color: white; /* 흰색 배경 */
    }
    .main {
        background: rgba(255, 255, 255, 0.9); /* 흰색 배경 유지 */
        padding: 2rem;
        border-radius: 10px;
    }
    .login-button {
        background: linear-gradient(to right, #B15EFF, #FEC163);
        color: white;
        font-weight: bold;
        padding: 0.8rem;
        border-radius: 25px;
        text-align: center;
        cursor: pointer;
        display: block;
        width: 100%;
        border: none;
    }
    .social-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 15px;
    }
    .social-buttons img {
        width: 40px;
        height: 40px;
        cursor: pointer;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #555;
    }
    .app-title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: black;
        margin-bottom: 20px;
    }
    </style>
    """
    st.markdown(page_bg_style, unsafe_allow_html=True)

# 배경을 흰색으로 설정
set_background()

# 앱 이름 표시
st.markdown("<div class='app-title'>DayPlanner</div>", unsafe_allow_html=True)

# 로그인 UI 구성
st.markdown("<h1 style='text-align: center; color: black;'>로그인</h1>", unsafe_allow_html=True)

with st.container():
    phone_number = st.text_input("휴대폰 번호", placeholder="010-1234-5678")
    password = st.text_input("비밀번호", type="password", placeholder="비밀번호 입력")
    
    # 로그인 버튼
    st.markdown("""
    <div style="text-align: center;">
        <button class="login-button">로그인</button>
    </div>
    """, unsafe_allow_html=True)

# ✅ 외부 로그인 버튼 (프로젝트 내부 이미지 사용)
st.markdown("<div class='social-buttons'>", unsafe_allow_html=True)
st.image(["KakaoTalk_logo.svg",
          "Naver_logo.png",
          "Google_logo.jpg",
          "Apple_logo.jpg"], 
         width=40, caption=["카카오", "네이버", "구글", "애플"])
st.markdown("</div>", unsafe_allow_html=True)

# 하단 링크
st.markdown("<div class='footer'>회원가입 | 비밀번호 찾기 | 로그인 문의</div>", unsafe_allow_html=True)


