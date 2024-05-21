class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.w
    def get_h(self):
        return self.h
    def intersection(self, other):
        x1 = max(self.x, other.get_x())
        y1 = max(self.y, other.get_y())
        x2 = min(self.x + self.w, other.get_x() + other.get_w())
        y2 = min(self.y + self.h, other.get_y() + other.get_h())

        if x1<x2 and y1<y2:
            return Rectangle(x1, y1, x2-x1, y2-y1)
        else:
            return None

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = rect1.intersection(rect2)
if rect3 is None:
    print('no intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(1, 4, 8, 6)
rect3 = rect1.intersection(rect2)
if rect3 is None:
    print('no intersection')
else:
    print('intercsection', rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())














class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
    def add_word(self, word):
        if len(' '.join(self.words)) + len(word) <= self.width:
            self.words.append(word)
        else:
            self.end()
            self.words.append(word)
    def end(self):
        print(' '.join(self.words))
        self.words = []

class RightParagraph:
    def __init__ (self, width):
        self.width = width
        self.words = []
    def add_word(self, word):
        if len(' '.join(self.words + [word])) <= self.width:
            self.words.append(word)
        else:
            self.end()
            self.words.append(word)
    def end(self):
        spaces = ' ' * (self.width - len(' '.join(self.words)))
        print(spaces + ' '.join(self.words))
        self.words = []

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()






class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range (10)]
        self.kill = []

    def shoot(self, row, col, result):
        if result == 'hit':
            self.map[row][col] = 'x'
        if result == 'sink':
            self.kill.append((row,col))

    def cell(self, row, col):
        if (row,col) in self.kill:
            return 'x'
        if self.map[row][col] =='x':
            return 'x'
        for r, c in self.kill:
            if (self.map[row][col] != 'x') and (abs(r-row) <=1 and abs(c-col) <= 1):
                return '*'
        return '.'

sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(6, 9, 'hit')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end = '')
    print()


class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
        elif actor.get_distance(target) > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
        else:
            print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
            target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0

    def get_coords(self):
        return (self.pos_x, self.pos_y)

    def get_distance(self, other):
        dist_x = self.pos_x - other.pos_x
        dist_y = self.pos_y - other.pos_y
        return (dist_x ** 2 + dist_y ** 2) ** 0.5


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
        else:
            self.weapon.hit(self, target)

    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.inventory = []
        self.equipped_weapon = None

    def hit(self, target):
        if not self.equipped_weapon:
            print("Я безоружен")
        elif not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
        else:
            self.equipped_weapon.hit(self, target)

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
        else:
            print(f"Подобрал {weapon}")
            self.inventory.append(weapon)
            if not self.equipped_weapon:
                self.equipped_weapon = weapon

    def next_weapon(self):
        if not self.inventory:
            print("Я безоружен")
        elif len(self.inventory) == 1:
            print("У меня только одно оружие")
        else:
            index = self.inventory.index(self.equipped_weapon)
            index = (index + 1) % len(self.inventory)
            self.equipped_weapon = self.inventory[index]
            print(f"Сменил оружие на {self.equipped_weapon}")

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")


weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)





class Mail:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

class MailServer:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def receive_mail(self):
        if self.inbox:
            mail = self.inbox.pop(0)
            return mail
        else:
            return None

    def send_mail(self, receiver_server, mail):
        receiver_server.inbox.append(mail)


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        mail = self.server.receive_mail()
        if mail:
            return f"Received mail from {mail.sender}: {mail.message}"
        else:
            return "No new mail"

    def send_mail(self, receiver_server, receiver_user, message):
        mail = Mail(self.user, receiver_user, message)
        self.server.send_mail(receiver_server, mail)
        return f"Sent mail to {receiver_user} on {receiver_server.name}"

server1 = MailServer("Server1")
server2 = MailServer("Server2")

client1 = MailClient(server1, "user1")
client2 = MailClient(server2, "user2")


print(client1.send_mail(server2, "user2", "Hello from user1"))
print(client2.receive_mail())