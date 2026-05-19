import streamlit as st

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

    # 顯示公告
    st.write("### 系統公告")
    st.info(st.session_state.announcement)

    # -------- Dialog --------
    @st.dialog("編輯公告")
    def edit_announcement():

        new_text = st.text_area(
            "修改公告內容",
            value=st.session_state.announcement
        )

        if st.button("儲存公告"):
            st.session_state.announcement = new_text
            st.rerun()

    # 開啟 Dialog
    if st.button("編輯公告"):
        edit_announcement()

# ---------------- Main Layout ----------------
left_col, right_col = st.columns([1, 3])

# -------- 左欄 --------
with left_col:

    st.write("## 新增行程")

    st.info("請輸入新的行程資訊")

    title = st.text_input("行程名稱")

    date = st.date_input("日期")

    time = st.time_input("時間")

    st.button("新增行程")

# -------- 右欄 --------
with right_col:

    with st.container(border=True):

        st.write("## 行程總覽")

        # Tabs
        tab1, tab2 = st.tabs(
            ["本月行程", "已封存行程"]
        )

        # -------- Tab1 --------
        with tab1:

            st.write("### 本月行程")

            st.write("📌 開學典禮")
            st.write("🕘 09:00")

            st.divider()

            st.write("📌 專題會議")
            st.write("🕒 15:00")

        # -------- Tab2 --------
        with tab2:

            st.write("### 已封存行程")

            st.write("✅ 寒假旅遊")
            st.write("✅ 期末聚餐")
