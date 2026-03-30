import logging

logging.basicConfig(
    level=logging.INFO,
    filename="utils.log",  # лог будет писаться в файл
    filemode="a",  # 'a' — добавлять к существующему файлу, 'w' — перезаписывать
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
