#!/usr/bin/python

from pathlib import Path
import yaml
import shutil
import re

CATEGORIES = [
    "administration",
    "moderation",
    "information",
    "integrations",
    "general",
]

with open("mkdocs.yml") as file:
    config = yaml.load(file, yaml.Loader)

def link_to(src, dst):
    if hasattr(src, "link_to"):
        src.link_to(dst)
    else:
        dst.write_bytes(src.read_bytes())

for item in config["nav"]:
    if "Cogs" in item:
        cog_nav = item["Cogs"]
        break
else:
    print("::error::Could not find cogs in mkdocs navigation!")
    exit(1)

docs = Path(__file__).parent.joinpath("cogs/pubsub.md")
if not docs.is_file():
    print(f"::error::Could not find pubsub documentation")
    exit(1)

target = Path("pubsub.md")
link_to(docs, Path("docs").joinpath(target))

cog_nav.clear()

for category in map(Path(__file__).parent.joinpath("cogs").joinpath, CATEGORIES):
    if not category.is_dir():
        print(f"::warning::Could not find category {category.name}")
        continue

    category_nav = []
    cog_nav.append({category.name.capitalize(): category_nav})

    for cog in sorted(category.iterdir()):
        if not cog.is_dir():
            continue

        docs = cog.joinpath("documentation.md")
        if not docs.is_file():
            print(f"::warning::Could not find documentation for {category.name}/{cog.name}")
            continue

        with docs.open() as file:
            name = re.match(r"^#? *(.*)$", file.readline()).group(1).strip()

        target = Path(f"cogs/{category.name}/{cog.name}.md")
        Path("docs").joinpath(target).parent.mkdir(parents=True, exist_ok=True)
        link_to(docs, Path("docs").joinpath(target))
        category_nav.append({name: str(target)})

with open("mkdocs.yml", "w") as file:
    yaml.dump(config, file)
