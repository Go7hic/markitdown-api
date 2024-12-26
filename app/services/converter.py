# app/services/converter.py
from markitdown import MarkItDown
import asyncio

md = MarkItDown()

async def convert_to_markdown(file_path: str) -> str:
    """
    Convert a file to markdown format using markitdown library
    """
    # Since markitdown.to_markdown is a synchronous function,
    # we run it in a thread pool to avoid blocking
    loop = asyncio.get_event_loop()
    markdown_content = await loop.run_in_executor(
        None, md.convert, file_path
    )
    return markdown_content