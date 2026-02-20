import streamlit as st
import numpy as np
import cv2
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="Medical X-Ray to 3D Organ Map")

st.title("🩻 X-Ray to 3D Organ Visualizer")
st.markdown("Upload a 2D medical scan to generate a simulated 3D organ surface.")

uploaded_file = st.file_uploader("Upload X-ray image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    img_array = np.array(image)

    st.image(image, caption="Uploaded X-Ray", use_column_width=True)

    # Normalize image
    normalized = img_array / 255.0

    # Create pseudo depth map
    depth_map = cv2.GaussianBlur(normalized, (15, 15), 0)

    st.subheader("Depth Map Generated")

    # Generate 3D surface
    x = np.linspace(0, 1, depth_map.shape[1])
    y = np.linspace(0, 1, depth_map.shape[0])
    x, y = np.meshgrid(x, y)

    fig = go.Figure(data=[go.Surface(z=depth_map, x=x, y=y)])

    fig.update_layout(
        title="3D Organ Surface (Simulated)",
        autosize=True,
        scene=dict(
            xaxis_title="Width",
            yaxis_title="Height",
            zaxis_title="Depth"
        )
    )

    st.plotly_chart(fig)

    st.success("Interactive 3D visualization ready!")
