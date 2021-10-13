<!--
The following is a template for all PyDrocsid documentation.
Exact phrasing and punctuation is part of the documentation. Everything in parentheses are comments for further explanations and should not be in the final documentation.
-->


# TemplateCog

This cog contains some commands to do something.


## `some_command`

This command contains subcommands to do something. / This command is used to do something. (depends on wether there are subcommands or not) <br>
If no subcommand is given, something else will be done. (only if there are subcommands and the default behavior is not the help message)

```css
.[some_command|sc]
```

Required Permissions: (only needed if the command is not publicly available)

- `templatecog.perm1`

!!! note
    Some note for additional information on `some_subcommand`.


### `some_subcommand`

This subcommand contains subcommands to do something. / This subcommand is used to to something. (depends on wether there are subcommands or not.) <br>
If no subcommand is given, something else will be done. (only if there are subcommands and the default behavior is not the help message)

```css
.some_command [some_subcommand|ssc] <some_arg1> [<some_arg2>]
```

Arguments:

|Argument|Required|Description|
|:------:|:------:|:----------|
|`some_arg1`|:heavy_check_mark:|Description for `some_arg1`|
|`some_arg2`||Description for `some_arg2`|

Required Permissions:

- `templatecog.perm1`
- `templatecog.perm2`

!!! note
    Some note for additional information on `some_subcommand`.
