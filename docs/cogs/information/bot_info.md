# Bot Info

This cog contains information about the bot and its tasks.

## Commands

### `info`
The `.info` command shows information about the bot.
```css
.[info|infos|about]
```

The information given by this command include:

- Bot name and description
- Author
- Contributors
- Version
- Number of enabled cogs
- Github repository
- [Discord](https://discord.pydrocsid.ml/) and [GitHub](https://github.com/PyDrocsid) links of the PyDrocsid framework
- Prefix
- Help command
- Where to submit bug reports and feature requests


### `version`
The `.version` command returns the current version of the bot.
```css
.[version|v]
```


### `github`
The `.github` command returns information about the GitHub repository of the bot.

```css
.[github|gh]
```


### `contributors`
The `.contributors` command returns a list of all people that contributed to the bot.
```css
.[contributors|contri|con]
```


### `cogs`
The `cogs` command returns a list of all cogs currently in use.
```css
.cogs
```


## Status Message
The bot displays a status message that is updated every 20 seconds. The list of status strings is defined under the `profile_status` [translation key](https://docs.pydrocsid.ml/library/translations/).
