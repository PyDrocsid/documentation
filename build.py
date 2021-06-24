#!/usr/bin/python

from pathlib import Path
import yaml
import shutil

CATEGORIES = [
    "administration",
    "moderation",
    "information",
    "integrations",
    "general",
]

with open("mkdocs.yml") as file:
    config = yaml.load(file, yaml.Loader)

for item in config["nav"]:
    if "Cogs" in item:
        cog_nav = item["Cogs"]
        break
else:
    print("::error::Could not find cogs in mkdocs navigation!")
    exit(1)

cog_nav.clear()

for category in map(Path(__file__).parent.joinpath("cogs").joinpath, CATEGORIES):
    if not category.is_dir():
        print(f"::warning::Could not find category {category.name}")
        continue

    cog_nav.append({category.name.capitalize(): (category_nav := [])})

    for cog in sorted(category.iterdir()):
        if not cog.is_dir():
            continue

        docs = cog.joinpath("documentation.md")
        if not docs.is_file():
            print(f"::warning::Could not find documentation for {category.name}/{cog.name}")
            continue

        with docs.open() as file:
            name = file.readline().removeprefix("# ").strip()

        target = Path(f"cogs/{category.name}/{cog.name}.md")
        Path("docs").joinpath(target).parent.mkdir(parents=True, exist_ok=True)
        # Path("docs").joinpath(target).symlink_to(docs)
        docs.link_to(Path("docs").joinpath(target))
        category_nav.append({name: str(target)})

with open("mkdocs.yml", "w") as file:
    yaml.dump(config, file)
