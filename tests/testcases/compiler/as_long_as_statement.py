from .util import inject

program1 = """
a系0。
只要a细过10咪
    a系a多伱咯。
    睇下a系乜呀。
。
"""
transpile1 = [(1, "a = 0"), (1, "while a < 10 :"), (2, "a = a + 1"), (2, "print( a )")]
data = [
    (program1, inject(transpile1)),
]
