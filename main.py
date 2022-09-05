#importded libraries
import streamlit as st
from streamlit_option_menu import option_menu
from LogSubmission import LogSubmission
from streamlit_imagegrid import streamlit_imagegrid
import requests
import base64
from PIL import Image

#CONSTANTS:
list_of_log_submissions = []

#side bar
with st.sidebar:
    #sidebar options
    choose = option_menu("Pixelator", ["Home", 'Log', 'Memories', 'Summary'],
        #sidebar icons
        icons=['house', 'card-text', 'card-image', 'bar-chart-line'],
                           menu_icon="emoji-sunglasses",
                           default_index=1,
                           #sidebar style css
                           styles={
                               "container": {"padding": "5!important",
                                             "background-color": "#fafafa"},
                               "nav-link": {"font-size": "16px",
                                            "text-align": "left",
                                            "margin": "0px",
                                            "--hover-color": "#eee"},
                               "nav-link-selected": {
                                   "background-color": "#606C38"},
                           }
                         )

logo = Image.open(r"/Users/aanyavgupta/Downloads/Pixelator.gif")
#for the home page
if choose == "Home":
    #homepage title
    st.markdown(
        "<h1 style='text-align: center; color: #b17946;'>Pixelator ~ the "
                 "Pixel Motivator </h1>",
                 unsafe_allow_html=True)
    #mental health quiz
    with st.sidebar:
        selected = option_menu("Home Quiz", ["Mad", 'Sad', "Meh", 'Glad',
                                             'Over the Top'],
                               icons=['emoji-angry', 'emoji-frown',
                                      "emoji-neutral", "emoji-smile",
                                      "emoji-smile-upside-down"],
                               menu_icon="cast",
                               default_index=1, orientation="horizontal")
    #opening the pixel aviator logo
    file_ = open("/Users/aanyavgupta/Downloads/Pixelator.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    #opening the logo as a gif
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )


#for the log page
elif choose == "Log":
    #adding in the form questions
    with st.form("my_form"):
        st.write("Daily Log")
        text_val = st.text_input("What exercise did you do?")
        slider_val = st.slider("How long? (minutes)")
        radio_val = st.radio("Did you have fun?", ("Yes!", "No...", "Meh."))
        rating_val = st.slider("Rate your experience!", min_value=0,
                               max_value=10)

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            list_of_log_submissions.append(LogSubmission(text_val,
                                                         slider_val,
                                                         radio_val, rating_val))

#this is the memories page
elif choose == "Memories":
    col1, col2 = st.columns([0.8, 0.2])
    with col1:  # To display the header text using css style
        st.markdown("<h1 style='text-align: left; color: #b17946;'> "
                    "Memories :D </h1>", unsafe_allow_html=True)

    with col2:  # To display brand logo
        st.image(logo, width=150)
    # Add file uploader to allow users to upload photos
    uploaded_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, width=300)


    st.title('Image Grid:')

    #opening the photos
    urls = [
        {
            "width": 403200,
            "height": 302400,
            "src": "https://images.unsplash.com/photo-1493166228553-4fa0fdb916e8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
        },
        {
            "width": 403200,
            "height": 302400,
            "src": "https://images.unsplash.com/photo-1485970247670-34cd80f5a996?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2874&q=80"
        },
        {
            "width": 600000,
            "height": 400000,
            "src": "https://images.unsplash.com/photo-1525115450806-c4b70fd049bd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
        }
    ]

    return_value = streamlit_imagegrid(urls=urls, height=700000)

    if return_value is not None:
        response = requests.get(return_value)

#this is the summary page
elif choose == "Summary":
    st.markdown("<h1 style='text-align: left; color: #b17946;'> "
                "Great Job! This month you were active for </h1>",
                unsafe_allow_html=True)
    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        st.markdown("<h2 style='text-align: left; color: #b17946;'> "
                    "Days: </h1>",
                    unsafe_allow_html=True)
    with col2:
        bluh = LogSubmission.streak_counter
        st.title(bluh)


