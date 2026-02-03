# Dockerfile (در ریشه پروژه: ai-agents-platform/Dockerfile)

# 1. ایمیج سبک و سریع
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1


COPY requirements.txt .

RUN pip install --no-cache-dir \
    -i https://mirrors.aliyun.com/pypi/simple \
    --trusted-host mirrors.aliyun.com \
    --progress-bar on \
    -r requirements.txt
RUN adduser --disabled-password --gecos '' appuser

# 6. کپی کد پروژه با مالکیت درست
COPY --chown=appuser:appuser . .


# Expose port
EXPOSE 8000    
