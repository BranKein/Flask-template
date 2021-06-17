from redis import StrictRedis
from config.redis import host, port, db_num


def Redis() -> StrictRedis:
    return StrictRedis(host=host, port=port, db=db_num, encoding='utf-8', decode_responses=True)


__all__ = ['Redis']
