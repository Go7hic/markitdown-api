# app/api/routes.py
from fastapi import APIRouter, UploadFile, Header, File, HTTPException
from markitdown import MarkItDown
import tempfile
import os

router = APIRouter()

# 设置文件大小限制（25MB）
MAX_FILE_SIZE = 100 * 1024 * 1024  # 25MB in bytes

@router.post("/convert")
async def convert_file(file: UploadFile = File(...),content_length: int = Header(None, lt=MAX_FILE_SIZE)):
    """
    Convert an uploaded file to Markdown format
    """
  
    # 创建临时文件保存上传的内容
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()
        
        try:
            # 使用 MarkItDown 转换
            md = MarkItDown()
            result = md.convert(temp_file.name)
            print(f"Conversion successful for: {file.filename}")  # 添加日志
                
            return {"markdown": result}
        except Exception as e:
            print(f"Conversion error: {str(e)}")  # 添加日志
            raise HTTPException(status_code=400, detail=str(e))
        finally:
            os.unlink(temp_file.name)