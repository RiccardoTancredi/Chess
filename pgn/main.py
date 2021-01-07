from pgn.replay import Replay
from pgn.pgn_parser import PGNParser

if __name__ == '__main__':
    matches = PGNParser().parse_file("Zukertort.pgn")

    print(f"Parsed {len(matches)} matches!")

    replay = Replay(matches[0])
    replay.play()


