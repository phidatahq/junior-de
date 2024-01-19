from ai.pygpt.pygpt import get_pygpt

pygpt = get_pygpt()

LOAD_KNOWLEDGE_BASE = True
if LOAD_KNOWLEDGE_BASE and pygpt.knowledge_base:
    pygpt.knowledge_base.load(recreate=False)

pygpt.print_response("What is the average rating of movies?")
