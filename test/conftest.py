import asyncio
import os
import sys
import pytest
import pytest_asyncio


# Ensure project root is on sys.path once for all tests
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def app_and_setup():
    """Import the server app and run setup once per test session.

    Returns the `app` instance for use by client fixtures and tests.
    """
    # Import here so tests don't need to manipulate sys.path
    from server import setup, app

    # Run the async setup once for the whole session
    await setup()
    return app


@pytest_asyncio.fixture
async def client(app_and_setup):
    """Provide an async FastMCP Client connected to the app.

    Tests can use `async with client as c: ...` or just `await client.call_tool(...)`
    if they prefer. This fixture yields a Client instance already connected.
    """
    from fastmcp import Client

    async with Client(app_and_setup) as c:
        yield c
