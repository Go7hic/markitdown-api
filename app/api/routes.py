# app/api/routes.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from markitdown import MarkItDown
import tempfile
import os

router = APIRouter()

# 设置文件大小限制（25MB）
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB in bytes

@router.post("/convert")
async def convert_file(file: UploadFile = File(...)):
    """
    Convert an uploaded file to Markdown format
    """
    file_size = 0
    content = await file.read()
    file_size = len(content)
    
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File size exceeds the {MAX_FILE_SIZE/1024/1024}MB limit"
        )
    # 创建临时文件保存上传的内容
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()
        
        try:
            # 使用 MarkItDown 转换
            md = MarkItDown()
            result = md.convert(temp_file.name)
            
            return {"markdown": result}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        finally:
            os.unlink(temp_file.name)