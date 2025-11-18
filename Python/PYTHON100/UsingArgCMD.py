import argparse

def print_age(name, age):
    print("Name is ", name, " age is ", age)

parser = argparse.ArgumentParser(description="LA knight")
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--age", type=int, required=True)


args = parser.parse_args()

print_age(args.name, args.age)

