from rubpy import Client, handlers
from rubpy.structs import Struct


import asyncio
import utils


async def main() -> None:
    async with Client('rb-session') as client:
        @client.on(handlers.MessageUpdates(utils.is_link))
        async def updates(update: Struct):
            if await utils.user_is_not_admin(client, update):
                return await update.delete_messages(update.object_guid, [update.message_id])

        @client.on(handlers.MessageUpdates(utils.username_finder))
        async def updates(update: Struct):
            if await utils.user_is_not_admin(client, update):
                return await update.delete_messages(update.object_guid, [update.message_id])

        @client.on(handlers.MessageUpdates(utils.is_forward))
        async def updates(update: Struct):
            if await utils.user_is_not_admin(client, update):
                return await update.delete_messages(update.object_guid, [update.message_id])

        await client.run_until_disconnected()


asyncio.run(main())