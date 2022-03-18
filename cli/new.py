import os
import argparse

def new():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--title', dest='t', type=str, required=True,
                    help="provides title for your article")
    parser.add_argument('-f', '--file', dest='f', type=str, required=True,
                        help="provides file name for your article")
    args = parser.parse_args()

    with open('index.rst', 'a+') as f:
        f.write('\n')
        f.write(f'   {args.t.title()} <{args.f}>')

    with open(args.f + '.md', 'w+') as f:
        f.write(f'# {args.t.title()}')
        f.write('\n')
        f.write('\n')
        f.write('## See also')
        f.write('\n')

def new_entry():
    new()

if __name__ == '__main__':
    new_entry()