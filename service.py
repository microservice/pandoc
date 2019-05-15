import os
from tempfile import NamedTemporaryFile

import rfc3986
import micro
import delegator
from requests import Session as HTTPSession
from requests.exceptions import RequestException


http = HTTPSession()


def fetch_or_not(uri_or_doc):
    if rfc3986.is_valid_uri(uri_or_doc):
        try:
            r = http.get(uri_or_doc)
            return r.text
        except RequestException:
            return uri_or_doc
    else:
        return uri_or_doc


def convert(doc: str, format: str, *, output: str) -> str:
    """Converts a document, using Pandoc."""

    doc = fetch_or_not(doc)

    tf = NamedTemporaryFile(prefix='pandoc-', suffix=f'-{format}.txt').name
    with open(tf, 'w') as f:
        f.write(doc)

    valid_input = delegator.run('pandoc --list-input-formats').out.split()
    valid_output = delegator.run('pandoc --list-output-formats').out.split()

    assert format in valid_input
    assert output in valid_output

    p = delegator.run(f'pandoc --from={format} --to={output} {tf}')
    os.remove(tf)

    return p.out


if __name__ == '__main__':
    service = micro.Service(name='pandoc')
    service.add(f=convert)
    service.serve(ensure=True)
