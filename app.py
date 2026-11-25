
import streamlit as st

st.set_page_config(
    page_title="Nourhan Khaled | Portfolio",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("Nourhan Khaled")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "About Me", "Skills", "Projects", "Education", "Contact"]
)

# Home
if page == "Home":
    st.title("Nourhan Khaled")
    st.subheader("AI | Machine Learning | Computer Vision | Data Engineering")

    st.write(
        "Building intelligent, data-driven solutions "
        "by combining AI, machine learning, computer vision, "
        "and data engineering."
    )

    st.markdown("[GitHub](https://github.com/Nourhan908)")

# About
elif page == "About Me":
    st.title("About Me")
    st.write("""
    I am a Computer Science senior specializing in Intelligent Systems,
    with interests spanning Artificial Intelligence, Machine Learning,
    Computer Vision, and Data Engineering.

    I enjoy building intelligent, data-driven solutions, from designing
    data pipelines and processing datasets to developing and training
    machine learning and deep learning models.
    """)

# Skills
elif page == "Skills":
    st.title("Technical Skills")

    st.subheader("Programming")
    st.write("Python | SQL")

    st.subheader("AI & Machine Learning")
    st.write("Machine Learning | Deep Learning | TensorFlow | Scikit-learn")

    st.subheader("Computer Vision")
    st.write("OpenCV | YOLO | Image Processing")

    st.subheader("Data Engineering")
    st.write("Data Processing | Data Cleaning | ETL Concepts")

    st.subheader("Tools")
    st.write("Git | GitHub | Streamlit | Docker")

# Projects
elif page == "Projects":
    st.title("My Projects")

    st.write(
        "A collection of projects combining AI, "
        "computer vision, and robotics."
    )

    # Soccer Robot
    st.header("⚽ Soccer Robot")

    st.write("""
    A robotics project focused on developing an intelligent
    soccer-playing robot using programming, robotics,
    and intelligent decision-making.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.image("C:\\Users\\nourh\\OneDrive\\Billeder\\Screenshots\\Screenshot 2026-11-25 171818.png", use_container_width=True)

    with col2:
        st.image("C:\\Users\\nourh\\OneDrive\\Billeder\\Screenshots\\Screenshot 2026-11-25 171711.png", use_container_width=True)

    st.divider()

    # 2D Object Detection
    st.header("🔍 2D Object Detection")

    st.write("""
    Developed a synthetic dataset using OpenCV and Albumentations
    and trained a YOLO model to detect five geometric shapes:
    circles, triangles, rectangles, squares, and stars.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.image("C:\\Users\\nourh\\OneDrive\\Billeder\\Screenshots\\Screenshot 2026-11-25 171524.png", use_container_width=True)

    with col2:
        st.image("C:\\Users\\nourh\\OneDrive\\Billeder\\Screenshots\\Screenshot 2026-11-25 171447.png", use_container_width=True)

    st.caption("Technologies: Python | OpenCV | Albumentations | YOLO")

    st.divider()

    # Gym Coach
    st.header("🏋️ AI Gym Coach")

    st.write("""
    An AI-powered gym coaching application focused on
    intelligent workout assistance.
    """)

# Education
elif page == "Education":
    st.title("Education")
    st.write("B.Sc. in Computer Science")
    st.write("Alexandria National University")
    st.write("Intelligent Systems Track")

# Contact
elif page == "Contact":
    st.title("Let's Connect!")

    st.write("GitHub: https://github.com/Nourhan908")
    st.write("LinkedIn: https://www.linkedin.com/in/nourhan-khaled-77484b292/")
