# Discord.py Documentation

This cog contains commands to access and search the documentations of [Python](https://docs.python.org/3/){target=_blank} and [discord.py](https://discordpy.readthedocs.io/en/latest/){target=_blank}. When using these commands to search for Python objects, the documentation is downloaded into the Redis cache to avoid repetitive queries.

## `.py_docs`
Use this command without arguments to get a direct link to the [Python documentation](https://docs.python.org/3/){target=_blank}:
```css
.[py_docs|py]
```

Optionally you can provide the name of any Python object to search for:
```css
.[py_docs|py] [object]
```

## `.dpy_docs`
Use this command without arguments to get a direct link to the [discord.py documentation](https://discordpy.readthedocs.io/en/latest/){target=_blank}:
```css
.[dpy_docs|dpy]
```

Optionally you can provide the name of any discord.py object to search for:
```css
.[dpy_docs|dpy] [object]
```
