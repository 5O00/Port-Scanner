import argparse

from utils.utils import parse_ports

def parse_args():
    parser = argparse.ArgumentParser(
        usage="Enter usage here",
        description="Un simple scanner de port")

    parser.add_argument("-p", "--port", 
        help="Les ports à scanner",
        type=str, 
        default="0:2048")

    parser.add_argument("--host",
        help="Adresse ip/nom de domaine à scanner",
        type=str,
        required=True)

    parser.add_argument("--max_thread",
        help="Numbers of threads to start, default is 30",
        type=int,
        required=False,
        default=30,
        dest="maxt"
        )


    return parser.parse_args()

