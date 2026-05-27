from pytrends.request import TrendReq


def get_google_trends():
    try:
        pytrends = TrendReq(hl='en-US', tz=330)
        data = pytrends.trending_searches(pn='india')
        return data[0].dropna().tolist()[:10]

    except Exception as e:
        print("Trend error:", e)
        return [
            "AI automation",
            "Personal branding",
            "Faceless content",
            "Business automation",
            "Content systems"
        ]