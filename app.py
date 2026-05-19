import streamlit as st
import datetime
from datetime import date

# ---------------- 網頁設定 ----------------
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

# ---------------- 主畫面 ----------------
st.title("微型 TimeTree")

# ===== 頂部：橫向膠囊鈕 =====
status = st.segmented_control(
    "顯示狀態",
    ["全部", "重要", "已完成"],
    default="全部"
)

st.write(f"目前狀態：{status}")

st.divider()

# ===== 對稱輸入區 =====
left_input, right_input = st.columns(2)

# -------- 左側 --------
with left_input:

    st.write("### 行程資訊")

    title = st.text_input(
        "行程主旨",
        placeholder="請填寫行程名稱..."
    )

    my_color = st.color_picker(
        "挑選辨識顏色",
        "#1A50E8"
    )

# -------- 右側 --------
with right_input:

    st.write("### 時間設定")

    today = st.date_input(
        "選擇日期",
        datetime.date.today()
    )

    meeting_time = st.time_input(
        "選擇時間"
    )

st.divider()

# ===== 新增按鈕 =====
if st.button("新增行程"):

    st.success("行程新增成功！")

    st.write("### 行程預覽")

    st.write(f"📌 主旨：{title}")
    st.write(f"📅 日期：{today}")
    st.write(f"🕒 時間：{meeting_time}")

    st.markdown(
        f"""
        <div style="
            width:100px;
            height:30px;
            background:{my_color};
            border-radius:10px;">
        </div>
        """,
        unsafe_allow_html=True
    )
