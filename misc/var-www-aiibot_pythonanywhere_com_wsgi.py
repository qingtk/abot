import sys
import os

# 项目路径
project_home = "/home/aiibot/abot"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 激活虚拟环境（如果有）
activate_env = "/home/aiibot/.virtualenvs/.venv/bin/activate_this.py"
if os.path.exists(activate_env):
    exec(open(activate_env).read(), dict(__file__=activate_env))

# ⭐ 关键：WSGI -> ASGI 转换
from a2wsgi import ASGIMiddleware
from app import app as fastapi_app

application = ASGIMiddleware(fastapi_app)