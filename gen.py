import argparse
import os
from configparser import ConfigParser
from itertools import combinations

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--char', type=str, action='append')
parser.add_argument('-a', '--association', type=str, action='append')

args = parser.parse_args()
characters = []

config = ConfigParser()
base_path = os.path.dirname(__file__)
config.read([os.path.join(base_path, 'characters', x) for x in args.char] + [os.path.join(base_path, 'associations', x) for x in args.association])

associations = {int(y): x for x, y in config['associations'].items()}
characters = {int(y): x for x, y in config['characters'].items()}

for l, r in combinations(characters.items(), 2):
    assoc = [associations[int(x)] for x in str(l[0] * r[0]) if int(x) in associations]
    print(f'{l[1]} - {r[1]}: {", ".join(assoc)}')
