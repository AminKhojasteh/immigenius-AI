# Dockerfile (در ریشه پروژه: ai-agents-platform/Dockerfile)

# 1. ایمیج سبک و سریع
FROM python:3.11-slim

# 5. اول requirements نصب بشه (بهترین کش داکر)


RUN pip install uv
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

RUN adduser --disabled-password --gecos '' appuser

# 6. کپی کد پروژه با مالکیت درست
COPY --chown=appuser:appuser . .


# Expose port
EXPOSE 8000    
