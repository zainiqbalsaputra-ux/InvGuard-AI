import streamlit as st
import cv2

from app.detection import detect_vehicles


def run_dashboard():

    st.set_page_config(
        page_title="InvGuard AI",
        layout="wide"
    )

    st.title("🚦 InvGuard AI Dashboard")
    st.write("AI-powered traffic monitoring system")

    # Video path
    video_path = "videos/thailand.mp4"

    cap = cv2.VideoCapture(video_path)

    frame_placeholder = st.empty()

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        annotated_frame, results = detect_vehicles(frame)

        annotated_frame = cv2.cvtColor(
            annotated_frame,
            cv2.COLOR_BGR2RGB
        )

        frame_placeholder.image(
            annotated_frame,
            channels="RGB",
            use_container_width=True
        )

    cap.release()