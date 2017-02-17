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


class PostgresqlLock(object):
    def __init__(self, lock_domain):
        from psycopg2.pool import ThreadedConnectionPool
        import platform
        import os

        self._lock_detail = (lock_domain, platform.node(), os.getpid())
        self._session = ThreadedConnectionPool()
        self._pool = None
        self._acquired = False

    @property
    def acquired(self):
        return self._acquired

    def acquire(self):
        with self._pool.acquire() as conn:
            cursor = conn.cursor()
            timestamp = cursor.callfunc('public.fn_acquire_lock', self._lock_detail)
        self._acquired = bool(timestamp)

    def release(self):
        with self._pool.acquire() as conn:
            cursor = conn.cursor()
            timestamp = cursor.callfunc('public.fn_release_lock', self._lock_detail)
        self._acquired = False
        return self

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

