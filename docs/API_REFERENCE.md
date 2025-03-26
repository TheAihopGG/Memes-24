# API Reference

All links are relative to `https:/localhost:8000`.
`app_token` is a password from the application. Use it to perform admin actions.

## Navigation

- [Memes (CRUD)](#memes-crud)
    - [CreateMeme](#creatememe)
    - [GetMeme](#readmeme)
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

#### Tags

**Description**

*Tags realization in progress*

**Data**

- `id`          
- `name`    

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

### GetMeme

|Method|Url|Description|
|------|---|-----------|
|GET|`/memes/meme`|Responses with a meme data|

JSON-data:

```json
{
    "id": "..." // meme id
}
```

### GetRandomMeme

|Method|Url|Description|
|------|---|-----------|
|GET|`/memes/random_meme`|Responses a random data|

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

### SuggestMeme

|Method|Url|Description|
|------|---|-----------|
|POST|`/suggested_memes/suggest`|Suggests a meme for adding to `Memes` table|

JSON-data:

```json
{
    "title": "...",
    "image_url": "...", // url to the image
    "author_name": "...",
    "app_token": "..."
}
```

### ApproveSuggestedMeme

|Method|Url|Description|
|------|---|-----------|
|POST|`/suggested_memes/approve`|Removes Suggested meme with the specified id and adds it to memes table|

JSON-data:

```json
{
    "id": "...", // Suggested meme id, which you want to approve
    "remove_invalid_images_urls": "true", // if true, suggested memes with invalid urls will be removed
    "app_token": "..."
}
```

Аfter the Suggested meme is approved, it is deleted from `SuggestedMemes` table and added to `Memes`.

### RejectSuggestedMeme

|Method|Url|Description|
|------|---|-----------|
|POST|`/suggested_memes/reject`|Rejects a Suggested meme|

JSON-data:

```json
{
    "id": "...", // Suggested meme id, which you want to reject
    "app_token": "..."
}
```

### GetSuggestedMemes

|Method|Url|Description|
|------|---|-----------|
|GET|`/suggested_memes/all`|Returns all suggested memes|

JSON-data:

```json
{
    "app_token": "..."
}
```

## Tags

### CreateTag

|Method|Url|Description|
|------|---|-----------|
|POST|`/tags/create`|Creates a tag|

JSON-data:

```json
{
    "tag_name":"...",
    "app_token": "..."
}
```

### GetTag

|Method|Url|Description|
|------|---|-----------|
|GET|`/tags/get`|Responses a tag|

JSON-data:

```json
{
    "tag_id":"..."
}
```

### UpdateTag

|Method|Url|Description|
|------|---|-----------|
|PUT|`/tags/update`|Updates a tag|

JSON-data:

```json
{
    "tag_id":"...",
    "tag_name":"..."
}
```

### DeleteTag

|Method|Url|Description|
|------|---|-----------|
|DELETE|`/tags/delete`|Deletes a tag|

JSON-data:

```json
{
    "tag_id":"...", // tag id
    "app_token": "..."
}
```