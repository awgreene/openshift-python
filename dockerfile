# Build from the latest Python 3 Image
FROM python:3

# Add the scripts folder from our project to the image
ADD ./scripts ./scripts

# Create a user that isn't root to avoid security vulnerabilities
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

# Switch to non-root user
USER appuser

# Run our Python script
CMD python ./scripts/hello.py
