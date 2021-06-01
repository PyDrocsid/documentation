# Invite Whitelist

This cog is for managing allowed discord invites.

# `invites`

```css
.[invites|i] <subcommand>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|subcommand|:heavy_check_mark:|A specification|

# *Subcommands:*

## `.add`
This subcommands adds an invite to the list.
|**Permissions**|invites.manage|
|:------:|:----------|
```css
.[invites|i] [add|+|a] <invite> <applicant>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|invite|:heavy_check_mark:|The invite link (should be permanent with unlimited usages)|
|applicant|:heavy_check_mark:|The user who wants to add the server to the list|

## `list`
This command returns a list of all allowed discord servers.
```css
.[invites|i] [list|l|?]
```

## `remove`
This command remnoves a server from the list.
|**Permissions**|invites.manage|
|:------:|:----------|
```css
.[invites|i] [remove|r|del|d|-] <server>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|server|:heavy_check_mark:|The ID from the server|

## `show`
This command show detailed information about a server.

```css
.[invites|i] [show|info|s|i] <server>
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|server|:heavy_check_mark:|The ID/Name from the server|

## `update`
This command updates an invite link from a server.
```css
.[invites|i] [update|u] <invite>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|invite|:heavy_check_mark:|The new invite link (should be permanent and with unlimited usages)|
