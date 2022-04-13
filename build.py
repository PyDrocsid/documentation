#!/usr/bin/python

from pathlib import Path
import mkdocs_gen_files
import re

CATEGORIES = [
    "administration",
    "moderation",
    "information",
    "integrations",
    "general",
]

with mkdocs_gen_files.open("cogs/SUMMARY.md", "w") as summary:
    for category in map(Path(__file__).parent.joinpath("cogs").joinpath, CATEGORIES):
        if not category.is_dir():
            print(f"::warning::Could not find category {category.name}")
            continue

        print(f"- {category.name.capitalize()}", file=summary)

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

            print(f"    - [{name}]({category.name}/{cog.name}.md)", file=summary)
            mkdocs_gen_files.set_edit_path(path, f"https://github.com/PyDrocsid/cogs/edit/develop/{category.name}/{cog.name}/documentation.md")

    with open("cogs/pubsub.md") as src, mkdocs_gen_files.open("pubsub.md", "w") as dst:
        dst.write(src.read())
