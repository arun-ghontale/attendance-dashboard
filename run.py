import os
from wsgiref import simple_server

# imports
import falcon
from falcon_cors import CORS
from falcon_multipart.middleware import MultipartMiddleware

from resources.student_report import StudentReportJSON
from resources.main_page import MainPageResource
from resources.send_mail import SendReport
from resources.media import MediaResource

# to check the health of app
class HealthResource:
    def on_get(self, req, resp):
        resp.body = 'healthy'
        resp.status = falcon.HTTP_200


cors = CORS(allow_all_headers=True,
            allow_all_methods=True,
            allow_all_origins=True)

# create Falcon APIs
api = falcon.API(middleware=[MultipartMiddleware(), cors.middleware])
api.req_options.auto_parse_form_urlencoded = True

# health
health_resource = HealthResource()
api.add_route('/health', health_resource)

main_page_css_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/mainPage.css')
main_page_js_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/mainPage.js')
main_page_html_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/mainPage.html')

main_page_resource = MainPageResource(html_path=main_page_html_path, css_path=main_page_css_path,
                                      js_path=main_page_js_path)
api.add_route('/', main_page_resource)

# sample json resource
student_report_resource = StudentReportJSON()
api.add_route('/student-report-json', student_report_resource)

# send report resource
send_report_resource = SendReport()
api.add_route('/send-report', send_report_resource)

# media
media_resource = MediaResource()
api.add_route('/media/{name}', media_resource)


def main():
    # create and start a server
    host = '0.0.0.0'
    port = 5005
    http = simple_server.make_server(host, port, api)
    print('Started server on : {}:{}'.format(host, port))
    http.serve_forever()


if __name__ == '__main__':
    main()

print('Started server')
