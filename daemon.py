import sys, time
from BaseDaemon import Daemon
import page_for_exua
import unittest
from StringIO import StringIO
class MyDaemon(Daemon):
        def run(self):
                while True:
                        stream = StringIO()
                        print("STARTED")
                        runner = unittest.TextTestRunner(stream=stream)
                        result = runner.run(unittest.makeSuite(page_for_exua.ExampleTestCase))
                        print 'Test output\n', runner, result, stream.read()
                        time.sleep(50)
 
if __name__ == "__main__":
        daemon = MyDaemon('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)