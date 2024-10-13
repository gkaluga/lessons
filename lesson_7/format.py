team_name1 = "Мастера кода"
team_name2 = "Волшебники данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'победа команды {team_name1}'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'победа команды {team_name2}'
else:
    challenge_result = 'ничья'

print('В команде %(name)s участников: %(num)d !' % {'name': team_name1, 'num': team1_num})
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

print('Команда {!r} решила задач: {!s} !'.format(team_name2, score_2))
print('{name} решили задачи за {time:.1f} с !'.format(name=team_name2, time=team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(
  f'Сегодня было решено {score_1+score_2} задач' +
  f', в среднем по {(team1_time+team2_time)/(score_1+score_2):.1f} секунды на задачу!')
