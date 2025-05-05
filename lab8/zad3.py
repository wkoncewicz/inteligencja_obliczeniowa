import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()  # or API("path-to.db") – default is `accounts.db`

    # ADD ACCOUNTS (for CLI usage see next readme section)

    # Option 1. Adding account with cookies (more stable)
    cookies = "auth_token=23276aa1c6bef30eea75a185a0e342b16459a327; ct0=c0a265506221e2a2f47f3e88bacb7bbbc228eb5a4bab116503358b956abd310e8071c20b610b57a891106b21e4bd5b0c271074a0cba41ca37b6a1d197b404b060a491eb02c09b1c5b84214d67eb4958d; twid=u%3D1298323791215562753"  # or '{"abc": "12", "ct0": "xyz"}'
    await api.pool.add_account("issaczesc", "", "", "", cookies=cookies)
    await api.pool.login_all()

    tweets = await gather(api.search("gorilla", limit=100, kv={"product": "Top"}))

    for tweet in tweets:
        print(f"[{tweet.date}] @{tweet.user.username}: {tweet.rawContent}")

asyncio.run(main())