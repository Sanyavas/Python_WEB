import json
import logging
from datetime import datetime
import urllib.parse
import pathlib
import mimetypes
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

from jinja2 import Environment, FileSystemLoader

BUFFER_SIZE = 1024
BASE_DIR = pathlib.Path()
env = Environment(loader=FileSystemLoader('templates'))
PORT_HTTP = 3000
SOCKET_HOST = '127.0.0.1'
SOCKET_PORT = 4000


class TheBestFastApp(BaseHTTPRequestHandler):
    def do_POST(self):
        length = self.headers.get('Content-Length')
        data = self.rfile.read(int(length))
        send_data_to_socket(data)
        self.send_response(302)
        self.send_header('Location', '/message')
        self.end_headers()
        self.send_html('message.html')

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)

        match route.path:
            case '/':
                self.send_html('index.html')
            case '/message':
                self.send_html('message.html')
            case '/blog':
                self.render_template('blog.html')
            case _:
                file = BASE_DIR.joinpath(route.path[1:])
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html('error.html', 404)

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self, filename, status_code=200):
        self.send_response(status_code)
        mt = mimetypes.guess_type(filename)
        if mt:
            self.send_header('Content-type', mt[0])
        else:
            self.send_header('Content-type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def render_template(self, filename):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('storage/blog.json', 'rb') as fd:
            blogs = json.load(fd)
        template = env.get_template(filename)
        html = template.render(title="Our Blog", blogs=blogs)
        self.wfile.write(html.encode())


def write_data_to_json(json_data):
    with open('storage/data.json', 'r', encoding='utf-8') as fd:
        new_data = json.load(fd)
        new_data[str(datetime.now())] = json_data
    with open('storage/data.json', 'w', encoding='utf-8') as fd:
        json.dump(new_data, fd, ensure_ascii=False, indent=4)


def save_data_message(data):
    parse_data = urllib.parse.unquote_plus(data.decode())
    try:
        dict_parse = {key: value for key, value in [el.split('=') for el in parse_data.split('&')]}

        storage_dir = pathlib.Path().joinpath('storage')
        file_storage = storage_dir / 'data.json'
        if not file_storage.exists():  # if data.json is not exists
            with open('storage/data.json', 'w', encoding='utf-8') as fd:
                json.dump({}, fd, ensure_ascii=False, indent=4)
            write_data_to_json(dict_parse)
        else:
            write_data_to_json(dict_parse)
    except ValueError as err:
        logging.debug(f"for data {parse_data} error: {err}")
    except OSError as err:
        logging.debug(f"Write data {parse_data} error: {err}")


def send_data_to_socket(data):
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c_socket.sendto(data, (SOCKET_HOST, SOCKET_PORT))
    c_socket.close()


def run_http_server():
    address = ('0.0.0.0', PORT_HTTP)
    httpd = HTTPServer(address, TheBestFastApp)
    logging.info('HTTP server started')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('HTTP server stopped')
    finally:
        httpd.server_close()


def run_socket_server(host, port):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_socket.bind((host, port))
    logging.info('Socket server started')
    try:
        while True:
            msg, address = s_socket.recvfrom(BUFFER_SIZE)
            save_data_message(msg)
    except KeyboardInterrupt:
        logging.info('Socket server stopped')
    finally:
        s_socket.close()


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

    th_server = Thread(target=run_http_server)
    th_server.start()

    th_socket = Thread(target=run_socket_server, args=(SOCKET_HOST, SOCKET_PORT))
    th_socket.start()


if __name__ == '__main__':
    main()
