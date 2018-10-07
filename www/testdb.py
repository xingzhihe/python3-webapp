import logging; logging.basicConfig(level=logging.INFO)
import asyncio

import orm
from models import User, Blog, Comment




async def test():
    global __pool
    #yield from orm.create_pool(loop, user='root', password='root', database='awesome')
    __pool = await orm.create_pool(loop, user='root', password='root', db='awesome')
    
    affected = await User.deleteAll()
    print('affected %s' % affected)
    
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

    u = User(name='xingzhihe', email='xingzhihe@sohu.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

#for x in test():
#    pass