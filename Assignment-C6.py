def stock_advice(market_trend, pe_ratio, news_sentiment):
    if market_trend == "up" and pe_ratio <= 25 and news_sentiment in ["positive", "neutral"]:
        return "Expert Advice: BUY the stock."
    elif market_trend == "stable" and 15 <= pe_ratio <= 25 and news_sentiment == "neutral":
        return "Expert Advice: HOLD the stock."
    elif market_trend == "down" and pe_ratio > 25 and news_sentiment == "negative":
        return "Expert Advice: SELL the stock."
    else:
        return "Advice: INSUFFICIENT DATA to make a decision."
print("Stock Market Expert System")
market_trend = input("Market trend (up/stable/down): ").lower()
pe_ratio = float(input("P/E Ratio of the stock (e.g., 18.5): "))
news_sentiment = input("News sentiment (positive/neutral/negative): ").lower()
result = stock_advice(market_trend, pe_ratio, news_sentiment)
print("\n" + result)
