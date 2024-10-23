import logging
from time import sleep

from common import configure_logging, timer
from threading import Thread


logger = logging.getLogger(__name__)


def get_users():
    """
    Получение пользователей
    """
    logger.info("Start get users")
    # Время выполнения скрипта занимает 1 сек
    sleep(1)
    logger.info("Done get users")


def get_posts():
    """
    Получение постов
    """
    logger.info("Start get posts")
    # Время выполнения скрипта занимает 1 сек
    sleep(1)
    logger.info("Done get posts")


@timer
def demo_threading():
    """
    Демонстрация использования потоков
    """
    logger.info("Start demo threading")
    # 1 - мультипроцессинг - 2.010
    # get_users()
    # get_posts()

    # 2 - мультитрединг - 1.002
    thread_users = Thread(target=get_users)
    thread_posts = Thread(target=get_posts)

    logger.info("Created threads. Starting")
    # запуск тредов
    thread_users.start()
    thread_posts.start()
    logger.info("Started threading. Joining...")
    thread_users.join()
    thread_posts.join()
    # ожидание завершения тредов
    logger.info("Done demo threading")


def main():
    """
    Основная функция приложения
    """
    configure_logging()
    logger.info("Start main")
    demo_threading()
    logger.info("Done main")


if __name__ == '__main__':
    main()
