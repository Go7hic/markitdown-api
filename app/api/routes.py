# app/api/routes.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from markitdown import MarkItDown
import tempfile
import os

router = APIRouter()

@router.post("/convert")
async def convert_file(file: UploadFile = File(...)):
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
            
            return {"markdown": result}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        finally:
            os.unlink(temp_file.name)