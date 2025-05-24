import argparse
import asyncio

def build_cmd_(args):
    """Build the search database."""
    from db_setup import build_search_db
    asyncio.run(build_search_db())


def search_cmd_(args):
    """Run the agent to answer a question."""
    from rag import run_agent
    asyncio.run(run_agent(args.query))


if __name__ == '__main__':
    command = argparse.ArgumentParser(
        description='Run the Pydantic AI RAG example application.',
    )
    action = command.add_subparsers(dest='action')
    build_cmd = action.add_parser(
        'build',
        help='Build the search database.',
    )
    build_cmd.set_defaults(func=build_cmd_)
    search_cmd = action.add_parser(
        'search',
        help='Run the agent to answer a question.',
    )
    search_cmd.add_argument(
        '--query',
        type=str,
        default='How do I configure logfire to work with FastAPI?',
        help='The question to ask the agent.',
    )
    search_cmd.set_defaults(func=search_cmd_)
    args = command.parse_args()
    if not hasattr(args, 'func'):
        command.print_help()
        exit(1)
    args.func(args)
