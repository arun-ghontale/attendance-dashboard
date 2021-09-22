import json
import os

import falcon


class StudentReportJSON:

    def __init__(self):
        self._json_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..', 'media',
                                       'student_report.json')

    def on_get(self, req, resp):
        with open(self._json_path) as f:
            resp.body = f.read()

        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.content_type = falcon.MEDIA_HTML
