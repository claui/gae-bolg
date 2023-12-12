"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from gae_bolg.api to gae_bolg)
from gae_bolg.path import draw as draw

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    'path',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    'path',
    'settings',
]
