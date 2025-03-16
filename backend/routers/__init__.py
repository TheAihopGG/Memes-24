from .api_v1 import views as api_v1
from .memes import views as memes
from .suggested_memes import views as suggested_memes
from .tags import views as tags

__all__ = (
    api_v1,
    memes,
    suggested_memes,
    tags,
)
