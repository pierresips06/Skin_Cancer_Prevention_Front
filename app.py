import streamlit as st
from PIL import Image
import requests
from dotenv import load_dotenv
import os
import tempfile

import json

# Set page tab display
st.set_page_config(
   page_title="Skin Cancer Detection Tool",
   page_icon= '🖼️',
   layout="wide",
   initial_sidebar_state="expanded",
)

# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
# url = 'http://localhost:8000'
load_dotenv()
#url = os.getenv('API_URL')
# url="https://apiskincancerprevention-hetftldjwa-ew.a.run.app" #initial model
url="https://apiskincancerpreventionmodelvgg-hetftldjwa-ew.a.run.app"

# App title and description
st.header('Skin Cancer Detection Tool 📸')
st.markdown('''
            > From a mole's picture, predict the disease that might be at the origin and if a dermatologist's consultation is required.

            > **What's here:**

            > * [Streamlit](https://docs.streamlit.io/) on the frontend
            > * [FastAPI](https://fastapi.tiangolo.com/) on the backend
            > * [PIL/pillow](https://pillow.readthedocs.io/en/stable/) and [opencv-python](https://github.com/opencv/opencv-python) for working with images
            > * Backend and frontend can be deployed with Docker
            ''')

st.markdown("---")

### Disclaimer
st.markdown('''
            **Disclaimer:** This tool is written to showcase the capabilities of AI deployment into medical fields and does not offer medical advice. For any medical advice, please consult a doctor.
            ''')


# Function to calculate color based on percentage
def get_color(percentage):
    r = int(255 * (percentage / 100))
    g = int(255 * ((100 - percentage) / 100))
    return f'rgb({r}, {g}, 0)'



### Create a native Streamlit file upload input
st.markdown("### Upload a mole's picture for skin cancer detection 👇")
img_file_buffer = st.file_uploader('Upload an image of a mole')
if img_file_buffer is not None:
    # Save the uploaded image to a temporary file to prevent a streamlit bug
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(img_file_buffer.read())
        temp_file_path = temp_file.name

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

  with col2:
    with st.spinner("Wait for it..."):
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()

      ### Make request to API (stream=True to stream response as bytes)
      res = requests.post(url + "/predict/", files={'file': open(temp_file_path,"rb")})
      resultat = str(res._content)
      if res.status_code == 200:
        ### Display the image returned by the API


        response_dict = json.loads(res.content)
        probability = response_dict.get('prediction')
        percentage = probability *100
        color = get_color(percentage)

        # # Display the result as a percentage
        st.markdown(f"<span style='color:{color}; font-size:24px;'>Probability of Skin Cancer: {percentage:.2f}%</span>", unsafe_allow_html=True)




      else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")
        print(res.content)
