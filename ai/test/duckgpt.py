from ai.duckgpt.duckgpt import get_duckgpt

duckgpt = get_duckgpt()

LOAD_KNOWLEDGE_BASE = True
if LOAD_KNOWLEDGE_BASE and duckgpt.knowledge_base:
    duckgpt.knowledge_base.load(recreate=False)

duckgpt.print_response("What is the average rating of movies?")
