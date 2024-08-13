---
title: PyConsole
emoji: 🐍
colorFrom: green
colorTo: green
sdk: docker
app_file: main.py
pinned: false
---


# PyConsole

<a href="https://pyconsole.up.railway.app">
  <img src="https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=railway&logoColor=white" alt="Railway Badge">
</a>

Turn browser into a console for Python using [FastHTML](https://github.com/answerdotai/fasthtml) (in 34 lines).

# Usage

**Setup**

```shell
pip install python-fasthtml
git clone https://github.com/iamaziz/fh_pyconsole.git
cd fh_pyconsole
```

**Run**

```python
python main.py
```

Open browser and navigate to `http://localhost:5001`

# Demo

[![](./demo.mov)](https://github.com/user-attachments/assets/3d37e95f-fcd2-491d-adac-be86777ef591)

A live demo is available [here](https://pyconsole.up.railway.app/) and [here](https://huggingface.co/spaces/azizalto/fh_pyconsole).

<br>

## Disclaimer ⚠️

> Under the hood, `exec()` is used to execute Python code.
