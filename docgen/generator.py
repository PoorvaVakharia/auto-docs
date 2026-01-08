from typing import List, Dict

def generate_markdown(docs: List[Dict]) -> str:
    md = "# Auto-Generated Documentation\n\n"
    for item in docs:
        md += f"## {item['type'].title()}: {item['name']}\n"
        docstring = item['docstring'] or "No docstring provided."
        md += f"{docstring}\n\n"
    return md
