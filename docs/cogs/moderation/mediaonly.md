# MediaOnly

This cog contains the `mediaonly` command which can set up channels, in which only pictures can be send.
```css
.[mediaonly|mo] <subcommand>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`subcommand`|:heavy_check_mark:|a subcommand|

# Subcommands

## `add`
The `add` subcommand sets up a mediaonly atribute to channel.

(`mediaonly.read` and `mediaonly.write` are required permissions)

```css
.mediaonly [add|a|+] <channel>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`channel`|:heavy_check_mark:|The channel|

## `remove`
The `remove` subcommand removes the mediaonly atribute channel.

(`mediaonly.read` and `mediaonly.write` are required permissions)

```css
.mediaonly [remove|del|r|d|-] <channel>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`channel`|:heavy_check_mark:|The channel|

## `list`

Shows a list of all channel with the mediaonly atribute.

(`mediaonly.read` is the rquired permission)

```css
.mediaonly [list|l|?]
```
