import re

from nose.tools import assert_not_equal

from coffeecompressorcompiler import CoffeePrecompiler as CP


class TestEmberPrecompiler(object):
    def test_init(self):
        # just make sure we dont raise exceptions
        CP()

    def test_compile(self):
        source = ''
        expected_re = r'^\(function.+\);$'
        cp = CP()

        compiled = cp.compile(source)

        matches = re.match(expected_re, compiled, flags=re.DOTALL)

        msg = '{0} doesn\'t match RE {1}'.format(compiled, expected_re)
        assert_not_equal(matches, None, msg)
