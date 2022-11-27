import random
import logging

logging.basicConfig(level=logging.INFO, filename="my_log.log", format="%(asctime)s %(levelname)s %(message)s")

while True:
    try:
        N = int(input('До какого числа будет диапозон? '))
        logging.info('n = {}'.format(N))
        assert N > 1
        logging.info('suitable')
        break
    except AssertionError:
        print('Число должно быть больше 1')
        logging.exception('less than 1')
    except ValueError:
        print('Введите натуральное число')
        logging.exception('incorrect input')
while True:
    try:
        k = int(input('Какое будет количество попыток? '))
        logging.info('k = {}'.format(k))
        assert k > 0
        break
    except AssertionError:
        print('Число должно быть больше 0')
        logging.exception('less than 0')
    except ValueError:
        print('Введите натуральное число')
        logging.exception('incorrect input')
hidden_number = random.randint(1, N)
logging.info('hidden_number = {}'.format(hidden_number))

while k > 0:
    print('Оставшееся количество попыток: {}'.format(k))
    try:
        number = int(input('Введите загаданное число '))
        logging.info('input num = {}'.format(number))
        assert 1 <= number <= N
        logging.info('suitable')
        if number == hidden_number:
            print('Вы угадали число.')
            logging.info('the number is guessed')
            break
        else:
            k -= 1
            print('Вы не угадали число.')
            logging.info('the number isn\'t guessed')
            if number < hidden_number:
                print('Число {} меньше загаданного'.format(number))
            else:
                print('Число {} больше загаданного'.format(number))
            if k == 0:
                print('Попытки закончились\n')
                logging.info('attempts ended')
    except AssertionError:
        print('Число должно быть в диапазоне от 1 до {}'.format(N))
        logging.exception('not in range')
    except ValueError:
        print('Введите натуральное число')
        logging.exception('incorrect input')