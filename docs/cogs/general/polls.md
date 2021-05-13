# Polls

This cog contains the poll commands.

```
<> - required
[] - optional
```

## `yes/no`
The `.yesno` command puts :thumbsup: :thumbsdown: as reactions under the message (pictures work, too).

```css
.[yesno|yn] [content]
```
If `content` is a message link the bot puts the reactions on the message the link refers to.

|Argument|Required|Description|
|:------:|:------:|:----------|
|`content`|       |The message content/A message link|



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
|`emojiX`|       |The reaction emote for option X|
|`option1`|:heavy_check_mark:|The poll content for this reaction|
|`optionX`|       |Poll option X|


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
|`emojiX`|       |The reaction emote for option X|
|`option1`|:heavy_check_mark:|The poll content for this reaction|
|`optionX`|       |The poll option for this reaction|
