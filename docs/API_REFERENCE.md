# API Reference

All links are relative to `https:/localhost:8000`.
`app_token` is a password from the application. Use it to perform admin actions.

## Navigation

- [Memes (CRUD)](#memes-crud)
    - [CreateMeme](#creatememe)
    - [ReadMeme](#readmeme)
    - [UpdateMeme](#updatememe)
    - [DeleteMeme](#deletememe)
- [Suggested memes](#suggested-memes)
    - [CreateSuggestedMeme](#createsuggestedmeme)
    - [ApproveSuggestedMeme](#approvesuggestedmeme)
    - [RejectSuggestedMeme](#rejectsuggestedmeme)

## Common

`app_token` is a password from the application. Use it to perform admin actions.

### Types of Resources

#### Meme

**Description**

The meme table contains memes that are displayed to the average user

**Data**

- `id`
- `title`
- `image_url`
- `author_name`
- `created_at`
- `updated_at`

#### SuggestedMeme

**Description**

The table contains memes that users suggest adding to the `memes` table

**Data**

- `id`          
- `title`       
- `image_url`   
- `author_name` 
- `created_at`  

## Memes (CRUD)

### CreateMeme

|Method|Url|Description|
|------|---|-----------|
|POST|`/memes/create`|Creates a meme|

JSON-data:

```json
{
    "title": "...",
    "image_url": "...", // url to the image
    "author_name": "...",
    "app_token": "..."
}
```

### ReadMeme

|Method|Url|Description|
|------|---|-----------|
|GET|`/memes/meme`|Responses with a meme data|

JSON-data:

```json
{
    "id": "..." // meme id
}
```

### UpdateMeme

|Method|Url|Description|
|------|---|-----------|
|PUT|`/memes/update`|Updates a meme with the specified id|

JSON-data:

```json
{
    "id": "...", // meme id, which you want to update
    "title": "...", // optional
    "image_url": "...", // optional
    "author_name": "...", // optional
    "app_token": "..."
}
```

### DeleteMeme

|Method|Url|Description|
|------|---|-----------|
|DELETE|`/memes/delete`|Deletes a meme|

JSON-data:

```json
{
    "id": "...",
    "app_token": "..."
}
```

## Suggested memes

### CreateSuggestedMeme

|Method|Url|Description|
|------|---|-----------|
|POST|`/memes/suggest`|Suggests a meme for adding to `Memes` table|

JSON-data:

```json
{
    "title": "...",
    "image_url": "...", // url to the image
    "author_name": "..." // tell us who are you
}
```

### ApproveSuggestedMeme

|Method|Url|Description|
|------|---|-----------|
|POST|`/memes/approve`|Removes Suggested meme with the specified id and adds it to memes table|

JSON-data:

```json
{
    "id": "...", // Suggested meme id, which you want to approve
    "app_token": "..."
}
```

Аfter the Suggested meme is approved, it is deleted from `SuggestedMemes` table and added to `Memes`.

### RejectSuggestedMeme

|Method|Url|Description|
|------|---|-----------|
|POST|`/memes/reject`|Rejects a Suggested meme|

JSON-data:

```json
{
    "id": "...", // Suggested meme id, which you want to reject
    "app_token": "..."
}
```