# The library you have to use
import numpy as np

# Some extra libraries to build the webapp and deal with images and files
import streamlit as st
import io
from PIL import Image


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write("Interactive Project to open, crop, display and save images using NumPy, PIL and Matplotlib.")


# ----- Title of the page -----
st.title("🖼️ Image Cropper")
st.divider()


# ----- Getting the image from the user or using a default one if the user didn't upload any, we get the image as a numpy array called img_arr -----
is_example = False
img = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if img is None:
    is_example = True
    with Image.open("data/starry_night.png") as img:
        img_arr = np.array(img)
else:
    with Image.open(img) as img:
        img_arr = np.array(img)

# Displaying the image
st.image(img_arr, caption="Original Image" if not is_example else "Original example image", width="content")
st.write("#")


# TODO: Ex. 1.1: Get the minimum and maximum values for the vertical and horizontal ranges, so the size of the img_arr array -----

min_height = 0 
max_height = img_arr.shape[0]   # TODO: Replace None with the maximum height of the image using np.shape() function

min_width = 0
max_width = img_arr.shape[1]    # TODO: Replace None with the maximum width of the image using np.shape() function  



# ----- Creating the sliders to receive the user input with the dimensions to crop the image ----- 
# Sliders (keep as‑is)
cols1 = st.columns([4, 1, 4])
crop_min_h, crop_max_h = cols1[0].slider("Crop Vertical Range", 0, img_arr.shape[0], (int(img_arr.shape[0]*0.1), int(img_arr.shape[0]*0.9)))
crop_min_w, crop_max_w = cols1[2].slider("Crop Horizontal Range", 0, img_arr.shape[1], (int(img_arr.shape[1]*0.1), int(img_arr.shape[1]*0.9)))

st.write("## Cropped Image")

# Crop & display (new)
crop_arr = img_arr[crop_min_h:crop_max_h, crop_min_w:crop_max_w, :]
st.image(crop_arr, caption=f"Cropped {crop_arr.shape[:2]}", use_column_width=True)

# Download
buf = io.BytesIO()
Image.fromarray(crop_arr).save(buf, format="PNG")
st.download_button("Download cropped", buf.getvalue(), "cropped.png")



# TODO: Ex. 1.3: Crop the image array img_arr using the crop_min_h, crop_max_h, crop_min_w and crop_max_w values -----

crop_arr =img_arr[crop_min_h:crop_max_h, crop_min_w:crop_max_w,:]   # TODO: Generate the crop array into a new variable, use NumPy array slicing


# ----- Displaying the cropped image and creating a download button to download the image -----

if type(crop_arr) == np.ndarray:
    st.image(crop_arr, caption="Cropped Image", use_column_width=True)

    buf = io.BytesIO()
    Image.fromarray(crop_arr).save(buf, format="PNG")
    cropped_img_bytes = buf.getvalue()

    cols2 = st.columns([4, 1, 4])
    file_name = cols2[0].text_input("Chose a File Name:", "cropped_image") + ".png"

    st.download_button(f"Download the image `{file_name}`", cropped_img_bytes, file_name=file_name)

else:
    st.subheader("⚠️ You still need to develop the Ex 1.3.")
