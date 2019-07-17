# _Pandoc_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
<!-- [![Docker Build Status](https://img.shields.io/docker/build/microservices/pandoc.svg?style=for-the-badge)](https://hub.docker.com/r/microservices/pandoc/) -->

This microservice exists to provide utilities for dealing with URIs.

## Direct usage in [Storyscript](https://storyscript.io/):

```coffee
>>> pandoc convert doc:'# hi' format:'markdown' output:'html'
'<p>hi</p>\n'
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Convert
```shell
$ omg run convert -a doc=<DOCUMENT> -a format=<FORMAT> -a output=<OUTPUT>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/pandoc/blob/master/LICENSE).
