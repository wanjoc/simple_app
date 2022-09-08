    FROM 012345678910.dkr.ecr.us-east-1.amazonaws.com/gold-image

    ENV PORT=80

    EXPOSE $PORT

    COPY app.js /app/

    CMD ["node", "/app/app.py"]