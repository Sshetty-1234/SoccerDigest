from django.core.wsgi import get_wsgi_application
from io import BytesIO

app = get_wsgi_application()

def handler(event, context):
    """
    AWS Lambda / Vercel-style handler for Django.
    Converts a Vercel event to a WSGI-compatible request.
    """
    environ = {
        'REQUEST_METHOD': event.get('method', 'GET'),
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': event.get('queryString', ''),
        'wsgi.input': BytesIO(event.get('body', '').encode('utf-8')),
        'CONTENT_LENGTH': str(len(event.get('body', ''))),
        'wsgi.errors': BytesIO(),
        'wsgi.version': (1, 0),
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'https',
        'SERVER_NAME': 'vercel.app',
        'SERVER_PORT': '443',
    }

    response = []

    def start_response(status, headers):
        response.append(status)
        response.append(headers)

    result = app(environ, start_response)
    body = b"".join(result).decode("utf-8")

    status_code = int(response[0].split()[0])

    return {
        "statusCode": status_code,
        "headers": dict(response[1]),
        "body": body
    }
