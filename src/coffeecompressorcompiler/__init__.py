import execjs
from pkg_resources import resource_string


class CoffeePrecompiler(object):
    def __init__(self):
        self.__setup()

    def __setup(self):
        source = ''
        for js in ['compiler', 'coffee-script']:
            source += resource_string(__name__, 'js/{0}.js'.format(js))
        self.ctx = execjs.compile(source)

    def compile(self, source):
        return self.ctx.call('CoffeeScript.compile', source)
