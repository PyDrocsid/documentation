# Invite Whitelist

This cog is for managing allowed discord invites.

## `list`
This command returns a list of all allowed Discord servers.

```css
.[invites|i] [list|l|?]
```


## `show`
This command shows detailed information about a given server.

```css
.[invites|i] [show|info|s|i] <server>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|server|:heavy_check_mark:|The server's name or id|


## `add`
This command adds a Discord server to the whitelist.

```css
.[invites|i] [add|+|a] <invite> <applicant>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|invite|:heavy_check_mark:|The invite link (should be permanent with unlimited usages)|
|applicant|:heavy_check_mark:|The user who wants to add the server to the list|

Required Permissions:

- `invites.manage`


## `remove`
This command removes a server from the list.

```css
.[invites|i] [remove|r|del|d|-] <server>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|server|:heavy_check_mark:|The server's name or id|

Required Permissions:

- `invites.manage`


## `update`
This command allows the applicant and members who have the `invites.manage` permission to update the invite link of a server.

```css
.[invites|i] [update|u] <invite>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|invite|:heavy_check_mark:|The new invite link (should be permanent and with unlimited usages)|
