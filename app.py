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

        event_data = {
            "title": t1,
            "date": t3,
            "time": t4,
            "remind": n1
        }

        st.session_state.events.append(event_data)

        st.success("行程已加入！")

# ================= 右欄：記憶 + 預覽 =================
with r:

            # -------- 最新行程 --------
        st.write("### 最新行程預覽")

        latest = st.session_state.events[-1]
    
    st.write("## 已儲存行程（記憶功能）")

    if len(st.session_state.events) == 0:
        st.info("目前尚無任何行程")

    else:

        # -------- 所有歷史行程 --------
        st.write("### 行程清單")

        for idx, event in enumerate(st.session_state.events, start=1):

            st.write(f"### 📌 行程 {idx}")
            st.write(f"主旨：{event['title']}")
            st.write(f"日期：{event['date']}")
            st.write(f"時間：{event['time']}")
            st.write(f"提醒：提前 {event['remind']} 分鐘")
            st.divider()



        st.success(latest["title"])
        st.write(f"📅 {latest['date']}  🕒 {latest['time']}")
        st.write(f"⏰ 提醒 {latest['remind']} 分鐘前")
