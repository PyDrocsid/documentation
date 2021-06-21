# MediaOnly

This cog contains the `mediaonly` command which can set up channels, in which only pictures can be sent.
```css
.[mediaonly|mo] <subcommand>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`subcommand`|:heavy_check_mark:|a subcommand|

# Subcommands

## `add`
The `add` subcommand adds a media-only attribute to the channel.

(`mediaonly.read` and `mediaonly.write` are required permissions)

```css
.mediaonly [add|a|+] <channel>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`channel`|:heavy_check_mark:|The channel|

## `remove`
The `remove` subcommand removes the media-only attribute from the channel.

(`mediaonly.read` and `mediaonly.write` are required permissions)

```css
.mediaonly [remove|del|r|d|-] <channel>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`channel`|:heavy_check_mark:|The channel|

## `list`

Shows a list of all channels with the media-only attribute.

(`mediaonly.read` is the required permission)

```css
.mediaonly [list|l|?]
```
