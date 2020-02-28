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

    python -m toisan_lang "你系10。讲你。"

Output:

`10`

### Show extra information

    python -m toisan_lang "你系10。讲你。" --show tree code

Output:

```
Parse Tree:
(START
  (begin_program (begin_scope))
  (block
    (statement (st_assign
      (var_list (var (variable_ref '你'))) '系'
      (exp_list (exp (constant (number '十')))))) '。'
    (statement (st_print '讲' (var
      (variable_ref '你'))) '。')
  (end_program (end_scope)))

Transpiled Python Code:
def main():
    你 = 10
    print( 你 )

if __name__ == '__main__':
    main()

10
```

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
