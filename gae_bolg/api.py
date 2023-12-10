"""The primary module in gae_bolg."""


def hello(name: str = 'world') -> str:
    """Says hello to someone.

    :param `name`:
        whom to greet.
        If left empty, we greet the `world`.

    :raises ValueError:
        if `name` is empty.

    :return: a friendly Hello, addressed to `name`.
    """

    if not name:
        raise ValueError('Name cannot be empty.')

    return f'Hello, {name}!'
