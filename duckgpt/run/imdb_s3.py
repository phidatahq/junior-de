from duckgpt.s3.conversation import duckdb_agent, get_duckgpt_conversation
from duckgpt.s3.load_tables import load_tables

duckgpt_conversation = get_duckgpt_conversation(debug_mode=False)

LOAD_DATABASE = True
if LOAD_DATABASE:
    load_tables(duckdb_agent=duckdb_agent)

duckgpt_conversation.print_response("Give me a histogram of movies by rating, decide the best bucket size?")
# duckgpt_conversation.print_response("Which actor was in the most movies?")
