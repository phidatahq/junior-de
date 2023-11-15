from duckgpt.local.conversation import duckdb_local_agent, get_duckgpt_local_conversation
from duckgpt.local.load_tables import load_local_tables

duckgpt_conversation = get_duckgpt_local_conversation(debug_mode=True)

LOAD_DATABASE = True
if LOAD_DATABASE:
    load_local_tables(duckdb_agent=duckdb_local_agent)

duckgpt_conversation.print_response("Give me a histogram of movies by rating, decide the best bucket size?")
