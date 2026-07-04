# app.py
import streamlit as st
import os
import io
from contextlib import redirect_stdout
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Graph Theory Lab Manager",
    page_icon="📘",
    layout="wide"
)

# =====================================================
# DARK THEME CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #000000 0%,
        #0f172a 50%,
        #111827 100%
    );
}

.main-title{
    text-align:center;
    color:white;
    font-size:65px;
    font-weight:900;
}

.sub-title{
    text-align:center;
    color:#d1d5db;
}

.section-card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.1);
    padding:20px;
    border-radius:20px;
    margin-bottom:20px;
}


.footer{
    text-align:center;
    color:white;
    font-size:18px;
    font-weight:bold;
    padding:20px;
}

[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #000000,
        #111827
    );
}

[data-testid="stSidebar"] *{
    color:white !important;
}

h1,h2,h3,h4,h5,h6{
    color:white !important;
}

p,li{
    color:white !important;
}

.stButton button{
    background:#2563eb;
    color:white;
    border:none;
    border-radius:10px;
}

.stCode{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📚 Navigation")

pages = ["🏠 Home"] + [f"Experiment {i}" for i in range(1, 12)]

selected_page = st.sidebar.selectbox(
    "Select Experiment",
    pages
)

# =====================================================
# HOME PAGE
# =====================================================

if selected_page == "🏠 Home":

    st.markdown("<br>", unsafe_allow_html=True)

    if os.path.exists("assets/gec_logo.png"):
        c1, c2, c3 = st.columns([1,3,1])
        with c2:
            st.image(
                "assets/gec_logo.png",
                width=700
            )

    st.markdown("""
    <div class="main-title">
        Graph Theory & Combinatorics Lab
    </div>

    <div class="sub-title">
        <h2>CMP-226 Laboratory Management System</h2>
        <h3>Goa College of Engineering</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
        <h2 style="text-align:center;color:white;">
            Welcome
        </h2>

        <p style="text-align:center;font-size:20px;">
            ✔ Theory<br>
            ✔ Source Code<br>
            ✔ Execute Program Live<br>
            ✔ Graph Visualization<br>
            ✔ Terminal Output<br>
            ✔ Conclusion<br>
            ✔ Experiment Documents<br>
            ✔ NetworkX Programs<br>
            ✔ Without NetworkX Programs<br>
            ✔ Pseudo Code
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# =====================================================
# EXPERIMENT NUMBER
# =====================================================

exp_no = int(selected_page.split()[-1])

# =====================================================
# HEADER
# =====================================================

if os.path.exists("assets/gec_logo.png"):
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image(
            "assets/gec_logo.png",
            width=500
        )

st.title(selected_page)

st.markdown(
    "<h2 style='text-align:center;'>Graph Theory & Combinatorics Lab</h2>",
    unsafe_allow_html=True
)


st.markdown(
    "<h4 style='text-align:center;'>CMP-226 | Semester 4</h4>",
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# IMPLEMENTATION TYPE
# =====================================================

if exp_no == 11:
    implementation = st.radio(
        "Select Implementation",
        [
            "With NetworkX",
            "Without NetworkX",
            "Pseudo Code"
        ],
        horizontal=True
    )
else:
    implementation = st.radio(
        "Select Implementation",
        [
            "With NetworkX",
            "Without NetworkX"
        ],
        horizontal=True
    )

# =====================================================
# FILE PATHS
# =====================================================

if implementation == "With NetworkX":

    code_file = (
        f"CODES/networkx/exp{exp_no}.py"
    )

elif implementation == "Without NetworkX":

    code_file = (
        f"CODES/without_networkx/exp{exp_no}a.py"
    )

else:

    code_file = (
        "CODES/Pseudo Code/exp11b.py"
    )

theory_file = (
    f"THEORY/exp{exp_no}.txt"
)

conclusion_file = (
    f"CONCLUSION/exp{exp_no}.txt"
)


# =====================================================
# TABS
# =====================================================

tab_theory, tab_code, tab_output, tab_conclusion = st.tabs(
    ["📖 Theory","💻 Source Code","🖥 Output","✅ Conclusion"]
)

with tab_theory:
    if os.path.exists(theory_file):
        with open(theory_file,"r",encoding="utf-8") as f:
            st.info(f.read())
    else:
        st.warning("Theory file not found.")

with tab_code:
    if os.path.exists(code_file):
        with open(code_file,"r",encoding="utf-8") as f:
            source_code = f.read()
        st.code(source_code, language="python")
    else:
        st.error("Source code file not found.")

with tab_output:

    st.header("🖥 Live Program Output")

    if exp_no == 5:
        st.info("Experiment 5 requires user input. Configure custom inputs here.")

    if os.path.exists(code_file):

        with open(code_file, "r", encoding="utf-8") as f:
            source_code = f.read()

        if st.button("▶ Execute Program", use_container_width=True):

            try:

                plt.close("all")

                buffer = io.StringIO()

                with redirect_stdout(buffer):

                    exec_globals = {
                        "__name__": "__main__"
                    }

                    exec(source_code, exec_globals)

                output = buffer.getvalue()

                if output.strip():
                    st.subheader("📟 Terminal Output")
                    st.code(output, language="text")

                fig = plt.gcf()

                if len(fig.axes) > 0:
                    st.subheader("📊 Graph Visualization")
                    st.pyplot(fig)

                elif not output.strip():
                    st.success("Program executed successfully.")

            except Exception as e:
              st.error(f"Execution Error:\n{e}")
    else:
        st.error("Code file not found.")

with tab_conclusion:

    if os.path.exists(conclusion_file):
        with open(conclusion_file,"r",encoding="utf-8") as f:
            st.success(f.read())
    else:
        st.warning("Conclusion file not found.")


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<div class="footer">
    Chirag Vengurlekar | 24B-CO-014 | Semester 4
</div>
""", unsafe_allow_html=True)

