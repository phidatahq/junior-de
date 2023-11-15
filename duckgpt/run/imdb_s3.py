from duckgpt.s3.conversation import duckdb_s3_agent, get_duckgpt_s3_conversation
from duckgpt.s3.load_tables import load_s3_tables

duckgpt_conversation = get_duckgpt_s3_conversation(debug_mode=False)

LOAD_DATABASE = True
if LOAD_DATABASE:
    load_s3_tables(duckdb_agent=duckdb_s3_agent)

duckgpt_conversation.print_response("Give me a histogram of movies by rating, decide the best bucket size?")
