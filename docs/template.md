<!--
The following is a template for all PyDrocsid documentation.
Exact phrasing and punctuation is part of the documentation. Everything in parentheses are comments for further explanations and should not be in the final documentation.
-->


# Template

Contains commands to do something.


## `some_command`

Contains subcommands to do something. / Does something. (depends on whether there are subcommands or not) <br>
If no subcommand is given, something else will be done. (only if there are subcommands and the default behavior is not the help message)

```css
.[some_command|sc]
```

Required Permissions: (only needed if the command is not publicly available)

- `templatecog.perm1`

!!! note (only needed if there is something noteworthy)
    Some note for additional information on `some_command`.


### `some_subcommand`

Contains subcommands to do something. / Does something. (depends on whether there are subcommands or not) <br>
If no subcommand is given, something else will be done. (only if there are subcommands and the default behavior is not the help message)

```css
.some_command [some_subcommand|ssc] <some_arg1> [<some_arg2>]
```

Arguments: (only needed if there are arguments)

| Argument    | Required           | Description                 |
|:-----------:|:------------------:|:----------------------------|
| `some_arg1` | :fontawesome-solid-check: | Description for `some_arg1` |
| `some_arg2` |                    | Description for `some_arg2` |
(column width matches longest string in column + 1 space padding per side, all text in columns is left aligned)

Required Permissions: (only needed if the command is not publicly available)

- `templatecog.perm1`
- `templatecog.perm2`

!!! note (only needed if there is something noteworthy)
    Some note for additional information on `some_subcommand`.
