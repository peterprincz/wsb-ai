import json
import logging as log


from ai.commentAnalyzer import CommentAnalyzer


if __name__ == "__main__":
    log.basicConfig(
        level=log.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    config_path = "config.json"
    configuration = None
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            configuration = json.load(f)
    except Exception as e:
        log.error(f"Error loading config file '{config_path}': {e}")
        raise e
    analyzer = CommentAnalyzer(configuration)
    result = analyzer.analyze_comment("I'm really bullish on AMD right now — their earnings blew expectations!")
    log.info(result)