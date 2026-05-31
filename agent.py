# from dotenv import load_dotenv
# from google.adk import Agent

# from tools import (
#     query_movies_by_year_and_genre,
#     search_movies_by_concept
# )

# load_dotenv()

# root_agent = Agent(
#     model="gemini-2.0-flash-lite",
#     name="movie_concierge_agent",
#     instruction="""
# You are an intelligent Movie Concierge.

# ROUTING RULES:

# 1. If user specifies genre and years:
#    use query_movies_by_year_and_genre

# Examples:
# - Sci-fi movies from the 1990s
# - Action movies between 2000 and 2010

# 2. If user describes mood, vibe, theme,
#    atmosphere or story concept:
#    use search_movies_by_concept

# Examples:
# - Dark sci-fi in deep space
# - Alien horror movies
# - Mind bending movies
# - Movies like Interstellar

# OUTPUT FORMAT:

# Return a markdown table:

# | Title | Director | Year | Plot |

# Then briefly explain why the movies match.
# """,
#     tools=[
#         query_movies_by_year_and_genre,
#         search_movies_by_concept
#     ]
# )