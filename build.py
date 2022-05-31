#!/usr/bin/python

from pathlib import Path
import mkdocs_gen_files
import sys
import re

sys.path.insert(0, "library")

CATEGORIES = sorted(f.name for f in Path("cogs").iterdir() if f.is_dir() and not f.name.startswith("."))

nav = mkdocs_gen_files.Nav()

for category in map(Path(__file__).parent.joinpath("cogs").joinpath, CATEGORIES):
    if not category.is_dir():
        print(f"::warning::Could not find category {category.name}")
        continue

    for cog in sorted(category.iterdir()):
        if not cog.is_dir():
            continue

        docs = cog.joinpath("documentation.md")
        if not docs.is_file():
            print(f"::warning::Could not find documentation for {category.name}/{cog.name}")
            continue

        path = f"cogs/{category.name}/{cog.name}.md"
        with docs.open() as src, mkdocs_gen_files.open(path, "w") as dst:
            content = src.read()
            dst.write(content)
            name = re.match(r"^#? *(.*)$", content.splitlines()[0])[1].strip()

        nav[(category.name.capitalize(), name)] = f"{category.name}/{cog.name}.md"
        mkdocs_gen_files.set_edit_path(path, f"https://github.com/PyDrocsid/cogs/edit/develop/{category.name}/{cog.name}/documentation.md")

nav[("PubSub Channels",)] = "pubsub.md"

with open("cogs/pubsub.md") as src, mkdocs_gen_files.open("cogs/pubsub.md", "w") as dst:
    dst.write(src.read())

with mkdocs_gen_files.open("cogs/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())

nav = mkdocs_gen_files.Nav()
for path in sorted(Path("library/PyDrocsid").rglob("*.py")):
    module_path = path.relative_to("library").with_suffix("")
    doc_path = path.relative_to("library").with_suffix(".md")
    full_doc_path = Path("library", doc_path)

    parts = list(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        print(f"::: {identifier}", file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("library/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())

sys.path.insert(0, "library")
