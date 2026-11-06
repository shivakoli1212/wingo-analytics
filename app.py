import os
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

API_URL = os.getenv("WINGO_API_URL", "https://api.wingobot.com/v2/30-sec-game-history")
API_TOKEN = os.getenv("WINGO_API_TOKEN", "")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/history")
def history():
    if not API_TOKEN:
        return jsonify({"success": False, "error": "API token is not configured on the server."}), 503
    try:
        response = requests.get(
            API_URL,
            headers={"Authorization": f"Bearer {API_TOKEN}"},
            timeout=15
        )
        response.raise_for_status()
        payload = response.json()
        if not payload.get("success"):
            return jsonify({"success": False, "error": payload.get("error", "API returned an unsuccessful response.")}), 502

        current = payload.get("current", {})
        history_rows = payload.get("history", [])
        stats = payload.get("stats", {})
        safe_rows = []
        for row in history_rows:
            safe_rows.append({
                "issueNumber": row.get("issueNumber"),
                "number": row.get("number"),
                "colour": row.get("colour"),
                "premium": row.get("premium"),
                "sum": row.get("sum")
            })
        return jsonify({
            "success": True,
            "current": {"issueNumber": current.get("issueNumber")},
            "history": safe_rows,
            "stats": {
                "fetched": stats.get("fetched"),
                "last_updated": stats.get("last_updated")
            },
            "feed_note": "Configured endpoint is 30-sec-game-history. Use a verified 1-minute endpoint before treating this as 1-minute data."
        })
    except requests.RequestException as exc:
        return jsonify({"success": False, "error": f"Could not reach game-history API: {exc}"}), 502
    except ValueError:
        return jsonify({"success": False, "error": "API did not return valid JSON."}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
