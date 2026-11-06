# Wingo Analytics Dashboard

A free, mobile-friendly Flask website that displays the history returned by your WingoBot API, counts number/colour/size frequencies, and refreshes automatically.

## Important
- Your supplied endpoint is `/v2/30-sec-game-history`, so this project labels the data as an unverified 30-second feed.
- Do not treat frequency or recent streaks as a reliable prediction. Random game outcomes cannot be guaranteed.
- The API token previously pasted into chat should be revoked/rotated. Never put a token in HTML or JavaScript.

## Run locally
1. Install Python 3.10+.
2. In this folder run: `pip install -r requirements.txt`
3. Set environment variables:
   - Linux/macOS: `export WINGO_API_TOKEN="YOUR_NEW_TOKEN"`
   - Windows PowerShell: `$env:WINGO_API_TOKEN="YOUR_NEW_TOKEN"`
4. Start: `python app.py`
5. Open `http://127.0.0.1:5000`

Optional: set `WINGO_API_URL` to a verified endpoint. Do not change it to a guessed URL.

## Free hosting
You can deploy this Flask app to a provider with a free web-service tier if currently offered. Set `WINGO_API_TOKEN` as a private environment variable in the hosting dashboard. Free-tier availability and sleep limits can change.
