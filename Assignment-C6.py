def stock_advice(market_trend, pe_ratio, news_sentiment, growth_rate, debt_to_equity):
    if (market_trend == "up" and pe_ratio <= 25 and 
        news_sentiment in ["positive", "neutral"] and 
        growth_rate >= 10 and debt_to_equity <= 1.0):
        return "Expert Advice: BUY the stock."
    elif (market_trend == "stable" and 15 <= pe_ratio <= 25 and 
          news_sentiment == "neutral" and 
          5 <= growth_rate < 10 and debt_to_equity <= 1.5):
        return "Expert Advice: HOLD the stock."
    elif (market_trend == "down" and pe_ratio > 25 and 
          news_sentiment == "negative" and 
          growth_rate < 5 and debt_to_equity > 2.0):
        return "Expert Advice: SELL the stock."
    else:
        return "Advice: INSUFFICIENT DATA to make a decision."
print("Stock Market Expert System")
market_trend = input("Market trend (up/stable/down): ").lower()
pe_ratio = float(input("P/E Ratio of the stock (e.g., 18.5): "))
news_sentiment = input("News sentiment (positive/neutral/negative): ").lower()
growth_rate = float(input("Company's annual growth rate (%): "))
debt_to_equity = float(input("Debt-to-Equity ratio (e.g., 1.2): "))

result = stock_advice(market_trend, pe_ratio, news_sentiment, growth_rate, debt_to_equity)
print("\n" + result)
