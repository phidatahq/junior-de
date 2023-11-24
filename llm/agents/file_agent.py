from phi.agent.file import FileAgent
from workspace.settings import ws_settings

duckgpt_file_agent = FileAgent(base_dir=ws_settings.ws_root.joinpath("duckgpt/op"))
