from .util import inject

program1 = "如果一加一细过2咪你系错。唔系个话区系真。。"
program2 = "如果我乘3大过2咪你系错。或者我减1细过0咪呆系“haha”。唔系个话区系真咯。。"

transpile1 = [
    (1, "if 1 + 1 < 2 :"),
    (2, "你 = False"),
    (1, "else:"),
    (2, "区 = True"),
]
transpile2 = [
    (1, "if 我 * 3 > 2 :"),
    (2, "你 = False"),
    (1, "elif 我 - 1 < 0 :"),
    (2, "呆 = 'haha'"),
    (1, "else:"),
    (2, "区 = True"),
]

data = [
    (program1, inject(transpile1)),
    (program2, inject(transpile2)),
]
