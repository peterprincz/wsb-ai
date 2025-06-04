import logging as log

if __name__ == "__main__":
    log.basicConfig(
        level=log.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    log.info("Hello world!")