#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy
from zeuspy import raw
from zeuspy import types


class AnswerWebAppQuery:
    async def answer_web_app_query(
        self: "zeuspy.Client",
        web_app_query_id: str,
        result: "types.InlineQueryResult"
    ) -> "types.SentWebAppMessage":
        """Set the result of an interaction with a `Web App <https://core.telegram.org/bots/webapps>`_ and send a
        corresponding message on behalf of the user to the chat from which the query originated.

        Parameters:
            web_app_query_id (``str``):
                Unique identifier for the answered query.

            result (:obj:`~zeuspy.types.InlineQueryResult`):
                A list of results for the inline query.

        Returns:
            :obj:`~zeuspy.types.SentWebAppMessage`: On success the sent web app message is returned.
        """

        r = await self.invoke(
            raw.functions.messages.SendWebViewResultMessage(
                bot_query_id=web_app_query_id,
                result=await result.write(self)
            )
        )

        return types.SentWebAppMessage._parse(r)
