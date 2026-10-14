import asyncio

from scripts.helpers.event import get_event


async def check():
    event = get_event()
    pull_request = event["pull_request"]
    if not pull_request["maintainer_can_modify"]:
        base_repo = pull_request["base"]["repo"]["full_name"]
        if pull_request["head"]["repo"]["full_name"] != base_repo:
            exit("::error::The PR is not editable by HACS maintainers")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(check())
