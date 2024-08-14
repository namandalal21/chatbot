def determine_intent(tokens):
    if 'weather' in tokens:
        return "weather"
    elif 'news' in tokens:
        return "news"
    else:
        return "general"
