import datetime
import sys

import feedparser
import sqlite_utils

FOSSTODON_PROFILE = "https://fosstodon.org/@{username}"
DEFAULT_USER = "bbelderbos"
DB = sqlite_utils.Database("toots.db")


def _parse_fosstodon_feed(rss_feed):
    entries = feedparser.parse(rss_feed).entries
    return entries


def update_db_with_new_toots(username, db=DB, rss_feed=None):
    if rss_feed is None:
        rss_feed = FOSSTODON_PROFILE.format(username=username) + ".rss"

    entries = _parse_fosstodon_feed(rss_feed)
    rows = [
        {
            "id": int(entry.id.split("/")[-1]),
            "summary": entry.summary,
            # could normalize, but KISS :) - also usually max 1 tag per post
            "published": datetime.datetime(*entry.published_parsed[:6]),
            "tags": ", ".join(t.term.lower() for t in getattr(entry, "tags", [])),
            "media": (
                entry.media_content[0]["url"]
                if getattr(entry, "media_content", False)
                else ""
            )
        } for entry in entries
    ]

    db[username].upsert_all(rows, pk="id")


if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_USER
    update_db_with_new_toots(username)
