from .bzipped import opener as bz2_opener
from .gzipped import opener as gz_opener

__all__ = ['bz2_opener', 'gz_opener']
print(__name__ + ' called')
