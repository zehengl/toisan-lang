<div align="center">
    <img src="logo.jpg" alt="taishan" height="196">
</div>

# toisan-lang

A programming language based on Toisanese, aka Taishanese, a dialect of Cantonese

## Install

    pip install toisan-lang

## Usage

- `python -m toisan_lang "..."` to transpile and execute toisan-lang in Python
- `--tree` to only show parse tree
- `--code` to show transpiled code before execution

For example,

### Show the parse tree without execution

    python -m toisan_lang "你系1。讲你。" --tree

Output:

```
(START
  (begin_program (begin_scope))
  (block
    (statement (st_assign
      (var_list (var (variable_ref '你'))) '系'
      (exp_list (exp (constant (number '1')))))) '。'
    (statement (st_print '讲' (var
      (variable_ref '你'))) '。')
  (end_program (end_scope)))
```

### Transpile and execute

    python -m toisan_lang "你系1。讲你。" --code

Output:

```
def main():
    你 = 1
    print( 你 )

if __name__ == '__main__':
    main()

1
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
