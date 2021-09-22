import os
import time
import uuid

import falcon


def _ext_to_media_type(ext):
    return 'video/' + ext


def _media_type_to_ext(media_type):
    return media_type[6:]


def _generate_id():
    return str(uuid.uuid4())


class MediaResource(object):
    def __init__(self):
        static_dir_path = os.path.dirname(os.path.realpath(__file__))
        self.storage_path = os.path.join(static_dir_path, '../..', 'media')

    def on_get(self, req, resp, name):
        ext = os.path.splitext(name)[1][1:]
        resp.content_type = _ext_to_media_type(ext)

        image_path = os.path.join(self.storage_path, name)
        # with open(image_path, 'rb') as f:
        #     resp.stream = f

        resp.stream = open(image_path, 'rb')
        resp.stream_len = os.path.getsize(image_path)
