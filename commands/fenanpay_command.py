import sys


class Command:
    help = 'My command'

    def handle(self, *args, **kwargs):
        print('All done')
        return 0


if __name__ == "__main__":
    command = Command()
    command.handle()
