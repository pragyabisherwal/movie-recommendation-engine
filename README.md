
#             MOVIE RECOMMENDATION ENGINE

Recommender System is a system that seeks to predict or filter preferences according to the user's choices. Recommender systems are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general.

Movie recommendation systems usually predict what movies a user will like based on the attributes present in previously liked movies. Such recommendation systems are beneficial for organizations that collect data from large amounts of customers, and wish to effectively provide the best suggestions possible.

## Acknowledgements

 - [Streamlit Documentation](https://docs.streamlit.io/)

 - [Content Based Filtering](https://developers.google.com/machine-learning/recommendation/content-based/basics)

 - [KNN Algorithm ](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)

- [Awesome README](https://github.com/matiassingers/awesome-readme)
## Video Demo And Working

Insert gif or link to demo


## Deployment

To deploy this project run

```bash
  streamlit run app.py
```


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


## Tech Stack

**WEB TECHNOLOGIES**

```bash
Backend -- Python

FrontEnd -- HTML,CSS,Streamlit
```

**DATA SET**

```bash
https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset
```




## License

[MIT](https://github.com/pragyabisherwal/movie-recommendation-engine/blob/master/LICENSE)

[GNU General Public License v3.0](https://github.com/pragyabisherwal/movie-recommendation-engine/blob/master/LICENSE)
## Lessons Learned

**KNN ALGORITHM**

The KNN algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other.

1. Load the data

2. Initialize K to your chosen number of neighbors

3. For each example in the data

3.1 Calculate the distance between the query example and the current example from the data.

3.2 Add the distance and the index of the example to an ordered collection

4. Sort the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances

5. Pick the first K entries from the sorted collection

6. Get the labels of the selected K entries

7. If regression, return the mean of the K labels

8. If classification, return the mode of the K labels


**CONTENT BASED FILTERING**

Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.
Content-based Filtering is a Machine Learning technique that uses similarities in features to make decisions. This technique is often used in recommender systems, which are algorithms designed to advertise or recommend things to users based on knowledge accumulated about the user.
## Run Locally

Clone the project

```bash
  git clone https://github.com/pragyabisherwal/movie-recommendation-engine.git
```

Go to the project directory

```bash
  cd movie-recommendation-engine
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```


## Author

- [@PragyaBisherwal](https://github.com/pragyabisherwal/)


## Features

- Content-based Filtering
- Imdb Direct Link
- Movie And Genre Based Filering
- Option To Select Multiple Genres
- A movie could also be chosen based on its rating.
- The range of movies available can be increased.

