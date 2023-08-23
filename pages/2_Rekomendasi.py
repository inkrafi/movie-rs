import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Rekomendasi Film",
    page_icon="🎥"
)


@st.cache_data
def get_recommendation(title):
    idx = df1.index[df1['title'] == title][0]
    poster = f'https://image.tmdb.org/t/p/w500/{df1.loc[idx, "poster_path"]}'
    title = df1.loc[idx, 'title']
    overview = df1.loc[idx, 'overview']
    rating = df1.loc[idx, 'vote_average']
    cast = df1.loc[idx, 'credits']
    date = df1.loc[idx, 'release_date']
    runtime = df1.loc[idx, 'runtime']

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(
        cosine_similarity(
            tfidf_matrix,
            tfidf_matrix[idx])))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:13]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    result = df1.iloc[movie_indices]

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_overview = []
    recommended_movie_genres = []
    recommended_movie_years = []

    for i, j in enumerate(result.poster_path):
        recommended_movie_names.append(result.iloc[i].title)
        recommended_movie_posters.append(
            f'https://image.tmdb.org/t/p/w500/{j}')
        recommended_movie_overview.append(result.iloc[i].overview)
        recommended_movie_genres.append(result.iloc[i].genres)
        recommended_movie_years.append(result.iloc[i].release_date)
    return poster, title, overview, rating, cast, date, runtime, recommended_movie_names, recommended_movie_posters, recommended_movie_overview, recommended_movie_genres, recommended_movie_years


# Yang Tampil di Web
st.title("Rekomendasi Film")

df1 = pickle.load(open('model/movie_list.pkl', 'rb'))
tfidf_matrix = pickle.load(open('model/tfidf_matrix.pkl', 'rb'))
movies_list = df1['title'].values

# Create text input for live search
search_text = st.text_input("Cari Film (opsional)", "")

# Filter movies based on search text
filtered_movies = [
    movie for movie in movies_list if search_text.lower() in movie.lower()]

# Create dropdown with filtered movie options
selected_movie = st.selectbox('Pilih Film', filtered_movies, index=0)

# Get the index of the selected movie
if selected_movie in df1['title'].values:
    idx = df1.index[df1['title'] == selected_movie][0]

    # Get the release year of the selected movie
    release_year = df1.loc[idx, 'release_date'].split('-')[0]

    # Display selected movie with release year
    st.write("Anda memilih film:", selected_movie, "(", release_year, ")")

    if st.button('Rekomendasikan'):
        poster, title, overview, rating, cast, date, runtime, recommended_movie_names, recommended_movie_posters, recommended_movie_overview, recommended_movie_genres, recommended_movie_years = get_recommendation(
            selected_movie)

        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(poster, width=160)
        with text_column:
            st.write("Judul : ", title)
            st.write("Sinopsis : ", overview)
            st.write("Tanggal Rilis : ", date)
            st.write("Pemeran : ", cast)
            st.write("Durasi : ", runtime, "menit")
            st.write("Rating : ", rating)

        st.subheader("Hasil Rekomendasi :")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(recommended_movie_posters[0])
            st.markdown(recommended_movie_names[0])
            with st.expander("Details"):
                st.write(recommended_movie_genres[0])
                st.write(recommended_movie_years[0])
                st.write(recommended_movie_overview[0])

            st.image(recommended_movie_posters[4])
            st.markdown(recommended_movie_names[4])
            with st.expander("Details"):
                st.write(recommended_movie_genres[4])
                st.write(recommended_movie_years[4])
                st.write(recommended_movie_overview[4])

            st.image(recommended_movie_posters[8])
            st.markdown(recommended_movie_names[8])
            with st.expander("Details"):
                st.write(recommended_movie_genres[8])
                st.write(recommended_movie_years[8])
                st.write(recommended_movie_overview[8])

        with col2:
            st.image(recommended_movie_posters[1])
            st.markdown(recommended_movie_names[1])
            with st.expander("Details"):
                st.write(recommended_movie_genres[1])
                st.write(recommended_movie_years[1])
                st.write(recommended_movie_overview[1])

            st.image(recommended_movie_posters[5])
            st.markdown(recommended_movie_names[5])
            with st.expander("Details"):
                st.write(recommended_movie_genres[5])
                st.write(recommended_movie_years[5])
                st.write(recommended_movie_overview[5])

            st.image(recommended_movie_posters[9])
            st.markdown(recommended_movie_names[9])
            with st.expander("Details"):
                st.write(recommended_movie_genres[9])
                st.write(recommended_movie_years[9])
                st.write(recommended_movie_overview[9])

        with col3:
            st.image(recommended_movie_posters[2])
            st.markdown(recommended_movie_names[2])
            with st.expander("Details"):
                st.write(recommended_movie_genres[2])
                st.write(recommended_movie_years[2])
                st.write(recommended_movie_overview[2])

            st.image(recommended_movie_posters[6])
            st.markdown(recommended_movie_names[6])
            with st.expander("Details"):
                st.write(recommended_movie_genres[6])
                st.write(recommended_movie_years[6])
                st.write(recommended_movie_overview[6])

            st.image(recommended_movie_posters[10])
            st.markdown(recommended_movie_names[10])
            with st.expander("Details"):
                st.write(recommended_movie_genres[10])
                st.write(recommended_movie_years[10])
                st.write(recommended_movie_overview[10])

        with col4:
            st.image(recommended_movie_posters[3])
            st.markdown(recommended_movie_names[3])
            with st.expander("Details"):
                st.write(recommended_movie_genres[3])
                st.write(recommended_movie_years[3])
                st.write(recommended_movie_overview[3])

            st.image(recommended_movie_posters[7])
            st.markdown(recommended_movie_names[7])
            with st.expander("Details"):
                st.write(recommended_movie_genres[7])
                st.write(recommended_movie_years[7])
                st.write(recommended_movie_overview[7])

            st.image(recommended_movie_posters[11])
            st.markdown(recommended_movie_names[11])
            with st.expander("Details"):
                st.write(recommended_movie_genres[11])
                st.write(recommended_movie_years[11])
                st.write(recommended_movie_overview[11])
else:
    # Handle jika film yang dipilih tidak ada dalam dataframe
    st.write("Film yang dipilih tidak ditemukan")
