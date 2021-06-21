# MediaOnly

This cog contains the `mediaonly` command which can set up channels, in which only pictures can be sent.

## `list`

The `list` subcommand shows a list of all media-only channels.

```css
.mediaonly [list|l|?]
```

Required Permissions:

- `mediaonly.read`

## `add`
The `add` subcommand sets the media-only flag for a given text channel.

```css
.mediaonly [add|a|+] <channel>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`channel`|:heavy_check_mark:|The channel|

Required Permissions:

- `mediaonly.read`
- `mediaonly.write`

## `remove`
The `remove` subcommand removes the media-only flag from a given text channel.

```css
.mediaonly [remove|del|r|d|-] <channel>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`channel`|:heavy_check_mark:|The channel|

Required Permissions:

- `mediaonly.read`
- `mediaonly.write`
