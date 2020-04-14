import tempfile
import os


def test():
    with tempfile.TemporaryFile() as fd:
        fd.write("data".encode('utf-8'))
        # re-open the file to get a read-only file descriptor
        return open(f"/proc/self/fd/{fd.fileno()}", "r")


def main():
   fd = test()
   fd.close()


if __name__ == "__main__":
    main()
