from app.utils import fetch


def run():
    """Run daily background logic: fetch and log the daily video status."""
    try:
        dailyvid = fetch.dailyvid()
        print(f"Daily video: {dailyvid.video.title} ({dailyvid.video.file})")
        print(f"Watched {dailyvid.watched} of {dailyvid.total} videos")
        print(f"Earliest: {dailyvid.earliest}")
        print(f"Latest: {dailyvid.latest}")
    except Exception as e:
        print(f"Background run failed: {e}")
        raise


if __name__ == "__main__":
    run()
