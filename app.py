import streamlit as st

from tools import (
    search_movies,
    save_preference,
    get_preferences,
    clear_preferences
)

st.set_page_config(
    page_title="CineMind",
    page_icon="🎬",
    layout="wide"
)

st.title(
    "🎬 CineMind - AI Movie Concierge"
)

st.markdown(
    """
    Powered by:

    - Gemini Embeddings
    - MongoDB Atlas Vector Search
    - MongoDB Persistent Memory
    """
)

# ==========================================================
# Preferences Section
# ==========================================================

st.header("🎯 Movie Preferences")

favorite_movie = st.text_input(
    "Enter a movie you love"
)

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "Save Preference"
    ):

        save_preference(
            favorite_movie
        )

        st.success(
            "Preference saved."
        )

with col2:

    if st.button(
        "Clear Preferences"
    ):

        clear_preferences()

        st.success(
            "Preferences cleared."
        )

prefs = get_preferences()

if prefs:

    st.subheader(
        "Saved Preferences"
    )

    for movie in prefs:

        st.write(
            f"🎬 {movie['title']}"
        )

st.divider()

# ==========================================================
# Search Section
# ==========================================================

st.header("🔍 Movie Search")

query = st.text_input(
    "Describe a movie vibe"
)

if st.button(
    "Find Movies"
):

    if not query.strip():

        st.warning(
            "Please enter a search query."
        )

    else:

        enhanced_query = query

        if prefs:

            memory_context = []

            for movie in prefs:

                plot = movie.get(
                    "plot",
                    ""
                )

                if plot:
                    memory_context.append(
                        plot
                    )

            if memory_context:

                enhanced_query += (
                    " "
                    + " ".join(
                        memory_context[:2]
                    )
                )

        with st.spinner(
            "Searching..."
        ):

            results = search_movies(
                enhanced_query
            )

        st.success(
            f"Found {len(results)} movies"
        )

        for movie in results:

            st.subheader(
                movie.get(
                    "title",
                    "Unknown"
                )
            )

            st.write(
                f"📅 Year: {movie.get('year')}"
            )

            directors = movie.get(
                "directors",
                []
            )

            if directors:

                st.write(
                    "🎬 Directors: "
                    + ", ".join(
                        directors
                    )
                )

            st.write(
                movie.get(
                    "plot",
                    ""
                )
            )

            st.write(
                f"⭐ Similarity Score: "
                f"{movie.get('score', 0):.4f}"
            )

            st.divider()

# ==========================================================
# Architecture
# ==========================================================

st.info(
    """
    Agent Workflow

    User Preferences
        ↓
    MongoDB Memory Retrieval
        ↓
    Gemini Embedding Generation
        ↓
    MongoDB Atlas Vector Search
        ↓
    Personalized Recommendations

    MongoDB acts as:

    • Operational Database
    • Vector Database
    • Persistent Memory Layer
    """
)