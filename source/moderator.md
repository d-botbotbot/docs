```{toctree}
```
# Moderator Commands
## `Customization` Category
### `set_prefix`

set the bot's prefix.

Required Permission: Server Owner

#### Syntax

```html
+set_prefix <prefix>
```
#### Arguments

`prefix`: new prefix for the bot

#### Examples

```
+set_prefix .
+set_prefix -
```
## `Moderation` Category
### `ban`

Ban one/many members

Required Permission: Ban Members

```{tip}
- you can ban multiple members at once
- you can specify members using their username and tag (`BotBotBot#7250`), id (`830238445854130208`) or by @mentioning them
```

#### Syntax

```html
+ban <member|members> [reason]
```
#### Arguments

`member`: one member to Ban
`members`: several members to ban
`reason`: reason for ban (defaults to `No Reason Given`)

#### Examples

```html
+ban <@830238445854130208>
+ban 830238445854130208 @BotBotBot being a bot
```

### `kick`

Kick one/many members

Required Permission: Kick Members

```{seealso}
Functions a lot like `+ban`
```

#### Syntax

```html
+kick <member|members> [reason]
```
#### Arguments

`member`: one member to kick
`members`: several members to kick
`reason`: reason for kick (defaults to `No Reason Given`)


#### Examples

```
+kick <@830238445854130208>
+kick 830238445854130208 @BotBotBot being a bot
```
