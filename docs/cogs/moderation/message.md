# Message Commands

This cog contains some functions to send messages as bot.

## `send`
The `.send` command is the main function to send messages. There are three different subcommands.

# copy
You can copy message content and send the message to a different channel by using:

```css
.send [copy|c] <channel> <message>
```
example:
`.send copy #general https://discord.com/channels/637234990404599809/637236069062148106/824732106599956521`

# text
You can send normal text-messages in a channel by using:

```css
.send [text|t] <channel>
```
example:
`.send text #general`

After entering the command, the bot expects you to enter the text. If you have changed your mind, you can abort the process by entering `CANCEL`.

# embed
You can send embeded messages in a channel by using:

(The color is optional)
```css
.send [embed|e] <channel> [color]
```
example:
`.send embed #general #339204`

After entering the command, the bot expects you to enter the title. The title can be between 1-256 
characters long. (Note that pings and channel-mentions dont work in titels)

After entering the title, the bot asks for the content of the message.

If you have changed your mind, you can abort the process by entering `CANCEL`.

## `edit`
Use the `.edit` command to edit messages send by the bot.

# copy
You can copy the content of a message and put it in another message from the bot by using:

```css
.edit [copy|c] <message> <source>
```

example:
`.edit copy https://discord.com/channels/637234990404599809/754443886843396226/840693698780987432 https://discord.com/channels/637234990404599809/754443886843396226/840693822529863690`

(The source has to be a message from the bot)

# text
Use this command to edit normal text-messages send from the bot by using:

```css
.edit [text|t] <message>
```

example:
`.edit text https://discord.com/channels/637234990404599809/754443886843396226/840697294864252968`

After entering the command, the bot expects you to enter the text. If you have changed your mind, you can abort the process by entering "CANCEL".

# embed
Use this command to edit embeded messages send from the bot by using:

```css
.edit [embed|e] <message> [color]
```

example:
`.edit embed #general #339204`

After entering the command, the bot expects you to enter the new title. The title can be between 1-256 
characters long. (Note that pings and channel-mentions dont work in titels)

After entering the new title, the bot asks for the new content of the message.

If you have changed your mind, you can abort the process by entering "CANCEL".

## `delete`
Use this command to delete a message send by the bot.

```css
.delete <message>
```

example:
`.delete https://discord.com/channels/637234990404599809/754443886843396226/840698580305182720`







```
Documentation created by Infinity aka NekoFanatic. Please note that I am not responsible for any grammar or spelling errors. If you still find some, you're welcome to keep them ^^
```
