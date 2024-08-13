from fasthtml.common import (
    Main, Div, Form, Input, Code, Pre, fast_app, serve, picolink, MarkdownJS, HighlightJS
)

from code_runner import execute_code as execute
from utils import github_fork_ribbon, clear_history

app, rt = fast_app(hdrs=[picolink, MarkdownJS(), HighlightJS()])
log = []


@app.get("/")
def pyconsole():
    return Main(
            github_fork_ribbon(),
            Div(id="output"),
            Form(
                Input(name="code", placeholder=">>> Type Python code here (and hit enter)"),
                hx_post="/run", hx_target="#output", hx_trigger="submit", id="input_form",
            ),
            cls="container",
            hx_swap="innerHTML show:window:bottom", # automatically scroll to the bottom of the page
        )


@app.post("/run")
def run_code(data: dict):
    log.append((data["code"], execute(data["code"])))
    return Div(*[Div(Pre(Code(code, klass="python")), Div(output, cls="marked"), Div("---", cls="marked")) for code, output in log]), clear_history()


@app.get("/clear")
def clear_log():
    global log
    log = []
    return ""

serve()
