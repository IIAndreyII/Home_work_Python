# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

data_str = f"""Задумка по реализации языка появилась в конце 1980-х годов, а разработка его реализации началась в 1989 
году сотрудником голландского института CWI Гвидо ван Россумом[45]. Для распределённой операционной системы Amoeba
требовался расширяемый скриптовый язык, и Гвидо начал разрабатывать Python на досуге, позаимствовав некоторые
наработки для языка ABC (Гвидо участвовал в разработке этого языка, ориентированного на обучение программированию).
В феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources[51]. С самого начала Python
проектировался как объектно-ориентированный язык.
Гвидо ван Россум назвал язык в честь популярного британского комедийного телешоу 1970-х Летающий цирк Монти
Пайтона[52], поскольку автор был поклонником этого телешоу, как и многие другие разработчики того времени,
а в самом шоу прослеживалась некая параллель с миром компьютерной техники[28].
Наличие дружелюбного, отзывчивого сообщества пользователей считается, наряду с дизайнерской интуицией Гвидо, одним из
факторов успеха Python. Развитие языка происходит согласно чётко регламентированному процессу создания, обсуждения,
отбора и реализации документов PEP (англ. Python Enhancement Proposal) предложений по развитию Python[53].
3 декабря 2008 года[54], после длительного тестирования, вышла первая версия Python 3000 (или Python 3.0, также
используется сокращение Py3k). В Python 3000 устранены многие недостатки архитектуры с максимально возможным (
    но не полным) сохранением совместимости со старыми версиями Python.
Дата окончания срока поддержки Python 2.7 первоначально была установлена на 2015 год, а затем перенесена на 2020
год из опасения, что большая часть существующего кода не может быть легко перенесена на Python 3[55][56].
Поддержка Python 2 была направлена лишь на уже существующие проекты, новые проекты должны были использовать
Python 3[44]. Официально Python 2.7 не поддерживается с 1 января 2020 года, хотя последнее обновление вышло
в апреле 2020. Больше никаких исправлений безопасности или других улучшений для Python 2.7 не будет
выпущено[43][57]. С окончанием срока службы Python 2.x поддерживаются только Python 3.6.x и более
поздние версии[58]."""

count_dict = {}
punct = """!()-[]{};:'"\,<>./?@#$%^&*_~1234567890"""
for i in punct:
    data_str = data_str.replace(i, "")
a = list(set(data_str.lower().split()))

for i in a:
    count_dict[i] = data_str.count(i)

t = []
for keys, values in count_dict.items():
    t.append([values, keys])
tt = sorted(t, reverse=True)

print(f'В статье {len(data_str.lower().split())} слов, из них уникальных {len(a)}.')
for i in range(10):
    print(f'{i + 1}. "{tt[i][1]}" встречается {tt[i][0]} раз')














