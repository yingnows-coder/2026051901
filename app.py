import streamlit as st
import calendar
from datetime import date

# ---------------- 網頁設定 ----------------
st.set_page_config(
    page_title="微型 TimeTree",
    layout="wide"
)

# ---------------- Session State ----------------
if "announcement" not in st.session_state:
    st.session_state.announcement = "本週請記得繳交作業！"

# ---------------- Sidebar ----------------
with st.sidebar:

    st.write("## 行事曆群組")

    group = st.radio(
        "選擇群組",
        ["工作", "家庭", "學校"]
    )

    st.success(f"目前群組：{group}")

    st.divider()

    # 公告區
    st.write("### 系統公告")
    st.info(st.session_state.announcement)

    # Dialog
    @st.dialog("編輯公告")
    def edit_announcement():

        new_text = st.text_area(
            "修改公告內容",
            value=st.session_state.announcement
        )

        if st.button("儲存公告"):
            st.session_state.announcement = new_text
            st.rerun()

    if st.button("編輯公告"):
        edit_announcement()

# ---------------- Main Layout ----------------
left_col, right_col = st.columns([1, 1])

# -------- 左欄 --------
with left_col:

    st.write("## 新增行程")

    title = st.text_input("行程名稱")

    event_date = st.date_input(
        "日期",
        value=date.today()
    )

    event_time = st.time_input("時間")

    st.button("新增行程")
    
st.write("上面是大標題")
st.divider()
st.write("下面是內容區塊")

st.button("按鈕 A")
st.write("")  # 塞入一行空白間距
st.button("按鈕 B")

with st.popover("快速進階篩選"):
    st.checkbox("隱藏已過期行程")


# -------- 右欄 --------
with right_col:

    
    # ===== Tabs =====
    with st.container(border=True):

        st.write("## 行程總覽")

        tab1, tab2 = st.tabs(
            ["本月行程", "已封存行程"]
        )

        # -------- 本月行程 --------
        with tab1:

            st.write("### 本月行程")

            st.write("📌 開學典禮")
            st.write("🕘 09:00")

            st.divider()

            st.write("📌 專題會議")
            st.write("🕒 15:00")

        # -------- 已封存 --------
        with tab2:

            st.write("### 已封存行程")

            st.write("✅ 寒假旅遊")
            st.write("✅ 期末聚餐")
