import streamlit as st
import json
from Classifier import KNearestNeighbours
from operator import itemgetter

from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components



#Setting the Page Configuration
img = Image.open('./images/favicon.png')
st.set_page_config(page_title='Movie Recommender Engine' , page_icon=img , layout="centered",initial_sidebar_state="expanded")

#Designing the footer and MainMenu creating the skeleton of the website.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:after{
                background-color:#a873b0;
                font-size:15px;
                text-align:center;
                width: 100%;
                height:40px;
                margin:1rem;
                padding:0.8rem;
                content:'Copyright © 2022 : Pragya Bisherwal';
                display:block;
                color:white;
            }
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#Loading the animation of the streamlit lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# URLS of all the lottie animation used
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_bb9bkg1h.json")
lottie_contact =load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dhcsd5b5.json")
lottie_loadLine =load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_yyjaansa.json")
lottie_video =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1cmhfk0l.json")
lottie_videoLine =load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_9B6yb3.json")
lottie_github =load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_S6vWEd.json")
lottie_resume=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_lrw0segg.json")
lottie_portfolio=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_dkuwscrg.json")


#Sidebar Designing And Functioning
with st.sidebar:
    selected = option_menu(
                menu_title="MOVIES MANIA",  # required
                options=["Home", "Work", "Github-Repo"],  # required
                icons=["house", "book", "github"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                 styles={
                "container": {"padding": "5!important", "background-color": "#0E1117" , "Font-family":"Monospace"},
                "icon": {"color": "#A0CFD3", "font-size": "25px"}, 
                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px","Font-family":"Monospace"},
                "nav-link-selected": {"background-color": "#90EE90"},
                }
                )

#Adding Functionality to the sidebar on the basis of option being selected from the main menu.       
    if selected == "Home":
      st.empty()
    if selected == "Work":
        if st.error("**PORTFOLIO**"):
            st_lottie(lottie_resume,key="coding6")
            link = '[**🎲  Visit My Portfolio >>** ](http://lnkiy.in/Pragya_Portfolio)'
            st.markdown(link, unsafe_allow_html=True)

        if st.error("**RESUME**"):
            st_lottie(lottie_portfolio,key="coding7")
            link = '[**🎲 Have A Look On my Resume >>** ](http://lnkiy.in/Pragya_Resume )'
            st.markdown(link, unsafe_allow_html=True)
            
    if selected == "Github-Repo":  
        st_lottie(lottie_github,height=220,width=300,key="coding5")
        if st.button("     MOVIE RECOMMENDATION ENGINE   "):
         link = '[     PRAGYA BISHERWAL     ](https://github.com/pragyabisherwal/movie-recommendation-engine)'
         st.markdown(link, unsafe_allow_html=True)


# Loading data and movies list from corresponding JSON files
with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)


#Applying the KNN algorithms on to the point
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
        # Returns back ---> Movie title and IMDB link
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table

#All the genres from which a user can select
if __name__ == '__main__':
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    
    movies = [title[0] for title in movie_titles]
    
    #Designing of the header and main section of the application.
    with st.container():
     left_column, right_column = st.columns(2)
     with left_column:
            st.write("")
            st.title('MOVIE RECOMMENDER ENGINE') 
     with right_column:
            st_lottie(lottie_coding, height=300,width=400, key="coding")
        
    
    #Selection basis of recommendation.

    apps = ['*--Select--*', 'Movie based', 'Genres based']   
    app_options = st.selectbox('Method Of Recommendation:', apps)


    
    #If Movie Based Recommendation is being selected this condtion will get executed.
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

        
    #If Genre Based Recommendation is being selected this condtion will get executed.
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

# The video section of the website in which the demo of the application is being embedded.
st.write("---")
st. markdown("<h2 style='text-align:center; color:#A0CFD3;font-size:60px;font-family:monospace;'> HOW IT WORKS 😲</h2>", unsafe_allow_html=True)
st.write("##")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.empty()

        
    with right_column:
        st_lottie(lottie_video,height=400,width=400,key="coding4")




# The documentation section of the website in which the substaining crux of the development of the application 
# is being added and embedded on to the application.

st.write("---")
st. markdown("<h1 style='text-align:center; color:#A0CFD3;font-size:55px;font-family:monospace;'>   EXPLORE THE CONTENT 😏</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTdOckh6g-mN8BHmdqjCXwuhcFyG9voMhbcmsuQkVNaXHuBJWnXCIphIJywZKHfN2El5Hn455H_L_YF/embed?start=true&loop=true&delayms=3000",width=670, height=400, scrolling=True)



#The contact me section of the website.Creation of an active form which directly notifies with
# all the details of the sender along with the message om to the mail box

st_lottie(lottie_loadLine,height=300,width=700,key="coding3")
st. markdown("<h1 style='text-align:center; color:#A0CFD3;font-size:60px;font-family:monospace;'> WANT TO CONNECT 👨‍⚖️</h1>", unsafe_allow_html=True)
# ---- CONTACT ----
st.write("")
with st.container():
    contact_form = """
    <form action="https://formsubmit.co/pragyabisherwal@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" style="height:50px; width:300px; font-size:14pt; margin:5px;padding:10px;border-radius:5px;" placeholder="Your name" required>
        <input type="email" name="email" style="height:50px; width:300px; font-size:14pt;margin:5px;padding:10px;border-radius:5px;" placeholder="Your email" required>
        <textarea name="message" style="height:150px; width:300px; font-size:14pt;margin:5px;padding:10px;border-radius:5px;" placeholder="Your message here" required></textarea>
        <button style=" height:50px; width:300px; font-size:14pt; margin:5px; padding:10px;border-radius:5px;background-color:#90EE90" type="submit">Send</button>
        <input type="hidden" name="_next" value="https://pragyabisherwal.github.io/ThankYou-FormSubmit/">
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

        
    with right_column:
        st_lottie(lottie_contact,height=300,width=400,key="coding2")
       