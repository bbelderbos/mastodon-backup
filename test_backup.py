import pathlib
import pytest
import sqlite_utils

from backup_toots import update_db_with_new_toots

TEST_DB_FILE = "test-toots.db"
TEST_DB = sqlite_utils.Database(TEST_DB_FILE)
FIRST_TEST_RSS = "test1.rss"
SECOND_TEST_RSS = "test2.rss"
USERNAME = "bbelderbos"
TOOT1 = {
    "id": 109398609743208478,
    "media": "",
    "published": "2022-11-24T11:45:09",
    "summary": "<p>Oops I wrote a lot of code, how do I keep my <a "
    'class="mention hashtag" href="https://fosstodon.org/tags/git" '
    'rel="tag">#<span>git</span></a> commits granular?</p><p>Useful '
    "command: git add -p .</p>",
    "tags": "git",
}
TOOT2 = {
    "id": 109398759036300470,
    "media": "",
    "published": "2022-11-24T12:23:07",
    "summary": "<p>When I saw that Mastodon supports RSS, I thought: &quot;cool "
    "let's backup my toots&quot; </p><p>Resulting script: <a "
    'href="https://github.com/bbelderbos/mastodon-backup" '
    'rel="nofollow noopener noreferrer" target="_blank"><span '
    'class="invisible">https://</span><span '
    'class="ellipsis">github.com/bbelderbos/mastodon</span><span '
    'class="invisible">-backup</span></a></p><p> I hooked it up with '
    "GitHub Actions to run a few times per day.</p><p>It was a nice "
    "opportunity as well to use the amazing sqlite_utils library "
    "😍</p>",
    "tags": "",
}
TOOT3 = {
    "id": 109399437435956867,
    "media": "",
    "published": "2022-11-24T15:15:39",
    "summary": "<p>Nice command to quickly get a future date:</p><p>$ date -v "
    "+1m<br />Sat Dec 24 15:48:04 CET 2022</p><p>(or -d, -v is for "
    "MacOS it seems)</p><p>Not sure how you can give it a future "
    "start date though ... so maybe time for a quick Python script + "
    "shell alias :)</p>",
    "tags": "",
}


@pytest.fixture(scope="session", autouse=True)
def cleanup_db():
    yield
    # only teardown
    db = pathlib.Path(TEST_DB_FILE)
    if db.exists():
        db.unlink()


def test_update_db_with_new_toots():
    update_db_with_new_toots(USERNAME, db=TEST_DB, rss_feed=FIRST_TEST_RSS)
    actual = list(TEST_DB[USERNAME].rows)
    assert len(actual) == 2
    assert actual == [TOOT1, TOOT2]

    # feed has one item more
    update_db_with_new_toots(USERNAME, db=TEST_DB, rss_feed=SECOND_TEST_RSS)
    actual = list(TEST_DB[USERNAME].rows)
    assert len(actual) == 3
    assert actual == [TOOT1, TOOT2, TOOT3]

    # calling it again for same content does not insert same content twice
    update_db_with_new_toots(USERNAME, db=TEST_DB, rss_feed=SECOND_TEST_RSS)
    actual = list(TEST_DB[USERNAME].rows)
    assert len(actual) == 3
    assert actual == [TOOT1, TOOT2, TOOT3]
