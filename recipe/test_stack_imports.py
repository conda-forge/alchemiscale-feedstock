from alchemiscale import *

for thing in [
    "Scope",
    "ScopedKey",
    "AlchemiscaleClient",
]:
    assert thing in dir(), f"{thing} not in dir()"
