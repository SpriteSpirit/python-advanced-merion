import logging
import requests
from time import sleep

from common import configure_logging, timer
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

logger = logging.getLogger(__name__)

"""
Для I/O bounds задач подходит мультитрединг
Для CPU bounds задач подходит только мультипроцессинг 
"""


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


def get_user(user_id: int):
    """
    Создание запроса в сеть для получения одного пользователя.
    Пользователи хранятся в JSON-файле
    """
    logger.info("Start get user %s", user_id)
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
    )
    result = response.json()
    logger.info("Got user %s", result)

    return result


def cpu_expensive(timeout: int):
    """
    Нагрузка процессора
    *CPU не может ждать несколько отдельных задач
    """
    logger.info("Countdown to %s", timeout)

    while timeout:
        timeout -= 1

    logger.info("Done countdown")


@timer
def demo_threading():
    """
    Демонстрация использования потоков в трединге
    """
    logger.info("Start demo threading")
    # 1 - 2.010 с.
    # get_users()
    # get_posts()

    # 2 - 1.002 с.
    # thread_users = Thread(target=get_users)
    # thread_posts = Thread(target=get_posts)
    #
    # logger.info("Created threads. Starting")
    # # запуск тредов
    # thread_users.start()
    # thread_posts.start()
    # logger.info("Started threading. Joining...")
    # thread_users.join()
    # thread_posts.join()

    # 3 - альтернатива варианту 2 - 1.002 с.
    # with ThreadPoolExecutor() as executor:
    #     """
    #     Выполнение воркера в пуле потоков
    #     """
    #     executor.submit(get_users)
    #     executor.submit(get_posts)

    # 4 - от 3.799 до 6.002
    # for user_id in range(1, 11):
    #     get_user(user_id)

    # 5 - 1.098!
    # with ThreadPoolExecutor() as executor:
    #     """
    #     Выполнение воркера в пуле потоков
    #     """
    #     executor.map(get_user, range(1, 11))
    #     executor.submit(get_posts)

    # 6 - 4.732
    # cpu_expensive(64_000_000)
    # cpu_expensive(72_000_000)

    # 7 - 4.235
    # with ThreadPoolExecutor() as executor:
    #     """
    #     Выполнение воркера в пуле потоков
    #     """
    #     executor.submit(cpu_expensive, 64_000_000)
    #     executor.submit(cpu_expensive, 72_000_000)


@timer
def demo_multiprocessing():
    logger.info("Start demo multiprocessing")
    # 1 - 3.086
    # process1 = multiprocessing.Process(
    #     target=cpu_expensive,
    #     args=(64_000_000,)
    # )
    # process2 = multiprocessing.Process(
    #     target=cpu_expensive,
    #     args=(72_000_000,)
    # )
    # logger.info("Created processes. Starting")
    # # запуск процессов
    # process1.start()
    # process2.start()
    # logger.info("Started multiprocessing. Joining...")
    # # ожидание завершения процессов
    # process1.join()
    # process2.join()
    # logger.info("Done demo multiprocessing")

    # 2 - 3.217
    with multiprocessing.Pool() as pool:
        pool.map(cpu_expensive, [64_000_000, 72_000_000])


# ожидание завершения тредов
logger.info("Done demo threading")


def main():
    """
    Основная функция приложения
    """
    configure_logging()
    logger.info("Start main")
    # demo_threading()
    demo_multiprocessing()

    logger.info("Done main")


if __name__ == '__main__':
    main()
