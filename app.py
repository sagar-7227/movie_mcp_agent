import streamlit as st

from tools import search_movies

st.set_page_config(
    page_title="AI Movie Concierge",
    page_icon="🎬"
)

st.title("🎬 AI Movie Concierge")

st.write(
    "Describe a movie vibe, theme, mood, or story."
)

query = st.text_input(
    "What kind of movie are you looking for?"
)

if st.button("Search"):

    if not query.strip():
        st.warning(
            "Please enter a movie description."
        )

    else:

        with st.spinner(
            "Searching movies..."
        ):

            results = search_movies(query)

        st.success(
            f"Found {len(results)} movies"
        )

        for movie in results:

            st.subheader(
                movie.get("title", "Unknown")
            )

            st.write(
                f"📅 Year: {movie.get('year')}"
            )

            st.write(
                f"🎬 Director(s): "
                f"{', '.join(movie.get('directors', []))}"
            )

            st.write(
                movie.get("plot", "")
            )

            st.write(
                f"🔍 Similarity Score: "
                f"{movie.get('score', 0):.3f}"
            )

            st.divider()