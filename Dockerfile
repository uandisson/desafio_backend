FROM python:3-slim AS builder
ADD . /credito-express-app
WORKDIR /credito-express-app

RUN pip install --target=/credito-express-app requests

FROM gcr.io/distroless/python3-debian10
COPY --from=builder /credito-express-app /credito-express-app
WORKDIR /credito-express-app
ENV PYTHONPATH /credito-express-app
CMD ["/credito-express-app/test_action.py"]
