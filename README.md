# Fosstodon backup script

Running [a cronjob](https://github.com/bbelderbos/mastodon-backup/blob/main/.github/workflows/backup.yml) to update `toots.db` with new toots retrieved [from my Fosstodon's user RSS feed](https://fosstodon.org/@bbelderbos).

I also added a `trends.py` script to show some data viz as I go. I can already see I post 4-5 times day so far (23th-30th of Nov 2022 period) 💪 and I tagged no less than 16 posts with #Python 🐍

```
$ streamlit run trends.py
```

Yields: 

<img width="806" alt="fosstodon-stats-bbelderbos" src="https://user-images.githubusercontent.com/387927/204764745-6af95468-10c6-426d-accd-230996b9dcf5.png">
