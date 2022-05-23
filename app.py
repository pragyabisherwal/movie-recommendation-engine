import streamlit as st
import json
from Classifier import KNearestNeighbours
from operator import itemgetter

from PIL import Image
from annotated_text import annotated_text
from streamlit_option_menu import option_menu

import requests
from streamlit_lottie import st_lottie

import streamlit.components.v1 as components

img = Image.open('./images/favicon.png')
st.set_page_config(page_title='Movie-Recommendation-Engine' , page_icon=img , layout="centered",initial_sidebar_state="expanded")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_bb9bkg1h.json")


# if st.button("VISIT ME"):
#     link = '[PRAGYA BISHERWAL](https://www.linkedin.com/in/pragya-bisherwal/)'
#     st.markdown(link, unsafe_allow_html=True)


with st.sidebar:
    selected = option_menu(
                menu_title="MOVIES MANIA",  # required
                options=["Home", "Work", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                
                 styles={
                "container": {"padding": "5!important", "background-color": "#0E1117" , "Font-family":"Monospace"},
                "icon": {"color": "#A0CFD3", "font-size": "25px"}, 
                "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px","Font-family":"Monospace"},
                "nav-link-selected": {"background-color": "#90EE90"},
    }
                
            )
            
    if selected == "MOVIE MANIA":
        st.title(f"MOVIE RECOMMENDATION ENGINE")

    if selected == "Work":
       
        if st.info("**PORTFOLIO**"):
            link = '[**🎲  Visit My Portfolio >>** ](http://lnkiy.in/Pragya_Portfolio)'
            st.markdown(link, unsafe_allow_html=True)
        if st.error("**RESUME**"):
            link = '[**🎲 Have A Look On my Resume >>** ](http://lnkiy.in/Pragya_Resume )'
            st.markdown(link, unsafe_allow_html=True)
        if st.success("**GITHUB**"):
            link = '[**🎲 Check Out My Github >>** ](http://lnkiy.in/Pragya_Github )'
            st.markdown(link, unsafe_allow_html=True)
    if selected == "Contact":  
        st.text("")
        st.text("")
        v2 = st.selectbox("-- Want to Connect 📧 --",[" -- Connect -- ","pragyabisherwal@gmail.com","www.linkedin.com/in/pragya-bisherwal"],index = 0)



# Load data and movies list from corresponding JSON files
with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)

def knn(test_point, k):
    # Create dummy target variable for the KNN Classifier
    target = [0 for item in movie_titles]
    # Instantiate object for the Classifier
    model = KNearestNeighbours(data, target, test_point, k=k)
    # Run the algorithm
    model.fit()
    # Distances to most distant movie
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    # Print list of 10 recommendations < Change value of k for a different number >
    table = list()
    for i in model.indices:
        # Returns back movie title and imdb link
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table

if __name__ == '__main__':
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    
    movies = [title[0] for title in movie_titles]

    with st.container():
     left_column, right_column = st.columns(2)
     with left_column:
         st.write("")
         st.title('MOVIE RECOMMENDATION ENGINE') 
     with right_column:
         st_lottie(lottie_coding, height=300,width=400, key="coding")
        
    
    

    apps = ['*--Select--*', 'Movie based', 'Genres based']   
    app_options = st.selectbox('Method Of Recommendation:', apps)
    
    
    if app_options == 'Movie based':
        movie_select = st.selectbox('Select a movie:', ['--Select--'] + movies)
        if movie_select == '--Select--':
            st.write('Select a movie')
        else:
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            genres = data[movies.index(movie_select)]
            test_point = genres
            table = knn(test_point, n)
            st.write("")
            st.write("")
            st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> RECOMMENDED MOVIES 📈 </h1>", unsafe_allow_html=True)
            st.write("")
            st.write("")
            
            for movie, link in table:
                st.warning(movie)
                st.markdown(f"📌 IMDB LINK --- [{movie}]({link})")

    elif app_options == apps[2]:
        options = st.multiselect('Select genres:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 8)
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            st.write("")
            st.write("")
            st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> RECOMMENDED MOVIES 📈 </h1>", unsafe_allow_html=True)
            st.write("")
            st.write("")
            
            for movie, link in table:
                # Displays movie title with link to imdb
                st.warning(movie)
                st.markdown(f"📌 IMDB LINK --- [{movie}]({link})")

        else:
                st.write(" _Can Select Multiple Genres_ ")
                        

    else:
        st.write('Select option')


st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> HOW IT WORKS 😲</h1>", unsafe_allow_html=True)

st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> EXPLORE THE CONTENT 😏</h1>", unsafe_allow_html=True)
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTdOckh6g-mN8BHmdqjCXwuhcFyG9voMhbcmsuQkVNaXHuBJWnXCIphIJywZKHfN2El5Hn455H_L_YF/embed?start=true&loop=true&delayms=3000",width=670, height=400, scrolling=True)

st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> WANT TO CONNECT 👨‍⚖️</h1>", unsafe_allow_html=True)
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/pragyabisherwal@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" style="height:50px; width:600px; font-size:14pt;" placeholder="Your name" required>
        <input type="email" name="email" style="height:50px; width:600px; font-size:14pt;" placeholder="Your email" required>
        <textarea name="message" style="height:50px; width:600px; font-size:14pt;" placeholder="Your message here" required></textarea>
        <button style="height:50px; width:600px; font-size:14pt;" type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()