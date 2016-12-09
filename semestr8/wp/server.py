# coding=utf-8
import inspect
import os

from datetime import datetime

from server_core import HTTPServer, BaseHTTPRequestHandler


class RomaHandler(BaseHTTPRequestHandler):

    def do_static(self):
        current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        url_path = self.path
        if "?" in url_path:
            url_path = url_path[:url_path.index("?")]
        if "#" in url_path:
            url_path = url_path[:url_path.index("#")]
        url_path = "index.html" if url_path == "/" else url_path[1:]
        file_path = os.path.join(current_dir, "static", url_path)
        if file_path != os.path.abspath(file_path):
            # если это подмена пути, то выхожу
            return False
        filename, file_extension = os.path.splitext(file_path)

        if os.path.isfile(file_path):
            self.send_response(200)
            print("file found " + file_path + " " + file_extension)
            if file_extension == ".html":
                self.send_header("Content-Type", "text/html; charset=utf-8")
            elif file_extension == ".css":
                self.send_header("Content-Type", "text/css")
            elif file_extension == ".js":
                self.send_header("Content-Type", "application/javascript")
            elif file_extension == ".xml":
                self.send_header("Content-Type", "text/xml")
            else:
                return False
            self.end_headers()
            with open(file_path, 'r') as f:
                self.wfile.write(f.read())
            return True
        return False

    def do_GET(self):
        if self.do_static():
            return

        if self.path == "/dynamic/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<html><head><title>Это динамическая страница</title></head><body><h1>")
            self.wfile.write("Текущее время на сервере: " + datetime.now().isoformat())
            self.wfile.write("</h1></body></html>")
            return

        self.log_error("wrong file " + self.path)
        self.send_error(code=404)


httpd = HTTPServer(('', 8047), RomaHandler)
httpd.serve_forever()
