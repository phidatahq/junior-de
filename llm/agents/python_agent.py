from phi.agent.python import PythonAgent
from workspace.settings import ws_settings

python_agent = PythonAgent(base_dir=ws_settings.ws_root.joinpath("pygpt/op"))
