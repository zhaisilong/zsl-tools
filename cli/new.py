import os
import argparse

def new():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', dest='n', type=str, required=True,
                    help="provides title for your article")
    args = parser.parse_args()

    with open('index.rst', 'a+') as f:
        f.write('\n')
        f.write(f'   {args.n.title()} <{args.n}>')

    with open(args.n + '.md', 'w+') as f:
        f.write(f'# {args.n.title()}')
        f.write('\n')
        f.write('\n')
        f.write('## See also')
        f.write('\n')

def new_entry():
    new()

if __name__ == '__main__':
    new_entry()