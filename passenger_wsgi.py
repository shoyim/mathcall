import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')

from mathcall.wsgi import application
