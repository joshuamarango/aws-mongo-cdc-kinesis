from src.core import stream


def main() -> None:
    (stream
        .MongoChangeStream()
        .start())


if __name__ == "__main__":
    main()
