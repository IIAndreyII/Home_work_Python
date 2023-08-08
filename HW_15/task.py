# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
import os
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='hw.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} {levelname} - {msg}',
                    style='{')

logger = logging.getLogger(__name__)

PathData = namedtuple('PathData', ['name', 'extension', 'is_dir', 'parent_dir'])

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str)
args = parser.parse_args()
path = Path(args.p)
