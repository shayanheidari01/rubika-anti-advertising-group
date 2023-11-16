from rubpy.structs import Struct
import re


USERNAME_PATTERN = r'.*\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*.*'
RUBIKA_LINK_PATTERN = r'(https?://)?rubika\.ir/(joing|joinc)/[A-Z0-32]+'
LINK_PATTERN = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'

async def username_finder(message: Struct, result) -> bool:
    if message.is_group:
        text = message.raw_text

        if isinstance(text, str):
            return bool(re.search(USERNAME_PATTERN, text))

async def is_link(message: Struct, result) -> bool:
    if message.is_group:
        text = message.raw_text

        if isinstance(text, str):
            if re.search(RUBIKA_LINK_PATTERN, text):
                return True
            else:
                return bool(re.search(LINK_PATTERN, text))

async def is_forward(message: Struct, result) -> bool:
    if message.is_group:
        try:
            forwarded_from = message.forwarded_from
            return True

        except AttributeError:
            return False

async def user_is_not_admin(client, update) -> bool:
    admins = [admin.member_guid for admin in (await client.get_group_admin_members(update.object_guid)).in_chat_members]
    return update.author_guid not in admins