from compressor.filters import FilterBase
from coffeecompressorcompiler import CoffeePrecompiler


class CoffeeScriptCompiler(FilterBase):
    """CoffeScriptCompiler"""

    def __init__(self, content, attrs, **kwargs):
        super(CoffeeScriptCompiler, self).__init__(content, **kwargs)
        self.cp = CoffeePrecompiler()
        self.attrs = attrs

    def input(self, **kwargs):
        return self.cp.compile(self.content)
