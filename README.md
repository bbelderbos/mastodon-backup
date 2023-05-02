# Fosstodon backup script

Running [a cronjob](https://github.com/bbelderbos/mastodon-backup/blob/main/.github/workflows/backup.yml) to update `toots.db` with new toots retrieved [from my Fosstodon's user RSS feed](https://fosstodon.org/@bbelderbos).

I also added a `trends.py` script to show some data visualization for a username / table in the DB:

```
$ streamlit run trends.py username
```

Yields:

<img width="806" alt="fosstodon-stats-bbelderbos" src="https://user-images.githubusercontent.com/387927/204764745-6af95468-10c6-426d-accd-230996b9dcf5.png">

I did a video about this project [here](https://youtu.be/NvGiPifbtl4)
