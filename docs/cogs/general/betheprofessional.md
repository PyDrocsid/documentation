# BeTheProfessional

This cog contains a system with which you can give yourself roles

## `role_list`
The `.?` shows all roles which can be added to a user.

```css
.?
```

## `add`
The `.+` command gives your self roles from the list

```css
.+ <topic>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`topic`|:heavy_check_mark:|A role from the list. Multible topics can be added by using a `,` between them|


## `remove`
The `.-` command removes a selfrole from your profile.

```css
.- <topic>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`topic`|:heavy_check_mark:|A role from the list. Multible topics can be removed by using a `,` between them. All roles kan be removed by using `.- *`|


## `new_topic`
The `.*` command adds a new role to the list.

```css
.* <topic>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`topic`|:heavy_check_mark:|A new role (If the role not exist, the role is created). Multible topics can be registered by using a `,` between them.|

## `delte_topic`
The `./` command removes (a) role(s) from the list and deletes the role(s).

```css
./ <topic>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`topic`|:heavy_check_mark:|A topic from the list. Multible roles can be deleted by using a `,` between them.|


## `disable_topic`
The `.%` command unregisters one or more topics without deleting the roles.

```css
.% <topic>
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`topic`|:heavy_check_mark:|A topic from the list. Multible topics can be removed from the list by using a `,` between them.|
