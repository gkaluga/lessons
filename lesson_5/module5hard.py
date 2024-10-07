from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if  list_usr := [u for u in self.users if u.nickname == nickname]:
            if list_usr[0].password == hash(password):
                self.current_user = list_usr[0]
            else:
                print('Неправильный пароль')
        else:
            print(f'Пользователь {nickname} не существует. Сначала зарегистрируйтесь.')

    def register(self, nickname, password, age):
        if [u for u in self.users if u.nickname == nickname]:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user_ := User(nickname, password, age))
            self.current_user = user_

    def log_out(self):
        self.current_user = None

    def find_video(self, title):
        if find_list := [v for v in self.videos if v.title == title]:
            return find_list[0]

    def __contains__(self, item):
        return bool([v for v in self.videos if v.title == item.title])

    def add(self, *args):
        for video_ in args:
            if not video_ in self:
                self.videos.append(video_)

    def get_videos(self, title):
        return [v.title for v in self.videos if title.lower() in v.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            if video_list := [v for v in self.videos if v.title == title]:
                video_ = video_list[0]
                if video_.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу"')
                else:
                    video_.time_now = 0
                    while video_.time_now < video_.duration:
                        sleep(1)
                        video_.time_now += 1
                        print(video_.time_now, end=' ')
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.log_in('vasya_pupki', 'F8098FM8fjm9jmi')
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
