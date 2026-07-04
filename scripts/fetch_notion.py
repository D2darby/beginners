#!/usr/bin/env python3
"""Notion 기록 DB → photos.json 생성. NOTION_TOKEN 환경변수 필요."""
import json, os, sys, urllib.request

DB_ID = "376b2e21a9b44e3486ad1f57c2153b43"  # Beginners 기록 DB
TOKEN = os.environ.get("NOTION_TOKEN")
if not TOKEN:
    sys.exit("NOTION_TOKEN 환경변수가 없습니다.")

def query(cursor=None):
    body = {"page_size": 100}
    if cursor:
        body["start_cursor"] = cursor
    req = urllib.request.Request(
        f"https://api.notion.com/v1/databases/{DB_ID}/query",
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def text(prop):
    return "".join(t.get("plain_text", "") for t in prop.get("title", []) or prop.get("rich_text", []))

pages, cursor = [], None
while True:
    data = query(cursor)
    pages += data.get("results", [])
    if not data.get("has_more"):
        break
    cursor = data.get("next_cursor")

photos = []
for pg in pages:
    p = pg.get("properties", {})
    files = (p.get("대표사진") or {}).get("files") or []
    url = None
    for f in files:
        if f.get("type") == "external":
            url = f["external"]["url"]; break
        if f.get("type") == "file":
            url = f["file"]["url"]; break  # 주의: Notion 내부 파일 URL은 1시간 만료
    if not url:
        continue
    title = text(p.get("제목", {}))
    for ext in (".PNG", ".JPG", ".JPEG", ".HEIC", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".WEBP"):
        if title.endswith(ext):
            title = title[: -len(ext)]
    date = ((p.get("날짜") or {}).get("date") or {}).get("start")
    photos.append({
        "title": title,
        "date": date,
        "year": ((p.get("연도") or {}).get("select") or {}).get("name"),
        "place": ((p.get("장소") or {}).get("select") or {}).get("name"),
        "people": [t["name"] for t in ((p.get("인물") or {}).get("multi_select") or [])],
        "category": ((p.get("분류") or {}).get("select") or {}).get("name"),
        "image": url,
    })

photos.sort(key=lambda x: x.get("date") or "", reverse=True)
with open("photos.json", "w", encoding="utf-8") as f:
    json.dump(photos, f, ensure_ascii=False, indent=2)
print(f"photos.json 갱신 완료 — {len(photos)}장")
