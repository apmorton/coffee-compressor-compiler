import re
from nose.tools import assert_not_equal

from django.conf import settings
settings.configure(STATIC_URL='/static/')

from coffeecompressorcompiler.filter import CoffeeScriptCompiler as CSC


class TestEmberHandlebarsCompiler(object):
    def test_input(self):
        expected_re = r'^\(function.+\);$'
        csc = CSC("", None)

        compiled = csc.input()

        matches = re.match(expected_re, compiled, flags=re.DOTALL)

        msg = '{0} doesn\'t match RE {1}'.format(compiled, expected_re)
        assert_not_equal(matches, None, msg)
