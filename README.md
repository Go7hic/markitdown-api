# markitdown-api

基于 Fastapi 开发的 MarkItDown API 服务

## 部署

可以直在 Railway 上面部署使用

> 可能需要设置适合你的 `MAX_FILE_SIZE` 


## 客户端使用

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