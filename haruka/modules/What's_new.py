from typing import Optional, List

from telegram import Message, Update, Bot, User

from telegram import MessageEntity

from telegram.ext import Filters, MessageHandler, run_async

from haruka import dispatcher, LOGGER

from haruka.modules.disable import DisableAbleCommandHandler

from googletrans import Translator

@run_async

def whats_new(bot: Bot, update: Update, args: List[str]):

    msg = update.effective_message # type: Optional[Message]

    lan = " ".join(args)


__help__ = """*What's new *
             -added hindi(beta) language
              Note: hindi is under beta
"""

__mod_name__ = "What's New"
