import os

import falcon
import jinja2


class MainPageResource:
    def __init__(self, html_path, css_path, js_path):
        self._html_path = html_path
        self._css_path = css_path
        self._js_paths = js_path

    def on_get(self, req, resp):
        resp.body = self.load_template(self._html_path, self._css_path, self._js_paths)

        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.content_type = falcon.MEDIA_HTML

    @staticmethod
    def load_template(html_path, css_path, js_path):
        with open(os.path.abspath(html_path), 'r') as fp:
            html_content = fp.read()

        with open(os.path.abspath(css_path), 'r') as fp:
            css_content = fp.read()

        with open(os.path.abspath(js_path), 'r') as fp:
            js_content = fp.read() + '\n'

        html_template = jinja2.Template(html_content)
        return html_template.render(css_content=css_content, js_content=js_content)
