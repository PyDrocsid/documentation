# Polls

This cog contains the poll commands.

```
<> - required
[] - optional
```

## `yes/no`
The `.yesno` command puts :thumbsup: :thumbsdown: as reactions under the message (pictures works too).

```css
.[yesno|yn] [content]
```

|Argument|Required|Description|
|:------:|:------:|:----------|
|`content`|       |The message/content|



## `poll`
The `.poll` command makes a poll with 1-19 options.

```css
.[poll|vote] <question>
[emoji1] <option1>
[emojiX] [optionX]
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`question`|:heavy_check_mark:|The poll topic/question|
|`emojiX`|       |The reaction emote under this message|
|`option1`|:heavy_check_mark:|The poll content for this reaction|
|`optionX`|       |The poll content for this reaction|


## `teampoll`
The `.teampoll` command starts a poll and shows, which teamler has not voted yet.

```css
.[teampoll|teamvote|tp] <question>
[emoji1] <option1>
[emojiX] [optionX]
```
|Argument|Required|Description|
|:------:|:------:|:----------|
|`team-role`|:heavy_check_mark:|Team-role from the staff|
|`question`|:heavy_check_mark:|The poll topic/question|
|`emojiX`|       |The reaction emote under this message|
|`option1`|:heavy_check_mark:|The poll content for this reaction|
|`optionX`|       |The poll content for this reaction|
