import json
import redis
from collections import defaultdict


class RedisDB:
    """Backend using Redis.

    Parameters to open the database can be passed with the url format::

        redis://[:password]@localhost:6379/0

    """
    def __init__(self, name):
        self.name = name
        self._dbm = redis.from_url(name)
        self._db = defaultdict(dict)
        self.dirty = set()

    def dump(self):
        """save/close DBM file"""
        for task_id in self.dirty:
            self._dbm[task_id] = json.dumps(self._db[task_id])
        self.dirty = set()

    sync = dump

    def set(self, task_id, dependency, value):
        """Store value in the DB."""
        self._db[task_id][dependency] = value
        self.dirty.add(task_id)

    def get(self, task_id, dependency):
        """Get value stored in the DB."""
        # optimization, just try to get it without checking it exists
        if task_id in self._db:
            return self._db[task_id].get(dependency, None)
        else:
            try:
                task_data = self._dbm[task_id]
            except KeyError:
                return
            self._db[task_id] = json.loads(task_data.decode('utf-8'))
            return self._db[task_id].get(dependency, None)

    def in_(self, task_id):
        """@return bool if task_id is in DB"""
        return task_id in self._dbm or task_id in self.dirty

    def remove(self, task_id):
        """remove saved dependecies from DB for taskId"""
        if task_id in self._db:
            del self._db[task_id]
        if task_id in self._dbm:
            del self._dbm[task_id]
        if task_id in self.dirty:
            self.dirty.remove(task_id)

    def remove_all(self):
        """remove saved dependecies from DB for all tasks"""
        self._db = defaultdict(dict)
        self._dbm.flushdb()
        self.dirty = set()
