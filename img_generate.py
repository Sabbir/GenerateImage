import streamlit as st
from generate import generate


st.set_page_config(page_title="Generate Image from text", page_icon="💍", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Generate Image from Text")

#Insert prompt for image. Example: "A flower garden by the side of river"
pmt = st.text_input("Prompt?", key="pmt", type="default", placeholder="A flower garden")

#set the default height and width
h=512
w=512

#select image size. default 512x512
size = st.selectbox(
    'Image Size?',
     ('512x512','912x512','800x512', '640x512', '480x512'))

#Set the user selected image size.
match size:
    case "912x512":
        w=912

    case "800x512":
        w=800

    case "640x512":
        w=640
    
    case "480x512":
        w=480

st.write('You selected:', size)

if st.button('Generate'):
    A,B = st.columns([.05, .95])
    C,D = st.columns([.05, .95])
    with A:
        st.caption("🥢")
    with C:
        st.caption("🧊")

    if pmt not in [None, "", []]:  
        with B:
            st.write( "<h2>The Prompt: ", pmt, "</h2>" )
        with D:
            #Generate the image and have the result
            result = generate(pmt,h,w)
            print("Done")

            #Show the image
            st.image(result.images[0], caption=pmt)
    else:
        with B:
            st.error( "The Prompt can not be null" )