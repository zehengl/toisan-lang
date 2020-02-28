from .util import inject

program1 = "如果真咪你系错。。"

transpile1 = [(1, "if True :"), (2, "你 = False")]

data = [
    (program1, inject(transpile1)),
]
