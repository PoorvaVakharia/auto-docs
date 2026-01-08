import os
from docgen.parser import parse_python_file
from docgen.generator import generate_markdown

EXAMPLE_FILE = os.path.join("examples", "sample_repo", "example.py")
OUTPUT_FILE = "README.md"

docs = parse_python_file(EXAMPLE_FILE)
markdown = generate_markdown(docs)

with open(OUTPUT_FILE, "w") as f:
    f.write(markdown)

print(f"Documentation generated in {OUTPUT_FILE}")
