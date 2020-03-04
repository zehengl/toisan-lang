class ToisanKeyword:
    """
    The toisan-lang keyword
    """

    truth = "岩唔岩啊"
    add = "加"
    subtract = "减"
    multiply = "乘"
    divide = "除以"
    inverse_divide = "除"
    greater_than = "大过"
    less_than = "细过"
    add_one = "多伱"
    subtract_one = "少伱"
    now = "丐时"
    _if_ = "如果"
    then = "咪"
    _elif_ = "或者"
    _else_ = "唔系个话"
    assign = "系"
    _or_ = "抑或"
    _and_ = "同埋"
    _in_ = "喺"
    dot_notation = "个"
    _print_ = "睇下"
    print_ending = "系乜"
    dict_init = "嚿叉烧"
    as_long_as = "只要"

    re_ending = "囖呀啊哇咯呢"
    re_number = "零一二三四五六七八九十"
    re_true = "真对"
    re_false = "假错"


keywords = "".join(
    set(
        "".join(
            [
                getattr(ToisanKeyword, attr)
                for attr in dir(ToisanKeyword)
                if not callable(getattr(ToisanKeyword, attr))
                and not attr.startswith("__")
            ]
        )
    )
)
