# pydantic-ai-agent
A pydantic ai rag example. A rag example of querying the logfire documentation.

## Install

```bash
uv sync
```

## Create env file

```bash
cp template.env .env
# Add your OpenAI API key to the .env file
```

## Start database
Use docker compose to run the database.
```bash
uv run docker compose up -d
```

## Usage
Use command line to query what commands are available.
```
uv run python app.py -h
```

## Example
You need to build the embedding database before you can run queries.
The example below shows how to build the database and then run a query.
```
# Build the database
uv run --env-file .env -- python app.py build
# Run the rag query
uv run --env-file .env -- python app.py search --query "What is logfire?"
```
