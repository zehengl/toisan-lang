from .util import inject

program1 = "你系123。讲你。"
program2 = "你系“1a2b3c你好”。讲你。"
program3 = "你系真。讲你。"
program4 = "你系假。讲你。"
program5 = "你系对。讲你。"
program6 = "你系错。讲你。"
program7 = "你系十。讲你。"
program8 = "你系嚿叉烧。讲你。"
program9 = "你系丐时。讲你。"

transpile1 = [(1, "你 = 123"), (1, "print( 你 )")]
transpile2 = [(1, "你 = '1a2b3c你好'"), (1, "print( 你 )")]
transpile3 = [(1, "你 = True"), (1, "print( 你 )")]
transpile4 = [(1, "你 = False"), (1, "print( 你 )")]
transpile5 = [(1, "你 = True"), (1, "print( 你 )")]
transpile6 = [(1, "你 = False"), (1, "print( 你 )")]
transpile7 = [(1, "你 = 10"), (1, "print( 你 )")]
transpile8 = [(1, "你 = dict()"), (1, "print( 你 )")]
transpile9 = [(1, "你 = datetime.now()"), (1, "print( 你 )")]


data = [
    (program1, inject(transpile1)),
    (program2, inject(transpile2)),
    (program3, inject(transpile3)),
    (program4, inject(transpile4)),
    (program5, inject(transpile5)),
    (program6, inject(transpile6)),
    (program7, inject(transpile7)),
    (program8, inject(transpile8)),
    (program9, inject(transpile9)),
]
