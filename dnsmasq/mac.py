import random


def gen(prefix="52:54:00") -> str:
    """

    :param prefix: def "52:54:00:"
    :return: string 52:54:00:12:34:56
    """
    return ":".join([prefix, "%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255))])