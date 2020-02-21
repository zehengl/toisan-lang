from .node import ToisanNode


class ToisanCompiler:
    """
    The toisan-lang compiler
    """

    _compiled = None

    def tree_factory(self, node):
        self._compiled = ToisanNode(node)
        return self._compiled
