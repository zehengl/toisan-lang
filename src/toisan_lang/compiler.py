from .node import ToisanNode


class ToisanCompiler:
    """
    The toisan-lang compiler
    """

    _compiled = None

    def tree_factory(self, node):
        self._compiled = ToisanNode(self, node)
        return self._compiled

    def compiled(self):
        result = []
        stack = [[self._compiled.compiled, 0]]
        indent = 0
        last = "\n"
        while stack:
            top = stack[-1]
            if len(top[0]) == top[1]:
                if isinstance(top[0], list):
                    last = "\n"
                    if result and not "".join(result[-2:]).endswith("\n\n"):
                        result.append(last)
                stack.pop()
                continue
            atom = top[0][top[1]]
            top[1] += 1
            if isinstance(atom, (list, tuple)):
                stack.append([atom, 0])
                continue
            if atom == ToisanNode.INDENT:
                indent += 1
                continue
            if atom == ToisanNode.OUTDENT:
                indent -= 1
                continue
            output = str(atom)
            if output == "":
                continue
            if last == "\n":
                last = "?"
                result.append("    " * indent)
            new_last = output[-1]
            if new_last == "?":
                output = output[:-1]
            if output[0] == "?":
                result.append(output[1:])
            elif last == "?":
                result.append(output)
            else:
                result.append(" ")
                result.append(output)
            last = new_last
        return "".join(result)
