# Twig

Minimal-effort reasonably preconfigured logger for Python.

## Installation

Installing this way show the correct instructions in `pip freeze`:

```{shell}
pip install -e git+https://github.com/numpde/twig.git@64d2b52#egg=twig
```

## Usage

```python
from twig import log, LOG_FILE
log.info("Hello, Dave.")
log.info(LOG_FILE)
```

## Authors

RA (2020-12-21)

## License

MIT/Expat
