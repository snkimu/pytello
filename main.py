import logging
import sys

#import config ←コンソールではなくログファイルに出力したい場合

import droneapp.controllers.server

logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout)
                    #filename=config.LOG_FILE ←ログファイルに出力したい場合


if __name__ == '__main__':
    droneapp.controllers.server.run()