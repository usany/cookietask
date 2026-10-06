import os
import signal
import sys
import time



from scheduler import start, stop  # noqa: E402


class Command:
    help = 'Start the APScheduler and keep the process alive'

    def handle(self, *args, **options):
        def sigterm_handler(signum, frame):
            print('Received SIGTERM, shutting down scheduler...')
            stop()
            sys.exit(0)

        signal.signal(signal.SIGTERM, sigterm_handler)
        signal.signal(signal.SIGINT, sigterm_handler)

        start()
        print('Scheduler started. Waiting for jobs...')

        while True:
            time.sleep(1)


if __name__ == '__main__':
    Command().handle()
