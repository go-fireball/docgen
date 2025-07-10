import os

def write_markdown(output_dir, rel_path, content):
    md_path = os.path.join(output_dir, rel_path + ".md")
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
