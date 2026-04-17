import http.server
import mimetypes
import os
from pathlib import Path
from urllib.parse import unquote, urlparse

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "5000"))
ROOT = Path(__file__).resolve().parent
PUBLIC_FILES = {
    "/": "index.html",
    "/index.html": "index.html",
    "/blog": "blog.html",
    "/blog/": "blog.html",
    "/blog.html": "blog.html",
    "/all-tools": "all-tools.html",
    "/all-tools/": "all-tools.html",
    "/all-tools.html": "all-tools.html",
    "/blogger-theme-multitools-professional-animations (1).xml": "blogger-theme-multitools-professional-animations (1).xml",
    "/toolshub-pro-blogger-theme.xml": "toolshub-pro-blogger-theme.xml",
}
PUBLIC_DIRECTORIES = {"attached_assets"}


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self._serve_request(send_body=True)

    def do_HEAD(self):
        self._serve_request(send_body=False)

    def _serve_request(self, send_body):
        parsed_path = unquote(urlparse(self.path).path)

        if parsed_path == "/favicon.ico":
            self._send_text(204, "", send_body)
            return

        relative_path = PUBLIC_FILES.get(parsed_path)

        if relative_path is None:
            relative_path = self._asset_path(parsed_path)

        if relative_path is None:
            self._send_text(404, "404 Not Found", send_body)
            return

        file_path = (ROOT / relative_path).resolve()

        if not self._is_public_path(file_path) or not file_path.is_file():
            self._send_text(404, "404 Not Found", send_body)
            return

        content_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
        content = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8" if content_type.startswith("text/") or content_type in {"application/xml"} else content_type)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        if send_body:
            self.wfile.write(content)

    def _asset_path(self, parsed_path):
        if not parsed_path.startswith("/attached_assets/"):
            return None

        relative_path = parsed_path.lstrip("/")
        first_part = relative_path.split("/", 1)[0]
        if first_part not in PUBLIC_DIRECTORIES:
            return None
        return relative_path

    def _is_public_path(self, file_path):
        try:
            relative = file_path.relative_to(ROOT)
        except ValueError:
            return False

        if any(part.startswith(".") for part in relative.parts):
            return False

        return str(relative) in PUBLIC_FILES.values() or relative.parts[0] in PUBLIC_DIRECTORIES

    def _send_text(self, status, message, send_body):
        body = message.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        if send_body:
            self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    class ReplitHTTPServer(http.server.ThreadingHTTPServer):
        allow_reuse_address = True

    with ReplitHTTPServer((HOST, PORT), Handler) as server:
        print(f"Serving on http://{HOST}:{PORT}")
        server.serve_forever()
