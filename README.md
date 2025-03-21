# markitdown-api

A MarkItDown API service built with FastAPI

## Deployment

You can deploy it directly on Railway

> You may need to set a suitable `MAX_FILE_SIZE` for your needs


## Client Usage

```js
const formData = new FormData();
formData.append('file', selectedFile);
try {
  const response = await fetch(`${API_BASE_URL}/api/convert`, {
    method: 'POST',
    body: formData,
  });
  if (!response.ok) {
    throw new Error(`Failed to convert file: ${response.statusText}`);
  }
  const data = await response.json();
} catch (err:any) {
  cosnole.error(err?.message || 'An error occurred while converting the file');
}
```