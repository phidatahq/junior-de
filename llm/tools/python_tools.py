from phi.tools.python import PythonTools
from workspace.settings import ws_settings

python_tools = PythonTools(base_dir=ws_settings.ws_root.joinpath("pygpt/op"))
