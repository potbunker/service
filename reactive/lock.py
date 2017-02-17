import os


class LockFile(object):
    def __init__(self, lock_file):
        self._file = lock_file
        self._acquired = False

    @property
    def acquired(self):
        return self._acquired

    def acquire(self):
        fh = open(self._file, 'w') if not os.path.isfile(self._file) else None
        self._acquired = bool(fh)

    def release(self):
        if self._acquired:
            os.remove(self._file)
        return self

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
