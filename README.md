<div align="center">
    <img src="https://raw.githubusercontent.com/zehengl/toisan-lang/main/logo.jpg" alt="taishan" height="128">
</div>

# toisan-lang

[![pytest](https://github.com/zehengl/toisan-lang/actions/workflows/pytest.yml/badge.svg)](https://github.com/zehengl/toisan-lang/actions/workflows/pytest.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![PyPI - License](https://img.shields.io/pypi/l/toisan-lang)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/toisan-lang)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/toisan-lang)
[![Downloads](https://static.pepy.tech/badge/toisan-lang)](https://pepy.tech/project/toisan-lang)
[![GitHub Pages](https://github.com/zehengl/toisan-lang/actions/workflows/gh-deploy.yml/badge.svg)](https://github.com/zehengl/toisan-lang/actions/workflows/gh-deploy.yml)

A programming language based on Toisanese, aka Taishanese, a dialect of Cantonese

## Install

    pip install toisan-lang

## Command Line Usage

- `python -m toisan_lang "..."` to transpile and execute toisan-lang in Python
- `--show xxx` to show extra information if given: `tree` for parse tree, `code` for transpiled python code

For example,

### Transpile and execute

    python -m toisan_lang "你系嚿叉烧。你个头系假咯。睇下你系乜呀。睇下（丐时）系乜。"

Output:

```
{'头': False}
2020-02-28 12:09:01.580252
```

<details>
<summary>To Show extra information</summary>

    python -m toisan_lang "你系嚿叉烧。你个头系假咯。睇下你系乜呀。睇下（丐时）系乜。" --show tree code

Output:

```

Parse Tree:
(START
  (begin_program (begin_scope))
  (block
    (statement (st_assign
      (var_list (var (variable_ref '你'))) '系'
      (exp_list (exp (dict_init '嚿叉烧'))))) '。'
    (statement (st_assign
      (var_list (var (variable_ref '你' '个' '头'))) '系'
      (exp_list (exp (constant (boolean '假')))))) '咯' '。'
    (statement (st_print '睇下'
      (var (variable_ref '你')) '系乜')) '呀' '。'
    (statement (st_print '睇下'
      (adjusted_exp '（'
        (exp (now '丐时')) '）') '系乜')) '。')
  (end_program (end_scope)))

Transpiled Python Code:
from datetime import datetime

def main():
    你 = dict()
    你['头'] = False
    print( 你 )
    print( ( datetime.now() ) )

if __name__ == '__main__':
    main()

{'头': False}
2020-03-03 22:26:13.549966
```

</details>

## Code Usage

```python
from toisan_lang import parse
program = """
...
"""
code, tree = parse(program)
print(code)
print(tree)
exec(code)
```

## Develop

    git clone https://github.com/zehengl/toisan-lang.git
    cd toisan-lang
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt

To run test, simply

    pytest

Happy hacking!

## Credits

- logo from https://izihun.com/yishuzi/564471.html
