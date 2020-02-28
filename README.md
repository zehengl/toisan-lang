<div align="center">
    <img src="logo.jpg" alt="taishan" height="196">
</div>

# toisan-lang

A programming language based on Toisanese, aka Taishanese, a dialect of Cantonese

## Install

    pip install toisan-lang

## Usage

- `python -m toisan_lang "..."` to transpile and execute toisan-lang in Python
- `--show xxx` to show extra information if given: `tree` for parse tree, `code` for transpiled python code

For example,

### Transpile and execute

    python -m toisan_lang "你系嚿叉烧。你个头系假。讲你。讲（丐时）。"

Output:

```
{'头': False}
2020-02-28 12:09:01.580252
```

<details>
<summary>To Show extra information</summary>

    python -m toisan_lang "你系嚿叉烧。你个头系假。讲你。讲（丐时）。" --show tree code

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
      (exp_list (exp (constant (boolean '假')))))) '。'
    (statement (st_print '讲' (var
      (variable_ref '你'))) '。'
    (statement (st_print '讲' (adjusted_exp
      '（'
      (exp (now '丐时')) '）')) '。')
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
2020-02-28 12:10:55.823484
```

</details>

## Develop

    git clone https://github.com/zehengl/toisan-lang.git
    cd toisan-lang
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

To run test, simply

    pytest

Happy hacking!

<hr>

<sup>Credit: logo from https://izihun.com/yishuzi/564471.html</sup>
