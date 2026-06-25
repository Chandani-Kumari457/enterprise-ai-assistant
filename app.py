import streamlit as st
import speech_recognition as sr
import pandas as pd
import plotly.express as px


from agents.rag_agent import (
    rag_agent,
    summarize_document
)
from agents.manager_agent import manager_agent
from utils.pdf_reader import read_pdf

from utils.chat_memory import (
    initialize_memory,
    save_message,
    get_history
)
from database.dashboard_data import (
    get_employee_count,
    get_average_attendance,
    get_project_count,
    get_employee_dataframe,
    get_top_performer
)


st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>

/* Global Text */
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

p, label {
    color: #E2E8F0 !important;
}
.stMarkdown,
.stText,
div[data-testid="stMarkdownContainer"],
ul, ol, li {
    color: #F8FAFC !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #F8FAFC !important;
}

/* Main App */
.stApp {
    background: linear-gradient(
        135deg,
        #0F172A,
        #1E293B
    );
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #374151;
}

/* Hero Title */
.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: white;
    text-align: center;
    margin-bottom: 10px;
}

/* Hero Subtitle */
.hero-subtitle {
    text-align: center;
    color: #CBD5E1;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

/* Metrics */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 10px;
    border: 1px solid rgba(255,255,255,0.08);
}
.dashboard-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(124,58,237,0.5);
    border-radius: 20px;
    padding: 18px;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
    cursor: pointer;
}
.dashboard-card:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 20px 40px rgba(124,58,237,0.6);
}

.employee-card {
    border-left: 6px solid #00BFFF;
    box-shadow: 0 0 20px rgba(0,191,255,0.5);
}
            
.project-card {
    border-left: 6px solid #00FF7F;
    box-shadow: 0 0 20px rgba(0,255,127,0.5);
}

.attendance-card {
    border-left: 6px solid #FFD700;
    box-shadow: 0 0 20px rgba(255,215,0,0.5);
}

.agent-card {
    border-left: 6px solid #C084FC;
    box-shadow: 0 0 20px rgba(192,132,252,0.5);
}

.performer-card {
    border-left: 6px solid #FF6B6B;
    box-shadow: 0 0 25px rgba(255,107,107,0.6);
}

.dashboard-card h3 {
    color: #CBD5E1;
    margin-bottom: 10px;
}

.dashboard-card h1 {
    color: white;
    margin: 0;
    font-size: 24px;
    font-weight: 700;
    line-height: 1;
}

.dashboard-card h3 {
    color: #CBD5E1;
    margin-bottom: 8px;
    font-size: 16px;
}
/* Dropdown menu options fix */

div[role="listbox"] {
    background-color: white !important;
}

div[role="option"] {
    color: black !important;
    background-color: white !important;
}

div[role="option"]:hover {
    background-color: #E5E7EB !important;
    color: black !important;
}
/* Dropdown Text Fix */

div[role="option"] {
    color: black !important;
}

div[role="option"] * {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)
st.sidebar.markdown(
    """
# 🤖 Enterprise AI

### Control Center
"""
)


page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "AI Assistant",
        "Documents",
        "HR Analytics"
    ]
)
st.sidebar.success(
    "🟢 Gemini Connected"
)

st.sidebar.info(
    "Enterprise AI v1.0"
)



st.markdown("""
<div style="
padding:30px;
border-radius:25px;
background:linear-gradient(135deg,#7C3AED,#4F46E5);
text-align:center;
margin-bottom:25px;
box-shadow:0px 10px 30px rgba(124,58,237,0.4);
">

<h1 style="color:white;">
🤖 Enterprise AI Assistant
</h1>

<p style="color:white;font-size:18px;">
Multi-Agent Intelligence Platform powered by Gemini, RAG and FAISS
</p>

</div>
""", unsafe_allow_html=True)

if page == "Dashboard":
    st.markdown("""
    ### ✨ Platform Highlights

   ✅ Multi-Agent Architecture

   ✅ Gemini Powered Intelligence

   ✅ RAG Document Search

   ✅ FAISS Vector Database

   ✅ Smart Analytics Dashboard
   """)

    df = get_employee_dataframe()

    employees = len(df)

    attrition_rate = round(
    (df["Attrition"] == "Yes").mean() * 100,
    1
)
    
    attendance = round(
    100 - (
        (df["Attrition"] == "Yes").mean() * 100
    ),
    1
)
   

    st.success("🟢 Gemini Connected")

    st.info("📄 RAG Engine Active")

    st.success("🚀 System Online")

    st.markdown("""
    ## 🚀 Enterprise Overview
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
      st.markdown(f"""
      <div class="dashboard-card employee-card">
        <h3>👥 Employees</h3>
        <h1>{employees}</h1>
    </div>
    """, unsafe_allow_html=True)


    with col2:
      st.markdown(f"""
      <div class="dashboard-card attendance-card">
        <h3>🏢 Departments</h3>
        <h1>{df["Department"].nunique()}</h1>
    </div>
    """, unsafe_allow_html=True)
      
    with col3:
      st.markdown(f"""
      <div class="dashboard-card project-card">
        <h3>📉 Attrition</h3>
        <h1>{attrition_rate}%</h1>
    </div>
    """, unsafe_allow_html=True)
    
    with col4:
      st.markdown("""
       <div class="dashboard-card agent-card">
        <h3>🤖 AI Agents</h3>
        <h1>2 Active</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
       
if page == "Documents":

    st.title("📄 Document Intelligence")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        pdf_text = read_pdf(uploaded_file)

        if st.button(
          "📄 Generate Summary"
    ):

          summary = summarize_document(
            pdf_text
        )

          st.subheader(
            "Document Summary"
        )

          st.write(summary)

          st.success(
            "PDF Uploaded Successfully"
        )

        question = st.text_input(
            "Ask a question from PDF"
        )

        if question:

            answer = rag_agent(
                question,
                pdf_text
            )

            st.write(answer)
initialize_memory()
if page == "AI Assistant":

    st.title("🤖 AI Assistant")

    st.subheader(
        "Conversation History"
    )
    history = get_history()

    for chat in history:

        st.write(
            f"{chat['role']}: {chat['message']}"
        )

    query = st.text_input(
        "Ask Anything"
    )
    if query:
        response = manager_agent(query)
        st.write("🤖 AI Response:")
        st.write(response)


if page == "HR Analytics":

    st.title("🏢 HR Analytics Dashboard")
    
    df_hr = pd.read_csv(
    "datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

    st.success(
      f"✅ Dataset Loaded Successfully ({len(df_hr)} Employees)"
)
    # KPI Values

    total_employees = len(df_hr)

    avg_age = round(
      df_hr["Age"].mean(),
      1
)

    attrition_rate = round(
       (
          len(
              df_hr[
                  df_hr["Attrition"] == "Yes"
              ]
          )
          / len(df_hr)
      ) * 100,
      1
)

    departments = df_hr[
      "Department"
    ].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
          "👥 Employees",
          total_employees
    )

    with col2:
        st.metric(
          "🎂 Average Age",
          avg_age
    )

    with col3:
        st.metric(
           "🚪 Attrition Rate",
           f"{attrition_rate}%"
    )

    with col4:
        st.metric(
          "🏢 Departments",
           departments
    )
    st.markdown("---")

    st.subheader(
       "🚪 Employee Attrition Analysis"
)
    attrition_data = df_hr[
    "Attrition"
   ].value_counts()

    fig = px.pie(
       names=attrition_data.index,
       values=attrition_data.values,
       title="Attrition Distribution",
       hole=0.45
)  
    fig.update_traces(
    textfont_color="white",
    textfont_size=18
)

    fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="white",
        size=18
    ),

    title_font=dict(
        color="white",
        size=24
    ),

    legend=dict(
        font=dict(
            color="white",
            size=16
        )
    )
)
    fig.update_traces(
    textinfo="percent+label",
    textfont_color="white",
    textfont_size=18
)

    st.plotly_chart(
       fig,
       use_container_width=True
)
    st.markdown("---")

    st.subheader(
       "🏢 Employees by Department"
)
    
    dept_data = df_hr[
    "Department"
   ].value_counts()

    fig_dept = px.bar(
      x=dept_data.index,
      y=dept_data.values,
      title="Department Distribution",
      template="plotly_dark"
)
    
    fig_dept.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="white",
        size=16
    ),

    title_font=dict(
        color="white",
        size=24
    )
)

    fig_dept.update_xaxes(
       showgrid=False
)

    fig_dept.update_yaxes(
       showgrid=False
)
    
    st.plotly_chart(
    fig_dept,
    use_container_width=True
)
    st.markdown("---")

    st.subheader(
      "💰 Average Salary by Department"
)
    
    salary_data = df_hr.groupby(
    "Department"
    )["MonthlyIncome"].mean().reset_index()

    fig_salary = px.bar(
       salary_data,
       x="Department",
       y="MonthlyIncome",
       title="Average Salary by Department",
       template="plotly_dark"
)
    
    fig_salary.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="white",
        size=16
    ),

    title_font=dict(
        color="white",
        size=24
    )
)

    fig_salary.update_xaxes(
      showgrid=False
)

    fig_salary.update_yaxes(
       showgrid=False
)
    
    st.plotly_chart(
    fig_salary,
    use_container_width=True
)