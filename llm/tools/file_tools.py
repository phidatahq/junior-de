from phi.tools.file import FileTools
from workspace.settings import ws_settings

duckgpt_file_tools = FileTools(base_dir=ws_settings.ws_root.joinpath("duckgpt/op"))
