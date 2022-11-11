from fastapi.responses import StreamingResponse
import aiofiles

async def download(filename, chunk_size=1024*1024):
    async def iterfile():
       async with aiofiles.open(filename, 'rb') as f:
            while chunk := await f.read(chunk_size):
                yield chunk
    headers = {'Content-Disposition': f'attachment; filename="{filename}"'}
    return StreamingResponse(iterfile(), headers=headers, media_type='application/x-zip')