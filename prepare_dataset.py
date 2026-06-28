import random
import pandas as pd

random.seed(42)

dataset = []

# -------------------------------
# Clean code templates
# -------------------------------

clean_templates = [
    'print("Hello World")',
    'x = 10\nprint(x)',
    'for i in range(5):\n    print(i)',
    'if x > 5:\n    print(x)',
    'numbers = [1,2,3]\nprint(numbers[1])',
    'def add(a,b):\n    return a+b',
    'name = "Alice"\nprint(name)',
    'x = 10\ny = 5\nprint(x/y)',
    'for i in range(3):\n    print(i*i)',
    'a = [1,2,3]\nprint(len(a))',
    'def square(x):\n    return x*x',
    'print(sum([1,2,3]))',
    'value = max([2,5,7])\nprint(value)',
    'text = "Python"\nprint(text.lower())',
    'nums = [5,4,3]\nnums.sort()\nprint(nums)'
]

# -------------------------------
# Bug generators
# -------------------------------

def missing_colon():
    return "for i in range(5)\n    print(i)"

def indentation_error():
    return "if x > 5:\nprint(x)"

def missing_parenthesis():
    return 'print("Hello World"'

def undefined_variable():
    return "print(total)"

def divide_by_zero():
    return "x = 10\nprint(x/0)"

def wrong_assignment():
    return "if x = 5:\n    print(x)"

def index_error():
    return "a = [1,2,3]\nprint(a[5])"

def missing_quotes():
    return "name = Alice\nprint(name)"

def missing_argument():
    return "def add(a,b):\n    return a+b\n\nprint(add(5))"

def unclosed_list():
    return "a = [1,2,3\nprint(a)"

bug_generators = [
    missing_colon,
    indentation_error,
    missing_parenthesis,
    undefined_variable,
    divide_by_zero,
    wrong_assignment,
    index_error,
    missing_quotes,
    missing_argument,
    unclosed_list
]

# -------------------------------
# Generate dataset
# -------------------------------

NUM_SAMPLES = 5000

for _ in range(NUM_SAMPLES // 2):
    code = random.choice(clean_templates)
    dataset.append([code, "clean"])

for _ in range(NUM_SAMPLES // 2):
    bug = random.choice(bug_generators)
    dataset.append([bug(), "buggy"])

# Shuffle dataset
random.shuffle(dataset)

# Save CSV
df = pd.DataFrame(dataset, columns=["code", "label"])
df.to_csv("dataset.csv", index=False)

print("Dataset generated successfully!")
print("Total Samples :", len(df))
print(df.head())