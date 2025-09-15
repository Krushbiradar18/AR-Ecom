import sys
sys.path.append('..')
from app import app
from io import BytesIO

def handler(event, context):
    # Convert Vercel event to WSGI environ
    environ = {
        'REQUEST_METHOD': event['httpMethod'],
        'PATH_INFO': event['path'],
        'QUERY_STRING': event.get('queryStringParameters', '') or '',
        'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
        'CONTENT_LENGTH': str(len(event.get('body', ''))),
        'SERVER_NAME': 'vercel',
        'SERVER_PORT': '443',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': BytesIO((event.get('body') or '').encode('utf-8')),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }

    # Add headers
    for key, value in event.get('headers', {}).items():
        environ['HTTP_' + key.upper().replace('-', '_')] = value

    # Response
    response_data = []

    def start_response(status, headers, exc_info=None):
        response_data.append((status, headers))

    result = app(environ, start_response)

    status, headers = response_data[0]

    return {
        'statusCode': int(status.split()[0]),
        'headers': dict(headers),
        'body': b''.join(result).decode('utf-8')
    }