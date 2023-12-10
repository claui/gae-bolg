"""Entry point for the command line interface."""

import sys
import fire  # type: ignore

from . import api
from . import fire_workarounds


def run(*args: str) -> None:
    """Runs the command line interface."""
    fire_workarounds.apply()
    fire.Fire({
        'hello': api.hello,
    }, command=list(args) + sys.argv[1:]
    )
