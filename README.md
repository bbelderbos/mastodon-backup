# Fosstodon backup script

Running [a cronjob](https://github.com/bbelderbos/mastodon-backup/blob/main/.github/workflows/backup.yml) to update `toots.db` with new toots retrieved [from my Fosstodon's user RSS feed](https://fosstodon.org/@bbelderbos).

I also added a `trends.py` script to show some data visualization for a username / table in the DB:

```
$ streamlit run trends.py username
```

Yields:

<img width="767" alt="mastodon-trends-example" src="https://user-images.githubusercontent.com/387927/235671008-92ffc84f-b988-4edf-b0db-5a0a76994857.png">

---

I did a video about this project [here](https://youtu.be/NvGiPifbtl4)
