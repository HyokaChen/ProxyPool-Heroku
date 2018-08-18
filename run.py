from proxypool.schedule import ProxyCountCheckProcess, ExpireCheckProcess
from proxypool.conf import VALID_CHECK_CYCLE, POOL_LEN_CHECK_CYCLE, \
    POOL_UPPER_THRESHOLD, POOL_LOWER_THRESHOLD
from proxypool.webapi import app
import os

def cli():
    p1 = ProxyCountCheckProcess(POOL_LOWER_THRESHOLD, POOL_UPPER_THRESHOLD, POOL_LEN_CHECK_CYCLE)
    p2 = ExpireCheckProcess(VALID_CHECK_CYCLE)
    p1.start()
    p2.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    cli()
