# Movie-Recommender-System

Myself Krupa Bhalani and this is my intership project.

I am here to present " Movie Recommender System "

Implementation of a movie recommendation system designed for seamless interaction between users and movie suggestions. The system comprises both frontend and backend components, each contributing distinct functionalities to the overall user experience.

Frontend:

The frontend of the application is built using Streamlit, a Python library renowned for its simplicity and ease of use in creating interactive web applications. Through the frontend interface, users can engage with the system by selecting a movie of interest from a dropdown menu. Once a movie is chosen, users can trigger the recommendation process by clicking a button conveniently placed within the interface. Subsequently, the system dynamically presents a list of recommended movies, accompanied by their respective posters fetched from The Movie Database (TMDb) API. This visually enriches the user experience and aids in better decision-making.

Backend:

In contrast, the backend of the Movie Recommender System is responsible for data preprocessing and model building. Leveraging the capabilities of Jupyter Notebook, data preprocessing tasks are efficiently executed to prepare the movie dataset for recommendation. This involves merging relevant datasets, handling missing values, and transforming textual data into a suitable format for analysis. The recommendation model is then developed using scikit-learn, a popular machine learning library in Python. By employing cosine similarity, the model computes the similarity between movies based on various features such as overview, genres, keywords, cast, and crew. The resulting similarity matrix enables accurate recommendations tailored to user preferences.

Components

Frontend - app.py: Streamlit web app for user interaction and recommendation display.
Backend - movie.ipynb: Jupyter Notebook containing data preprocessing steps and model building.
