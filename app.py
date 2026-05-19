import streamlit as st
import datetime

# ---------------- 網頁設定 ----------------
st.set_page_config(
    page_title="微型 TimeTree",
    layout="wide"
)

# ---------------- Session State ----------------
if "events" not in st.session_state:
    st.session_state.events = []

# ---------------- 群組選擇 ----------------
mode = st.radio(
    "選擇群組",
    ["學生", "老師", "家長會", "校友會"],
    horizontal=True
)

# ---------------- 左右欄 ----------------
l, r = st.columns(2)

# ================= 左欄：新增行程 =================
with l:

    st.write("## 新增行程")

    t1 = st.text_input("行程主旨")

    t3 = st.date_input(
        "日期選擇",
        datetime.date.today()
    )

    t4 = st.time_input("時間選擇")

    n1 = st.number_input(
        "行程開始前幾分鐘提醒？",
        min_value=0,
        max_value=60,
        value=15
    )

    if st.button("新增行程"):

        st.session_state.events.append({
            "title": t1,
            "date": t3,
            "time": t4,
            "remind": n1
        })

        st.success("行程已加入！")
        st.rerun()

# ================= 右欄：記憶 + 刪除 =================
with r:

    st.write("## 已儲存行程")

    if not st.session_state.events:
        st.info("目前尚無任何行程")

    else:

        for idx, event in enumerate(st.session_state.events):

            col_a, col_b = st.columns([4, 1])

            with col_a:
                st.write(f"### 📌 {event['title']}")
                st.write(f"📅 {event['date']}  🕒 {event['time']}")
                st.write(f"⏰ 提前 {event['remind']} 分鐘")

            with col_b:
                if st.button("刪除", key=f"del_{idx}"):
                    st.session_state.events.pop(idx)
                    st.rerun()

            st.divider()

        # 最新行程
        st.write("### 最新行程預覽")

        latest = st.session_state.events[-1]

        st.success(latest["title"])
        st.write(f"📅 {latest['date']} 🕒 {latest['time']}")
