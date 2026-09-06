import sys
import os
import traceback

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from main import create_app
    app = create_app()
except Exception as e:
    traceback.print_exc()
    raise e
