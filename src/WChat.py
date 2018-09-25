# coding=utf-8

__author__ = 'Lian'


class WChat(object):
    def __init__(self, import_name):
        self.funs = {}
        self.menus = {}

    def dispatch_request(self, content):
        pass

    def route(self, keyword, **options):
        def decorator(f):
            print(f.__name__)
            endpoint = options.pop("endpoint", None)
            if endpoint is None:
                endpoint = self.endpoint_from_func(f)
            self.menus[endpoint] = f

        return decorator

    def endpoint_from_func(self, f):
        assert f is not None, 'expected view func if endpoint is not provided.'
        return f.__name__

    def cut(self, msg):
        pass


if __name__ == '__main__':
    wc = WChat()


    @wc.route("cmd")
    def ff():
        pass


    @wc.route("cmd_@")
    def dd():
        pass
