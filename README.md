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

![](./demo.mov)

A live demo is available as a HuggingFace space [here](https://huggingface.co/spaces/azizalto/fh_pyconsole).

<br>

## Disclaimer ⚠️

> Under the hood, `exec()` is used to execute Python code.