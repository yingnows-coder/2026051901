import streamlit as st

# 網頁設定
st.set_page_config(
    page_title="微型 TimeTree",
    layout="wide"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.write("## 行事曆群組")

    group = st.radio(
        "選擇群組",
        ["工作", "家庭", "學校"]
    )

    st.success(f"目前群組：{group}")

# ---------------- Main Layout ----------------
left_col, right_col = st.columns([1, 3])

# -------- 左欄：新增行程 --------
with left_col:
    st.write("## 新增行程")

    st.info("請輸入新的行程資訊")

    title = st.text_input("行程名稱")

    date = st.date_input("日期")

    time = st.time_input("時間")

    st.button("新增行程")

# -------- 右欄：行程看板 --------
with right_col:

    # 外框容器
    with st.container(border=True):

        st.write("## 行程總覽")

        # Tabs 分頁
        tab1, tab2 = st.tabs(
            ["本月行程", "已封存行程"]
        )

        # -------- Tab 1 --------
        with tab1:
            st.write("### 本月行程")

            st.write("📌 開學典禮")
            st.write("🕘 09:00")

            st.divider()

            st.write("📌 專題會議")
            st.write("🕒 15:00")

        # -------- Tab 2 --------
        with tab2:
            st.write("### 已封存行程")

            st.write("✅ 寒假旅遊")
            st.write("✅ 期末聚餐")
