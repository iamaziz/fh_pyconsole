from fasthtml.common import Div, A, Img, Link, Button


def app_badge_railway():
    return A(
        Img(src='https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=railway&logoColor=white', alt='Railway Badge'), 
        href='https://pyconsole.up.railway.app'
    )

def github_fork_ribbon():
    return Div(
        Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css'),
        A('Fork me on GitHub', href='https://github.com/iamaziz/fh_pyconsole', data_ribbon='Fork me on GitHub', title='Fork me on GitHub', cls='github-fork-ribbon'),
    )

def clear_history():
    return Button(
    "Clear log",
    hx_get="/clear",
    hx_target="#output",
    style="""
        background-color: #e0e0e0;
        color: #333;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    """
    )