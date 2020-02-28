from .util import inject

program1 = "如果真咪你系错。或者错咪我系真。唔系个话区系1。。"

transpile1 = [
    (1, "if True :"),
    (2, "你 = False"),
    (1, "elif False :"),
    (2, "我 = True"),
    (1, "else:"),
    (2, "区 = 1"),
]

data = [
    (program1, inject(transpile1)),
]
