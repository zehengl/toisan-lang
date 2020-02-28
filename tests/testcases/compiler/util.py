_template = """from datetime import datetime

def main():
{{ program }}

if __name__ == '__main__':
    main()
"""


def inject(transpile, template=_template):
    return template.replace(
        "{{ program }}", "\n".join([" " * 4 * l + code for l, code in transpile])
    )
