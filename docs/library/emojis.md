# Emojis


## Emoji Map

The `PyDrocsid.emojis` module contains dictionaries for easy conversion between emoji names (e.g. `slight_smile`) and the corresponding unicode characters (e.g. :slight_smile:).


### `name_to_emoji`

This dictionary maps an emoji name to the corresponding unicode character.

```python
>>> emojis.name_to_emoji["slight_smile"]
'🙂'
```


### `emoji_to_name`

This dictionary maps an emoji unicode character to the corresponding emoji names.

```python
>>> emojis.emoji_to_name["🙂"]
['slight_smile', 'slightly_smiling_face']
```
