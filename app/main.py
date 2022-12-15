import argparse
import sys

from client.main import main as client
from server.main import main as server

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="server", choices=["server", "client"], help="running mode")

    args = parser.parse_args(sys.argv[1:])

    if args.mode == "server":
        server()
    else:
        client()

if __name__ == "__main__":
    main()
