import collections
import itertools
import sys

import streamlit as st
import pandas as pd


def main(table):
    st.title("My Mastodon (Fosstodon) usage")
    conn = "sqlite:///toots.db"
    df = pd.read_sql(f"SELECT * FROM {table}", conn)

    # TODO: over time change this to monthly or even yearly
    st.subheader("Daily activity")
    df["day"] = df.published.str[:10]

    df_activity = pd.DataFrame(df.groupby(["day"]).count()["id"])
    df_activity.columns = ["# toots"]

    st.line_chart(df_activity)

    st.subheader("Most used tags")
    tags_per_toot = [t.split(", ") for t in df.tags if t]
    tags_flattened = itertools.chain.from_iterable(tags_per_toot)
    most_common_tags = collections.Counter(tags_flattened)

    df_tags = pd.DataFrame.from_dict(most_common_tags, orient="index")
    df_tags.columns = ["# toots per tag"]
    st.bar_chart(df_tags)


if __name__ == "__main__":
    username = sys.argv[1]
    main(username)
