# Sudo
This cog contains the `sudo` command. This command is similiar to the sudo command on Linux.

To use that command your ID has to be in the sudoers file. 
The `.sudo` command has the highest permission level and it is bound to IDs and not role permissions.

## `sudo`
The `.sudo` command allows a user to execute any command even without having the necessary permissions by role.
```css
.sudo <cmd>
```

## `kill`
This command kills the running bot instance.
```css
.sudo kill
```

## `reload`
This command reloads the bot by refiring all startup functions.
```css
.sudo reload
```

## `stop`
This command stops the running bot instance.
```css
.sudo stop
```

## `clear_cache`
This command clears the redis cache.
```css
.sudo reload_cache
```

```
This command is mainly used by the worst employer(Defelo#2022) Whoever is reading this please save us...
```
