from fasthtml.common import Div, A, Img, Link


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