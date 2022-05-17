import streamlit as st
import json
from traitlets import default
from Classifier import KNearestNeighbours
# from PIL import Image
# from annotated_text import annotated_text
from streamlit_option_menu import option_menu
from operator import itemgetter



# img = Image.open('favicon.png')
# st.set_page_config(page_title='Movie-Recommendation-Engine' , page_icon=img , layout="centered",initial_sidebar_state="expanded")


if st.button("VISIT ME"):
    link = '[PRAGYA BISHERWAL](https://www.linkedin.com/in/pragya-bisherwal/)'
    st.markdown(link, unsafe_allow_html=True)
    

with st.sidebar:
    selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "My Work", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
            

    if selected == "Home":
        st.title(f"MOVIE RECOMMENDATION ENGINE")
    if selected == "My Work":
        st.markdown(""" ## -- Check Out My Work 💻 -- <br>🎲  http://lnkiy.in/Pragya_Github 🎲 http://lnkiy.in/Pragya_Resume 🎲 http://lnkiy.in/Pragya_Portfolio """,True)

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
    st.header('Movie Recommendation System') 

    apps = ['--Select--', 'Movie based', 'Genres based']   
    app_options = st.selectbox('Select application:', apps)
    
    
    if app_options == 'Movie based':
        movie_select = st.selectbox('Select movie:', ['--Select--'] + movies)
        if movie_select == '--Select--':
            st.write('Select a movie')
        else:
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            genres = data[movies.index(movie_select)]
            test_point = genres
            table = knn(test_point, n)
            st.write("")
            st.write("")
            # annotated_text(
            # ("-- THE RECOMMENDED MOVIES 📈--","","#e98a15"),".")
            # st.write("")
            # st.write("")

            for movie, link in table:
                st.markdown(f"[{movie}]({link})")
    elif app_options == apps[2]:
        options = st.multiselect('Select genres:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 8)
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            # annotated_text(
            # ("-- THE RECOMMENDED MOVIES 📈--","","#e98a15"),".")
            for movie, link in table:
                # Displays movie title with link to imdb
                
                st.markdown(f"[{movie}]({link})")

        else:
                st.write("This is a simple Movie Recommender application.HOPE YOU LIKE IT "
                        "You can select the genres and change the IMDb score.")
                        

    else:
        st.write('Select option')