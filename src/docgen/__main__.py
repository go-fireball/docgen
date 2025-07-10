# src/docgen/__main__.py
"""
Generate Markdown summaries for every .ts/.js file in a repository.

Usage:
    python -m docgen --input /path/to/repo --output output_docs
"""
from __future__ import annotations

import argparse
import datetime
import os
import time
from pathlib import Path

from .repo_scanner import scan_repo
from .llm_client import prompt_ollama
from .doc_writer import write_markdown


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Scan a repo, summarise TypeScript/JavaScript files with LLM, "
                    "and write Markdown docs."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Path to the root of the source repository to scan",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("output_docs"),
        help="Directory where Markdown files will be written (default: %(default)s)",
    )
    return parser.parse_args()


def generate_docs(input_repo: Path, output_docs: Path) -> None:
    """Main workflow: scan repo, summarise each file, write docs."""
    input_repo = input_repo.resolve()
    output_docs.mkdir(parents=True, exist_ok=True)

    files = scan_repo(str(input_repo))

    for filepath in files:
        path = Path(filepath)
        with path.open("r", encoding="utf-8") as f:
            code = f.read()
        start = time.perf_counter()
        summary = prompt_ollama(code)

        # Strip extension and make path repo-relative
        rel_path = path.relative_to(input_repo).with_suffix("")
        write_markdown(str(output_docs), str(rel_path), summary)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Writing doc took {elapsed:.2f}s for {filepath} ")



def main() -> None:
    args = parse_args()
    generate_docs(args.input, args.output)


if __name__ == "__main__":
    main()
