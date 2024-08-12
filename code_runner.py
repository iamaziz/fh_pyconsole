import sys
from io import StringIO


def execute_code(code: str):
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(code, globals())
        sys.stdout = old_stdout
        return redirected_output.getvalue()
    except Exception as e:
        return str(e)

