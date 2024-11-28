import time  # noqa
late = [time.strptime('14:40:00+08:00', '%H:%M:%S') > time.strptime('14:40:00', '%H:%M:%S')]
